#!/usr/bin/env python3
"""Build a public literature report using only files in this repository."""
import csv
from html import escape
import json
from pathlib import Path
import re

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

ROOT = Path(__file__).resolve().parent


def register_fonts():
    candidates = [
        (Path('/System/Library/Fonts/Supplemental'), ['Arial.ttf', 'Arial Bold.ttf']),
        (Path('/usr/share/fonts/truetype/dejavu'), ['DejaVuSans.ttf', 'DejaVuSans-Bold.ttf']),
    ]
    if not any(all((folder / name).is_file() for name in names) for folder, names in candidates):
        try:
            import matplotlib
            candidates.append((Path(matplotlib.get_data_path()) / 'fonts/ttf', ['DejaVuSans.ttf', 'DejaVuSans-Bold.ttf']))
        except ImportError:
            pass
    for folder, names in candidates:
        if all((folder / name).is_file() for name in names):
            for alias, name in zip(['ReportText', 'ReportBold'], names):
                pdfmetrics.registerFont(TTFont(alias, str(folder / name)))
            return
    raise RuntimeError('Install Arial or DejaVu Sans to build the report.')


def optional_number(value):
    return float(value) if value else None


def load_materials():
    references = json.loads((ROOT / 'references.json').read_text())
    with (ROOT / 'data/materials.csv').open(newline='') as stream:
        rows = list(csv.DictReader(stream))
    for row in rows:
        if row['source_id'] not in references:
            raise ValueError('Unknown literature reference')
        signed = optional_number(row['theta_cw_K'])
        magnitude = optional_number(row['theta_abs_K'])
        ordering = optional_number(row['ordering_K'])
        if magnitude is not None and magnitude < 0:
            raise ValueError('An intercept magnitude must be nonnegative')
        if signed is not None and magnitude is not None and abs(signed) != magnitude:
            raise ValueError('Signed intercept and magnitude disagree')
        if ordering is not None and ordering <= 0:
            raise ValueError('An ordering temperature must be positive')
        row['ratio'] = magnitude / ordering if magnitude is not None and ordering is not None else None
    return rows, references


def format_number(value):
    return format(float(value), '.6g') if value else '—'


def table_rows(rows):
    result = [['Material / structure', 'Intercept (K)', 'Ordering (K)', 'Ratio']]
    for row in rows:
        intercept = format_number(row['theta_cw_K'])
        if not row['theta_cw_K']:
            intercept = '|theta| = ' + format_number(row['theta_abs_K'])
        elif row['theta_uncertainty_K']:
            intercept += ' ± ' + format_number(row['theta_uncertainty_K'])
        result.append([row['material'] + ' / ' + row['structure'], intercept,
                       format_number(row['ordering_K']),
                       f'{row["ratio"]:.3f}' if row['ratio'] is not None else '—'])
    return result


def main():
    rows, references = load_materials()
    computed = ROOT / 'data/ratios.csv'
    with computed.open('w', newline='') as stream:
        writer = csv.writer(stream)
        writer.writerow(['material', 'structure', 'ratio', 'source_id'])
        for row in rows:
            writer.writerow([row['material'], row['structure'], row['ratio'], row['source_id']])

    register_fonts()
    body = ParagraphStyle('Body', fontName='ReportText', fontSize=10.2, leading=14, spaceAfter=8)
    title = ParagraphStyle('Title', fontName='ReportBold', fontSize=19, leading=23, spaceAfter=12)
    heading = ParagraphStyle('Heading', fontName='ReportBold', fontSize=12, leading=16,
                             spaceBefore=8, spaceAfter=6, keepWithNext=True)
    small = ParagraphStyle('Small', fontName='ReportText', fontSize=8.4, leading=11, spaceAfter=7)
    cell = ParagraphStyle('Cell', fontName='ReportText', fontSize=8.7, leading=12)
    numbers = {key: str(i) for i, key in enumerate(references, 1)}

    def render_text(text, style=body):
        text = escape(text)
        text = re.sub(r'`([^`]+)`', r'\1', text)
        text = re.sub(r'\[([^\]]+)\]\((https://[^)]+)\)', r'<link href="\2" color="#184d78">\1</link>', text)
        for key, number in numbers.items():
            text = text.replace('[' + key + ']', '[' + number + ']')
        return Paragraph(text, style)

    story = []
    for paragraph in (ROOT / 'analysis.md').read_text().split('\n\n'):
        paragraph = paragraph.strip()
        if not paragraph:
            continue
        if paragraph.startswith('| Material / structure'):
            content = [[render_text(value, cell) for value in row] for row in table_rows(rows)]
            table = Table(content, colWidths=[220, 110, 95, 80], repeatRows=1, hAlign='LEFT')
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#e7edf3')),
                ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f5f7f9')]),
                ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                ('TOPPADDING', (0, 0), (-1, -1), 4),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
            ]))
            story.extend([table, Spacer(1, 9)])
        elif re.match(r'^\[\d+\] ', paragraph):
            story.append(render_text(paragraph, small))
        elif paragraph.startswith('## '):
            story.append(render_text(paragraph[3:], heading))
        elif paragraph.startswith('# '):
            story.append(render_text(paragraph[2:], title))
        else:
            story.append(render_text(paragraph))

    def footer(canvas, document):
        canvas.setFont('ReportText', 8)
        canvas.setFillColor(colors.HexColor('#40536a'))
        canvas.drawString(43, 23, 'Curie–Weiss temperature and magnetic order')
        canvas.drawRightString(A4[0] - 43, 23, str(document.page))

    report = ROOT / 'report.pdf'
    document = SimpleDocTemplate(str(report), pagesize=A4, leftMargin=43, rightMargin=43,
                                 topMargin=40, bottomMargin=43, title='Curie–Weiss temperature and magnetic order',
                                 author='', subject='Literature examples and interpretation', creator='Public analysis report')
    document.build(story, onFirstPage=footer, onLaterPages=footer)
    print(f'Built report.pdf and data/ratios.csv from {len(rows)} literature examples.')


if __name__ == '__main__':
    main()

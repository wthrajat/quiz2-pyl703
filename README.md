# Curie–Weiss temperature and magnetic order

A small, reproducible comparison of magnetic interaction scales and ordering temperatures. It explains why the sign and magnitude of a Curie–Weiss intercept do not uniquely identify a magnetic structure.

- [Read the analysis](analysis.md)
- [Download the report](report.pdf)
- [Inspect the example data](data/materials.csv)
- [Check the literature references](references.json)

The public dataset contains nine literature examples. Signed intercepts and unsigned magnitudes are separate fields. A missing ordering temperature remains missing, and source-specific caveats are kept alongside the values. These examples are illustrative rather than a comprehensive or independently remeasured database.

## Rebuild

Requires Python 3.9 or later. Install the dependencies in a virtual environment, then build the report and computed ratios:

```sh
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python build_report.py
```

The script writes `report.pdf` and `data/ratios.csv`. It uses Arial on macOS, DejaVu Sans on Linux, or the DejaVu Sans fonts bundled with Matplotlib when available. No network access or account credentials are needed to rebuild.

## Interpretation

Large ratios can motivate checking geometric frustration or reduced dimensionality, but they do not establish a glass or spin liquid. Small ratios can result from competing exchanges or the susceptibility of multiple magnetic sublattices. Read the source notes before interpreting either extreme.

References link to published papers or accessible manuscripts. Raw course documents, conversation exports, personal identifiers, local workspace paths, and original spreadsheets are not part of this public edition.

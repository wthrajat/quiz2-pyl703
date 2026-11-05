# Curie–Weiss temperature and magnetic order

A small, reproducible comparison of magnetic interaction scales and ordering temperatures. It explains why the sign and magnitude of a Curie–Weiss intercept do not uniquely identify a magnetic structure.

- [Read the analysis](analysis.md)
- [Download the report](report.pdf)
- [Inspect the example data](data/materials.csv)
- [Check the literature references](references.json)

## Assignment workflow

The reviewed workflow covers the original 22-entry assignment workbook and explains differences from the nine literature examples used in this public analysis.

- [Step-by-step report](docs/quiz-workflow/step_by_step_report.pdf) ([editable text](docs/quiz-workflow/step_by_step_report.md))
- [Reconstructed prompts](docs/quiz-workflow/reconstructed_prompts.pdf) ([copyable text](docs/quiz-workflow/reconstructed_prompts.md))

The ten prompts reconstruct the reasoning during a later review. They are not original student messages or a substitute for the actual chat history required by the assignment. The original chat export and other local submission files are kept separately.

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

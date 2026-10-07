# Excel Q&A — Evaluation guide

Start with the smallest path that exercises the project. Distinguish source inspection,
syntax/build checks, functional behavior and domain validation when recording a result.

## Guided reading and demonstration

1. **Upload an XLSX.** Pandas reads the first worksheet by default. Other sheets are not
automatically incorporated into the question context.

2. **Inspect the text conversion.** Nonnull row values are joined into text. Headers, coordinates,
types and formula semantics are not preserved as a structured evidence model.

3. **Submit the question.** The flattened text and question enter one generation prompt sent to
Google. A configured account and compatible model/SDK are required.

4. **Verify the result.** Compare the answer with workbook cells manually. The app does not
recompute numerical answers or attach source-cell references.

## Declared checks

These commands/checks describe the intended verification path. Their presence in this
guide does not claim that they passed. See the dated evidence below and the README for setup.

```text
python -m py_compile app.py
```

## Evidence levels

| Level | What it establishes | What it does not establish |
| --- | --- | --- |
| Source review | A path exists in tracked code | Successful runtime behavior |
| Syntax/build | Parser/compiler accepts that path | End-to-end correctness |
| Behavioral check | A specific input/output case passed | Generalization beyond cases |
| Domain evaluation | Performance on a stated target setting | Other users/data/environments |

## What to record

- Commit, environment, dependency versions and date.
- Input provenance and whether data is synthetic, public or privately supplied.
- Absolute pass/fail/skip counts; keep failed cases and their root causes.
- Whether external services, hardware or a production deployment were actually exercised.
- Expected output and an artifact showing the observation.

## Review scenarios

- **First-sheet scope:** The context boundary is narrower than an entire multi-sheet workbook.

- **Generation is labeled:** A model answer is not a pandas-calculated aggregate.

- **Credentials are local configuration:** Use your own authorized key rather than repository
artifacts.

## Documentation inspection — 7 October 2026

The documentation was traced to committed source and checked for local links, balanced
code fences and supported implementation claims. Historical notebook outputs remain labeled
as historical. Live provider access, private databases and hardware behavior are not inferred
from configuration or dependency files. Any fresh run is recorded separately in the README.

## Next evidence to collect

- Verify provider/SDK compatibility without real workbook data.
- Evaluate multi-sheet and known-total synthetic workbooks.
- Add source-cell and deterministic calculation boundaries if extending the app.

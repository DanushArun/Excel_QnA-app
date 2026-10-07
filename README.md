# Excel Q&A App

A Streamlit application that turns the first worksheet of an uploaded Excel file into text
and sends that text with a question to a Google Gemini generation model.

## Data flow

```mermaid
flowchart LR
    XLSX[Uploaded XLSX] --> Pandas[Read first worksheet]
    Pandas --> Text[Join nonempty row values]
    Text --> Prompt[Workbook text and question]
    Prompt --> Gemini[Google generation API]
    Gemini --> Answer[Streamlit answer]
```

The application uses a full-text prompt. It does not implement embeddings, vector retrieval,
spreadsheet formulas, deterministic numeric checks or source-cell citations.

## Local setup

```bash
git clone https://github.com/DanushArun/Excel_QnA-app.git
cd Excel_QnA-app
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
streamlit run app.py
```

Set `GEMINI_API_KEY` in your local environment before launch. Supply your own account key;
do not reuse or publish credentials stored in a checkout.
The app names `gemini-1.5-flash` and pins `google-generativeai` 0.3.2. Current model access and
SDK compatibility were not verified with a live provider account in this update.

## What the UI does

1. Accept an `.xlsx` upload.
2. Read it through pandas and flatten nonempty row values into text.
3. Accept a question and submit a generation request.
4. Render the returned answer as Markdown.

Workbook content and the question leave the machine for the configured provider.
Use synthetic or authorized files when evaluating the app.

## Evidence and limits

Python syntax and README links were checked. No workbook-to-answer provider evaluation or
Cloud Run deployment check was performed. There is no automated test suite here.

Only the first worksheet is read by default. Flattening loses column names, data types and
cell coordinates. Large workbooks may exceed the model context limit. Answers, totals and
relevance refusals are not verified by the application; inspect the workbook before relying
on a generated result. A Dockerfile is included, but live deployment status is unverified.

## License

See [LICENSE](LICENSE).

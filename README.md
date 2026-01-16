# InsightForge

A Streamlit + LangChain + OpenAI + FAISS news research tool.

## Run locally

1. Create a virtualenv and install deps:

```bash
pip install -r requirements.txt
```

2. Set your OpenAI API key (recommended via env var):

```bash
export OPENAI_API_KEY="your_key_here"
```

3. Start the app:

```bash
streamlit run app.py
```

## How it works

- Paste up to 3 article URLs
- Click **Build Index** to ingest + chunk + embed + build a FAISS index
- Ask questions and get grounded answers + sources

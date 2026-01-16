# InsightForge 🔍📊
**AI-powered News Research & Question Answering Tool**

🔗 Live Demo: https://insightforge-4e3pnp3kwd5b6votnbuzpl.streamlit.app/

InsightForge is a Retrieval-Augmented Generation (RAG) application that enables users to ingest news articles from the web, build a semantic search index, and ask natural-language questions with source-backed answers.

The system is designed for **research, analysis, and fact-grounded exploration of unstructured online content**.

---

## ✨ Features

- 🌐 Ingest up to 3 online articles via URL
- ✂️ Intelligent text chunking with overlap
- 🧠 Semantic embeddings using OpenAI
- ⚡ Fast similarity search with FAISS
- ❓ Natural language Q&A grounded strictly in retrieved context
- 🔗 Transparent source attribution
- ☁️ Free deployment on Streamlit Community Cloud

---

## 🧠 Architecture Overview


---

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **LLM Orchestration**: LangChain
- **Embeddings**: OpenAI `text-embedding-3-small`
- **Vector Store**: FAISS
- **Content Extraction**: UnstructuredURLLoader
- **Language Model**: OpenAI Chat Models

---

## 🚀 Running Locally

```bash
pip install -r requirements.txt
OPENAI_API_KEY=your_api_key_here
streamlit run app.py

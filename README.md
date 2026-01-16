# InsightForge 🔍📊  
**AI-Powered News Research & Question Answering Tool**

🌐 Live Demo: https://insightforge-4e3pnp3kwd5b6votnbuzpl.streamlit.app/

InsightForge is a Retrieval-Augmented Generation (RAG) application that allows users to ingest online news articles, build a semantic search index, and ask natural-language questions with answers grounded strictly in source content.

The project demonstrates a complete end-to-end RAG pipeline using modern LLM tooling, vector search, and a clean modular architecture.

---

## 🚀 Features

- 🌐 Ingest up to 3 news article URLs  
- ✂️ Intelligent text chunking with overlap  
- 🧠 Semantic embeddings using OpenAI  
- ⚡ Fast similarity search with FAISS  
- ❓ Natural-language Q&A grounded in retrieved context  
- 🔗 Transparent source attribution  
- ☁️ Deployed for free on Streamlit Community Cloud  

---

## 🧠 High-Level Architecture

```
User
  ↓
Streamlit UI
  ↓
URL Loader (Unstructured)
  ↓
Text Chunking
  ↓
Embeddings (OpenAI)
  ↓
FAISS Vector Index
  ↓
Retriever (Top-K Similarity Search)
  ↓
LLM (Chat Model)
  ↓
Answer + Sources
```

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit  
- **LLM Orchestration**: LangChain  
- **Language Model**: OpenAI Chat Models  
- **Embeddings**: OpenAI `text-embedding-3-small`  
- **Vector Store**: FAISS  
- **Content Extraction**: UnstructuredURLLoader  
- **Deployment**: Streamlit Community Cloud  

---

## 📂 Project Structure

```
insightforge/
├── app.py                 # Streamlit entry point
├── config.py              # Centralized configuration
├── requirements.txt
├── core/
│   ├── loaders.py         # URL ingestion
│   ├── splitter.py        # Text chunking logic
│   ├── vectorstore.py     # FAISS index operations
│   ├── rag.py             # RAG pipeline
│   └── utils.py           # Helper utilities
```

---

## ⚙️ How It Works

1. **URL Ingestion**  
   Articles are loaded using `UnstructuredURLLoader`, extracting readable text from web pages.

2. **Text Chunking**  
   Documents are split into overlapping chunks (1000 chars, 150 overlap) to preserve semantic continuity.

3. **Embedding & Indexing**  
   Each chunk is embedded using OpenAI embeddings and stored in a FAISS vector index.

4. **Retrieval-Augmented Generation (RAG)**  
   - User query is embedded  
   - Top-K relevant chunks are retrieved  
   - Retrieved context is injected into the prompt  
   - LLM generates an answer strictly from context  

5. **Source Attribution**  
   URLs used in the answer are displayed for transparency and trust.

---

## ▶️ Run Locally

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Set environment variables
Create a `.env` file:
```bash
OPENAI_API_KEY=your_api_key_here
```

### 3. Run the app
```bash
streamlit run app.py
```

---

## ☁️ Free Deployment on Streamlit Cloud

1. Push this repository to GitHub  
2. Go to Streamlit Community Cloud → **Create App**  
3. Select your repo and branch  
4. Set main file path:
```
app.py
```
5. Add secrets:
```toml
OPENAI_API_KEY="your_api_key_here"
```

---

## ⚠️ Notes & Limitations

- Some websites block automated content extraction  
- If a URL loads no text, try a different source  
- FAISS index is stored locally (not shared across users)  
- Designed for research/demo scale workloads  

---

## 📌 Future Enhancements

- Multi-agent research workflows  
- Incremental indexing  
- Multi-document summarization  
- Exportable citations (PDF/Markdown)  
- Cloud vector database support  
- User session persistence  

---

## 👨‍💻 Author

Built by **Smit Rami**

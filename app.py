import os

import streamlit as st
from dotenv import load_dotenv

from config import (
    APP_TITLE,
    SIDEBAR_TITLE,
    MAX_URLS,
    INDEX_DIR,
    CHUNK_SIZE,
    CHUNK_OVERLAP,
    SEPARATORS,
    TOP_K,
    EMBEDDING_MODEL,
    CHAT_MODEL,
    TEMPERATURE,
    ALLOW_DANGEROUS_DESERIALIZATION,
)

from core.utils import clean_urls
from core.loaders import load_documents_from_urls
from core.splitter import split_documents
from core.vectorstore import build_and_save_faiss_index, load_faiss_index
from core.rag import build_rag_chain, run_query, extract_sources


load_dotenv()

st.title(APP_TITLE)
st.sidebar.title(SIDEBAR_TITLE)

# --- URL Inputs ---
raw_urls = []
for i in range(MAX_URLS):
    raw_urls.append(st.sidebar.text_input(f"URL {i+1}"))

process_url_clicked = st.sidebar.button("Build Index")
main_placeholder = st.empty()

# --- Build Index Flow ---
if process_url_clicked:
    urls = clean_urls(raw_urls)
    if not urls:
        st.error("Please provide at least one valid URL.")
        st.stop()

    main_placeholder.text("Loading articles...✅")
    docs = load_documents_from_urls(urls)
    if not docs:
        st.error(
            "No text could be extracted from these URLs (blocked/empty pages). Try different URLs."
        )
        st.stop()

    main_placeholder.text("Splitting into chunks...✅")
    chunks = split_documents(
        docs,
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        separators=SEPARATORS,
    )
    if not chunks:
        st.error(
            "Loaded content but chunking produced no usable chunks. Try different URLs."
        )
        st.stop()

    main_placeholder.text(f"Building FAISS index from {len(chunks)} chunks...✅")
    build_and_save_faiss_index(
        chunks=chunks,
        index_dir=INDEX_DIR,
        embedding_model=EMBEDDING_MODEL,
    )
    st.success(f"Index saved to '{INDEX_DIR}'. You can now ask questions.")

# --- Query Flow ---
query = main_placeholder.text_input("Question: ")
if query:
    if not os.path.isdir(INDEX_DIR):
        st.error("No index found. Click 'Build Index' first.")
        st.stop()

    vectorstore = load_faiss_index(
        index_dir=INDEX_DIR,
        embedding_model=EMBEDDING_MODEL,
        allow_dangerous_deserialization=ALLOW_DANGEROUS_DESERIALIZATION,
    )

    rag_chain = build_rag_chain(
        vectorstore=vectorstore,
        chat_model=CHAT_MODEL,
        temperature=TEMPERATURE,
        top_k=TOP_K,
    )

    result = run_query(rag_chain, query)

    st.header("Answer")
    st.write(result.get("answer", ""))

    sources = extract_sources(result)
    if sources:
        st.subheader("Sources")
        for s in sources:
            st.write(s)

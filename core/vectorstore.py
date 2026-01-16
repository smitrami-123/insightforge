from __future__ import annotations

import os
from typing import List

from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings


def build_and_save_faiss_index(
    chunks: List[Document],
    index_dir: str,
    embedding_model: str,
) -> None:
    """Create FAISS index from chunks and persist it locally."""
    embeddings = OpenAIEmbeddings(model=embedding_model)
    vs = FAISS.from_documents(chunks, embeddings)
    vs.save_local(index_dir)


def load_faiss_index(
    index_dir: str,
    embedding_model: str,
    allow_dangerous_deserialization: bool = True,
) -> FAISS:
    """Load a persisted FAISS index."""
    if not os.path.isdir(index_dir):
        raise FileNotFoundError(f"Index directory not found: {index_dir}")

    embeddings = OpenAIEmbeddings(model=embedding_model)
    return FAISS.load_local(
        index_dir,
        embeddings,
        allow_dangerous_deserialization=allow_dangerous_deserialization,
    )

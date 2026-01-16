from __future__ import annotations

from typing import List

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents(
    docs: List[Document],
    chunk_size: int,
    chunk_overlap: int,
    separators: List[str],
) -> List[Document]:
    """Split documents into overlapping chunks for better retrieval."""
    splitter = RecursiveCharacterTextSplitter(
        separators=separators,
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )
    chunks = splitter.split_documents(docs)
    return [c for c in chunks if c.page_content and c.page_content.strip()]

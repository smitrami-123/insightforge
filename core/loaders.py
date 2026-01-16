from __future__ import annotations

from typing import List

from langchain_community.document_loaders import UnstructuredURLLoader
from langchain_core.documents import Document


def _ensure_nltk_punkt() -> None:
    """Ensure NLTK punkt tokenizer is available (needed by unstructured in some setups)."""
    try:
        import nltk
        try:
            nltk.data.find("tokenizers/punkt")
        except LookupError:
            nltk.download("punkt", quiet=True)
    except Exception:
        # If NLTK isn't installed or download fails, loader may still work depending on environment.
        pass


def load_documents_from_urls(urls: List[str]) -> List[Document]:
    """Load web pages via UnstructuredURLLoader and filter empty docs."""
    _ensure_nltk_punkt()

    loader = UnstructuredURLLoader(urls=urls)
    docs = loader.load()
    return [d for d in docs if d.page_content and d.page_content.strip()]

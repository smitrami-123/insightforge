from __future__ import annotations

from typing import Dict, Any, List

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


def build_rag_components(
    vectorstore,
    chat_model: str,
    temperature: float,
    top_k: int,
):
    """
    Build modular RAG components without relying on the monolithic `langchain` package.
    Returns: (llm, retriever, prompt)
    """
    llm = ChatOpenAI(model=chat_model, temperature=temperature)
    retriever = vectorstore.as_retriever(search_kwargs={"k": top_k})

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a helpful assistant. Answer using ONLY the provided context. "
                "If not enough information is available, say you don't know.",
            ),
            ("human", "Question: {question}\n\nContext:\n{context}\n\nAnswer:"),
        ]
    )

    return llm, retriever, prompt


def run_query(llm, retriever, prompt, question: str) -> Dict[str, Any]:
    """
    Retrieval + Prompt + LLM (manual RAG).
    Returns a normalized result dict:
      - answer: str
      - context: List[Document]
    """
    docs = retriever.get_relevant_documents(question)

    context_text = "\n\n".join(
        [d.page_content for d in docs if getattr(d, "page_content", None)]
    ).strip()

    if not context_text:
        return {"answer": "I don't know.", "context": docs}

    messages = prompt.format_messages(question=question, context=context_text)
    response = llm.invoke(messages)

    # response can be an AIMessage
    answer = getattr(response, "content", str(response))
    return {"answer": answer, "context": docs}


def extract_sources(result: Dict[str, Any]) -> List[str]:
    """
    Extract unique sources from retrieved docs metadata.
    """
    ctx_docs = result.get("context", [])
    sources = []
    for d in ctx_docs:
        src = getattr(d, "metadata", {}).get("source")
        if src:
            sources.append(src)

    # unique preserve order
    seen = set()
    out = []
    for s in sources:
        if s not in seen:
            seen.add(s)
            out.append(s)
    return out

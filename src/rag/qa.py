from pathlib import Path

from src.rag.retriever import ReviewRetriever


def build_context(results) -> str:
    return "\n".join(
        f"Avaliação {item.rating}/5: {item.text}"
        for item in results
    )


def answer_with_retrieval(
    query: str,
    top_k: int = 5,
    generate: bool = False,
    data_path: Path | None = None,
) -> dict:
    """Retrieve evidence and optionally pass it to a generative model."""
    if not query.strip():
        raise ValueError("Query cannot be empty.")
    if top_k < 1 or top_k > 20:
        raise ValueError("top_k must be between 1 and 20.")

    retriever = ReviewRetriever.from_csv(data_path) if data_path else ReviewRetriever.from_csv()
    results = retriever.search(query, top_k=top_k)
    context = build_context(results)
    response = None

    if generate:
        from src.rag.llm import generate_answer
        response = generate_answer(query, context)

    return {
        "query": query,
        "context": context,
        "sources": [item.review_id for item in results],
        "answer": response,
        "mode": "rag+llm" if generate else "retrieval-only",
    }


if __name__ == "__main__":
    result = answer_with_retrieval("pedidos atrasados")
    print(result["context"])

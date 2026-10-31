from .retriever import ReviewRetriever


def build_context(results) -> str:
    return "\n".join(
        f"Avaliação {item.rating}/5: {item.text}"
        for item in results
    )


def answer_with_retrieval(query: str, top_k: int = 5, generate: bool = False) -> dict:
    """Retrieve evidence and optionally pass it to a generative model."""
    retriever = ReviewRetriever.from_csv()
    results = retriever.search(query, top_k=top_k)
    context = build_context(results)
    response = None

    if generate:
        from .llm import generate_answer
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

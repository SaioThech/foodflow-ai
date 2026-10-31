from .retriever import ReviewRetriever


def build_context(results) -> str:
    return "\n".join(
        f"Avaliação {item.rating}/5: {item.text}" for item in results
    )


def answer_with_retrieval(query: str, top_k: int = 5) -> dict:
    """RAG-ready interface: retrieve evidence before an LLM is called."""
    retriever = ReviewRetriever.from_csv()
    results = retriever.search(query, top_k=top_k)
    context = build_context(results)
    return {
        "query": query,
        "context": context,
        "sources": [item.review_id for item in results],
        "next_step": "Enviar o contexto para um LLM e gerar a resposta fundamentada.",
    }


if __name__ == "__main__":
    result = answer_with_retrieval("pedidos atrasados")
    print(result["context"])

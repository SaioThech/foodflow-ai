import pandas as pd

from src.rag.retriever import ReviewRetriever


def test_retriever_returns_ranked_results():
    reviews = pd.DataFrame(
        {
            "review_id": ["V1", "V2"],
            "review_text": ["pedido chegou atrasado", "comida excelente e rápida"],
            "rating": [1, 5],
        }
    )
    retriever = ReviewRetriever(reviews)
    results = retriever.search("pedido atrasado", top_k=1)
    assert len(results) == 1
    assert results[0].review_id == "V1"

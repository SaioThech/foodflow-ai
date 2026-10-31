import pandas as pd

from src.rag.qa import answer_with_retrieval


def test_rag_retrieval_returns_sources(tmp_path):
    data = pd.DataFrame(
        {
            "review_id": ["r1", "r2"],
            "review_text": ["pedido chegou atrasado", "entrega muito rápida"],
            "rating": [2, 5],
        }
    )
    csv_path = tmp_path / "reviews.csv"
    data.to_csv(csv_path, index=False)

    result = answer_with_retrieval("pedido atrasado", top_k=1, data_path=csv_path)

    assert result["mode"] == "retrieval-only"
    assert result["sources"] == ["r1"]
    assert "atrasado" in result["context"]

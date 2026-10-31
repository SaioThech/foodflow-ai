"""Optional Hugging Face sentiment inference.

Install the optional dependencies first:
    pip install -r requirements-optional.txt
"""

from transformers import pipeline

MODEL_NAME = "cardiffnlp/twitter-xlm-roberta-base-sentiment"


def build_classifier():
    return pipeline("sentiment-analysis", model=MODEL_NAME)


def predict(text: str) -> dict:
    classifier = build_classifier()
    result = classifier(text, truncation=True)[0]
    return {"label": result["label"], "score": float(result["score"])}


if __name__ == "__main__":
    print(predict("O pedido chegou rápido e a comida estava excelente!"))

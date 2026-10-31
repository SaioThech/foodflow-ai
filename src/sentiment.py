from pathlib import Path

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

DATA_PATH = Path("data/generated/reviews.csv")


def label_sentiment(rating: int) -> str:
    if rating <= 2:
        return "negative"
    if rating == 3:
        return "neutral"
    return "positive"


def main():
    df = pd.read_csv(DATA_PATH)
    df["sentiment"] = df["rating"].apply(label_sentiment)

    X_train, X_test, y_train, y_test = train_test_split(
        df["review_text"], df["sentiment"], test_size=0.2, random_state=42, stratify=df["sentiment"]
    )

    model = Pipeline([
        ("tfidf", TfidfVectorizer(ngram_range=(1, 2), min_df=1)),
        ("classifier", LogisticRegression(max_iter=1000)),
    ])
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    print(classification_report(y_test, predictions, zero_division=0))


if __name__ == "__main__":
    main()

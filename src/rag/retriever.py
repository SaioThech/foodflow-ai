from dataclasses import dataclass
from pathlib import Path

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

DATA_PATH = Path("data/generated/reviews.csv")


@dataclass
class SearchResult:
    review_id: str
    text: str
    rating: int
    score: float


class ReviewRetriever:
    """Small, dependency-light retrieval layer for the FoodFlow RAG demo."""

    def __init__(self, reviews: pd.DataFrame):
        self.reviews = reviews.reset_index(drop=True)
        self.vectorizer = TfidfVectorizer(ngram_range=(1, 2), min_df=1)
        self.matrix = self.vectorizer.fit_transform(self.reviews["review_text"])

    @classmethod
    def from_csv(cls, path: Path = DATA_PATH):
        if not path.exists():
            raise FileNotFoundError("Run 'python data/generate_data.py' first.")
        return cls(pd.read_csv(path))

    def search(self, query: str, top_k: int = 5) -> list[SearchResult]:
        query_vector = self.vectorizer.transform([query])
        scores = cosine_similarity(query_vector, self.matrix).ravel()
        indices = scores.argsort()[::-1][:top_k]
        return [
            SearchResult(
                review_id=str(self.reviews.iloc[i]["review_id"]),
                text=str(self.reviews.iloc[i]["review_text"]),
                rating=int(self.reviews.iloc[i]["rating"]),
                score=float(scores[i]),
            )
            for i in indices
        ]

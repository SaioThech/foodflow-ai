from typing import Any

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field

from src.predict_cancellation import predict_cancellation
from src.rag.qa import answer_with_retrieval

app = FastAPI(
    title="FoodFlow AI API",
    version="1.1.0",
    description="API demonstrativa para previsão de cancelamento e consulta RAG sobre avaliações.",
)


class OrderInput(BaseModel):
    order_hour: int = Field(ge=0, le=23)
    category: str
    order_value: float = Field(gt=0)
    delivery_fee: float = Field(ge=0)
    discount: float = Field(ge=0)
    distance_km: float = Field(gt=0)
    preparation_time_min: int = Field(gt=0)
    traffic: str
    contract: str
    payment_method: str


class ReviewQuery(BaseModel):
    query: str = Field(min_length=2, max_length=500)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "foodflow-ai"}


@app.post("/predict/cancellation")
def cancellation(order: OrderInput) -> dict[str, Any]:
    try:
        probability = predict_cancellation(order.model_dump())
    except FileNotFoundError as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc

    return {
        "cancellation_probability": round(probability, 4),
        "risk": "high" if probability >= 0.5 else "low",
    }


@app.post("/rag/search")
def rag_search(
    payload: ReviewQuery,
    top_k: int = Query(default=5, ge=1, le=20),
) -> dict[str, Any]:
    try:
        return answer_with_retrieval(payload.query, top_k=top_k, generate=False)
    except FileNotFoundError as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc

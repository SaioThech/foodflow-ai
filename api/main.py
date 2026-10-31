from pathlib import Path
from typing import Any

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from src.predict_cancellation import predict_cancellation

app = FastAPI(
    title="FoodFlow AI API",
    version="1.0.0",
    description="API demonstrativa para previsão de cancelamento de pedidos.",
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

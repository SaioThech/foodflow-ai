from pathlib import Path
import json

import joblib
import pandas as pd
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, roc_auc_score
from sklearn.model_selection import train_test_split

DATA_PATH = Path("data/generated/orders.csv")
MODEL_PATH = Path("models/cancellation_model.joblib")
REPORT_PATH = Path("reports/cancellation_metrics.json")
FEATURES = [
    "order_hour", "category", "order_value", "delivery_fee", "discount",
    "distance_km", "preparation_time_min", "traffic", "contract", "payment_method"
]


def main():
    if not DATA_PATH.exists():
        raise FileNotFoundError("Run 'python data/generate_data.py' first.")
    if not MODEL_PATH.exists():
        raise FileNotFoundError("Run 'python src/train_cancellation.py' first.")

    df = pd.read_csv(DATA_PATH)
    X = df[FEATURES]
    y = df["cancelled"]
    _, X_test, _, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    model = joblib.load(MODEL_PATH)
    predictions = model.predict(X_test)
    probabilities = model.predict_proba(X_test)[:, 1]
    metrics = {
        "accuracy": accuracy_score(y_test, predictions),
        "precision": precision_score(y_test, predictions, zero_division=0),
        "recall": recall_score(y_test, predictions, zero_division=0),
        "f1": f1_score(y_test, predictions, zero_division=0),
        "roc_auc": roc_auc_score(y_test, probabilities),
        "test_samples": int(len(y_test)),
    }
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(json.dumps(metrics, indent=2), encoding="utf-8")
    for name, value in metrics.items():
        print(f"{name}: {value:.4f}" if isinstance(value, float) else f"{name}: {value}")
    print(f"Métricas salvas em: {REPORT_PATH}")


if __name__ == "__main__":
    main()

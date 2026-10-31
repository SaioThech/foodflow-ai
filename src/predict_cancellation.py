from pathlib import Path

import joblib
import pandas as pd

MODEL_PATH = Path("models/cancellation_model.joblib")


def predict_cancellation(order: dict) -> float:
    """Return the estimated cancellation probability for one order."""
    if not MODEL_PATH.exists():
        raise FileNotFoundError("Model not found. Run 'python src/train_cancellation.py' first.")
    model = joblib.load(MODEL_PATH)
    frame = pd.DataFrame([order])
    return float(model.predict_proba(frame)[0, 1])

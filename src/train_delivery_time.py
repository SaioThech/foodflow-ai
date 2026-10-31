from pathlib import Path

import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

DATA_PATH = Path("data/generated/orders.csv")
MODEL_PATH = Path("models/delivery_time_model.joblib")
REPORT_PATH = Path("reports/delivery_time_metrics.json")

FEATURES = [
    "order_hour", "category", "order_value", "distance_km",
    "preparation_time_min", "traffic", "payment_method"
]
TARGET = "delivery_time_min"


def main():
    if not DATA_PATH.exists():
        raise FileNotFoundError("Run 'python data/generate_data.py' first.")

    df = pd.read_csv(DATA_PATH)
    X = df[FEATURES]
    y = df[TARGET]

    numeric = ["order_hour", "order_value", "distance_km", "preparation_time_min"]
    categorical = ["category", "traffic", "payment_method"]

    preprocessor = ColumnTransformer([
        ("numeric", SimpleImputer(strategy="median"), numeric),
        ("categorical", Pipeline([
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(handle_unknown="ignore")),
        ]), categorical),
    ])

    model = Pipeline([
        ("preprocessor", preprocessor),
        ("regressor", RandomForestRegressor(
            n_estimators=200, random_state=42, n_jobs=-1
        )),
    ])

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    metrics = {
        "mae_minutes": float(mean_absolute_error(y_test, predictions)),
        "rmse_minutes": float(mean_squared_error(y_test, predictions) ** 0.5),
        "r2": float(r2_score(y_test, predictions)),
        "test_samples": int(len(y_test)),
    }

    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    REPORT_PATH.write_text(pd.Series(metrics).to_json(indent=2), encoding="utf-8")

    print("=== Delivery Time Model ===")
    for key, value in metrics.items():
        print(f"{key}: {value:.4f}" if isinstance(value, float) else f"{key}: {value}")
    print(f"Modelo salvo em: {MODEL_PATH}")


if __name__ == "__main__":
    main()

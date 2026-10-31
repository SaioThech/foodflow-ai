from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

DATA_DIR = Path("data/generated")
REPORT_DIR = Path("reports")


def main():
    REPORT_DIR.mkdir(exist_ok=True)
    orders = pd.read_csv(DATA_DIR / "orders.csv")
    reviews = pd.read_csv(DATA_DIR / "reviews.csv")

    orders["order_date"] = pd.to_datetime(orders["order_date"])
    orders["gross_value"] = orders["order_value"] + orders["delivery_fee"] - orders["discount"]

    summary = pd.DataFrame({
        "metric": [
            "total_orders", "cancelled_orders", "cancellation_rate",
            "gross_revenue", "avg_order_value", "avg_delivery_time_min",
            "avg_distance_km", "reviews"
        ],
        "value": [
            len(orders),
            int(orders["cancelled"].sum()),
            orders["cancelled"].mean(),
            orders["gross_value"].sum(),
            orders["order_value"].mean(),
            orders["delivery_time_min"].mean(),
            orders["distance_km"].mean(),
            len(reviews),
        ],
    })
    summary.to_csv(REPORT_DIR / "business_summary.csv", index=False)
    print(summary.to_string(index=False))

    daily = orders.groupby("order_date", as_index=False).agg(
        orders=("order_id", "count"),
        revenue=("gross_value", "sum"),
        cancellation_rate=("cancelled", "mean"),
    )
    daily.to_csv(REPORT_DIR / "daily_metrics.csv", index=False)

    plt.figure(figsize=(10, 5))
    plt.plot(daily["order_date"], daily["orders"])
    plt.title("FoodFlow — Pedidos por dia")
    plt.xlabel("Data")
    plt.ylabel("Pedidos")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(REPORT_DIR / "orders_over_time.png", dpi=150)
    plt.close()

    by_category = orders.groupby("category", as_index=False).agg(
        orders=("order_id", "count"),
        revenue=("gross_value", "sum"),
        cancellation_rate=("cancelled", "mean"),
    ).sort_values("revenue", ascending=False)
    by_category.to_csv(REPORT_DIR / "category_metrics.csv", index=False)

    print("\nRelatórios salvos em reports/")


if __name__ == "__main__":
    main()

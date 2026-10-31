from pathlib import Path

import numpy as np
import pandas as pd

SEED = 42
N_CUSTOMERS = 5000
N_RESTAURANTS = 300
N_COURIERS = 800
N_ORDERS = 30000

OUTPUT_DIR = Path(__file__).resolve().parent / "generated"

rng = np.random.default_rng(SEED)

CITIES = ["Rio de Janeiro", "Niterói", "Petrópolis", "Nova Friburgo", "Juiz de Fora", "São Paulo"]
CATEGORIES = ["Hambúrguer", "Pizza", "Comida Brasileira", "Japonesa", "Açaí", "Massas", "Lanches", "Saudável"]
PAYMENTS = ["PIX", "Cartão de crédito", "Cartão de débito", "Carteira digital"]
CONTRACTS = ["Avulso", "Mensalidade FoodFlow"]


def weighted_choice(values, probabilities, size):
    return rng.choice(values, size=size, p=probabilities)


def generate_customers():
    return pd.DataFrame({
        "customer_id": [f"C{i:05d}" for i in range(1, N_CUSTOMERS + 1)],
        "city": rng.choice(CITIES, N_CUSTOMERS),
        "age": rng.integers(18, 71, N_CUSTOMERS),
        "signup_channel": weighted_choice(["Instagram", "Google", "Indicação", "Orgânico"], [0.30, 0.25, 0.20, 0.25], N_CUSTOMERS),
        "is_premium": rng.choice([0, 1], N_CUSTOMERS, p=[0.72, 0.28]),
    })


def generate_restaurants():
    return pd.DataFrame({
        "restaurant_id": [f"R{i:04d}" for i in range(1, N_RESTAURANTS + 1)],
        "city": rng.choice(CITIES, N_RESTAURANTS),
        "category": rng.choice(CATEGORIES, N_RESTAURANTS),
        "restaurant_rating": np.round(np.clip(rng.normal(4.35, 0.35, N_RESTAURANTS), 3.0, 5.0), 2),
        "avg_preparation_min": rng.integers(12, 41, N_RESTAURANTS),
        "is_partner_premium": rng.choice([0, 1], N_RESTAURANTS, p=[0.75, 0.25]),
    })


def generate_couriers():
    return pd.DataFrame({
        "courier_id": [f"E{i:04d}" for i in range(1, N_COURIERS + 1)],
        "city": rng.choice(CITIES, N_COURIERS),
        "vehicle": rng.choice(["Moto", "Bicicleta", "Carro"], N_COURIERS, p=[0.68, 0.22, 0.10]),
        "experience_months": rng.integers(1, 85, N_COURIERS),
    })


def generate_orders(customers, restaurants, couriers):
    customer_ids = rng.choice(customers["customer_id"], N_ORDERS)
    restaurant_ids = rng.choice(restaurants["restaurant_id"], N_ORDERS)
    courier_ids = rng.choice(couriers["courier_id"], N_ORDERS)
    dates = pd.to_datetime("2026-01-01") + pd.to_timedelta(rng.integers(0, 273, N_ORDERS), unit="D")
    hours = weighted_choice(np.arange(10, 24), [0.03, 0.03, 0.04, 0.05, 0.07, 0.09, 0.11, 0.13, 0.14, 0.12, 0.09, 0.06, 0.03, 0.01], N_ORDERS)
    distance = np.round(np.clip(rng.gamma(2.0, 2.0, N_ORDERS), 0.5, 18), 2)
    value = np.round(np.clip(rng.lognormal(3.6, 0.45, N_ORDERS), 18, 250), 2)
    prep = rng.integers(10, 46, N_ORDERS)
    delivery = np.maximum(8, np.round(prep * 0.55 + distance * rng.uniform(3.0, 5.0, N_ORDERS) + rng.normal(4, 5, N_ORDERS)).astype(int))
    traffic = weighted_choice(["Baixo", "Médio", "Alto"], [0.35, 0.45, 0.20], N_ORDERS)
    discount = np.round(np.where(rng.random(N_ORDERS) < 0.32, rng.uniform(3, 25, N_ORDERS), 0), 2)

    # Cancelamento sintético: maior probabilidade com distância, trânsito e preparação longa.
    logit = -4.1 + 0.11 * (prep - 25) + 0.10 * (distance - 4) + 0.65 * (traffic == "Alto") + 0.45 * (hours >= 21)
    probability = 1 / (1 + np.exp(-logit))
    cancelled = rng.random(N_ORDERS) < probability

    return pd.DataFrame({
        "order_id": [f"FF{i:07d}" for i in range(1, N_ORDERS + 1)],
        "customer_id": customer_ids,
        "restaurant_id": restaurant_ids,
        "courier_id": courier_ids,
        "order_date": dates.strftime("%Y-%m-%d"),
        "order_hour": hours,
        "category": rng.choice(CATEGORIES, N_ORDERS),
        "order_value": value,
        "delivery_fee": np.round(np.clip(3 + distance * 1.2 + rng.normal(0, 1, N_ORDERS), 3, 25), 2),
        "discount": discount,
        "distance_km": distance,
        "preparation_time_min": prep,
        "delivery_time_min": delivery,
        "traffic": traffic,
        "contract": rng.choice(CONTRACTS, N_ORDERS, p=[0.82, 0.18]),
        "payment_method": rng.choice(PAYMENTS, N_ORDERS, p=[0.45, 0.30, 0.12, 0.13]),
        "cancelled": cancelled.astype(int),
    })


def generate_payments(orders):
    return pd.DataFrame({
        "order_id": orders["order_id"],
        "payment_status": np.where(orders["cancelled"].eq(1), rng.choice(["Estornado", "Cancelado"], len(orders)), "Aprovado"),
        "net_value": np.round(orders["order_value"] + orders["delivery_fee"] - orders["discount"], 2),
    })


def generate_reviews(orders, restaurants):
    completed = orders[orders["cancelled"] == 0].copy()
    n = min(len(completed), int(len(orders) * 0.72))
    reviews = completed.sample(n=n, random_state=SEED)
    ratings = np.clip(np.rint(rng.normal(4.2, 1.0, n)), 1, 5).astype(int)
    texts = {
        1: "Pedido chegou muito atrasado e a experiência foi ruim.",
        2: "Demorou mais do que o esperado e a comida poderia estar melhor.",
        3: "Pedido razoável, mas o tempo de entrega poderia melhorar.",
        4: "Boa experiência, pedido chegou bem e no prazo.",
        5: "Excelente experiência! Pedido rápido, comida boa e atendimento ótimo.",
    }
    return pd.DataFrame({
        "review_id": [f"V{i:07d}" for i in range(1, n + 1)],
        "order_id": reviews["order_id"].values,
        "customer_id": reviews["customer_id"].values,
        "rating": ratings,
        "review_text": [texts[r] for r in ratings],
    })


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    customers = generate_customers()
    restaurants = generate_restaurants()
    couriers = generate_couriers()
    orders = generate_orders(customers, restaurants, couriers)
    payments = generate_payments(orders)
    reviews = generate_reviews(orders, restaurants)

    for name, frame in {
        "customers": customers,
        "restaurants": restaurants,
        "couriers": couriers,
        "orders": orders,
        "payments": payments,
        "reviews": reviews,
    }.items():
        frame.to_csv(OUTPUT_DIR / f"{name}.csv", index=False)
        print(f"{name}: {len(frame):,} registros")

    print(f"\nDados gerados em: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()

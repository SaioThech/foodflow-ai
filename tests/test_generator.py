import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from data.generate_data import generate_customers, generate_restaurants, generate_couriers, generate_orders


def test_generated_tables_have_expected_sizes():
    customers = generate_customers()
    restaurants = generate_restaurants()
    couriers = generate_couriers()
    orders = generate_orders(customers, restaurants, couriers)

    assert len(customers) == 5000
    assert len(restaurants) == 300
    assert len(couriers) == 800
    assert len(orders) == 30000


def test_orders_have_valid_target_and_values():
    customers = generate_customers()
    restaurants = generate_restaurants()
    couriers = generate_couriers()
    orders = generate_orders(customers, restaurants, couriers)

    assert set(orders["cancelled"].unique()).issubset({0, 1})
    assert (orders["order_value"] > 0).all()
    assert (orders["distance_km"] > 0).all()

"""Analyze dummy customer orders data using only the Python standard library."""

import random
from collections import defaultdict
from datetime import date, timedelta

CUSTOMERS = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]
PRODUCTS = {"Laptop": 900.0, "Phone": 600.0, "Headphones": 120.0, "Keyboard": 50.0, "Mouse": 25.0}


def generate_orders(n=50, seed=42):
    """Create a list of dummy orders."""
    random.seed(seed)
    start = date(2026, 1, 1)
    orders = []
    for order_id in range(1, n + 1):
        product = random.choice(list(PRODUCTS))
        quantity = random.randint(1, 3)
        orders.append({
            "order_id": order_id,
            "customer": random.choice(CUSTOMERS),
            "product": product,
            "quantity": quantity,
            "total": PRODUCTS[product] * quantity,
            "date": start + timedelta(days=random.randint(0, 179)),
        })
    return orders


def analyze(orders):
    total_revenue = sum(o["total"] for o in orders)
    print(f"Total orders:        {len(orders)}")
    print(f"Total revenue:       ${total_revenue:,.2f}")
    print(f"Average order value: ${total_revenue / len(orders):,.2f}")

    by_customer = defaultdict(float)
    by_product = defaultdict(int)
    by_month = defaultdict(float)
    for o in orders:
        by_customer[o["customer"]] += o["total"]
        by_product[o["product"]] += o["quantity"]
        by_month[o["date"].strftime("%Y-%m")] += o["total"]

    print("\nRevenue by customer:")
    for name, amount in sorted(by_customer.items(), key=lambda x: x[1], reverse=True):
        print(f"  {name:<10} ${amount:>10,.2f}")

    print("\nUnits sold by product:")
    for product, qty in sorted(by_product.items(), key=lambda x: x[1], reverse=True):
        print(f"  {product:<12} {qty:>4}")

    print("\nRevenue by month:")
    for month in sorted(by_month):
        print(f"  {month}  ${by_month[month]:>10,.2f}")

    top = max(by_customer, key=by_customer.get)
    print(f"\nTop customer: {top} (${by_customer[top]:,.2f})")


if __name__ == "__main__":
    analyze(generate_orders())

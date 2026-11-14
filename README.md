# testRepo

A simple Python project that analyzes dummy customer orders data.

## Requirements

- Python 3 (no external packages needed)

## Usage

### analyze_orders.py

Generates 50 dummy customer orders and prints a summary:

- Total orders, total revenue, and average order value
- Revenue by customer
- Units sold by product
- Revenue by month
- Top customer

```bash
python3 analyze_orders.py
```

Sample output (trimmed):

```
Total orders:        50
Total revenue:       $45,710.00
Average order value: $914.20

Revenue by customer:
  Diana      $ 12,400.00
  Charlie    $ 12,010.00
  ...

Top customer: Diana ($12,400.00)
```

The data uses a fixed random seed, so results are the same on every run. Change the `seed` argument in `generate_orders()` to get different data.

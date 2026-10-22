import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV files. IDs are the keys used to connect the tables.
customers = pd.read_csv("customers.csv", parse_dates=["registration_date"])
products = pd.read_csv("products.csv")
orders = pd.read_csv("orders.csv", parse_dates=["order_date"])
order_items = pd.read_csv("order_items.csv")
payments = pd.read_csv("payments.csv", parse_dates=["payment_date"])

# Example: create one analysis table by joining on IDs.
# You can also do joins in SQL in DBeaver and export the result to CSV.
sales = (
    order_items
    .merge(orders[["order_id", "order_date", "status", "customer_id"]], on="order_id", how="left")
    .merge(products[["product_id", "product_name", "category"]], on="product_id", how="left")
)

# Suggested first chart: monthly completed-order revenue.
completed_sales = sales[sales["status"] == "completed"].copy()
completed_sales["revenue"] = completed_sales["quantity"] * completed_sales["unit_price"]
monthly = completed_sales.groupby(completed_sales["order_date"].dt.to_period("M"))["revenue"].sum()
monthly.index = monthly.index.astype(str)

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(monthly.index, monthly.values, marker="o")
ax.set_title("Monthly Revenue from Completed Orders")
ax.set_xlabel("Month")
ax.set_ylabel("Revenue (€)")
ax.tick_params(axis="x", rotation=45)
ax.grid(axis="y", alpha=0.3)
fig.tight_layout()
plt.show()

# Student task: create a figure with at least 3 useful visualizations.

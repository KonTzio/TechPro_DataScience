# Retail Matplotlib Project Dataset

All data are fictional and generated for teaching.

## Files
- `customers.csv`: 180 customers
- `products.csv`: 30 products
- `orders.csv`: 650 orders
- `order_items.csv`: order line items (typically 1–5 per order; under 2,000 rows)
- `payments.csv`: one payment record per order

Each CSV has at most 7 columns. IDs are explicit keys and relationships are based on IDs, not names.

## Tables and relationships
- `customers.customer_id` (PK) -> `orders.customer_id` (FK)
- `products.product_id` (PK) -> `order_items.product_id` (FK)
- `orders.order_id` (PK) -> `order_items.order_id` (FK)
- `orders.order_id` (PK) -> `payments.order_id` (FK; one payment row per order)

## Column guide
### customers.csv
- `customer_id`: string ID, primary key
- `city`, `country`: strings
- `registration_date`: date in YYYY-MM-DD format

### products.csv
- `product_id`: string ID, primary key
- `product_name`, `category`: strings
- `unit_price`: decimal number

### orders.csv
- `order_id`: string ID, primary key
- `customer_id`: string foreign key
- `order_date`: date in YYYY-MM-DD format
- `status`: string (`completed`, `cancelled`, `returned`)

### order_items.csv
- `order_item_id`: string ID, primary key
- `order_id`, `product_id`: string foreign keys
- `quantity`: integer
- `unit_price`: decimal number representing the price paid per unit

### payments.csv
- `payment_id`: string ID, primary key
- `order_id`: string foreign key
- `payment_date`: date in YYYY-MM-DD format
- `amount`: decimal number
- `payment_method`: string

## Suggested SQL joins
```sql
SELECT
    o.order_date,
    p.category,
    SUM(oi.quantity * oi.unit_price) AS item_revenue
FROM orders AS o
JOIN order_items AS oi ON oi.order_id = o.order_id
JOIN products AS p ON p.product_id = oi.product_id
WHERE o.status = 'completed'
GROUP BY o.order_date, p.category
ORDER BY o.order_date;
```

## Teaching caveats
- Revenue from order items can be calculated as `quantity * unit_price`.
- For a simple net sales analysis, use only `completed` orders. Returned orders are included to support discussion of business definitions; this dataset does not record refund transactions.
- Cancelled orders have payment amount 0. Returned orders retain their original payment amount, so do not treat payments as net revenue without defining a policy.
- The dataset spans calendar year 2025 for orders.

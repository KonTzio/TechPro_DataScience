# E-Commerce Performance Dataset

As a Data Analyst, you have been provided with four clean, analysis-ready datasets reflecting various operational areas of an online retail company. All datasets cover a unified business context, but each is self-contained so you can choose one or more datasets to build your visualization dashboard.

---

## 1. `monthly_sales.csv`
* **Overview**: Aggregated monthly high-level financial and customer growth metrics covering a 1-year operating period (12 records).

### Data Dictionary

| Column Name | Data Type | Example | Description |
| :--- | :--- | :--- | :--- |
| `month` | Date (`YYYY-MM-DD`) | `2024-01-01` | The first day of the corresponding sales month. |
| `revenue` | Integer (USD) | `45000` | Total dollar revenue generated during the month. |
| `orders` | Integer | `600` | Total number of completed customer orders. |
| `average_order_value` | Float (USD) | `75.0` | Average monetary spend per order (`revenue / orders`). |
| `new_customers` | Integer | `120` | Count of first-time purchasing customers during the month. |
| `return_rate_pct` | Float (%) | `3.25` | Percentage of purchased items that were returned by customers. |

---

## 2. `product_sales.csv`
* **Overview**: Product-level performance summary comparing sales velocity, pricing, total revenue, and product reviews across multiple retail categories (25 records).

### Data Dictionary

| Column Name | Data Type | Example | Description |
| :--- | :--- | :--- | :--- |
| `product_name` | Text | `Wireless Earbuds` | Name of the individual product item. |
| `category` | Text | `Electronics` | Product line category (`Electronics`, `Apparel`, `Home & Kitchen`, `Beauty`, `Fitness`). |
| `units_sold` | Integer | `824` | Total volume of units sold across the period. |
| `avg_selling_price` | Float (USD) | `89.99` | Average retail listing price per unit sold. |
| `total_revenue` | Float (USD) | `74151.76` | Gross revenue earned from the product (`units_sold` × `avg_selling_price`). |
| `avg_rating` | Float (1.0 to 5.0) | `4.6` | Customer satisfaction rating averaged across all submitted customer reviews. |

---

## 3. `customer_data.csv`
* **Overview**: Customer demographic and purchasing behavior details sampled across major metropolitan markets (150 records).

### Data Dictionary

| Column Name | Data Type | Example | Description |
| :--- | :--- | :--- | :--- |
| `customer_id` | Text | `CUST-1000` | Unique alphanumeric identifier for each customer. |
| `city` | Text | `New York` | Primary delivery location/city of the customer. |
| `age` | Integer | `29` | Age of the customer in years. |
| `total_orders` | Integer | `14` | Total lifetime order count placed by the customer. |
| `avg_order_value` | Float (USD) | `85.50` | Average dollar amount spent per order. |
| `total_spending` | Float (USD) | `1197.00` | Cumulative lifetime dollar spend (`total_orders` × `avg_order_value`). |

---

## 4. `daily_website.csv`
* **Overview**: Daily digital marketing and website engagement performance indicators spanning a 90-day period (90 records).

### Data Dictionary

| Column Name | Data Type | Example | Description |
| :--- | :--- | :--- | :--- |
| `date` | Date (`YYYY-MM-DD`) | `2024-06-01` | Daily calendar date recorded over a 90-day tracking period. |
| `daily_visitors` | Integer | `2840` | Total number of web sessions / unique visitors recorded on the site. |
| `conversions` | Integer | `92` | Total number of desired actions completed on site (e.g., purchases, registrations). |
| `ad_spend_usd` | Float (USD) | `210.50` | Total dollar amount spent on digital marketing campaigns on that day (`0.00` if no active ad campaign). |
| `campaign_type` | Text | `Social Media Ad` | Marketing strategy run on that day (`No Campaign`, `Social Media Ad`, `Email Blast`, `Search Ad`). |
| `bounce_rate_pct` | Float (%) | `48.2` | Percentage of single-page visits where the user left without taking any action. |

---

from fastapi import FastAPI
import pandas as pd


# =========================================================
# CREATE FASTAPI APPLICATION
# =========================================================

app = FastAPI(
    title="Sales Analysis API",
    description="API for retrieving and analyzing sales data",
    version="1.0"
)


# =========================================================
# LOAD SALES DATA
# =========================================================

df = pd.read_csv("data/sales_data.csv")


# =========================================================
# DATA PROCESSING
# =========================================================

# Convert Date column to date format
df["Date"] = pd.to_datetime(df["Date"])

# Calculate Total Sales
df["Total_Sales"] = df["Quantity"] * df["Price"]


# =========================================================
# HOME ENDPOINT
# =========================================================

@app.get("/")
def home():
    return {
        "message": "Welcome to Sales Analysis API",
        "status": "API is running successfully"
    }


# =========================================================
# GET ALL SALES
# =========================================================

@app.get("/sales")
def get_sales():

    result = df.copy()

    # Convert dates to strings so FastAPI can return them
    result["Date"] = result["Date"].dt.strftime("%Y-%m-%d")

    # Convert dataframe to list of dictionaries
    return result.to_dict(orient="records")


# =========================================================
# TOTAL SALES / REVENUE
# =========================================================

@app.get("/sales/total")
def get_total_sales():

    total_revenue = df["Total_Sales"].sum()

    return {
        "total_revenue": float(total_revenue)
    }


# =========================================================
# AVERAGE SALE
# =========================================================

@app.get("/sales/average")
def get_average_sale():

    average_sale = df["Total_Sales"].mean()

    return {
        "average_sale": float(average_sale)
    }


# =========================================================
# HIGHEST SALE
# =========================================================

@app.get("/sales/highest")
def get_highest_sale():

    highest_sale = df["Total_Sales"].max()

    return {
        "highest_sale": float(highest_sale)
    }


# =========================================================
# LOWEST SALE
# =========================================================

@app.get("/sales/lowest")
def get_lowest_sale():

    lowest_sale = df["Total_Sales"].min()

    return {
        "lowest_sale": float(lowest_sale)
    }


# =========================================================
# TOTAL QUANTITY SOLD
# =========================================================

@app.get("/sales/quantity")
def get_total_quantity():

    total_quantity = df["Quantity"].sum()

    return {
        "total_quantity_sold": int(total_quantity)
    }


# =========================================================
# PRODUCT-WISE SALES
# =========================================================

@app.get("/sales/products")
def get_product_sales():

    product_sales = (
        df.groupby("Product")["Total_Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    return {
        str(product): float(sales)
        for product, sales in product_sales.items()
    }


# =========================================================
# CATEGORY-WISE SALES
# =========================================================

@app.get("/sales/categories")
def get_category_sales():

    category_sales = (
        df.groupby("Category")["Total_Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    return {
        str(category): float(sales)
        for category, sales in category_sales.items()
    }


# =========================================================
# BEST-SELLING PRODUCT
# =========================================================

@app.get("/sales/best-product")
def get_best_product():

    product_sales = (
        df.groupby("Product")["Total_Sales"]
        .sum()
    )

    best_product = product_sales.idxmax()
    best_product_sales = product_sales.max()

    return {
        "best_selling_product": str(best_product),
        "sales": float(best_product_sales)
    }


# =========================================================
# BEST SALES DAY
# =========================================================

@app.get("/sales/best-day")
def get_best_day():

    daily_sales = (
        df.groupby("Date")["Total_Sales"]
        .sum()
    )

    best_day = daily_sales.idxmax()
    best_day_sales = daily_sales.max()

    return {
        "best_sales_day": best_day.strftime("%Y-%m-%d"),
        "sales": float(best_day_sales)
    }


# =========================================================
# DAILY SALES
# =========================================================

@app.get("/sales/daily")
def get_daily_sales():

    daily_sales = (
        df.groupby("Date")["Total_Sales"]
        .sum()
    )

    return {
        date.strftime("%Y-%m-%d"): float(sales)
        for date, sales in daily_sales.items()
    }


# =========================================================
# MONTHLY SALES
# =========================================================

@app.get("/sales/monthly")
def get_monthly_sales():

    monthly_sales = (
        df.groupby(df["Date"].dt.to_period("M"))["Total_Sales"]
        .sum()
    )

    return {
        str(month): float(sales)
        for month, sales in monthly_sales.items()
    }


# =========================================================
# SUMMARY
# =========================================================

@app.get("/sales/summary")
def get_sales_summary():

    total_revenue = df["Total_Sales"].sum()
    average_sale = df["Total_Sales"].mean()
    highest_sale = df["Total_Sales"].max()
    lowest_sale = df["Total_Sales"].min()
    total_quantity = df["Quantity"].sum()

    # Product analysis
    product_sales = (
        df.groupby("Product")["Total_Sales"]
        .sum()
    )

    best_product = product_sales.idxmax()
    best_product_sales = product_sales.max()

    # Daily analysis
    daily_sales = (
        df.groupby("Date")["Total_Sales"]
        .sum()
    )

    best_day = daily_sales.idxmax()
    best_day_sales = daily_sales.max()

    # Category analysis
    category_sales = (
        df.groupby("Category")["Total_Sales"]
        .sum()
    )

    return {
        "total_revenue": float(total_revenue),

        "average_sale": float(average_sale),

        "highest_sale": float(highest_sale),

        "lowest_sale": float(lowest_sale),

        "total_quantity_sold": int(total_quantity),

        "best_selling_product": str(best_product),

        "best_product_sales": float(best_product_sales),

        "best_sales_day": best_day.strftime("%Y-%m-%d"),

        "best_day_sales": float(best_day_sales),

        "product_wise_sales": {
            str(product): float(sales)
            for product, sales in product_sales.items()
        },

        "category_wise_sales": {
            str(category): float(sales)
            for category, sales in category_sales.items()
        }
    }

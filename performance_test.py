import time
import pandas as pd
import numpy as np


def sales_analysis_pipeline(df):
    """Run the main sales analysis operations."""

    df = df.copy()

    # Convert date
    df["Date"] = pd.to_datetime(df["Date"])

    # Calculate total sales
    df["Total_Sales"] = df["Quantity"] * df["Price"]

    # Product-wise sales
    product_sales = df.groupby("Product")["Total_Sales"].sum()

    # Category-wise sales
    category_sales = df.groupby("Category")["Total_Sales"].sum()

    # Daily sales
    daily_sales = df.groupby("Date")["Total_Sales"].sum()

    # Monthly sales
    df["Month"] = df["Date"].dt.to_period("M")
    monthly_sales = df.groupby("Month")["Total_Sales"].sum()

    return {
        "product_sales": product_sales,
        "category_sales": category_sales,
        "daily_sales": daily_sales,
        "monthly_sales": monthly_sales
    }


# Load original dataset
df = pd.read_csv("data/sales_data.csv")

# Create a larger dataset for performance testing
large_df = pd.concat([df] * 1000, ignore_index=True)

print("Original dataset size:", len(df))
print("Performance test dataset size:", len(large_df))

# Start timer
start_time = time.perf_counter()

# Run pipeline
result = sales_analysis_pipeline(large_df)

# End timer
end_time = time.perf_counter()

execution_time = end_time - start_time

print("\n===== PERFORMANCE TEST =====")
print("Execution time:", round(execution_time, 4), "seconds")

if execution_time < 1:
    print("Performance: Excellent")
elif execution_time < 3:
    print("Performance: Good")
else:
    print("Performance: Needs improvement")
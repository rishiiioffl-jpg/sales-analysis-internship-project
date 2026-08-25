import time
import pandas as pd


def optimized_sales_pipeline(df):
    """Optimized sales analysis pipeline."""

    # Work only with required columns
    df = df[
        ["Date", "Product", "Category", "Quantity", "Price"]
    ].copy()

    # Use efficient data types
    df["Date"] = pd.to_datetime(df["Date"])

    df["Product"] = df["Product"].astype("category")
    df["Category"] = df["Category"].astype("category")

    # Calculate total sales
    df["Total_Sales"] = df["Quantity"] * df["Price"]

    # Perform groupby operations
    product_sales = (
        df.groupby("Product", observed=True)["Total_Sales"]
        .sum()
    )

    category_sales = (
        df.groupby("Category", observed=True)["Total_Sales"]
        .sum()
    )

    daily_sales = (
        df.groupby("Date")["Total_Sales"]
        .sum()
    )

    # Monthly sales
    df["Month"] = df["Date"].dt.to_period("M")

    monthly_sales = (
        df.groupby("Month")["Total_Sales"]
        .sum()
    )

    return {
        "product_sales": product_sales,
        "category_sales": category_sales,
        "daily_sales": daily_sales,
        "monthly_sales": monthly_sales
    }


# Load original dataset
df = pd.read_csv("data/sales_data.csv")

# Create a large dataset
large_df = pd.concat(
    [df] * 10000,
    ignore_index=True
)

print("Original dataset size:", len(df))
print("Large dataset size:", len(large_df))

# Performance test
start_time = time.perf_counter()

result = optimized_sales_pipeline(large_df)

end_time = time.perf_counter()

execution_time = end_time - start_time

print("\n===== OPTIMIZED PERFORMANCE TEST =====")
print(
    "Execution time:",
    round(execution_time, 4),
    "seconds"
)

print("\nOptimization techniques used:")
print("1. Selected only required columns")
print("2. Used categorical data types")
print("3. Reduced unnecessary calculations")
print("4. Used efficient pandas groupby operations")
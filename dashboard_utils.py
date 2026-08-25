import pandas as pd
import matplotlib.pyplot as plt


def load_sales_data(file_path):
    """Load and validate sales data."""

    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
        return None

    required_columns = [
        "Date",
        "Product",
        "Category",
        "Quantity",
        "Price"
    ]

    missing_columns = [
        column for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        print("Error: Missing columns:", missing_columns)
        return None

    df["Date"] = pd.to_datetime(
        df["Date"],
        errors="coerce"
    )

    if df["Date"].isnull().any():
        print("Warning: Invalid dates found.")

    df["Total_Sales"] = df["Quantity"] * df["Price"]

    return df


def get_sales_summary(df):
    """Return important sales metrics."""

    return {
        "total_revenue": df["Total_Sales"].sum(),
        "average_sale": df["Total_Sales"].mean(),
        "total_quantity": df["Quantity"].sum(),
        "best_product": (
            df.groupby("Product")["Total_Sales"]
            .sum()
            .idxmax()
        )
    }


def create_product_sales_chart(df):
    """Create an improved product sales chart."""

    product_sales = (
        df.groupby("Product")["Total_Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    plt.figure(figsize=(9, 5))

    product_sales.plot(kind="bar")

    plt.title(
        "Product-wise Sales",
        fontsize=14
    )

    plt.xlabel("Product")
    plt.ylabel("Total Sales")

    plt.xticks(rotation=45)
    plt.grid(axis="y", alpha=0.3)

    plt.tight_layout()

    plt.savefig(
        "product_wise_sales_improved.png"
    )

    plt.show()


def create_sales_trend_chart(df):
    """Create an improved sales trend chart."""

    daily_sales = (
        df.groupby("Date")["Total_Sales"]
        .sum()
        .sort_index()
    )

    plt.figure(figsize=(10, 5))

    plt.plot(
        daily_sales.index,
        daily_sales.values,
        marker="o"
    )

    plt.title(
        "Daily Sales Trend",
        fontsize=14
    )

    plt.xlabel("Date")
    plt.ylabel("Total Sales")

    plt.xticks(rotation=45)

    plt.grid(
        axis="y",
        alpha=0.3
    )

    plt.tight_layout()

    plt.savefig(
        "sales_trend_improved.png"
    )

    plt.show()


def display_summary(df):
    """Display a clean sales summary."""

    summary = get_sales_summary(df)

    print("\n================================")
    print("        SALES SUMMARY")
    print("================================")

    print(
        f"Total Revenue: "
        f"{summary['total_revenue']:.2f}"
    )

    print(
        f"Average Sale: "
        f"{summary['average_sale']:.2f}"
    )

    print(
        f"Total Quantity Sold: "
        f"{summary['total_quantity']}"
    )

    print(
        f"Best-Selling Product: "
        f"{summary['best_product']}"
    )

    print("================================")


def main():

    df = load_sales_data(
        "data/sales_data.csv"
    )

    if df is None:
        return

    display_summary(df)

    create_product_sales_chart(df)
    create_sales_trend_chart(df)


if __name__ == "__main__":
    main()
    
import pandas as pd
import matplotlib.pyplot as plt


def load_data(file_path):
    """Load sales data from a CSV file."""
    return pd.read_csv(file_path)


def prepare_data(df):
    """Prepare sales data for analysis."""
    df = df.copy()

    df["Date"] = pd.to_datetime(df["Date"])
    df["Total_Sales"] = df["Quantity"] * df["Price"]
    df["Month"] = df["Date"].dt.to_period("M")

    return df


def calculate_basic_metrics(df):
    """Calculate basic sales metrics."""
    total_revenue = df["Total_Sales"].sum()
    average_sale = df["Total_Sales"].mean()
    highest_sale = df["Total_Sales"].max()
    lowest_sale = df["Total_Sales"].min()
    total_quantity = df["Quantity"].sum()

    return {
        "total_revenue": total_revenue,
        "average_sale": average_sale,
        "highest_sale": highest_sale,
        "lowest_sale": lowest_sale,
        "total_quantity": total_quantity
    }


def product_sales(df):
    """Calculate total sales for each product."""
    return df.groupby("Product")["Total_Sales"].sum().sort_values(
        ascending=False
    )


def category_sales(df):
    """Calculate total sales for each category."""
    return df.groupby("Category")["Total_Sales"].sum().sort_values(
        ascending=False
    )


def daily_sales(df):
    """Calculate total sales for each day."""
    return df.groupby("Date")["Total_Sales"].sum()


def monthly_sales(df):
    """Calculate total sales for each month."""
    return df.groupby("Month")["Total_Sales"].sum()


def quantity_by_product(df):
    """Calculate quantity sold for each product."""
    return df.groupby("Product")["Quantity"].sum().sort_values(
        ascending=False
    )


def get_best_product(df):
    """Find the best-selling product by revenue."""
    sales = product_sales(df)

    return sales.idxmax(), sales.max()


def get_best_sales_day(df):
    """Find the day with the highest sales."""
    sales = daily_sales(df)

    return sales.idxmax(), sales.max()


def create_product_sales_chart(df):
    """Create product-wise sales chart."""
    sales = product_sales(df)

    plt.figure(figsize=(8, 5))
    sales.plot(kind="bar")

    plt.title("Product-wise Sales")
    plt.xlabel("Product")
    plt.ylabel("Total Sales")
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig("product_wise_sales.png")
    plt.show()


def create_monthly_sales_chart(df):
    """Create monthly sales chart."""
    sales = monthly_sales(df)

    plt.figure(figsize=(8, 5))
    sales.plot(kind="bar")

    plt.title("Monthly Sales")
    plt.xlabel("Month")
    plt.ylabel("Total Sales")
    plt.tight_layout()

    plt.savefig("monthly_sales.png")
    plt.show()


def create_quantity_chart(df):
    """Create quantity sold by product chart."""
    quantity = quantity_by_product(df)

    plt.figure(figsize=(8, 5))
    quantity.plot(kind="bar")

    plt.title("Quantity Sold by Product")
    plt.xlabel("Product")
    plt.ylabel("Quantity Sold")
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig("quantity_by_product.png")
    plt.show()


def main():
    """Run the complete sales analysis pipeline."""

    df = load_data("data/sales_data.csv")
    df = prepare_data(df)

    metrics = calculate_basic_metrics(df)

    print("\n===== SALES ANALYSIS =====")
    print("Total Revenue:", metrics["total_revenue"])
    print("Average Sale:", metrics["average_sale"])
    print("Highest Sale:", metrics["highest_sale"])
    print("Lowest Sale:", metrics["lowest_sale"])
    print("Total Quantity Sold:", metrics["total_quantity"])

    print("\nProduct-wise Sales:")
    print(product_sales(df))

    print("\nCategory-wise Sales:")
    print(category_sales(df))

    best_product, best_product_sales = get_best_product(df)
    print("\nBest-Selling Product:", best_product)
    print("Best Product Sales:", best_product_sales)

    best_day, best_day_sales = get_best_sales_day(df)
    print("\nBest Sales Day:", best_day)
    print("Best Day Sales:", best_day_sales)

    print("\nQuantity Sold by Product:")
    print(quantity_by_product(df))

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:", df.duplicated().sum())

    create_product_sales_chart(df)
    create_monthly_sales_chart(df)
    create_quantity_chart(df)


if __name__ == "__main__":
    main()
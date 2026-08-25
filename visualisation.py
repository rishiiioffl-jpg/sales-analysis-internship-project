import pandas as pd
import matplotlib.pyplot as plt


def load_data(file_path):
    """Load and prepare sales data."""

    df = pd.read_csv(file_path)

    df["Date"] = pd.to_datetime(df["Date"])
    df["Total_Sales"] = df["Quantity"] * df["Price"]

    return df


def product_sales_chart(df):
    """Display an improved product-wise sales chart."""

    sales = (
        df.groupby("Product")["Total_Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    plt.figure(figsize=(10, 6))

    bars = plt.bar(
        sales.index,
        sales.values
    )

    plt.title(
        "Product-wise Sales",
        fontsize=16,
        fontweight="bold"
    )

    plt.xlabel("Product", fontsize=12)
    plt.ylabel("Total Sales", fontsize=12)

    plt.xticks(
        rotation=45,
        ha="right"
    )

    # Display values on bars
    for bar in bars:
        value = bar.get_height()

        plt.text(
            bar.get_x() + bar.get_width() / 2,
            value,
            f"{value:.0f}",
            ha="center",
            va="bottom",
            fontsize=9
        )

    plt.grid(
        axis="y",
        linestyle="--",
        alpha=0.3
    )

    plt.tight_layout()

    plt.savefig(
        "product_sales_ui.png",
        dpi=150
    )

    plt.show()


def sales_trend_chart(df):
    """Display an improved daily sales trend."""

    daily_sales = (
        df.groupby("Date")["Total_Sales"]
        .sum()
        .sort_index()
    )

    plt.figure(figsize=(11, 6))

    plt.plot(
        daily_sales.index,
        daily_sales.values,
        marker="o",
        linewidth=2
    )

    plt.title(
        "Daily Sales Trend",
        fontsize=16,
        fontweight="bold"
    )

    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Total Sales", fontsize=12)

    plt.xticks(
        rotation=45,
        ha="right"
    )

    plt.grid(
        axis="y",
        linestyle="--",
        alpha=0.3
    )

    plt.tight_layout()

    plt.savefig(
        "sales_trend_ui.png",
        dpi=150
    )

    plt.show()


def category_sales_chart(df):
    """Display an improved category sales chart."""

    category_sales = (
        df.groupby("Category")["Total_Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    plt.figure(figsize=(9, 6))

    bars = plt.bar(
        category_sales.index,
        category_sales.values
    )

    plt.title(
        "Category-wise Sales",
        fontsize=16,
        fontweight="bold"
    )

    plt.xlabel("Category", fontsize=12)
    plt.ylabel("Total Sales", fontsize=12)

    plt.xticks(
        rotation=30,
        ha="right"
    )

    for bar in bars:
        value = bar.get_height()

        plt.text(
            bar.get_x() + bar.get_width() / 2,
            value,
            f"{value:.0f}",
            ha="center",
            va="bottom",
            fontsize=9
        )

    plt.grid(
        axis="y",
        linestyle="--",
        alpha=0.3
    )

    plt.tight_layout()

    plt.savefig(
        "category_sales_ui.png",
        dpi=150
    )

    plt.show()


def main():

    df = load_data(
        "data/sales_data.csv"
    )

    print("Creating improved visualizations...")

    product_sales_chart(df)
    sales_trend_chart(df)
    category_sales_chart(df)

    print("\nVisualization UI/UX improvements completed.")


if __name__ == "__main__":
    main()
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def prepare_sales_data(file_path):
    """Load and prepare sales data."""
    df = pd.read_csv(file_path)

    df["Date"] = pd.to_datetime(df["Date"])
    df["Total_Sales"] = df["Quantity"] * df["Price"]

    return df


def sales_forecast(df, forecast_days=7):
    """
    Forecast future sales using a simple moving average.
    """

    daily_sales = (
        df.groupby("Date")["Total_Sales"]
        .sum()
        .sort_index()
    )

    # Calculate 7-day moving average
    moving_average = daily_sales.rolling(
        window=7,
        min_periods=1
    ).mean()

    last_forecast = moving_average.iloc[-1]

    last_date = daily_sales.index[-1]

    future_dates = pd.date_range(
        start=last_date + pd.Timedelta(days=1),
        periods=forecast_days
    )

    forecast = pd.Series(
        last_forecast,
        index=future_dates
    )

    return forecast


def recommend_products(df, top_n=3):
    """
    Recommend products based on total sales revenue.
    """

    product_sales = (
        df.groupby("Product")["Total_Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    recommendations = product_sales.head(top_n)

    return recommendations


def display_forecast(forecast):
    """Display sales forecast."""

    print("\n===== SALES FORECAST =====")

    for date, sales in forecast.items():
        print(
            f"{date.strftime('%Y-%m-%d')}: "
            f"{sales:.2f}"
        )


def display_recommendations(recommendations):
    """Display recommended products."""

    print("\n===== PRODUCT RECOMMENDATIONS =====")

    for product, sales in recommendations.items():
        print(
            f"{product}: "
            f"{sales:.2f} total sales"
        )


def create_forecast_chart(df, forecast):
    """Create historical and forecast sales chart."""

    daily_sales = (
        df.groupby("Date")["Total_Sales"]
        .sum()
        .sort_index()
    )

    plt.figure(figsize=(10, 5))

    plt.plot(
        daily_sales.index,
        daily_sales.values,
        marker="o",
        label="Historical Sales"
    )

    plt.plot(
        forecast.index,
        forecast.values,
        marker="o",
        linestyle="--",
        label="Forecast"
    )

    plt.title("Sales Forecast")
    plt.xlabel("Date")
    plt.ylabel("Total Sales")

    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()

    plt.savefig("sales_forecast.png")
    plt.show()


def main():

    df = prepare_sales_data(
        "data/sales_data.csv"
    )

    # Sales forecasting
    forecast = sales_forecast(
        df,
        forecast_days=7
    )

    display_forecast(forecast)

    # Product recommendations
    recommendations = recommend_products(
        df,
        top_n=3
    )

    display_recommendations(
        recommendations
    )

    # Forecast visualization
    create_forecast_chart(
        df,
        forecast
    )


if __name__ == "__main__":
    main()
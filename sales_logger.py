import logging
import pandas as pd


# Configure logging
logging.basicConfig(
    filename="sales_analysis.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


def load_sales_data(file_path):
    """Load sales data and record the process."""

    logger.info("Starting sales data loading.")

    try:
        df = pd.read_csv(file_path)

        logger.info(
            "Sales data loaded successfully. Rows: %d, Columns: %d",
            df.shape[0],
            df.shape[1]
        )

        return df

    except FileNotFoundError:
        logger.error(
            "Sales data file not found: %s",
            file_path
        )

        return None

    except Exception as error:
        logger.error(
            "Error while loading sales data: %s",
            error
        )

        return None


def prepare_sales_data(df):
    """Prepare sales data and log the process."""

    logger.info("Starting data preparation.")

    if df is None:
        logger.warning(
            "Data preparation skipped because dataframe is empty."
        )
        return None

    try:
        df = df.copy()

        df["Date"] = pd.to_datetime(
            df["Date"],
            errors="coerce"
        )

        df["Total_Sales"] = (
            df["Quantity"] * df["Price"]
        )

        logger.info(
            "Data preparation completed successfully."
        )

        return df

    except Exception as error:
        logger.error(
            "Error during data preparation: %s",
            error
        )

        return None


def analyze_sales(df):
    """Perform basic sales analysis with logging."""

    if df is None:
        logger.warning(
            "Sales analysis skipped because dataframe is empty."
        )
        return None

    logger.info("Starting sales analysis.")

    try:
        total_revenue = df["Total_Sales"].sum()

        average_sale = df["Total_Sales"].mean()

        best_product = (
            df.groupby("Product")["Total_Sales"]
            .sum()
            .idxmax()
        )

        logger.info(
            "Sales analysis completed successfully."
        )

        logger.info(
            "Total revenue: %.2f",
            total_revenue
        )

        logger.info(
            "Best-selling product: %s",
            best_product
        )

        return {
            "total_revenue": total_revenue,
            "average_sale": average_sale,
            "best_product": best_product
        }

    except Exception as error:
        logger.error(
            "Error during sales analysis: %s",
            error
        )

        return None


def main():

    logger.info("===== SALES ANALYSIS STARTED =====")

    file_path = "data/sales_data.csv"

    df = load_sales_data(file_path)

    df = prepare_sales_data(df)

    results = analyze_sales(df)

    if results:

        print("\n===== SALES ANALYSIS =====")

        print(
            "Total Revenue:",
            results["total_revenue"]
        )

        print(
            "Average Sale:",
            results["average_sale"]
        )

        print(
            "Best-Selling Product:",
            results["best_product"]
        )

        logger.info(
            "Sales analysis completed successfully."
        )

    else:
        logger.warning(
            "Sales analysis did not produce results."
        )

    logger.info("===== SALES ANALYSIS FINISHED =====")


if __name__ == "__main__":
    main()
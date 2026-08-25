import unittest
import pandas as pd
from data_processing import load_data, clean_data, process_data


class TestSalesDataProcessing(unittest.TestCase):

    def setUp(self):
        # Sample sales data for testing
        self.data = pd.DataFrame({
            "Date": ["2026-01-01", "2026-01-02", "2026-01-02"],
            "Product": ["Laptop", "Mouse", "Mouse"],
            "Quantity": [2, 5, 5],
            "Price": [50000, 500, 500]
        })

    def test_load_data(self):
        # Test whether CSV data can be loaded
        df = load_data("data/sales_data.csv")

        self.assertIsInstance(df, pd.DataFrame)
        self.assertFalse(df.empty)

    def test_remove_duplicates(self):
        # Test whether duplicate rows are removed
        df = clean_data(self.data)

        self.assertEqual(len(df), 2)

    def test_remove_missing_values(self):
        # Test whether rows containing missing values are removed
        data = self.data.copy()
        data.loc[0, "Price"] = None

        df = clean_data(data)

        self.assertFalse(df.isnull().values.any())

    def test_date_conversion(self):
        # Test whether Date column is converted to datetime
        df = clean_data(self.data)

        self.assertTrue(
            pd.api.types.is_datetime64_any_dtype(df["Date"])
        )

    def test_process_data(self):
        # Test the complete data-processing pipeline
        df = process_data("data/sales_data.csv")

        self.assertIsInstance(df, pd.DataFrame)
        self.assertFalse(df.empty)
        self.assertFalse(df.isnull().values.any())


if __name__ == "__main__":
    unittest.main()
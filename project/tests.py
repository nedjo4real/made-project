import os
import unittest
import sqlite3
import pandas as pd


class TestPipeline(unittest.TestCase):
    def setUp(self):
        # Paths to datasets and database
        self.db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'data.sqlite'))
        # print("db_path => "+self.db_path)

    def test_pipeline_execution(self):
        """Test if the pipeline creates the SQLite database."""
        # Run the pipeline script
        os.system("python pipeline.py")
        self.assertTrue(os.path.exists(self.db_path), "Database file was not created.")

    def test_table_existence(self):
        """Test if the database contains the expected table."""
        if not os.path.exists(self.db_path):
            self.fail("Database file does not exist.")
        
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()
            self.assertIn(('income_data',), tables, "Table 'income_data' is missing.")

    def test_salary_categories(self):
        """Test if Salary column contains only expected categories."""
        if not os.path.exists(self.db_path):
            self.fail("Database file does not exist.")

        with sqlite3.connect(self.db_path) as conn:
            df = pd.read_sql("SELECT * FROM income_data", conn)

            expected_categories = {'>50K', '>=50K', '<50K', '<=50K'}
            actual_categories = set(df['Salary'].unique())
            self.assertEqual(expected_categories, actual_categories,
                             f"Salary column has unexpected categories: {actual_categories}")

    def test_no_missing_age_range(self):
        """Test that Age.Range column has no missing values."""
        if not os.path.exists(self.db_path):
            self.fail("Database file does not exist.")

        with sqlite3.connect(self.db_path) as conn:
            df = pd.read_sql("SELECT * FROM income_data", conn)

            self.assertFalse(df['Age.Range'].isna().any(),
                             "Age.Range column contains missing values.")

    def test_country_column_validity(self):
        """Test that the Country column contains only valid entries."""
        if not os.path.exists(self.db_path):
            self.fail("Database file does not exist.")

        with sqlite3.connect(self.db_path) as conn:
            df = pd.read_sql("SELECT * FROM income_data", conn)

            invalid_countries = df['Country'].apply(lambda x: not isinstance(x, str) or x.isdigit()).any()
            self.assertFalse(invalid_countries,
                             "Country column contains invalid entries.")

    def test_combined_data(self):
        """Test if the combined data has reasonable size and structure."""
        if not os.path.exists(self.db_path):
            self.fail("Database file does not exist.")
        
        with sqlite3.connect(self.db_path) as conn:
            df = pd.read_sql("SELECT * FROM income_data", conn)

            # Test for sufficient number of records
            self.assertGreater(len(df), 1000, "Combined dataset has insufficient rows.")

            # Test for presence of required columns
            expected_columns = {'Age.Range', 'Education', 'Country', 'Salary'}
            self.assertTrue(expected_columns.issubset(df.columns),
                            "Missing expected columns in the combined dataset.")


if __name__ == "__main__":
    unittest.main()

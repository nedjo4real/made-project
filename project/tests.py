import os
import unittest
import sqlite3
import pandas as pd


class TestPipeline(unittest.TestCase):
    def setUp(self):
        # Paths to datasets and database
        self.db_path = './data/data.sqlite'
        self.dataset1_url = "https://www.kaggle.com/datasets/amirhosseinmirzaie/americancitizenincome"
        self.dataset2_url = "https://www.kaggle.com/datasets/ricardoaugas/salary-transparency-dataset-2022"

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

    def test_data_quality(self):
        """Test data quality: no missing values and proper salary ranges."""
        if not os.path.exists(self.db_path):
            self.fail("Database file does not exist.")
        
        with sqlite3.connect(self.db_path) as conn:
            df = pd.read_sql("SELECT * FROM income_data", conn)

            # Test for missing values
            self.assertFalse(df.isna().any().any(), "Data contains missing values.")

            # Test for salary range values
            self.assertTrue(set(df['Salary'].unique()).issubset({'>=50K', '<50K'}),
                        "Salary column contains unexpected values.")


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

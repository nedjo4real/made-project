import pandas as pd
import os
import kagglehub
import numpy as np
import sqlite3

# Download datasets
path_ds1 = kagglehub.dataset_download("amirhosseinmirzaie/americancitizenincome")
csv_file_path_ds1 = os.path.join(path_ds1, "income.csv")

columns_to_remove_ds1 = ['fnlwgt', 'education.num', 'race', 'sex', 'capital.loss',
                         'relationship', 'marital.status', 'workclass', 'occupation',
                         'hours.per.week', 'capital.gain']

try:
    income_data_ds1 = pd.read_csv(csv_file_path_ds1)
    income_data_ds1.replace('?', np.nan, inplace=True)
    income_data_ds1.replace('United-States', 'US', inplace=True)
    income_data_ds1.rename(columns={'age': 'Age.Range', 'education': 'Education',
                                     'native.country': 'Country', 'income': 'Salary'}, inplace=True)
    income_data_ds1 = income_data_ds1.drop(columns=columns_to_remove_ds1).dropna()
except FileNotFoundError:
    print("The file 'income.csv' was not found in the dataset directory!")

path_ds2 = kagglehub.dataset_download("ricardoaugas/salary-transparency-dataset-2022")
csv_file_ds2 = os.path.join(path_ds2, "Salary_Data_2022_REV15.csv")

columns_to_remove_ds2 = ['ID', 'Timestamp', 'Open.To.Discuss.Salary', 'Sick.Days', 'Office.Days',
                         'Gender', 'X', 'Description', 'Signing.Bonus',
                         'Diverse.Identity..Optional.', 'How.many.months.Maternity.or.Paternity.does.your.company.offer.',
                         'Annual.Bonus', 'Maternity.Paternity.Months', 'Location',
                         'Annual.Average.of.RSUs', 'Industry', 'Years.of.Experience',
                         'Job.Title', 'Company.Name', 'Currency']

try:
    income_data_ds2 = pd.read_csv(csv_file_ds2)
    income_data_ds2.replace('NaN', np.nan, inplace=True)
    income_data_ds2['Salary'] = income_data_ds2['Salary'].apply(lambda x: '>=50K' if x >= 50000 else '<50K')
    income_data_ds2.replace(0, np.nan, inplace=True)
    income_data_ds2 = income_data_ds2.drop(columns=columns_to_remove_ds2).dropna()
except FileNotFoundError:
    print("The file 'Salary_Data_2022_REV15.csv' was not found in the dataset directory!")

# Combine datasets
df_combined = pd.concat([income_data_ds1, income_data_ds2], axis=0, ignore_index=True)

# Ensure directory exists
db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'data.sqlite'))
os.makedirs(os.path.dirname(db_path), exist_ok=True)

# Save to SQLite database
with sqlite3.connect(db_path) as conn:
    df_combined.to_sql('income_data', conn, if_exists='replace', index=False)
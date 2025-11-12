# Load libraries
import pandas as pd
import numpy as np
import warnings
import os
import sys

warnings.filterwarnings('ignore')

# --- Get input file name from user and validate ---
while True:
    file_name = input("")
    file_path = os.path.join(sys.path[0], file_name)
    
    if os.path.isfile(file_path):
        break
    else:
        print("File not found. Please enter a valid filename in the current directory.")

# --- Load dataset (CSV only) ---
df = pd.read_csv(file_path)

# --- Initial data cleaning ---
df['previous_year_rating'].fillna(0, inplace=True)
df['education'].fillna(df['education'].mode()[0], inplace=True)
df['avg_training_score'].fillna(df['avg_training_score'].mode()[0], inplace=True)
df_cleaned = df.drop_duplicates()
if 'department' in df_cleaned.columns:
    df_cleaned['department'] = df_cleaned['department'].str.title()

# --- Analyze the ‘avg_training_score’ column ---
print(df_cleaned['avg_training_score'].describe().astype(int))
print(f"median      {df_cleaned['avg_training_score'].median()}")
print(f"mode        {df_cleaned['avg_training_score'].mode()[0]}")
print(f"skewness    {df_cleaned['avg_training_score'].skew().round(2)}")

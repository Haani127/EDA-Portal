import pandas as pd
import numpy as np
import warnings
import os, sys

# Suppress warnings
warnings.filterwarnings("ignore")

# Prompt user for filename
filename = input().strip()

try:
    # Read CSV file
    path = os.path.join(sys.path[0], filename)
    df = pd.read_csv(path)
    # Check for required columns
    required_cols = [
        'employee_id', 'department', 'region', 'education', 'gender',
        'recruitment_channel', 'no_of_trainings', 'age', 'previous_year_rating',
        'length_of_service', 'awards_won', 'avg_training_score', 'is_promoted',
        'performance_score', 'years_since_last_promotion',
        'is_eligible_for_promotion', 'experience_level', 'training_effectiveness_ratio'
    ]
    if not all(col in df.columns for col in required_cols):
        raise ValueError("Missing required columns in CSV file.")

    # Drop duplicate rows
    df = df.drop_duplicates()

    # Standardize text columns (e.g., capitalization)
    text_cols = df.select_dtypes(include=['object']).columns
    df[text_cols] = df[text_cols].apply(lambda x: x.str.strip().str.title())

    # Handle missing values
    df['previous_year_rating'].fillna(0, inplace=True)
    if df['avg_training_score'].isnull().any():
        mode_val = df['avg_training_score'].mode()[0]
        df['avg_training_score'].fillna(mode_val, inplace=True)

    # Statistical summary for age
    age_summary = df['age'].describe().astype(int)

    # Compute median, mode, and skewness
    median_age = df['age'].median()
    mode_age = df['age'].mode()[0]
    skewness_age = round(df['age'].skew(), 2)

    # Output results
    print(age_summary)
    print(f"median      {median_age}")
    print(f"mode        {mode_age}")
    print(f"skewness    {skewness_age}")

except FileNotFoundError:
    print("Error: File not found. Please make sure the CSV file exists in the same directory.")
except ValueError as ve:
    print(f"Error: {ve}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
import pandas as pd
import os
import sys

required_columns = [
    'EmployeeID', 'Age', 'Attrition', 'BusinessTravel', 'Department', 'DistanceFromHome',
    'Education', 'EducationField', 'EnvironmentSatisfaction', 'Gender', 'JobInvolvement',
    'JobLevel', 'JobRole', 'JobSatisfaction', 'MaritalStatus', 'MonthlyIncome',
    'NumCompaniesWorkedPrevious', 'OverTime', 'PercentSalaryHike', 'PerformanceRating',
    'RelationshipSatisfaction', 'Shift', 'TotalWorkingYears', 'TrainingTimesLastYear',
    'WorkLifeBalance', 'YearsAtCompany', 'YearsInCurrentRole', 'YearsSinceLastPromotion',
    'YearsWithCurrManager'
]

path = os.path.join(sys.path[0] , input())
df = pd.read_csv(path)

if not set(required_columns).issubset(set(df.columns)):
    print("Error: Missing required columns in the CSV file.")
    sys.exit(1)

print(f"Shape of dataset: {df.shape}")
print("Data types:")
print(df.dtypes)
print("\nPreview of data:")
print(df.head())

print("\nChecking for null values:")
print(df.isnull().sum())

for col in df.columns:
    if df[col].dtype in ['int64', 'float64']:
        df[col].fillna(df[col].median(), inplace=True)
    else:
        df[col].fillna(df[col].mode()[0], inplace=True)

print("\nMissing values handled.")

dup_count = df.duplicated().sum()
print(f"\nFound {dup_count} duplicate records.")
if dup_count > 0:
    df.drop_duplicates(inplace=True)
    print("Duplicates removed.")
else:
    print("No duplicates found.")

df['NumCompaniesWorkedPrevious'] = df['NumCompaniesWorkedPrevious'].astype('Int64')
df['YearsSinceLastPromotion'] = df['YearsSinceLastPromotion'].astype('Int64')
df['OverTime'] = df['OverTime'].str.strip().map({'Yes': 1, 'No': 0}).astype(int)

def age_group(age):
    if age < 30:
        return 'Young'
    elif age <= 44:
        return 'Mid-age'
    else:
        return 'Senior'

df['AgeGroup'] = df['Age'].apply(age_group)

print("\nFormatting fixed. Added AgeGroup column.")

print("\nFinal Dataset Preview:")
print(df.head())
print(f"\nFinal Shape: {df.shape}")

print("Cleaned dataset saved")
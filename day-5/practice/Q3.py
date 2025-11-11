import os
import sys
import pandas as pd

filename = input()
file_path = os.path.join(sys.path[0], filename)

df = pd.read_csv(file_path)


# Step 1: Load and Explore the Dataset
print(f"Shape of dataset: {df.shape}")
print("Data types:\n", df.dtypes)

print("\nPreview of data:")
print(df.head(), "\n")

# Step 2: Identify and Handle Missing Values
print("Checking for null values:\n", df.isnull().sum(), "\n")

# Handle missing values (numeric → median, categorical → mode)
for col in df.columns:
    if df[col].isnull().sum() > 0:
        if df[col].dtype in ['int64', 'float64']:
            df[col].fillna(df[col].median(), inplace=True)
        else:
            df[col].fillna(df[col].mode()[0], inplace=True)

print("Missing values handled.\n")

# Step 3: Detect and Remove Duplicate Records
duplicates = df.duplicated().sum()
print(f"Found {duplicates} duplicate records.")
if duplicates > 0:
    df.drop_duplicates(inplace=True)
    print("Duplicates removed.\n")
else:
    print("No duplicates found.\n")

# Step 4: Fix Formatting Inconsistencies
df["NumCompaniesWorkedPrevious"] = df["NumCompaniesWorkedPrevious"].astype("Int64")
df["YearsSinceLastPromotion"] = df["YearsSinceLastPromotion"].astype("Int64")
df["OverTime"] = df["OverTime"].map({"Yes": 1, "No": 0})

def age_group(age):
    if age < 30:
        return "Young"
    elif 30 <= age <= 44:
        return "Mid-age"
    else:
        return "Senior"

df["AgeGroup"] = df["Age"].apply(age_group)
print("Formatting fixed. Added AgeGroup column.\n")

# Step 5: Final Dataset Summary
print("Final Dataset Preview:")
print(df.head(), "\n")
print(f"Final Shape: {df.shape}\n")

# Step 6: Save cleaned dataset
df.to_csv("cleaned_employees.csv", index=False)
print("Cleaned dataset saved")

import os, sys
import pandas as  pd

def load(file):
	path = os.path.join(sys.path[0], file)
	
	if os.path.exists(path):
		return pd.read_csv(path)
	return None
	
file = input()

df = load(file)

print("First 5 records:")
print(df.head())

print("Last 5 records:")
print(df.tail())

print(f"Data shape: {df.shape}")

print("Column names and data types:")
print(df.dtypes)

print("Complete info:")
print(df.info())

print("Missing values per column:")
print(df.isna().sum())

total_missing = sum(df.isna().sum())

print("Percentage of missing values per column:")
print((df.isna().mean() * 100))

df.fillna(method='ffill', inplace=True)
print("Missing values after imputation:")
print(df.isnull().sum())

print(f"Number of duplicate rows: {df.duplicated().sum()}")

print("Unique departments after formatting:")
df['department'] = df['department'].str.title()
print(df['department'].unique())


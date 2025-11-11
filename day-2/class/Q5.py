import os
import sys
import pandas as pd

file = input()

file2 = input()

df1 = pd.read_csv(os.path.join(sys.path[0],file))

df2 = pd.read_csv(os.path.join(sys.path[0],file2)) 

print("Initial DataFrame Preview")

print(df1.head())

print("\nMissing Values Count")

print(df1.isnull().sum())

print("\nDropped rows with missing 'cuisine_type'.")

print("\nDataFrame After Dropping Missing Values")

droped_df = df1.dropna()

print(droped_df.head())

print("\nFinal Missing Values Count")

print(df1.isnull().sum())
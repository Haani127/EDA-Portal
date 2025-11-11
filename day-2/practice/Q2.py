import os
import sys
import pandas as pd

file = input()

df = pd.read_csv(os.path.join(sys.path[0],file))

print("Null values in key columns:")

print(df[['discount%','tax','tax_amount(INR)','service_rating']].isnull().sum())

df.dropna(subset='discount%')

print("\nCleaned DataFrame:")

df[['tax','tax_amount(INR)']]=df[['tax','tax_amount(INR)']].fillna(0)

df['service_rating']=df['service_rating'].fillna(df['service_rating'].mean())

print(df)
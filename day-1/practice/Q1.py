import os
import sys
import pandas as pd
import numpy as np

filename = input()

filepath = os.path.join(sys.path[0],filename)

df = pd.read_csv(filepath)

print(df.head())

print("\nNumpy Array of First 10 final_amount values:")

arr = np.array(df['final_amount'].head(10))

print(arr)
print("Shape: ",arr.shape)
print("Data type: ",arr.dtype)

print("\nUpdated final_amounts array (values < 500 increased by 50):")

updated_arr = arr.copy()

updated_arr = np.where(arr<500,arr+50,arr)

print(updated_arr)

print("\nExplanation: Used np.where() to conditionally add 50 to values under 500.")

col_name = df.head(0)

print(f"\nColumns of Payments DataFrame: {df.columns.tolist()}")

print("Data types of columns:")

print(df.dtypes)

print("\na) Payment Method and Final Amount columns:")

print(df[['payment_method' , 'final_amount']])

print("\nb) Records with payment_method as 'Credit Card':")

print(df.loc[df['payment_method'] == 'Credit Card'])

tol_discount_amount = df['discounted_amount(INR)'].sum()

print(f"\nc) Total Discounted Amount across all transactions: ₹{tol_discount_amount:.2f}")
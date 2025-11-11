import os
import sys
import pandas as pd
import numpy as np

file = input()

filepath = os.path.join(sys.path[0],file)

df = pd.read_csv(filepath)

print(df.head(10))

print("\n2D Numpy Array (first 10 rows - amount, discounted_amount, final_amount):")

TwoD_array = df[['amount(INR)' , 'discounted_amount(INR)' , 'final_amount']].head(10).to_numpy(dtype=float)

print(TwoD_array)

print("\nSliced Array (first 5 rows, first 2 columns):")

print(TwoD_array[:5,:2])

print("\nUpdated 2D Array (discounted_amount < 1200 set to 1200):")

updated_arr = TwoD_array.copy()

updated_arr[:,1] = np.where(updated_arr[:,1] < 1200 , 1200 , updated_arr[:,1])

print(updated_arr)

avg_amount = np.mean(updated_arr[:,2])

print(f"\nAverage Final Amount: ₹{avg_amount:.2f}")
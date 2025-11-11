import os
import sys
import numpy as np
import pandas as pd

filename = input()

filepath = os.path.join(sys.path[0],filename)

df = pd.read_csv(filepath)

print(df.head())

print("\nTotal Amounts of All Orders:")

print(df['total_amount'])

print("\nDetails of the 4th order:")

print(df.iloc[3].astype(str))

avg_amount = df['total_amount'].mean()

print(f"\nAverage Total Amount: ₹{avg_amount:.2f}")

if 'ORD0004' not in df['order_id']:
    print("\nORD0004 not found in the dataset!")
    
else:
    df.loc[df['order_id']=='ORD0004' , 'restaurant_id'] = '8'
    df.loc[df['order_id']=='ORD0004' , 'total_amount'] = 1300
    print(df.loc[df['order_id'] == 'ORD0004' ])
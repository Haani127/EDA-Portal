import os
import sys
import pandas as pd

filename = input()
file_path = os.path.join(sys.path[0], filename)

df = pd.read_csv(file_path)

print("Enter the CSV filename (with .csv extension):")
print("--- Orders DataFrame Loaded ---")
print(df.head())

print("\nTotal Amounts of All Orders:")
print(df['total_amount'])

print("\nDetails of the 4th Order:")
print(df.iloc[3])

avg_amount = df['total_amount'].mean()
print(f"\nAverage Total Amount: ₹{avg_amount:.2f}")

print("\nUpdated details for ORD0004:")
df.loc[df['order_id'] == 'ORD0004', 'payment_method'] = 'UPI'
df.loc[df['order_id'] == 'ORD0004', 'total_amount'] = 1300

print(df.loc[df['order_id'] == 'ORD0004'])

import os, sys
import pandas as  pd
import numpy as np

def load(file):
	path = os.path.join(sys.path[0], file)
	
	if os.path.exists(path):
		return pd.read_csv(path)
	return None

file = input()
df = load(file)

completed_df = df[df['order_status'] == 'Completed']

mean = completed_df['total_amount'].mean()
median = completed_df['total_amount'].median()
mode_series = completed_df['total_amount'].mode()

mode_value = mode_series[0] if not mode_series.empty else np.nan

print("Central Tendency Measures of order amounts (₹):\n")

print(f"Mean: {round(mean, 2)}")
print(f"Median: {median}")
print(f"Mode: {mode_value}")

print("Summary Statistics of Order Amounts:")
print(completed_df['total_amount'].describe())
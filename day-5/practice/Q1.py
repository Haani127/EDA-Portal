import os, sys
import pandas as  pd

def load(file):
	path = os.path.join(sys.path[0], file)
	
	if os.path.exists(path):
		return pd.read_csv(path)
	return None

file = input()

df = load(file)

df = df[df['status'] == 'Completed']

print("Central Tendency Measures of service amounts (₹):")
amt_mean = df['final_amount'].mean()
amt_median = df['final_amount'].median()
amt_modes = df['final_amount'].mode()

amt_mode = 0;
if len(amt_modes) > 0:
    amt_mode = amt_modes[0]
    
print(f"Mean: {round(amt_mean, 2)}, Median: {round(amt_median,2)}, Mode: {round(amt_mode, 2)}")

print("Central Tendency Measures of service ratings:")
r_mean = df['service_rating'].mean()
r_median = df['service_rating'].median()
r_modes = df['service_rating'].mode()

if len(r_modes) > 0:
    r_mode = r_modes[0]

print(f"Mean: {round(r_mean, 2)}, Median: {round(r_median, 2)}, Mode: {round(r_mode, 2)}")
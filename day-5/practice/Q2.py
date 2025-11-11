import os, sys
import pandas as  pd
from scipy.stats import skew, kurtosis

def load(file):
	path = os.path.join(sys.path[0], file)
	
	if os.path.exists(path):
		return pd.read_csv(path)
	return None
	

def printer(ran, var, sd, skw, kurt,mean, median, mode, column):
    
    if column=='service_amount':
        print("Distribution of service amounts (₹):")
    else:
        print("Distribution Measurese of service ratings:")
    
    print(f"Range: {round(ran, 2)}, Variance: {round(var, 2)}, Standard Deviation: {round(sd, 2)}")


    print(f"Skewness and Kurtosis of service "+"amounts (₹)" if column=='service_amount' else "ratings:")

    print(f"Skewness: {round(skw, 3)},\tKurtosis: {round(kurt, 3)}")

    print("Insights on "+"Final Amount" if column=='service_amount' else "Service Rating:")

    print("1. Typical Service " + "Amount:" if column=='service_amount' else "Rating:")
    
    print(f"\t - Median: {round(median, 2)}, Mean: {round(mean, 2)}, Mode: {round(mode, 1)}")


file = input()

df = load(file)

p_df = df['amount(INR)']

amt_range = p_df.max() - p_df.min()

amt_var = p_df.var()
amt_sd = p_df.std()

amt_skw = skew(p_df)
amt_kurt = kurtosis(p_df)

amt_mean = p_df.mean()
amt_median = p_df.median()
amt_modes = p_df.mode()
amt_mode = 0
if len(amt_modes):
    amt_mode = amt_modes[0]

printer(amt_range, amt_var, amt_sd, amt_skw, amt_kurt, amt_mean, amt_median, amt_mode, 'service_amount')
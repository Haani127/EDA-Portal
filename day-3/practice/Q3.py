import os, sys
import pandas as  pd

def load(file):
	path = os.path.join(sys.path[0], file)
	
	if os.path.exists(path):
		return pd.read_csv(path)
	return None
	

file = input()
df = load(file)

print("Records with inconsistent payment methods:")

lst = ['gpay', 'Google Pay', 'PhonePe', 'Paytm']

print(df[df['payment_method'].isin(lst)])

df.loc[df['payment_method'].isin(lst), 'payment_method'] = 'UPI'

print("After replacement, inconsistent payment methods should be gone:")
print(df[df['payment_method'].isin(lst)])
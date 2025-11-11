import os, sys
import pandas as  pd

def load(file):
	path = os.path.join(sys.path[0], file)
	
	if os.path.exists(path):
		return pd.read_csv(path)
	return None
	
file = input()
df = load(file)

print("Service ratings for appointments in Mumbai:")
print(df[df['city'] == 'Mumbai'][['appointment_id', 'service_rating']])

pid, amt = df.iloc[9]['provider_id'], df.iloc[9]['final_amount']

print("Provider ID and Final Amount of the 10th appointment:")
print(f"Provider ID: {pid}, Final Amount: {amt}")

completed = df[df['status'] == 'Completed'].copy()
completed['appointment_date'] = pd.to_datetime(completed['appointment_date'], dayfirst=True)

completed.sort_values(by='appointment_date', inplace=True)

print("Last 5 completed appointments (date & service):")
print(completed.iloc[-5:][['appointment_date', 'service_name']].sort_values(by='appointment_date', ascending=False))


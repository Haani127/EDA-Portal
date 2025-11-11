import os, sys
import pandas as  pd

def load(file):
	path = os.path.join(sys.path[0], file)
	
	if os.path.exists(path):
		return pd.read_csv(path)
	return None
	
file = input()
df = load(file)

df.loc[df['status'] == 'Scheduled', 'status'] = 'Completed'

df = df[df['appointment_id'] != 'APT801']

if 'appointment_month' in df.columns :
    df.drop(df['appointment_month'], axis=1, inplace=True)

print("Updated Data Preview:")
print(df.head())

print("Final file saved")

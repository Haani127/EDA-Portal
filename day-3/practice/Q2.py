import os, sys
import pandas as  pd

def load(file):
	path = os.path.join(sys.path[0], file)
	
	if os.path.exists(path):
		return pd.read_csv(path)
	return None
	
file = input()
df = load(file)

df['appointment_date'] = pd.to_datetime(df['appointment_date'], dayfirst=True)

df['appointment_month'] = df['appointment_date'].dt.month_name();

new_df = pd.concat([df[:5], df[-5:]])

print(new_df)

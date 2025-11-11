import pandas as pd
import sys,os

filename=input()
filepath=os.path.join(sys.path[0],filename)
df=pd.read_csv(filepath)

date = pd.to_datetime(df['appointment_date'], format='mixed', dayfirst=True)
df['appointment_month'] = date.dt.strftime('%B')

report=pd.concat([df.head(5), df.tail(5)])
print(report)
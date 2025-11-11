import os
import sys
import pandas as pd

file = input()

filepath = os.path.join(sys.path[0],file)

df = pd.read_csv(filepath)

df['appointment_date'] = pd.to_datetime(df['appointment_date'] , dayfirst = True,errors = 'coerce')

df['appointment_time'] = pd.to_datetime(df['appointment_time'] , format='%H:%M' ,errors = 'coerce').dt.time

duplicates = df[df.duplicated(subset= ['appointment_id'] , keep = False)]

print("Duplicate appointments based on appointment_id:")

print(duplicates)
    
df_sorted = df.sort_values(by = ['user_id' , 'appointment_date' ,'appointment_time'],ascending = [True,True,False])

df_cleaned =df_sorted.drop_duplicates(subset = ['appointment_id'],keep='first')

df_cleaned = df_cleaned.sort_values(by=['user_id','appointment_date','appointment_time'],ascending=[True,False,False])

print("\nCleaned DataFrame:")

print(df_cleaned)

df_cleaned.to_csv(filepath,index = False)

print("\nCleaned data saved to the same file")

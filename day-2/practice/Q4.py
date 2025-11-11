import os
import sys
import pandas as pd
import numpy as np

appointments_df = pd.read_csv(os.path.join(sys.path[0],input()))
payments_df = pd.read_csv(os.path.join(sys.path[0],input()))
services_df = pd.read_csv(os.path.join(sys.path[0],input()))

appoint_payment_merge =pd.merge(appointments_df,payments_df,on='appointment_id',how='left')

avg_rating_per_rating = (
    appoint_payment_merge.groupby('provider_id')
    .agg(
    service_rating = ('service_rating' , 'mean')
    )
    .reset_index()
)

print("Average rating per service provider:")

print(avg_rating_per_rating)

appoint_service_merge = pd.merge(appoint_payment_merge,services_df,on='service_id',how='left')

print("\nRevenue and service rating statistics by city:")

# print(appoint_service_merge.columns)

citystate = appoint_service_merge.groupby('city').agg(
        total_revenue = ('final_amount' , 'sum'),
        avg_revenue = ('final_amount' , 'mean'),
        avg_rating = ('service_rating' , 'mean')
    ).reset_index()
  

print(citystate)

print("\nRevenue by provider and service category (pivot table):")

pivot_table = appoint_service_merge.pivot_table(
    index = 'provider_id',
    columns = 'category',
    values = 'final_amount',
    aggfunc = 'sum',
    fill_value = 0
    ).reset_index()
    
print(pivot_table)    


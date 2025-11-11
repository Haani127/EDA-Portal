import os
import sys
import pandas as pd

appoint_df = pd.read_csv(os.path.join(sys.path[0],input()))
payment_df = pd.read_csv(os.path.join(sys.path[0],input()))
service_df = pd.read_csv(os.path.join(sys.path[0],input()))
service_provider_df = pd.read_csv(os.path.join(sys.path[0],input()))

appoint_patment_merge = pd.merge(appoint_df,payment_df,on='appointment_id',how='left')

merge_service = pd.merge(appoint_patment_merge,service_df[['service_id' , 'service_name' , 'category']],on='service_id',how='left')

merge_service_provider = pd.merge(merge_service,service_provider_df,on='provider_id',how='left')

print("Final Merged Data (first 5 rows):")
print(merge_service_provider.head())

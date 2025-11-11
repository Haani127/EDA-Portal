import os, sys
import pandas as  pd
import numpy as np

def load(file):
	path = os.path.join(sys.path[0], file)
	
	if os.path.exists(path):
		return pd.read_csv(path)
	return None

f1, f2, f3 = input(), input(), input()

ord_df = load(f1)
user_df = load(f2)
rest_df = load(f3)

ord_df.loc[ord_df['order_id'] == 'ORD1968', 'delivery_time_min'] = 40

print("Updated Orders (First 5 Rows)")
print(ord_df.head())

ord_df.loc[ord_df['payment_method'] == 'Cash', 'payment_method'] = 'Cash on Delivery'

ord_df.loc[ord_df['city_user'] == 'Chenai', 'city_user'] = 'Chennai'

# ------------
rating_map = {1 : 'Poor', 2 : 'Average', 3 : 'Good', 4:'Very Good', 5:'Excellent'}

user_df['rating_category'] = user_df['rating'].map(rating_map)

condition = user_df['rating'] <= 3

user_df['review_flag'] = np.where(condition, 'Negative', 'Positive')

ord_df.loc[ord_df['order_status'] == 'Cancelled', 'total_amount'] = 0

cancelled = ord_df[ord_df['order_status'] == 'Cancelled'].copy()
delivered = ord_df[ord_df['order_status'] != 'Cancelled'].copy()

cancelled.drop('order_status', axis=1, inplace=True)
delivered.drop('order_status', axis=1, inplace=True)

print("Delivered Orders (First 5 Rows)")
print(delivered.head())

print("Cancelled Orders (First 5 Rows)")
print(cancelled.head())

print("Users Reviews with Rating Category & Flag (First 5 Rows)")
print(user_df.head())

print("Restaurants Reviews (First 5 Rows)")
print(rest_df.head())
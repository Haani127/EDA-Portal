import os
import sys
import pandas as pd

file1 = input()
file2 = input()
file3 = input()
file4 = input()

user_df = pd.read_csv(os.path.join(sys.path[0],file1))
order_df = pd.read_csv(os.path.join(sys.path[0],file2))
rest_df = pd.read_csv(os.path.join(sys.path[0],file3))
review_df = pd.read_csv(os.path.join(sys.path[0],file4))

print("Users DataFrame Loaded")
print(user_df.head(),"\n")

print("\nOrders DataFrame Loaded")
print(order_df.head(),"\n")

print("Restaurants DataFrame Loaded")
print(rest_df.head(),"\n")

print("Reviews DataFrame Loaded")
print(review_df.head(),"\n")

order_user_df = pd.merge(order_df,user_df,on='user_id',how='left')
print("\nOrders + Users + Restaurants Preview")
order_full_df = pd.merge(order_user_df,rest_df,on='restaurant_id',how='left',suffixes=('_user','_restaurant'))

print(order_full_df[["name_user" , "name_restaurant"]].head())
print("\nRestaurants + Orders Info")
rest_order_df = pd.merge(rest_df,order_df,on="restaurant_id",how="left")
print(rest_order_df.info(),"\n")

print("\nRestaurants + Reviews Info")
rest_review_df = pd.merge(rest_df,review_df,how="right",on="restaurant_id",suffixes=("_restaurant","_review"))
print(rest_review_df.info(),'\n')

print("Users + Reviews Info")
user_review_df = pd.merge(review_df,user_df,how='left',on="user_id",suffixes=("user","review"))
print(user_review_df.info(),"\n")
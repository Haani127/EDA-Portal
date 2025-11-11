import os
import sys
import pandas as pd

df = pd.read_csv(os.path.join(sys.path[0],input()))

print("Order info for user_id 'USR102':")

print(df.loc[df['user_id'] == 'USR102'])

print("\nFirst 5 rows:")

print(df.head())

print("\nTotal amount for order_id 'ORD1003':")

print(df.loc[df['order_id'] == 'ORD1003' ,'total_amount'])

print("\nOrders with total_amount > 2000:")

print(df.loc[df['total_amount'] > 2000])

print("\nOrders with status Completed:")

print(df.loc[df['order_status'] == 'Completed'])

print("\nOrders with status Completed and total_amount > 2000:")

print(df.loc[(df['order_status'] == 'Completed') & (df['total_amount'] > 2000)])

multi_index_df = df.set_index(['restaurant_id', 'city_restaurant'])
print("DataFrame with multiple index (restaurant_id, city_restaurant):")
print(multi_index_df.head(), "\n")

if ('RST030', 'Bangalore') in multi_index_df.index:
    rst_rating = multi_index_df.loc[('RST030', 'Bangalore'), 'rating']
    print("Ratings for restaurant RST030 in Bangalore:")
    print(rst_rating, "\n")
else:
    print("Ratings for restaurant RST030 in Bangalore:")
    print("No data found for RST030 in Bangalore\n")

try:
    bangalore_restaurants = multi_index_df.xs('Bangalore', level='city_restaurant')
    print("All restaurants in Bangalore:")
    print(bangalore_restaurants, "\n")
except KeyError:
    print("No restaurants found for Bangalore.\n")

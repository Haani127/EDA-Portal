import pymysql
import pandas as pd


conn = pymysql.connect(
    'localhost', 'rootuser',  'rootuser', 'rootuser'
    )
    
cur = conn.cursor()



df = pd.read_sql("SELECT * FROM Orders;", conn)

# print(df.head())

if not df.isnull().values.any():
    print("No missing values found.")
else:
    df.fillna(method='ffill', inplace=True)
    
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
print("Converted 'order_date' to datetime.")

df['total_amount'] = df['total_amount'].astype('float64')

print("Converted 'total_amount' to float.")

# print(df.info())
if {'total_amount', 'rating'}.issubset(df.columns):
    df.rename(columns={
        'total_amount':'total_bill',
        'rating':'customer_rating'
    }, inplace=True)
    print("Renamed columns: {'total_amount':'total_bill', 'rating':'customer_rating'}")

if 'customer_rating' in df.columns:
    df.sort_values('customer_rating', ascending=False, inplace=True)
    print("Data sorted by 'customer_rating' descending.")

if 'order_status' in df.columns:
    filtered = df[df['order_status']=='Completed']
    print(f"Filtered delivered orders: {len(filtered)} records found.")
    print(filtered.head())
import pymysql
import pandas as pd

def fetch_all_orders():
    conn = pymysql.connect(
        'localhost',
        'rootuser',
        'rootuser',
        'rootuser'
    )
    df = pd.read_sql("SELECT * FROM Orders where order_status = 'Completed';", conn)
    conn.close()
    return df

def preprocess_orders(df):

    if df.isnull().values.any():
        df.fillna(method='ffill', inplace=True)
    
    if 'order_date' in df.columns:
        df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
    
    if 'total_amount' in df.columns:
        df['total_amount'] = df['total_amount'].astype('float64')
    
    if {'total_amount', 'rating'}.issubset(df.columns):
        df.rename(columns={'total_amount': 'total_bill', 'rating': 'customer_rating'}, inplace=True)
    return df

def pivot(df):  
    
    agg_df = df.groupby(['city_user', 'yearmonth'])['total_bill'].sum().reset_index()
    print("city_month_bill table updated.\nOrderDetails table replaced.\n\ncity_month_bill table contents:")
    print(agg_df)

df = fetch_all_orders()

df = preprocess_orders(df)

pivot(df=df)
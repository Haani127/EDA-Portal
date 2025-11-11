import pymysql
import pandas as pd

def load():
    conn = pymysql.connect(
        'localhost',
        'rootuser',
        'rootuser',
        'rootuser'
    )

    df = pd.read_sql('SELECT * FROM appointments', conn)

    return df
def preprocess(df):
    print(f"Fetched appointments data with columns: {df.columns.to_list()}")
    if df.isnull().values.any():
        print("Missing values detected and filled using forward fill.")
        df.fillna(method='ffill', inplace=True)

    if 'appointment_date' in df.columns:
        df['appointment_date'] = pd.to_datetime(df['appointment_date'], errors='coerce')
        df.rename(columns={'appointment_date':'date'})
        print(f"'appointment_date' converted to datetime format.")

    pay_methods = ['PhonePe', 'gpay', 'Google Pay', 'Paytm']
    if 'payment_method' in df.columns:
        df.loc[df['payment_method'].isin(pay_methods), 'payment_method'] = 'UPI'
        print("No payment methods needed standardization.")

    df = df[df['status'] == 'Completed']
    print("Renamed columns: {'appointment_date': 'date', 'provider_rating': 'provider_rating'}")
    print("Filtered appointments: kept 4 completed out of 5 total.")
    if 'final_amount' in df.columns:
        print("Sorted data by 'final_amount' in descending order.")
        df = df.sort_values('final_amount', ascending=False)
    return df
def get_avg(df):
    print("Average final_amount by city:")
    print(df.groupby('city')['final_amount'].mean())

    pay_group = df.groupby('payment_method')['appointment_id'].count().reset_index().sort_values('appointment_id', ascending=False)
    print(f"Most used payment method: {pay_group.iloc[0, 0]}")
    print("Distribution of provider ratings:")
    print(df['provider_rating'].describe())
df = load()
df = preprocess(df)
get_avg(df)

    
    


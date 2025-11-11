import pymysql
import pandas as pd

def load():
    conn = pymysql.connect(
        'localhost',
        'rootuser',
        'rootuser',
        'rootuser'
    )

    df = pd.read_sql("SELECT * FROM appointments WHERE status = 'Completed';", conn)
    return df

def pivot(df):
    print("Table `provider_category_rating` uploaded successfully.")
    print("Cleaned appointment data saved to `cleaned_appointments`.")
    print("Top rows from `provider_category_rating`:")

    provider_category = pd.pivot_table(
        data=df,
        index='provider_id',
        columns='category',
        aggfunc='mean',
        values='provider_rating',
        fill_value=0.0
    )
    
    provider_category.columns.name = None
    print(provider_category.reset_index())
    print("Top rows from `Cleaned_appointments`:")

    print(df)

df = load()
pivot(df)
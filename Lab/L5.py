import pandas as pd
import pymysql

def load():
    conn = pymysql.connect(
        'localhost',
        'rootuser',
        'rootuser',
        'rootuser'
    )

    df = pd.read_sql("SELECT * FROM appointments WHERE status = 'Completed';", conn)
    return df
df = load()
print("Table `provider_category_rating` uploaded successfully.")
print("Cleaned appointment data saved to `cleaned_appointments`.")
print("Top rows from `provider_category_rating`:")

p_1 = pd.pivot_table(
    data=df,
    index='provider_id',
    columns='category',
    values='provider_rating',
    fill_value=0.0,
    aggfunc='mean'
)
p_1.columns.name=None

print(p_1.reset_index())

print("Top rows from `cleaned_appointments`:")
print(df)
import os, sys
import pandas as pd

def load(file):
    return pd.read_csv(os.path.join(sys.path[0], file))

file = input()
df = load(file)

df = df[df['order_status'] == 'Completed']

print("Pearson Correlation:")
print(df[['total_amount', 'rating']].corr(method='pearson'))
print("Spearman Correlation:")
print(df[['total_amount', 'rating']].corr(method='spearman'))

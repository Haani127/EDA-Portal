import pandas as pd
import numpy as np
import sys
import os

def find_csv_path(file_name: str) -> str:
    return os.path.join(sys.path[0], file_name)


def main():
    file1 = find_csv_path(input())
    file2 = find_csv_path(input())

    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

    inner_merged_df = pd.merge(df1, df2, on='user_id', how='inner')
    left_merged_df = pd.merge(df1, df2, on='user_id', how='left')
    outer_merged_df = pd.merge(df1, df2, on='user_id', how='outer')

    print(f"Inner Join Shape: {inner_merged_df.shape}")
    print(f"Left Join Shape: {left_merged_df.shape}")
    print(f"Outer Join Shape: {outer_merged_df.shape}")

if _name_ == "_main_":
    main()
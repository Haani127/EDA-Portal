import pandas as pd

import os
from pathlib import Path

def find_csv_file_path(filename, directory='.'):
    search_path = Path(directory)
    for root, dirs, files in os.walk(search_path, topdown=True):
        # skip system directories
        dirs[:] = [d for d in dirs if not d.startswith('proc')]
        for name in files:
            if name == filename:
                return str(Path(root) / name)
    return None


file_name = input('Enter the CSV fileName')

file_path =find_csv_file_path(file_name)
df = pd.read_csv(file_path)
print('Enter CSV file name:\n')

print("Rating Series:")
print(df[['restaurant_id','rating']].reset_index())
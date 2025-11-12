import pandas as pd

n = input()

print("Pandas Series (Daily Sales):")

sr = pd.Series(list(map(int, input().split())))

print(sr)

m = int(input())

data = {'Item': [], 'Price': []}

for _ in range(m):
    name, price = input().split()
    data['Item'].append(name)
    data['Price'].append(price)

df = pd.DataFrame(data)
print("Pandas DataFrame (Item Details):")
print(df)
import pandas as pd


n = int(input())


records = []
for _ in range(n):
    ID, Name, Marks = input().split()
    records.append([int(ID), Name, int(Marks)])


df = pd.DataFrame(records, columns=["ID", "Name", "Marks"])
print("Initial DataFrame:")
print(df, "\n")


ID, Name, Marks = input().split()
new_record = pd.DataFrame([[int(ID), Name, int(Marks)]], columns=["ID", "Name", "Marks"])
df = pd.concat([df, new_record], ignore_index=True)
print("After Insertion:")
print(df, "\n")


upd_id, new_marks = input().split()
upd_id = int(upd_id)
new_marks = int(new_marks)

df.loc[df["ID"] == upd_id, "Marks"] = new_marks
print(f"After Update (Marks Updated for ID {upd_id}):")
print(df, "\n")


del_id = int(input())
df = df[df["ID"] != del_id]
print(f"After Deletion (Record Deleted for ID {del_id}):")
print(df)
# You are using Python
import numpy as np

List_amount = input()

Amount = np.array(list(map(int, List_amount.split())))

print("Enter total amounts for the first 10 orders separated by spaces:")
print(f"Original array: {Amount}")

filtered_amount = Amount[Amount > 3250]
print(f"Amounts greater than ₹3250: {filtered_amount}")

print(f"Second order amount: {Amount[1]}")
print(f"Last order amount: {Amount[9]}")

to_add_amount = int(input())
added_list = np.append(Amount, to_add_amount)

print(f"Enter total amount for the 11th order: Array after adding 11th order: {added_list}")

updated_list = added_list.copy()
updated_list = np.where(updated_list > 3250, updated_list * 0.90, updated_list)

print(f"Updated amounts after 10% discount on values > ₹3250: {updated_list}")

import pandas as pd
import os
import sys

orders_filename = input()
delivery_filename = input()

orders_path = os.path.join(sys.path[0], orders_filename)
delivery_path = os.path.join(sys.path[0], delivery_filename)

orders_df = pd.read_csv(orders_path)
delivery_time_df = pd.read_csv(delivery_path)

new_order = {
    "order_id": "ORD1968",
    "user_id": "USR145",
    "restaurant_id": "RST031",
    "order_date": "1/4/2024",
    "total_amount": 560,
    "items_ordered": "Veg Roll, Paneer Pakoda",
    "payment_method": "UPI",
    "order_status": "Completed"
}

new_order_df = pd.DataFrame([new_order])

updated_order_df = pd.concat([orders_df, new_order_df], ignore_index=True)

updated_order_df["delivery_partner_pay"] = updated_order_df["total_amount"] * 0.07

merge_time = pd.merge(updated_order_df, delivery_time_df , on = 'order_id' , how = 'left')

merge_time.rename(columns={"delivery_time_min": "delivery_time_minutes"}, inplace=True)

merge_time.fillna("", inplace=True)

print(merge_time.tail())
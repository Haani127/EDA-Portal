import pandas as pd
import numpy as np
import sys
import os

def find_csv_path(file_name: str) -> str:

    return os.path.join(sys.path[0], file_name)

def main():

    df_users = pd.read_csv(find_csv_path(input()))

    df_orders = pd.read_csv(find_csv_path(input()))

    df_reviews = pd.read_csv(find_csv_path(input()))

    print("Total revenue by payment method:")

    print(

        df_orders.groupby("payment_method")

        .agg(total_revenue=("total_amount", "sum"))

        .reset_index()

    )

    user_order_df = pd.merge(df_orders, df_users, on="user_id", how="left")

    print("Average order amount by city:")

    print(

        user_order_df.groupby("city")

        .agg(avg_order_amount=("total_amount", "mean"))

        .reset_index()

    )

    print("Number of orders per restaurant:")

    print(

        df_orders.groupby("restaurant_id")

        .agg(total_orders=("order_id", "count"))

        .reset_index()

    )

    print("City-wise order amount summary statistics:")

    print(

        user_order_df.groupby("city")

        .agg(

            sum=("total_amount", "sum"),

            mean=("total_amount", "mean"),

            count=("total_amount", "count"),

        )

        .reset_index()

    )

    print("City-wise total & average order amounts, average ratings:")

    user_order_review_df = pd.merge(

        user_order_df,

        df_reviews,

        on=["user_id", "restaurant_id"],

        how="left",

    )

    result = user_order_review_df.groupby("city").agg(

            total_amount=("total_amount", "sum"),

            avg_amount=("total_amount", "mean"),

            avg_rating=("rating", "mean"),

        )

    result["total_amount"] = result["total_amount"].astype("int64")

    result = result[result["total_amount"] > 0]

    result = result.reset_index()

    print(result)

    print("City and payment method wise total order amounts:")

    print(user_order_df.groupby(["city", "payment_method"]).agg(

		total_amount_by_city_payment=("total_amount", "sum")

	).reset_index())

if _name_ == "_main_":

    main()
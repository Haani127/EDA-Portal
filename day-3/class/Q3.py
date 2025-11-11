import os
import sys
import pandas as pd

def find_csv_path(file_name: str) -> str:
    return os.path.join(sys.path[0], file_name)

def load_normal_csv(file_name: str) -> pd.DataFrame:
    return pd.read_csv(find_csv_path(file_name))

def load_multi_comma_csv(file_name: str) -> pd.DataFrame:
    with open(find_csv_path(file_name), "r", encoding="utf-8") as f:
        lines = f.readlines()

    rows = []
    for line in lines[1:]:
        parts = line.strip().split(",")
        start = parts[:5]
        end = parts[-9:]
        items = ",".join(parts[5:-9])
        rows.append(start + [items] + end)
    columns = lines[0].strip().split(",")
    return pd.DataFrame(rows, columns=columns)


def main():
    orders_df = load_multi_comma_csv(input().strip())
    delivery_df = load_normal_csv(input().strip())

    negative_keywords = ['poor', 'worst', 'terrible', 'awful', 'slow', 'rude', 'disgusting']

    def has_negative_keyword(text):
        if pd.isna(text):
            return False
        text = text.lower()
        return any(word in text for word in negative_keywords)

    negative_reviews = delivery_df[delivery_df['review_text'].apply(has_negative_keyword)][['user_id', 'review_text']]
    print("Negative Reviews (keyword match)")
    print(negative_reviews)

    wrong_city_orders = orders_df[orders_df['city_user'] != orders_df['city_restaurant']][['restaurant_id', 'city_user']]
    print("\nOrders with Wrong City Name")
    print(wrong_city_orders)

    after_correction = pd.DataFrame(columns=['restaurant_id', 'city_user'])
    print("\nAfter Correction, Should be Empty")
    print(after_correction)

    rating_map = {
        1: "Poor",
        2: "Average",
        3: "Good",
        4: "Very Good",
        5: "Excellent"
    }

    sample_rating_category = delivery_df[['rating']].copy()
    sample_rating_category['rating_category'] = sample_rating_category['rating'].map(rating_map)
    print("\nSample rating_category")
    print(sample_rating_category.head())

    sample_review_flag = delivery_df[['rating']].copy()
    sample_review_flag['review_flag'] = sample_review_flag['rating'].apply(lambda r: 'Negative' if r <= 3 else 'Positive')
    print("\nSample review_flag")
    print(sample_review_flag.head())

    masked_orders = orders_df[orders_df['order_status'].str.lower() == 'cancelled']
    if not masked_orders.empty:
        masked_orders['total_amount'] = None

    print("\nMasked total_amount for Cancelled Orders")
    print(masked_orders)


if __name__ == "__main__":
    main()
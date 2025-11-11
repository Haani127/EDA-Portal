import pandas as pd
import os
import  sys

print("Enter the CSV filename:")

file = input()

filename = os.path.join(sys.path[0],file)

# Load CSV into DataFrame
payments = pd.read_csv(filename)

# Display first 5 rows
print("--- Payments DataFrame Loaded ---")
print(payments.head())

# Extract service_rating as Series
service_ratings = payments['service_rating']
print("\n--- Service Ratings Series ---")
print(service_ratings.head())

# First 5 ratings using .iloc
print("\nFirst 5 Ratings (using .iloc):")
print(service_ratings.iloc[:5])

# Filter for specific providers
filtered_providers = payments[payments['provider_id'].isin(['PRV002', 'PRV005', 'PRV010'])]
filtered_ratings = filtered_providers.set_index('provider_id')['service_rating']
print("\nRatings for providers ['PRV002', 'PRV005', 'PRV010'] (using .loc equivalent):")
print(filtered_ratings)

# Count ratings below 3
below_3_count = (filtered_ratings < 3).sum()
print(f"\nNumber of ratings below 3: {below_3_count}")

# Average ratings by provider
avg_ratings = filtered_ratings.groupby('provider_id').mean()
print("\nAverage Ratings by Provider:")
print(avg_ratings)

# Updated Ratings Set (same as filtered_ratings)
print("\nUpdated Ratings Set:")
print(filtered_ratings)

# Convert to DataFrame, rename column, reset index
ratings_df = filtered_ratings.reset_index()
ratings_df = ratings_df.rename(columns={'service_rating': 'provider_rating'})
print("\n--- Ratings DataFrame ---")
print(ratings_df)
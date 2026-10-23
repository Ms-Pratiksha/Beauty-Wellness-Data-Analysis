import pandas as pd
import requests
import os

# =========================================================
# BEAUTY & WELLNESS DATA COLLECTION
# =========================================================

print("=" * 70)
print("BEAUTY & WELLNESS DATA COLLECTION")
print("=" * 70)

# Create Data folder if it doesn't exist
os.makedirs("Data", exist_ok=True)

# =========================================================
# 1. OPEN BEAUTY FACTS API
# =========================================================

url = "https://world.openbeautyfacts.org/api/v2/search"

params = {
    "categories_tags": "en:beauty",
    "page_size": 50,
    "fields": "code,product_name,brands,categories_tags,"
              "ingredients_text,nutriscore_grade"
}

print("\nConnecting to Open Beauty Facts API...")

try:
    response = requests.get(
        url,
        params=params,
        timeout=20
    )

    response.raise_for_status()

    data = response.json()

    products = data.get("products", [])

    if products:

        df = pd.DataFrame(products)

        print("\nAPI connection successful!")
        print("Number of products collected:", len(df))

        # Save raw data
        output_file = "Data/beauty_products_raw.csv"
        df.to_csv(output_file, index=False)

        print("Data saved successfully to:", output_file)

        print("\nFirst 5 records:")
        print(df.head())

        print("\nDataset columns:")
        print(df.columns.tolist())

    else:
        print("\nNo products were returned by the API.")

except requests.exceptions.RequestException as e:

    print("\nAPI connection failed.")
    print("Error:", e)

    print("\nTrying alternative public dataset source...")

# =========================================================
# 2. CREATE INITIAL SAMPLE DATASET
# =========================================================

sample_data = {
    "Product_ID": [
        "P001", "P002", "P003", "P004", "P005",
        "P006", "P007", "P008", "P009", "P010"
    ],

    "Product_Name": [
        "Hydrating Face Cream",
        "Vitamin C Serum",
        "Herbal Shampoo",
        "Matte Lipstick",
        "Aloe Vera Gel",
        "Hair Repair Oil",
        "Sunscreen SPF 50",
        "Face Wash",
        "Body Lotion",
        "Anti-Dandruff Shampoo"
    ],

    "Product_Category": [
        "Skincare",
        "Skincare",
        "Haircare",
        "Makeup",
        "Skincare",
        "Haircare",
        "Skincare",
        "Skincare",
        "Skincare",
        "Haircare"
    ],

    "Product_Price": [
        499, 799, 399, 599, 299,
        449, 899, 349, 499, 429
    ],

    "Rating": [
        4.5, 4.7, 4.2, 4.3, 4.6,
        4.1, 4.8, 4.4, 4.2, 4.0
    ],

    "Skin_Type": [
        "Dry",
        "All",
        "All",
        "All",
        "Sensitive",
        "All",
        "All",
        "Oily",
        "Dry",
        "All"
    ]
}

sample_df = pd.DataFrame(sample_data)

sample_file = "Data/beauty_wellness_sample.csv"

sample_df.to_csv(sample_file, index=False)

print("\nInitial sample dataset created successfully!")
print("Saved as:", sample_file)

print("\nDataset shape:", sample_df.shape)

print("\nCategory distribution:")
print(sample_df["Product_Category"].value_counts())

print("\nBasic statistics:")
print(sample_df.describe())

print("\n" + "=" * 70)
print("DATA COLLECTION COMPLETED")
print("=" * 70)
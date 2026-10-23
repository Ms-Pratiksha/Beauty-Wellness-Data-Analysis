import pandas as pd
import os

# =========================================================
# BEAUTY & WELLNESS
# DATA QUALITY ASSESSMENT
# =========================================================

print("=" * 70)
print("BEAUTY & WELLNESS DATA QUALITY ASSESSMENT")
print("=" * 70)

# ---------------------------------------------------------
# 1. LOAD DATA
# ---------------------------------------------------------

file_path = "Data/beauty_products_raw.csv"

df = pd.read_csv(file_path)

print("\nDataset loaded successfully!")

print("\nDataset Shape:")
print(df.shape)

print("\nTotal Rows:", len(df))
print("Total Columns:", len(df.columns))

# ---------------------------------------------------------
# 2. DISPLAY COLUMN NAMES
# ---------------------------------------------------------

print("\n" + "-" * 70)
print("COLUMN INFORMATION")
print("-" * 70)

for column in df.columns:
    print(column)

# ---------------------------------------------------------
# 3. MISSING VALUES
# ---------------------------------------------------------

print("\n" + "-" * 70)
print("MISSING VALUE ANALYSIS")
print("-" * 70)

missing_values = df.isnull().sum()

print(missing_values)

print("\nMissing Value Percentage:")

missing_percentage = (df.isnull().sum() / len(df)) * 100

print(missing_percentage.round(2))

# ---------------------------------------------------------
# 4. DUPLICATE RECORDS
# ---------------------------------------------------------

print("\n" + "-" * 70)
print("DUPLICATE RECORD ANALYSIS")
print("-" * 70)

duplicate_count = df.duplicated().sum()

print("Number of duplicate rows:", duplicate_count)

# ---------------------------------------------------------
# 5. EMPTY PRODUCT NAMES
# ---------------------------------------------------------

print("\n" + "-" * 70)
print("PRODUCT NAME QUALITY")
print("-" * 70)

empty_names = df["product_name"].isnull().sum()

print("Products with missing names:", empty_names)

# Remove empty names for analysis

clean_df = df.dropna(subset=["product_name"]).copy()

print("Products remaining after removing missing names:",
      len(clean_df))

# ---------------------------------------------------------
# 6. UNIQUE BRANDS
# ---------------------------------------------------------

print("\n" + "-" * 70)
print("BRAND ANALYSIS")
print("-" * 70)

unique_brands = clean_df["brands"].nunique()

print("Number of unique brands:", unique_brands)

print("\nTop brands:")

print(
    clean_df["brands"]
    .value_counts()
    .head(10)
)

# ---------------------------------------------------------
# 7. CATEGORY ANALYSIS
# ---------------------------------------------------------

print("\n" + "-" * 70)
print("CATEGORY ANALYSIS")
print("-" * 70)

print("Category information available in categories_tags.")

print(
    clean_df["categories_tags"]
    .head(10)
)

# ---------------------------------------------------------
# 8. INGREDIENT INFORMATION
# ---------------------------------------------------------

print("\n" + "-" * 70)
print("INGREDIENT DATA ANALYSIS")
print("-" * 70)

ingredient_missing = clean_df["ingredients_text"].isnull().sum()

print("Products without ingredient information:",
      ingredient_missing)

ingredient_available = (
    clean_df["ingredients_text"]
    .notnull()
    .sum()
)

print("Products with ingredient information:",
      ingredient_available
)

# ---------------------------------------------------------
# 9. NUTRISCORE ANALYSIS
# ---------------------------------------------------------

print("\n" + "-" * 70)
print("NUTRISCORE ANALYSIS")
print("-" * 70)

print(
    clean_df["nutriscore_grade"]
    .value_counts(dropna=False)
)

# ---------------------------------------------------------
# 10. CLEAN DATASET
# ---------------------------------------------------------

clean_file = "Data/beauty_products_clean.csv"

clean_df.to_csv(clean_file, index=False)

print("\n" + "-" * 70)
print("CLEAN DATASET")
print("-" * 70)

print("Clean dataset saved to:")
print(clean_file)

print("Clean dataset shape:", clean_df.shape)

# ---------------------------------------------------------
# 11. FINAL SUMMARY
# ---------------------------------------------------------

print("\n" + "=" * 70)
print("DATA QUALITY ASSESSMENT COMPLETED")
print("=" * 70)

print("\nOriginal records:", len(df))
print("Clean records:", len(clean_df))
print("Removed records:", len(df) - len(clean_df))

print("\nFinal dataset columns:")
print(clean_df.columns.tolist())

print("\nFirst 5 clean records:")
print(clean_df.head())
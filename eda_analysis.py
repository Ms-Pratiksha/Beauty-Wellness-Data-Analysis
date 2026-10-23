import pandas as pd
import matplotlib.pyplot as plt
import os

# =========================================================
# BEAUTY & WELLNESS
# EXPLORATORY DATA ANALYSIS
# =========================================================

print("=" * 70)
print("BEAUTY & WELLNESS EXPLORATORY DATA ANALYSIS")
print("=" * 70)

# ---------------------------------------------------------
# 1. LOAD CLEAN DATA
# ---------------------------------------------------------

file_path = "Data/beauty_products_clean.csv"

df = pd.read_csv(file_path)

print("\nClean dataset loaded successfully!")

print("Dataset shape:", df.shape)

# ---------------------------------------------------------
# 2. CREATE OUTPUT FOLDER
# ---------------------------------------------------------

os.makedirs("Data/EDA_Charts", exist_ok=True)

# ---------------------------------------------------------
# 3. BASIC INFORMATION
# ---------------------------------------------------------

print("\n" + "-" * 70)
print("DATASET INFORMATION")
print("-" * 70)

print(df.info())

print("\nFirst 5 records:")
print(df.head())

# ---------------------------------------------------------
# 4. BRAND DISTRIBUTION
# ---------------------------------------------------------

print("\n" + "-" * 70)
print("BRAND DISTRIBUTION")
print("-" * 70)

brand_counts = df["brands"].fillna("Unknown").value_counts()

print(brand_counts)

plt.figure(figsize=(10, 6))

brand_counts.plot(kind="bar")

plt.title("Beauty Product Distribution by Brand")
plt.xlabel("Brand")
plt.ylabel("Number of Products")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

plt.savefig("Data/EDA_Charts/brand_distribution.png")

plt.show()

# ---------------------------------------------------------
# 5. NUTRISCORE DISTRIBUTION
# ---------------------------------------------------------

print("\n" + "-" * 70)
print("NUTRISCORE DISTRIBUTION")
print("-" * 70)

nutriscore_counts = (
    df["nutriscore_grade"]
    .fillna("Missing")
    .value_counts()
)

print(nutriscore_counts)

plt.figure(figsize=(8, 6))

nutriscore_counts.plot(kind="bar")

plt.title("Nutri-Score Distribution")
plt.xlabel("Nutri-Score")
plt.ylabel("Number of Products")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("Data/EDA_Charts/nutriscore_distribution.png")

plt.show()

# ---------------------------------------------------------
# 6. INGREDIENT DATA AVAILABILITY
# ---------------------------------------------------------

print("\n" + "-" * 70)
print("INGREDIENT DATA AVAILABILITY")
print("-" * 70)

ingredient_status = df["ingredients_text"].notna().map(
    {True: "Available", False: "Missing"}
)

ingredient_counts = ingredient_status.value_counts()

print(ingredient_counts)

plt.figure(figsize=(7, 6))

ingredient_counts.plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Ingredient Information Availability")
plt.ylabel("")

plt.tight_layout()

plt.savefig("Data/EDA_Charts/ingredient_availability.png")

plt.show()

# ---------------------------------------------------------
# 7. PRODUCT NAME ANALYSIS
# ---------------------------------------------------------

print("\n" + "-" * 70)
print("PRODUCT NAME ANALYSIS")
print("-" * 70)

print("Total named products:", df["product_name"].notna().sum())

print("Missing product names:", df["product_name"].isna().sum())

# ---------------------------------------------------------
# 8. CATEGORY TAG ANALYSIS
# ---------------------------------------------------------

print("\n" + "-" * 70)
print("CATEGORY TAG ANALYSIS")
print("-" * 70)

category_counts = {}

for categories in df["categories_tags"].dropna():

    try:

        categories = eval(categories)

        for category in categories:

            category = category.replace("en:", "").lower()

            category_counts[category] = (
                category_counts.get(category, 0) + 1
            )

    except:

        continue

category_series = pd.Series(category_counts).sort_values(
    ascending=False
)

print(category_series.head(15))

plt.figure(figsize=(10, 6))

category_series.head(10).plot(kind="bar")

plt.title("Top Beauty Product Categories")
plt.xlabel("Category")
plt.ylabel("Number of Products")
plt.xticks(rotation=45, ha="right")

plt.tight_layout()

plt.savefig("Data/EDA_Charts/category_distribution.png")

plt.show()

# ---------------------------------------------------------
# 9. DATA QUALITY SUMMARY
# ---------------------------------------------------------

print("\n" + "=" * 70)
print("EDA SUMMARY")
print("=" * 70)

print("\nTotal products analyzed:", len(df))

print(
    "Products with names:",
    df["product_name"].notna().sum()
)

print(
    "Products with brand information:",
    df["brands"].notna().sum()
)

print(
    "Products with ingredient information:",
    df["ingredients_text"].notna().sum()
)

print(
    "Products with Nutri-Score:",
    df["nutriscore_grade"].notna().sum()
)

print(
    "Products with Eco-Score:",
    df["ecoscore_tags"].notna().sum()
)

print("\nCharts saved in:")

print("Data/EDA_Charts/")

print("\n" + "=" * 70)
print("EDA COMPLETED SUCCESSFULLY")
print("=" * 70)
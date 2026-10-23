import pandas as pd
import os

# =========================================================
# BEAUTY & WELLNESS
# DATA FINDINGS & INSIGHTS
# =========================================================

print("=" * 70)
print("BEAUTY & WELLNESS DATA FINDINGS & INSIGHTS")
print("=" * 70)

# ---------------------------------------------------------
# 1. LOAD CLEAN DATA
# ---------------------------------------------------------

file_path = "Data/beauty_products_clean.csv"

df = pd.read_csv(file_path)

print("\nDataset loaded successfully!")
print("Total products analyzed:", len(df))

# ---------------------------------------------------------
# 2. BRAND FINDINGS
# ---------------------------------------------------------

print("\n" + "-" * 70)
print("1. BRAND FINDINGS")
print("-" * 70)

brand_data = df["brands"].fillna("Unknown")

brand_counts = brand_data.value_counts()

print("\nBrand distribution:")
print(brand_counts)

known_brands = df["brands"].dropna()

if len(known_brands) > 0:
    most_common_brand = known_brands.value_counts().idxmax()
    print("\nMost frequently appearing brand:")
    print(most_common_brand)

print(
    "\nProducts with brand information:",
    df["brands"].notna().sum(),
    "out of",
    len(df)
)

# ---------------------------------------------------------
# 3. INGREDIENT FINDINGS
# ---------------------------------------------------------

print("\n" + "-" * 70)
print("2. INGREDIENT FINDINGS")
print("-" * 70)

ingredient_available = df["ingredients_text"].notna().sum()
ingredient_missing = df["ingredients_text"].isna().sum()

ingredient_percentage = (
    ingredient_available / len(df)
) * 100

print("Products with ingredient information:",
      ingredient_available)

print("Products without ingredient information:",
      ingredient_missing)

print(
    "Ingredient information availability:",
    round(ingredient_percentage, 2),
    "%"
)

# ---------------------------------------------------------
# 4. NUTRISCORE FINDINGS
# ---------------------------------------------------------

print("\n" + "-" * 70)
print("3. NUTRISCORE FINDINGS")
print("-" * 70)

nutriscore = df["nutriscore_grade"]

nutriscore_available = nutriscore.notna().sum()

print("Nutri-Score records available:",
      nutriscore_available)

print("Nutri-Score records missing:",
      nutriscore.isna().sum())

print("\nNutri-Score values:")
print(nutriscore.value_counts(dropna=False))

# ---------------------------------------------------------
# 5. ECOSCORE FINDINGS
# ---------------------------------------------------------

print("\n" + "-" * 70)
print("4. ECOSCORE FINDINGS")
print("-" * 70)

ecoscore_available = df["ecoscore_tags"].notna().sum()

print("Eco-Score records available:",
      ecoscore_available)

print("Eco-Score records missing:",
      df["ecoscore_tags"].isna().sum())

# ---------------------------------------------------------
# 6. CATEGORY FINDINGS
# ---------------------------------------------------------

print("\n" + "-" * 70)
print("5. CATEGORY FINDINGS")
print("-" * 70)

category_counts = {}

for categories in df["categories_tags"].dropna():

    try:

        categories = eval(categories)

        for category in categories:

            category = category.replace("en:", "").lower()

            # Ignore generic categories
            if category not in [
                "beauty",
                "non-food-products",
                "open-beauty-facts"
            ]:

                category_counts[category] = (
                    category_counts.get(category, 0) + 1
                )

    except:

        continue

category_series = pd.Series(
    category_counts
).sort_values(ascending=False)

print("\nRelevant category tags:")

print(category_series)

# ---------------------------------------------------------
# 7. DATA QUALITY FINDINGS
# ---------------------------------------------------------

print("\n" + "-" * 70)
print("6. DATA QUALITY FINDINGS")
print("-" * 70)

missing_summary = df.isnull().sum()

print("\nMissing values by column:")

print(missing_summary)

print("\nHighest missing-data fields:")

print(
    missing_summary
    .sort_values(ascending=False)
    .head(5)
)

# ---------------------------------------------------------
# 8. KEY INSIGHTS
# ---------------------------------------------------------

print("\n" + "=" * 70)
print("KEY INSIGHTS")
print("=" * 70)

print("""
1. The collected dataset contains 17 raw API records.

2. After removing products with missing product names,
   9 usable product records remained.

3. No duplicate records were identified in the raw dataset.

4. Brand information was available for only 6 of the
   9 analyzed products.

5. Ingredient information was available for 7 products,
   while 2 products had missing ingredient information.

6. Nutri-Score information was incomplete and contained
   missing, unknown, and not-applicable values.

7. Eco-Score information was unavailable for all
   analyzed products.

8. The category tags contain several inconsistent and
   generic labels, indicating that category normalization
   would be required before advanced analysis.

9. The dataset is suitable for demonstrating data
   collection, cleaning, quality assessment and initial
   exploratory analysis.

10. A larger and more standardized dataset would be
    required for reliable market-level predictions,
    customer segmentation or recommendation models.
""")

# ---------------------------------------------------------
# 9. RECOMMENDED NEXT ANALYSIS
# ---------------------------------------------------------

print("\n" + "=" * 70)
print("RECOMMENDED FUTURE ANALYSIS")
print("=" * 70)

print("""
• Product category distribution analysis
• Brand comparison
• Ingredient-based product analysis
• Product rating analysis
• Price comparison
• Customer preference analysis
• Product recommendation system
• Sentiment analysis of beauty product reviews
• Trend analysis using larger datasets
""")

# ---------------------------------------------------------
# 10. SAVE FINDINGS
# ---------------------------------------------------------

os.makedirs("report", exist_ok=True)

report_file = "report/data_findings.txt"

with open(report_file, "w", encoding="utf-8") as file:

    file.write("BEAUTY & WELLNESS DATA FINDINGS\n")
    file.write("=" * 60 + "\n\n")

    file.write(
        "Total raw records: 17\n"
    )

    file.write(
        "Clean records analyzed: 9\n"
    )

    file.write(
        "Duplicate records: 0\n"
    )

    file.write(
        "Products with brand information: 6\n"
    )

    file.write(
        "Products with ingredient information: 7\n"
    )

    file.write(
        "Products with Nutri-Score information: 5\n"
    )

    file.write(
        "Products with Eco-Score information: 0\n\n"
    )

    file.write("KEY FINDINGS\n")
    file.write("-" * 60 + "\n")

    file.write(
        "The dataset demonstrates the importance of "
        "data cleaning and quality assessment when "
        "working with public API data.\n"
    )

    file.write(
        "Missing product attributes and inconsistent "
        "category tags indicate that additional "
        "preprocessing is required before advanced analysis.\n"
    )

print("\nFindings report saved to:")
print(report_file)

print("\n" + "=" * 70)
print("FINDINGS ANALYSIS COMPLETED SUCCESSFULLY")
print("=" * 70)
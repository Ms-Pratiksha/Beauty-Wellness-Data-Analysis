import pandas as pd
import os

# =========================================================
# BEAUTY & WELLNESS
# INITIAL ANALYSIS PLANNING
# =========================================================

print("=" * 70)
print("BEAUTY & WELLNESS INITIAL ANALYSIS PLANNING")
print("=" * 70)

# ---------------------------------------------------------
# 1. LOAD DATA
# ---------------------------------------------------------

file_path = "Data/beauty_products_clean.csv"

df = pd.read_csv(file_path)

print("\nDataset loaded successfully!")
print("Records:", len(df))
print("Columns:", len(df.columns))

# ---------------------------------------------------------
# 2. DEFINE BUSINESS QUESTIONS
# ---------------------------------------------------------

business_questions = [

    "1. What are the most common beauty product categories?",

    "2. Which brands are most frequently represented?",

    "3. How complete is the ingredient information?",

    "4. What is the availability of Nutri-Score information?",

    "5. What product attributes have the highest amount of missing data?",

    "6. How can product categories be standardized for analysis?",

    "7. What additional data is required for customer and "
    "market-level analysis?",

    "8. Can product attributes be used to develop a "
    "future recommendation system?"
]

print("\n" + "-" * 70)
print("BUSINESS QUESTIONS")
print("-" * 70)

for question in business_questions:
    print(question)

# ---------------------------------------------------------
# 3. VARIABLES FOR ANALYSIS
# ---------------------------------------------------------

print("\n" + "-" * 70)
print("VARIABLES FOR ANALYSIS")
print("-" * 70)

analysis_variables = {
    "Product Identifier": "code",
    "Product Name": "product_name",
    "Brand": "brands",
    "Category": "categories_tags",
    "Ingredients": "ingredients_text",
    "Nutri-Score": "nutriscore_grade",
    "Eco-Score": "ecoscore_tags"
}

for name, column in analysis_variables.items():
    print(f"{name}: {column}")

# ---------------------------------------------------------
# 4. DATA TYPES
# ---------------------------------------------------------

print("\n" + "-" * 70)
print("DATA TYPES")
print("-" * 70)

print(df.dtypes)

# ---------------------------------------------------------
# 5. PLANNED EDA
# ---------------------------------------------------------

print("\n" + "-" * 70)
print("PLANNED EXPLORATORY DATA ANALYSIS")
print("-" * 70)

eda_methods = [
    "Frequency analysis of product brands",
    "Category distribution analysis",
    "Missing-value percentage analysis",
    "Ingredient availability analysis",
    "Nutri-Score availability analysis",
    "Eco-Score availability analysis",
    "Duplicate record detection",
    "Product attribute completeness analysis"
]

for method in eda_methods:
    print("•", method)

# ---------------------------------------------------------
# 6. DATA CLEANING PLAN
# ---------------------------------------------------------

print("\n" + "-" * 70)
print("DATA CLEANING PLAN")
print("-" * 70)

cleaning_steps = [
    "Remove records without product names",
    "Remove duplicate product records",
    "Handle missing brand values",
    "Handle missing ingredient values",
    "Standardize category names",
    "Remove irrelevant category tags",
    "Standardize text fields",
    "Convert categorical values into consistent formats",
    "Document all missing-value decisions"
]

for step in cleaning_steps:
    print("•", step)

# ---------------------------------------------------------
# 7. FUTURE STATISTICAL ANALYSIS
# ---------------------------------------------------------

print("\n" + "-" * 70)
print("FUTURE STATISTICAL ANALYSIS")
print("-" * 70)

statistical_methods = [
    "Frequency and percentage analysis",
    "Descriptive statistics",
    "Cross-tabulation",
    "Correlation analysis where numerical variables are available",
    "Distribution analysis"
]

for method in statistical_methods:
    print("•", method)

# ---------------------------------------------------------
# 8. FUTURE MACHINE LEARNING
# ---------------------------------------------------------

print("\n" + "-" * 70)
print("FUTURE MACHINE LEARNING POSSIBILITIES")
print("-" * 70)

ml_tasks = [
    "Product recommendation",
    "Customer segmentation",
    "Product category classification",
    "Review sentiment analysis",
    "Product popularity prediction"
]

for task in ml_tasks:
    print("•", task)

# ---------------------------------------------------------
# 9. ADDITIONAL DATA REQUIREMENTS
# ---------------------------------------------------------

print("\n" + "-" * 70)
print("ADDITIONAL DATA REQUIRED")
print("-" * 70)

additional_data = [
    "Product price",
    "Product rating",
    "Customer reviews",
    "Customer age",
    "Customer preferences",
    "Purchase frequency",
    "Product sales",
    "Product availability",
    "Standardized product category",
    "Brand information"
]

for item in additional_data:
    print("•", item)

# ---------------------------------------------------------
# 10. LIMITATIONS
# ---------------------------------------------------------

print("\n" + "-" * 70)
print("CURRENT DATASET LIMITATIONS")
print("-" * 70)

limitations = [
    "Small number of usable records",
    "High amount of missing Eco-Score information",
    "Incomplete Nutri-Score information",
    "Missing brand information for some products",
    "Incomplete ingredient information",
    "Inconsistent category tags",
    "Dataset may not represent the complete beauty market"
]

for limitation in limitations:
    print("•", limitation)

# ---------------------------------------------------------
# 11. SAVE ANALYSIS PLAN
# ---------------------------------------------------------

os.makedirs("report", exist_ok=True)

output_file = "report/initial_analysis_plan.txt"

with open(output_file, "w", encoding="utf-8") as file:

    file.write("BEAUTY & WELLNESS\n")
    file.write("INITIAL ANALYSIS PLAN\n")
    file.write("=" * 60 + "\n\n")

    file.write("BUSINESS QUESTIONS\n")
    file.write("-" * 60 + "\n")

    for question in business_questions:
        file.write(question + "\n")

    file.write("\nVARIABLES FOR ANALYSIS\n")
    file.write("-" * 60 + "\n")

    for name, column in analysis_variables.items():
        file.write(f"{name}: {column}\n")

    file.write("\nPLANNED EDA\n")
    file.write("-" * 60 + "\n")

    for method in eda_methods:
        file.write("• " + method + "\n")

    file.write("\nDATA CLEANING PLAN\n")
    file.write("-" * 60 + "\n")

    for step in cleaning_steps:
        file.write("• " + step + "\n")

    file.write("\nFUTURE MACHINE LEARNING\n")
    file.write("-" * 60 + "\n")

    for task in ml_tasks:
        file.write("• " + task + "\n")

    file.write("\nDATASET LIMITATIONS\n")
    file.write("-" * 60 + "\n")

    for limitation in limitations:
        file.write("• " + limitation + "\n")

print("\nAnalysis plan saved to:")
print(output_file)

print("\n" + "=" * 70)
print("INITIAL ANALYSIS PLANNING COMPLETED")
print("=" * 70)
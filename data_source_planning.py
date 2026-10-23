import pandas as pd

# =========================================================
# DATA IDENTIFICATION, SOURCING STRATEGY & INITIAL ANALYSIS
# =========================================================

data_sources = [
    {
        "Source": "Open Beauty Facts",
        "Data_Type": "Cosmetic Products, Ingredients, Labels",
        "Accessibility": "High",
        "Update_Frequency": "Ongoing",
        "Reliability": "Medium-High",
        "Primary_Use": "Product and ingredient analysis"
    },
    {
        "Source": "Kaggle Cosmetics Dataset",
        "Data_Type": "Customer and Purchase Data",
        "Accessibility": "Medium",
        "Update_Frequency": "Static",
        "Reliability": "Medium",
        "Primary_Use": "Customer behavior analysis"
    },
    {
        "Source": "Sephora Products & Reviews",
        "Data_Type": "Products, Ratings and Reviews",
        "Accessibility": "Medium",
        "Update_Frequency": "Static",
        "Reliability": "Medium",
        "Primary_Use": "Review and sentiment analysis"
    },
    {
        "Source": "Data.gov Cosmetics",
        "Data_Type": "Cosmetic Chemicals and Safety Data",
        "Accessibility": "High",
        "Update_Frequency": "Periodic",
        "Reliability": "High",
        "Primary_Use": "Ingredient and safety analysis"
    }
]

df = pd.DataFrame(data_sources)

print("=" * 70)
print("DATA SOURCING STRATEGY")
print("=" * 70)

print(df.to_string(index=False))

print("\nTotal Potential Data Sources:", len(df))

print("\nRecommended Primary Source:")
print("Open Beauty Facts")
import base64
import io
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Beauty & Wellness Data Dashboard",
    page_icon="💄",
    layout="wide"
)

# =========================================================
# BACKGROUND IMAGE
# =========================================================

def set_background(image_file):

    try:
        with open(image_file, "rb") as file:
            encoded_image = base64.b64encode(
                file.read()
            ).decode()

        st.markdown(
            f"""
            <style>

            .stApp {{
                background-image:
                    linear-gradient(
                        rgba(0, 0, 0, 0.72),
                        rgba(0, 0, 0, 0.72)
                    ),
                    url("data:image/png;base64,{encoded_image}");

                background-size: cover;
                background-position: center;
                background-attachment: fixed;
            }}

            .main {{
                background: transparent !important;
            }}

            /* ==============================
               MAIN TEXT
            ============================== */

            .stApp p,
            .stApp label,
            .stApp span {{
                color: white;
            }}

            /* ==============================
               HEADINGS
            ============================== */

            h1, h2, h3, h4, h5, h6 {{
                color: white !important;
                font-weight: 600 !important;
                text-shadow: 1px 1px 6px rgba(0,0,0,0.8);
            }}

            h1 {{
                text-align: center;
                font-size: 42px !important;
                font-weight: 700 !important;
            }}

            .subtitle {{
                color: white !important;
                text-align: center;
                font-size: 18px;
                margin-bottom: 30px;
                text-shadow: 1px 1px 5px rgba(0,0,0,0.8);
            }}

            .section-title {{
                color: white !important;
                font-size: 25px;
                font-weight: 600;
                margin-top: 25px;
                margin-bottom: 15px;
                text-shadow: 1px 1px 5px rgba(0,0,0,0.8);
            }}

            /* ==============================
               SIDEBAR
            ============================== */

            section[data-testid="stSidebar"] {{
                background-color: rgba(0, 0, 0, 0.90);
            }}

            section[data-testid="stSidebar"] * {{
                color: white !important;
            }}

            /* ==============================
               SEARCH BOX
            ============================== */

            input {{
                color: black !important;
                background-color: white !important;
            }}

            /* ==============================
               MULTISELECT
            ============================== */

            div[data-baseweb="select"] {{
                background-color: white !important;
            }}

            div[data-baseweb="select"] * {{
                color: black !important;
            }}

            /* ==============================
               METRIC CARDS
            ============================== */

            div[data-testid="stMetric"] {{
                background-color: rgba(0, 0, 0, 0.70);
                padding: 18px;
                border-radius: 15px;
                border: 1px solid rgba(255,255,255,0.30);
                box-shadow: 0px 4px 15px rgba(0,0,0,0.40);
            }}

            [data-testid="stMetricLabel"] {{
                color: white !important;
                font-weight: 600 !important;
            }}

            [data-testid="stMetricValue"] {{
                color: white !important;
                font-size: 30px !important;
                font-weight: 700 !important;
            }}

            /* ==============================
               ALERT BOXES
            ============================== */

            div[data-testid="stAlert"] {{
                background-color: rgba(0, 0, 0, 0.78) !important;
                border-radius: 12px;
            }}

            div[data-testid="stAlert"] * {{
                color: white !important;
            }}

            /* ==============================
               INSIGHT BOX
            ============================== */

            .insight-box {{
                padding: 20px;
                border-radius: 15px;
                background-color: rgba(0, 0, 0, 0.80);
                border: 1px solid rgba(255,255,255,0.30);
                margin-top: 10px;
                color: white !important;
                box-shadow: 0px 4px 15px rgba(0,0,0,0.40);
                line-height: 1.6;
            }}

            .insight-box * {{
                color: white !important;
            }}

            /* ==============================
               DATAFRAME
            ============================== */

            div[data-testid="stDataFrame"] {{
                background-color: rgba(255,255,255,0.96);
                border-radius: 12px;
            }}

            /* ==============================
               HORIZONTAL LINE
            ============================== */

            hr {{
                border-color: rgba(255,255,255,0.35);
            }}

            </style>
            """,
            unsafe_allow_html=True
        )

    except FileNotFoundError:
        st.warning(
            "background.png was not found. "
            "The dashboard will continue without the background image."
        )


# Apply background
set_background("background.png")


# =========================================================
# CHART DISPLAY FUNCTION
# =========================================================

def display_transparent_chart(fig):

    buffer = io.BytesIO()

    fig.savefig(
        buffer,
        format="png",
        transparent=True,
        dpi=200,
        bbox_inches="tight"
    )

    buffer.seek(0)

    st.image(
        buffer,
        use_container_width=True
    )

    plt.close(fig)


# =========================================================
# LOAD DATA
# =========================================================

file_path = "Data/beauty_products_clean.csv"

try:

    df = pd.read_csv(file_path)

except FileNotFoundError:

    st.error(
        "Dataset not found. Please make sure "
        "Data/beauty_products_clean.csv exists."
    )

    st.stop()


# =========================================================
# HEADER
# =========================================================

st.title("💄 Beauty & Wellness Data Dashboard")

st.markdown(
    """
    <p class="subtitle">
    Data Identification, Quality Assessment & Initial Analysis
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown("---")


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("🔎 Dashboard Filters")

brands = sorted(
    df["brands"]
    .dropna()
    .unique()
    .tolist()
)

selected_brands = st.sidebar.multiselect(
    "Select Brand",
    brands
)

search = st.sidebar.text_input(
    "Search Product"
)

filtered_df = df.copy()

if selected_brands:

    filtered_df = filtered_df[
        filtered_df["brands"].isin(selected_brands)
    ]

if search:

    filtered_df = filtered_df[
        filtered_df["product_name"]
        .astype(str)
        .str.contains(
            search,
            case=False,
            na=False
        )
    ]


# =========================================================
# KPI SECTION
# =========================================================

st.markdown(
    '<div class="section-title">📊 Dataset Overview</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        "Products Analyzed",
        len(filtered_df)
    )


with col2:

    st.metric(
        "Brands Available",
        filtered_df["brands"].nunique()
    )


with col3:

    if len(filtered_df) > 0:

        ingredient_percentage = (
            filtered_df["ingredients_text"]
            .notna()
            .mean()
            * 100
        )

    else:

        ingredient_percentage = 0

    st.metric(
        "Ingredient Availability",
        f"{ingredient_percentage:.1f}%"
    )


with col4:

    eco_available = (
        filtered_df["ecoscore_tags"]
        .notna()
        .sum()
    )

    st.metric(
        "Eco-Score Available",
        eco_available
    )


st.markdown("---")


# =========================================================
# BRAND ANALYSIS
# =========================================================

st.markdown(
    '<div class="section-title">🏷️ Brand Analysis</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)


with col1:

    brand_counts = (
        filtered_df["brands"]
        .fillna("Unknown")
        .value_counts()
    )

    fig, ax = plt.subplots(figsize=(8, 5))

    brand_counts.plot(
        kind="bar",
        ax=ax
    )

    ax.set_title(
        "Product Distribution by Brand",
        color="white",
        fontsize=14,
        fontweight="bold"
    )

    ax.set_xlabel(
        "Brand",
        color="white"
    )

    ax.set_ylabel(
        "Number of Products",
        color="white"
    )

    ax.tick_params(
        axis="both",
        colors="white"
    )

    ax.set_facecolor("none")
    fig.patch.set_alpha(0)

    plt.xticks(
        rotation=45,
        ha="right"
    )

    plt.tight_layout()

    display_transparent_chart(fig)


with col2:

    st.markdown("### 📌 Brand Insights")

    known_brands = filtered_df["brands"].dropna()

    if len(known_brands) > 0:

        top_brand = (
            known_brands
            .value_counts()
            .idxmax()
        )

        top_brand_count = (
            known_brands
            .value_counts()
            .max()
        )

        st.info(
            f"**Most represented brand:** {top_brand}"
        )

        st.write(
            f"{top_brand} appears in "
            f"{top_brand_count} product record(s)."
        )

    st.write(
        "Brand information is incomplete for some "
        "products, so brand-level conclusions should "
        "be interpreted carefully."
    )


# =========================================================
# NUTRI-SCORE ANALYSIS
# =========================================================

st.markdown("---")

st.markdown(
    '<div class="section-title">🥗 Nutri-Score Analysis</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)


with col1:

    nutriscore_counts = (
        filtered_df["nutriscore_grade"]
        .fillna("Missing")
        .value_counts()
    )

    fig, ax = plt.subplots(figsize=(8, 5))

    nutriscore_counts.plot(
        kind="bar",
        ax=ax
    )

    ax.set_title(
        "Nutri-Score Availability",
        color="white",
        fontsize=14,
        fontweight="bold"
    )

    ax.set_xlabel(
        "Nutri-Score",
        color="white"
    )

    ax.set_ylabel(
        "Number of Products",
        color="white"
    )

    ax.tick_params(
        axis="both",
        colors="white"
    )

    ax.set_facecolor("none")
    fig.patch.set_alpha(0)

    plt.xticks(rotation=0)

    plt.tight_layout()

    display_transparent_chart(fig)


with col2:

    st.markdown("### 📌 Nutri-Score Insights")

    available = (
        filtered_df["nutriscore_grade"]
        .notna()
        .sum()
    )

    missing = (
        filtered_df["nutriscore_grade"]
        .isna()
        .sum()
    )

    st.write(
        f"Nutri-Score available: **{available}**"
    )

    st.write(
        f"Nutri-Score missing: **{missing}**"
    )

    st.warning(
        "Nutri-Score information is incomplete "
        "and contains unknown/not-applicable values."
    )


# =========================================================
# INGREDIENT ANALYSIS
# =========================================================

st.markdown("---")

st.markdown(
    '<div class="section-title">🧪 Ingredient Information</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)


with col1:

    ingredient_status = (
        filtered_df["ingredients_text"]
        .notna()
        .map({
            True: "Available",
            False: "Missing"
        })
    )

    ingredient_counts = (
        ingredient_status
        .value_counts()
    )

    fig, ax = plt.subplots(figsize=(7, 5))

    ingredient_counts.plot(
        kind="pie",
        autopct="%1.1f%%",
        startangle=90,
        ax=ax
    )

    ax.set_title(
        "Ingredient Information Availability",
        color="white",
        fontsize=14,
        fontweight="bold"
    )

    ax.set_ylabel("")

    ax.set_facecolor("none")
    fig.patch.set_alpha(0)

    plt.tight_layout()

    display_transparent_chart(fig)


with col2:

    st.markdown("### 📌 Ingredient Insights")

    ingredient_available = (
        filtered_df["ingredients_text"]
        .notna()
        .sum()
    )

    ingredient_missing = (
        filtered_df["ingredients_text"]
        .isna()
        .sum()
    )

    st.success(
        f"Ingredient information available for "
        f"**{ingredient_available}** product(s)."
    )

    st.write(
        f"Missing ingredient information: "
        f"**{ingredient_missing} product(s)**."
    )


# =========================================================
# CATEGORY ANALYSIS
# =========================================================

st.markdown("---")

st.markdown(
    '<div class="section-title">🏷️ Category Analysis</div>',
    unsafe_allow_html=True
)

category_counts = {}


for categories in filtered_df["categories_tags"].dropna():

    try:

        # Convert string representation of list
        # into actual list safely
        import ast

        categories = ast.literal_eval(categories)

        for category in categories:

            category = (
                str(category)
                .replace("en:", "")
                .lower()
                .strip()
            )

            if category not in [
                "beauty",
                "non-food-products",
                "open-beauty-facts"
            ]:

                category_counts[category] = (
                    category_counts.get(
                        category,
                        0
                    ) + 1
                )

    except (ValueError, SyntaxError, TypeError):

        continue


category_series = pd.Series(
    category_counts
).sort_values(
    ascending=False
)


if not category_series.empty:

    top_categories = (
        category_series
        .head(10)
    )

    fig, ax = plt.subplots(
        figsize=(10, 5)
    )

    top_categories.plot(
        kind="bar",
        ax=ax
    )

    ax.set_title(
        "Top Product Category Tags",
        color="white",
        fontsize=14,
        fontweight="bold"
    )

    ax.set_xlabel(
        "Category",
        color="white"
    )

    ax.set_ylabel(
        "Number of Products",
        color="white"
    )

    ax.tick_params(
        axis="both",
        colors="white"
    )

    ax.set_facecolor("none")
    fig.patch.set_alpha(0)

    plt.xticks(
        rotation=45,
        ha="right"
    )

    plt.tight_layout()

    display_transparent_chart(fig)

else:

    st.info(
        "No category information available."
    )


st.warning(
    "Category tags contain inconsistent and generic "
    "labels. Category normalization is recommended "
    "before advanced analysis."
)


# =========================================================
# DATA QUALITY DASHBOARD
# =========================================================

st.markdown("---")

st.markdown(
    '<div class="section-title">⚠️ Data Quality Assessment</div>',
    unsafe_allow_html=True
)


quality_data = pd.DataFrame({

    "Field": [
        "Product Name",
        "Brand",
        "Ingredients",
        "Nutri-Score",
        "Eco-Score"
    ],

    "Available": [
        filtered_df["product_name"].notna().sum(),
        filtered_df["brands"].notna().sum(),
        filtered_df["ingredients_text"].notna().sum(),
        filtered_df["nutriscore_grade"].notna().sum(),
        filtered_df["ecoscore_tags"].notna().sum()
    ],

    "Missing": [
        filtered_df["product_name"].isna().sum(),
        filtered_df["brands"].isna().sum(),
        filtered_df["ingredients_text"].isna().sum(),
        filtered_df["nutriscore_grade"].isna().sum(),
        filtered_df["ecoscore_tags"].isna().sum()
    ]
})


st.dataframe(
    quality_data,
    use_container_width=True,
    hide_index=True
)


# =========================================================
# PRODUCT DATA
# =========================================================

st.markdown("---")

st.markdown(
    '<div class="section-title">🧴 Product Dataset</div>',
    unsafe_allow_html=True
)


display_columns = [
    "product_name",
    "brands",
    "categories_tags",
    "nutriscore_grade"
]


st.dataframe(
    filtered_df[display_columns],
    use_container_width=True,
    hide_index=True
)


# =========================================================
# KEY INSIGHTS
# =========================================================

st.markdown("---")

st.markdown(
    '<div class="section-title">💡 Key Insights</div>',
    unsafe_allow_html=True
)


st.markdown(
    """
    <div class="insight-box">

    <b>1. Dataset Size</b><br>
    The current cleaned dataset contains 9 usable product records.

    <br><br>

    <b>2. Data Completeness</b><br>
    Ingredient information is available for 77.78% of the analyzed products.

    <br><br>

    <b>3. Brand Coverage</b><br>
    Brand information is available for 6 out of 9 products.

    <br><br>

    <b>4. Eco-Score Limitation</b><br>
    Eco-Score information is unavailable in the analyzed records.

    <br><br>

    <b>5. Category Quality</b><br>
    Category tags require standardization because several tags are generic or inconsistent.

    <br><br>

    <b>6. Future Scope</b><br>
    A larger standardized dataset can support recommendation systems,
    customer segmentation, sentiment analysis, and product classification.

    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.markdown(
    """
    <div style="
        text-align:center;
        color:white !important;
        font-size:15px;
        padding:15px;
    ">

    <b style="color:white !important;">
    Beauty & Wellness Data Science Project — Week 2
    </b>

    <br>

    <span style="color:white !important;">
    Data Identification • Data Sourcing • Quality Assessment • EDA
    </span>

    </div>
    """,
    unsafe_allow_html=True
)

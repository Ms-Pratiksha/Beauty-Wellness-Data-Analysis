# 💄 Beauty & Wellness Data Analysis

## 📌 Project Overview

**Beauty & Wellness Data Analysis** is a data science project focused on collecting, cleaning, assessing, and exploring beauty and wellness product data.

The project uses data collected from the **Open Beauty Facts API** and performs initial data quality assessment and Exploratory Data Analysis (EDA) using Python.

A Streamlit dashboard is developed to present the analyzed data, data-quality findings, product information, and visual insights in an interactive and professional format.

---

## 🎯 Objectives

- Collect beauty and wellness product data from a public API.
- Identify relevant product attributes and variables.
- Assess the quality and completeness of the collected data.
- Handle missing and duplicate records.
- Analyze product brands and category tags.
- Examine ingredient information availability.
- Analyze Nutri-Score and Eco-Score availability.
- Perform initial Exploratory Data Analysis.
- Build an interactive Streamlit dashboard.
- Identify limitations and future analysis opportunities.

---

## 🛠️ Technologies Used

- **Python**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **Streamlit**
- **Requests**
- **Open Beauty Facts API**
- **VS Code**
- **Git & GitHub**

---

## 📂 Project Structure

```text
Beauty-Wellness-Data-Analysis/
│
├── analysis/
│   ├── data_collection.py
│   ├── data_quality.py
│   ├── eda_analysis.py
│   ├── findings.py
│   └── analysis_plan.py
│
├── Data/
│   ├── beauty_products_raw.csv
│   ├── beauty_wellness_sample.csv
│   ├── beauty_products_clean.csv
│   └── EDA_Charts/
│
├── report/
│   ├── data_findings.txt
│   └── initial_analysis_plan.txt
│
├── app.py
├── background.png
└── README.md
```

---

## 🔄 Project Workflow

```text
Public Data Source
       ↓
Open Beauty Facts API
       ↓
Data Collection
       ↓
Raw Dataset
       ↓
Data Quality Assessment
       ↓
Data Cleaning
       ↓
Clean Dataset
       ↓
Exploratory Data Analysis
       ↓
Findings & Insights
       ↓
Interactive Streamlit Dashboard
```

---

## 📊 Data Collection

Beauty and wellness product information is collected using the **Open Beauty Facts API**.

The collected raw dataset contains fields such as:

- Brand
- Product Name
- Product Code
- Categories
- Ingredients
- Nutri-Score
- Eco-Score

The collected raw dataset initially contained **17 product records**.

---

## 🧹 Data Quality Assessment

The collected dataset was analyzed for:

- Missing values
- Duplicate records
- Product-name availability
- Brand information
- Ingredient information
- Nutri-Score availability
- Eco-Score availability
- Category consistency

After removing records with missing product names, **9 usable product records** remained.

No duplicate records were identified in the raw dataset.

---

## 🔍 Exploratory Data Analysis

The EDA phase analyzes:

### 🏷️ Brand Distribution

Brand information was available for 6 out of the 9 analyzed products.

The dashboard displays the distribution of products across available brands.

### 🧪 Ingredient Information

Ingredient information was available for **7 out of 9 products**, giving an availability rate of approximately **77.78%**.

### 🥗 Nutri-Score

Nutri-Score information was incomplete and included missing, unknown, and not-applicable values.

### 🌱 Eco-Score

Eco-Score information was unavailable for the analyzed clean records.

### 🏷️ Category Tags

The dataset contains several inconsistent and generic category tags.

Category normalization is therefore recommended before performing advanced analysis.

---

## 📈 Streamlit Dashboard

The project includes an interactive dashboard developed using **Streamlit**.

The dashboard provides:

- 📊 Dataset overview
- 🏷️ Brand analysis
- 🥗 Nutri-Score analysis
- 🧪 Ingredient information analysis
- 🏷️ Category analysis
- ⚠️ Data quality assessment
- 🧴 Product dataset view
- 💡 Key project insights
- 🔎 Brand filtering
- 🔍 Product search

The dashboard also uses a professional beauty and wellness themed background.

---

## ▶️ How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Beauty-Wellness-Data-Analysis.git
```

### 2. Open the Project

```bash
cd Beauty-Wellness-Data-Analysis
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

For Windows:

```bash
venv\Scripts\activate
```

### 5. Install Required Libraries

```bash
python -m pip install pandas numpy matplotlib streamlit requests
```

### 6. Run the Streamlit Dashboard

```bash
python -m streamlit run app.py
```

The dashboard will open in your browser.

---

## 💡 Key Insights

The initial analysis identified the following:

1. The raw API dataset contained 17 product records.
2. 9 usable products remained after removing products without names.
3. No duplicate records were identified.
4. Brand information was incomplete for some products.
5. Ingredient information was available for most analyzed products.
6. Nutri-Score information was incomplete.
7. Eco-Score information was unavailable.
8. Category tags contained inconsistent and generic labels.
9. The dataset is suitable for demonstrating data collection, cleaning, quality assessment, and initial EDA.
10. A larger and more standardized dataset would be required for reliable market-level analysis and machine learning.

---

## 🚀 Future Scope

The project can be extended with:

- Product price analysis
- Product rating analysis
- Customer preference analysis
- Customer segmentation
- Product recommendation systems
- Review sentiment analysis
- Product category classification
- Product popularity prediction
- Sales and market trend analysis
- Larger beauty and wellness datasets

---

## ⚠️ Current Limitations

- Small number of usable records
- High missing Eco-Score information
- Incomplete Nutri-Score information
- Missing brand information for some products
- Incomplete ingredient information
- Inconsistent category tags
- Current dataset may not represent the complete beauty and wellness market

---

## 📚 Learning Outcomes

Through this project, I gained practical experience in:

- API-based data collection
- Data sourcing
- Data cleaning
- Missing-value analysis
- Duplicate detection
- Data quality assessment
- Exploratory Data Analysis
- Data visualization
- Python data analysis
- Streamlit dashboard development
- Project documentation
- Git and GitHub workflow

---

## 👩‍💻 Author

**Pratiksha Bhatage**

B.E. Artificial Intelligence and Data Science

---

## 📌 Project Status

**Week 2 Project — Completed ✅**

**Focus:** Data Identification, Data Sourcing Strategy, Data Quality Assessment & Initial Analysis Planning

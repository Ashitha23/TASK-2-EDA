# TASK-2-EDA
# 🚀 60 Days Data Analytics Internship
### ApexPlanet Software Pvt. Ltd.

![Python](https://img.shields.io/badge/Python-3.14-blue)
![Pandas](https://img.shields.io/badge/Pandas-2.0-green)
![Status](https://img.shields.io/badge/Status-In%20Progress-orange)

---

## 👩‍💻 About Me
- **Name:** Ashitha
- **Internship:** Data Analytics — ApexPlanet Software Pvt. Ltd.
- **Duration:** 60 Days
- **Goal:** Master data analytics from wrangling to machine learning

---

## 📌 Task 1 — Data Immersion & Wrangling
**Timeline: 10 Days**

### Dataset Used
- Superstore Sales Dataset (9,800 rows, 18 columns)

### What I Did
- Explored dataset — shape, dtypes, missing values
- Performed Data Quality Assessment
- Detected 1,145 Sales outliers using IQR method
- Fixed date columns (string to datetime)
- Handled 11 missing Postal Code values
- Feature engineered 3 new columns:
  - Order Year
  - Order Month
  - Shipping Days
- Created a Data Dictionary for all 18 columns
- Saved final analysis-ready cleaned dataset (21 columns)

### Key Findings
- Zero duplicate rows — very clean dataset
- Sales mean ($230) vs median ($54) — bulk orders skew average
- Orders span 4 years: 2015 to 2018
- 4 Regions: West, East, Central, South
- 3 Categories: Furniture, Office Supplies, Technology

### Files
| File | Description |
|---|---|
| `firstcode.py` | Initial data exploration |
| `dataquality.py` | Data quality assessment |
| `datacleaning.py` | Data cleaning & transformation |
| `comparis.py` | Before vs After comparison |
| `data_dictionary.csv` | Column definitions & metadata |
| `superstore_cleaned.csv` | Final cleaned dataset |

---

## 📌 Task 2 — Exploratory Data Analysis & Business Intelligence
**Timeline: 14 Days**

### Dataset Used
- Superstore Cleaned Dataset (9,800 rows, 21 columns)

### What I Did
- Descriptive statistics for all numerical & categorical columns
- Univariate analysis — histograms, bar charts, pie charts
- Answered 8 SQL business questions using SQLite & Python
- Multivariate analysis — heatmaps, scatter plots, pair plots
- Built a complete static KPI Dashboard

### Business Questions Answered (SQL)
| # | Question | Key Finding |
|---|---|---|
| Q1 | Top 5 products by sales? | Canon Copier leads at $61,599 |
| Q2 | Sales by region? | West leads with $710,219 |
| Q3 | Revenue by category? | Technology tops at $827,455 |
| Q4 | Monthly sales trends? | Sep, Nov, Dec are peak months |
| Q5 | Sales by segment? | Consumer leads at $1.14M |
| Q6 | Top 5 states? | California dominates at $446,306 |
| Q7 | Ship mode by segment? | All segments prefer Standard Class |
| Q8 | Avg shipping days? | Same Day = 0.04 days, Standard = 5 days |

### Key Insights
- Technology generates highest revenue despite fewer orders
- California alone accounts for ~20% of total sales
- November is consistently the peak sales month every year
- Office Supplies has most orders but lowest average sale value
- Sales grew every year — 2018 was the best year overall
- Home Office segment has highest average order value ($243)

### Files
| File | Description |
|---|---|
| `eda_step1.py` | Descriptive statistics & univariate analysis |
| `eda_step2_sql.py` | SQL business questions |
| `eda_step3_multivariate.py` | Multivariate analysis & correlation |
| `eda_step4_dashboard.py` | KPI Dashboard |
| `sql_results.xlsx` | All SQL query results |
| `eda_numerical.png` | Numerical distributions |
| `eda_categorical.png` | Categorical distributions |
| `eda_top10.png` | Top 10 analysis |
| `step3_heatmap.png` | Correlation heatmap |
| `step3_scatter.png` | Scatter plots |
| `step3_region_category.png` | Region vs Category |
| `step3_yearly_trend.png` | Yearly sales trend |
| `step3_monthly_heatmap.png` | Monthly sales heatmap |
| `step3_boxplots.png` | Sales distribution boxplots |
| `step3_pairplot.png` | Pair plot |
| `superstore_dashboard.png` | Final KPI Dashboard |

---

## 🛠️ Tools & Technologies
| Tool | Purpose |
|---|---|
| Python 3.14 | Core programming language |
| Pandas | Data manipulation & cleaning |
| Matplotlib | Data visualization |
| Seaborn | Advanced visualizations |
| SQLite3 | SQL queries on dataset |
| VS Code | Code editor |

---

## 📈 Progress Tracker
| Task | Status | Timeline |
|---|---|---|
| Task 1 — Data Immersion & Wrangling | ✅ Complete | 10 Days |
| Task 2 — EDA & Business Intelligence | ✅ Complete | 14 Days |
| Task 3 — In Progress | 🔄 Ongoing | — |

---

## 🔗 Connect with Me
- **GitHub:** [Ashitha23](https://github.com/Ashitha23)
- **LinkedIn:** [Your LinkedIn URL here]

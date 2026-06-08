import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("superstore_cleaned.csv")

sns.set_style("whitegrid")

# ============================================================
# 1. DESCRIPTIVE STATISTICS
# ============================================================

print("=" * 60)
print("DESCRIPTIVE STATISTICS")
print("=" * 60)

# Numerical columns summary
print("\n📊 Numerical Columns Summary:")
print(df.describe())

# Categorical columns summary
print("\n📋 Categorical Columns Summary:")
cat_cols = ['Ship Mode', 'Segment', 'Region', 'Category', 'Sub-Category']
for col in cat_cols:
    print(f"\n🔹 {col} — {df[col].nunique()} unique values:")
    print(df[col].value_counts())

# ============================================================
# 2. UNIVARIATE ANALYSIS — NUMERICAL
# ============================================================

fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('Numerical Columns Distribution', fontsize=16, fontweight='bold')

# 2a. Sales Distribution
axes[0, 0].hist(df['Sales'], bins=50, color='#3498db', edgecolor='white')
axes[0, 0].set_title('Sales Distribution')
axes[0, 0].set_xlabel('Sales ($)')
axes[0, 0].set_ylabel('Count')
axes[0, 0].axvline(df['Sales'].mean(), color='red', linestyle='--', label=f'Mean: ${df["Sales"].mean():.0f}')
axes[0, 0].axvline(df['Sales'].median(), color='green', linestyle='--', label=f'Median: ${df["Sales"].median():.0f}')
axes[0, 0].legend()

# 2b. Sales without outliers (better view)
sales_filtered = df[df['Sales'] < df['Sales'].quantile(0.95)]
axes[0, 1].hist(sales_filtered['Sales'], bins=50, color='#2ecc71', edgecolor='white')
axes[0, 1].set_title('Sales Distribution (95th percentile)')
axes[0, 1].set_xlabel('Sales ($)')
axes[0, 1].set_ylabel('Count')

# 2c. Shipping Days Distribution
axes[1, 0].hist(df['Shipping Days'], bins=20, color='#9b59b6', edgecolor='white')
axes[1, 0].set_title('Shipping Days Distribution')
axes[1, 0].set_xlabel('Days')
axes[1, 0].set_ylabel('Count')
axes[1, 0].axvline(df['Shipping Days'].mean(), color='red', linestyle='--', label=f'Mean: {df["Shipping Days"].mean():.1f} days')
axes[1, 0].legend()

# 2d. Order Year Distribution
year_counts = df['Order Year'].value_counts().sort_index()
axes[1, 1].bar(year_counts.index.astype(str), year_counts.values, color='#e67e22', edgecolor='white')
axes[1, 1].set_title('Orders by Year')
axes[1, 1].set_xlabel('Year')
axes[1, 1].set_ylabel('Number of Orders')
for i, v in enumerate(year_counts.values):
    axes[1, 1].text(i, v + 10, str(v), ha='center', fontweight='bold')

plt.tight_layout()
plt.savefig('eda_numerical.png', dpi=150, bbox_inches='tight')
plt.show()
print("✅ Numerical charts saved!")

# ============================================================
# 3. UNIVARIATE ANALYSIS — CATEGORICAL
# ============================================================

fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('Categorical Columns Distribution', fontsize=16, fontweight='bold')

# 3a. Sales by Category
cat_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
axes[0, 0].bar(cat_sales.index, cat_sales.values, color=['#3498db', '#2ecc71', '#e74c3c'])
axes[0, 0].set_title('Total Sales by Category')
axes[0, 0].set_ylabel('Total Sales ($)')
for i, v in enumerate(cat_sales.values):
    axes[0, 0].text(i, v + 1000, f'${v:,.0f}', ha='center', fontweight='bold')

# 3b. Orders by Region
region_counts = df['Region'].value_counts()
colors = ['#f1c40f', '#3498db', '#e67e22', '#2ecc71']
axes[0, 1].bar(region_counts.index, region_counts.values, color=colors)
axes[0, 1].set_title('Number of Orders by Region')
axes[0, 1].set_ylabel('Number of Orders')
for i, v in enumerate(region_counts.values):
    axes[0, 1].text(i, v + 10, str(v), ha='center', fontweight='bold')

# 3c. Orders by Segment
segment_counts = df['Segment'].value_counts()
axes[1, 0].pie(segment_counts.values, labels=segment_counts.index,
               autopct='%1.1f%%', colors=['#3498db', '#2ecc71', '#e74c3c'],
               startangle=90)
axes[1, 0].set_title('Orders by Customer Segment')

# 3d. Orders by Ship Mode
ship_counts = df['Ship Mode'].value_counts()
axes[1, 1].barh(ship_counts.index, ship_counts.values, color='#1abc9c')
axes[1, 1].set_title('Orders by Ship Mode')
axes[1, 1].set_xlabel('Number of Orders')
for i, v in enumerate(ship_counts.values):
    axes[1, 1].text(v + 5, i, str(v), va='center', fontweight='bold')

plt.tight_layout()
plt.savefig('eda_categorical.png', dpi=150, bbox_inches='tight')
plt.show()
print("✅ Categorical charts saved!")

# ============================================================
# 4. TOP 10 ANALYSIS
# ============================================================

fig, axes = plt.subplots(1, 2, figsize=(18, 7))
fig.suptitle('Top 10 Analysis', fontsize=16, fontweight='bold')

# 4a. Top 10 Sub-Categories by Sales
subcat_sales = df.groupby('Sub-Category')['Sales'].sum().sort_values(ascending=False).head(10)
axes[0].barh(subcat_sales.index[::-1], subcat_sales.values[::-1], color='#3498db')
axes[0].set_title('Top 10 Sub-Categories by Sales')
axes[0].set_xlabel('Total Sales ($)')
for i, v in enumerate(subcat_sales.values[::-1]):
    axes[0].text(v + 100, i, f'${v:,.0f}', va='center', fontweight='bold', fontsize=9)

# 4b. Top 10 States by Sales
state_sales = df.groupby('State')['Sales'].sum().sort_values(ascending=False).head(10)
axes[1].barh(state_sales.index[::-1], state_sales.values[::-1], color='#e67e22')
axes[1].set_title('Top 10 States by Sales')
axes[1].set_xlabel('Total Sales ($)')
for i, v in enumerate(state_sales.values[::-1]):
    axes[1].text(v + 100, i, f'${v:,.0f}', va='center', fontweight='bold', fontsize=9)

plt.tight_layout()
plt.savefig('eda_top10.png', dpi=150, bbox_inches='tight')
plt.show()
print("✅ Top 10 charts saved!")

print("\n🎉 Step 1 Complete! Files saved:")
print("   → eda_numerical.png")
print("   → eda_categorical.png")
print("   → eda_top10.png")
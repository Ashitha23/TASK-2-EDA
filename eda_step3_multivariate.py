import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv("superstore_cleaned.csv")

sns.set_style("whitegrid")

# ============================================================
# 1. CORRELATION HEATMAP
# ============================================================

fig, ax = plt.subplots(figsize=(10, 8))
numeric_cols = df[['Sales', 'Order Year', 'Order Month', 'Shipping Days']]
correlation = numeric_cols.corr()

sns.heatmap(correlation, annot=True, fmt='.2f', cmap='coolwarm',
            linewidths=0.5, ax=ax, vmin=-1, vmax=1,
            annot_kws={'size': 14, 'weight': 'bold'})
ax.set_title('Correlation Heatmap — Numerical Variables', fontsize=16, fontweight='bold')

plt.tight_layout()
plt.savefig('step3_heatmap.png', dpi=150, bbox_inches='tight')
plt.show()
print("✅ Heatmap saved!")

# ============================================================
# 2. SCATTER PLOTS
# ============================================================

fig, axes = plt.subplots(1, 2, figsize=(16, 6))
fig.suptitle('Scatter Plot Analysis', fontsize=16, fontweight='bold')

# 2a. Sales vs Shipping Days
colors = {'Furniture': '#e74c3c', 'Office Supplies': '#3498db', 'Technology': '#2ecc71'}
for category, color in colors.items():
    subset = df[df['Category'] == category]
    axes[0].scatter(subset['Shipping Days'], subset['Sales'],
                   alpha=0.4, color=color, label=category, s=20)
axes[0].set_title('Sales vs Shipping Days by Category')
axes[0].set_xlabel('Shipping Days')
axes[0].set_ylabel('Sales ($)')
axes[0].legend()

# 2b. Sales vs Order Month
for category, color in colors.items():
    subset = df[df['Category'] == category]
    axes[1].scatter(subset['Order Month'], subset['Sales'],
                   alpha=0.4, color=color, label=category, s=20)
axes[1].set_title('Sales vs Order Month by Category')
axes[1].set_xlabel('Order Month')
axes[1].set_ylabel('Sales ($)')
axes[1].legend()

plt.tight_layout()
plt.savefig('step3_scatter.png', dpi=150, bbox_inches='tight')
plt.show()
print("✅ Scatter plots saved!")

# ============================================================
# 3. SALES BY CATEGORY & REGION (Grouped Bar)
# ============================================================

fig, ax = plt.subplots(figsize=(12, 6))
pivot = df.groupby(['Region', 'Category'])['Sales'].sum().unstack()
pivot.plot(kind='bar', ax=ax, color=['#e74c3c', '#3498db', '#2ecc71'],
           edgecolor='white', width=0.7)
ax.set_title('Sales by Region and Category', fontsize=16, fontweight='bold')
ax.set_xlabel('Region')
ax.set_ylabel('Total Sales ($)')
ax.legend(title='Category')
ax.tick_params(axis='x', rotation=0)
for container in ax.containers:
    ax.bar_label(container, fmt='$%.0f', fontsize=7, padding=2)

plt.tight_layout()
plt.savefig('step3_region_category.png', dpi=150, bbox_inches='tight')
plt.show()
print("✅ Region vs Category chart saved!")

# ============================================================
# 4. SALES TREND BY YEAR & CATEGORY (Line Plot)
# ============================================================

fig, ax = plt.subplots(figsize=(12, 6))
yearly_cat = df.groupby(['Order Year', 'Category'])['Sales'].sum().unstack()
yearly_cat.plot(kind='line', ax=ax, marker='o', linewidth=2,
                color=['#e74c3c', '#3498db', '#2ecc71'])
ax.set_title('Sales Trend by Year & Category', fontsize=16, fontweight='bold')
ax.set_xlabel('Year')
ax.set_ylabel('Total Sales ($)')
ax.legend(title='Category')
ax.set_xticks([2015, 2016, 2017, 2018])

plt.tight_layout()
plt.savefig('step3_yearly_trend.png', dpi=150, bbox_inches='tight')
plt.show()
print("✅ Yearly trend chart saved!")

# ============================================================
# 5. HEATMAP — SALES BY MONTH & YEAR
# ============================================================

fig, ax = plt.subplots(figsize=(14, 5))
monthly_pivot = df.groupby(['Order Year', 'Order Month'])['Sales'].sum().unstack()
monthly_pivot.index = ['2015', '2016', '2017', '2018']
monthly_pivot.columns = ['Jan', 'Feb', 'Mar', 'Apr', 'May',
                          'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

sns.heatmap(monthly_pivot, annot=True, fmt='.0f', cmap='YlOrRd',
            linewidths=0.5, ax=ax, annot_kws={'size': 8})
ax.set_title('Sales Heatmap — Month vs Year', fontsize=16, fontweight='bold')
ax.set_xlabel('Month')
ax.set_ylabel('Year')

plt.tight_layout()
plt.savefig('step3_monthly_heatmap.png', dpi=150, bbox_inches='tight')
plt.show()
print("✅ Monthly heatmap saved!")

# ============================================================
# 6. BOXPLOT — SALES BY CATEGORY & SEGMENT
# ============================================================

fig, axes = plt.subplots(1, 2, figsize=(16, 6))
fig.suptitle('Sales Distribution Analysis', fontsize=16, fontweight='bold')

# 6a. Sales by Category (without outliers for clarity)
sns.boxplot(x='Category', y='Sales', data=df,
            palette=['#e74c3c', '#3498db', '#2ecc71'],
            ax=axes[0], showfliers=False)
axes[0].set_title('Sales by Category (outliers hidden)')
axes[0].set_xlabel('Category')
axes[0].set_ylabel('Sales ($)')

# 6b. Sales by Segment
sns.boxplot(x='Segment', y='Sales', data=df,
            palette=['#f1c40f', '#9b59b6', '#1abc9c'],
            ax=axes[1], showfliers=False)
axes[1].set_title('Sales by Segment (outliers hidden)')
axes[1].set_xlabel('Segment')
axes[1].set_ylabel('Sales ($)')

plt.tight_layout()
plt.savefig('step3_boxplots.png', dpi=150, bbox_inches='tight')
plt.show()
print("✅ Boxplots saved!")

# ============================================================
# 7. PAIR PLOT
# ============================================================

pair_df = df[['Sales', 'Order Month', 'Shipping Days', 'Order Year']].sample(500)
pair_plot = sns.pairplot(pair_df, diag_kind='kde',
                          plot_kws={'alpha': 0.4, 'color': '#3498db'},
                          diag_kws={'color': '#e74c3c'})
pair_plot.fig.suptitle('Pair Plot — Numerical Variables', y=1.02,
                        fontsize=16, fontweight='bold')

plt.savefig('step3_pairplot.png', dpi=150, bbox_inches='tight')
plt.show()
print("✅ Pair plot saved!")

print("\n🎉 Step 3 Complete! Files saved:")
print("   → step3_heatmap.png")
print("   → step3_scatter.png")
print("   → step3_region_category.png")
print("   → step3_yearly_trend.png")
print("   → step3_monthly_heatmap.png")
print("   → step3_boxplots.png")
print("   → step3_pairplot.png")
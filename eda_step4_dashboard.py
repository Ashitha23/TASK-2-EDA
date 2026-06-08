import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns
import numpy as np

df = pd.read_csv("superstore_cleaned.csv")

# ============================================================
# SUPERSTORE KPI DASHBOARD
# ============================================================

fig = plt.figure(figsize=(24, 16))
fig.patch.set_facecolor('#1a1a2e')

gs = gridspec.GridSpec(4, 4, figure=fig, hspace=0.45, wspace=0.35)

# Color palette
BLUE = '#3498db'
GREEN = '#2ecc71'
RED = '#e74c3c'
ORANGE = '#e67e22'
PURPLE = '#9b59b6'
YELLOW = '#f1c40f'
BG = '#16213e'
CARD = '#0f3460'
WHITE = '#ffffff'
GRAY = '#a0a0b0'

def style_ax(ax, title):
    ax.set_facecolor(BG)
    ax.tick_params(colors=WHITE, labelsize=8)
    ax.set_title(title, color=WHITE, fontsize=10, fontweight='bold', pad=8)
    for spine in ax.spines.values():
        spine.set_edgecolor(GRAY)

# ============================================================
# ROW 1 — KPI CARDS (4 cards)
# ============================================================

kpis = [
    ('Total Sales', f"${df['Sales'].sum():,.0f}", BLUE),
    ('Total Orders', f"{len(df):,}", GREEN),
    ('Avg Order Value', f"${df['Sales'].mean():,.0f}", ORANGE),
    ('Avg Shipping Days', f"{df['Shipping Days'].mean():.1f} days", PURPLE),
]

for i, (label, value, color) in enumerate(kpis):
    ax = fig.add_subplot(gs[0, i])
    ax.set_facecolor(CARD)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    ax.add_patch(plt.Rectangle((0, 0), 1, 1, color=CARD, zorder=0))
    ax.add_patch(plt.Rectangle((0, 0), 0.06, 1, color=color, zorder=1))
    ax.text(0.5, 0.65, value, ha='center', va='center',
            fontsize=22, fontweight='bold', color=color, transform=ax.transAxes)
    ax.text(0.5, 0.25, label, ha='center', va='center',
            fontsize=11, color=GRAY, transform=ax.transAxes)

# ============================================================
# ROW 2 — Sales by Category | Sales by Region | Monthly Trend
# ============================================================

# 2a. Sales by Category (spans 1 col)
ax1 = fig.add_subplot(gs[1, 0])
style_ax(ax1, '💰 Sales by Category')
cat_sales = df.groupby('Category')['Sales'].sum().sort_values()
bars = ax1.barh(cat_sales.index, cat_sales.values,
                color=[RED, BLUE, GREEN], edgecolor='none', height=0.5)
for bar, val in zip(bars, cat_sales.values):
    ax1.text(val + 5000, bar.get_y() + bar.get_height()/2,
             f'${val:,.0f}', va='center', color=WHITE, fontsize=8, fontweight='bold')
ax1.set_xlabel('Sales ($)', color=GRAY, fontsize=8)
ax1.tick_params(colors=WHITE)

# 2b. Sales by Region (spans 1 col)
ax2 = fig.add_subplot(gs[1, 1])
style_ax(ax2, '🌍 Sales by Region')
region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
colors_region = [BLUE, GREEN, ORANGE, RED]
bars2 = ax2.bar(region_sales.index, region_sales.values,
                color=colors_region, edgecolor='none', width=0.5)
for bar, val in zip(bars2, region_sales.values):
    ax2.text(bar.get_x() + bar.get_width()/2, val + 5000,
             f'${val/1000:.0f}K', ha='center', color=WHITE, fontsize=8, fontweight='bold')
ax2.set_ylabel('Sales ($)', color=GRAY, fontsize=8)
ax2.tick_params(colors=WHITE)

# 2c. Monthly Sales Trend (spans 2 cols)
ax3 = fig.add_subplot(gs[1, 2:])
style_ax(ax3, '📈 Monthly Sales Trend (2015-2018)')
monthly = df.groupby(['Order Year', 'Order Month'])['Sales'].sum().reset_index()
monthly['Period'] = monthly['Order Year'].astype(str) + '-' + monthly['Order Month'].astype(str).str.zfill(2)
ax3.plot(range(len(monthly)), monthly['Sales'], color=BLUE, linewidth=2)
ax3.fill_between(range(len(monthly)), monthly['Sales'], alpha=0.2, color=BLUE)
# Mark peaks
peak_idx = monthly['Sales'].idxmax()
ax3.scatter(peak_idx, monthly['Sales'].iloc[peak_idx], color=YELLOW, s=100, zorder=5)
ax3.text(peak_idx, monthly['Sales'].iloc[peak_idx] + 3000,
         f"Peak\n${monthly['Sales'].iloc[peak_idx]:,.0f}",
         ha='center', color=YELLOW, fontsize=8, fontweight='bold')
ax3.set_xticks(range(0, len(monthly), 6))
ax3.set_xticklabels(monthly['Period'].iloc[::6], rotation=45, fontsize=7, color=WHITE)
ax3.set_ylabel('Sales ($)', color=GRAY, fontsize=8)

# ============================================================
# ROW 3 — Segment Pie | Top 10 Sub-Categories | Ship Mode
# ============================================================

# 3a. Segment Pie
ax4 = fig.add_subplot(gs[2, 0])
style_ax(ax4, '👥 Orders by Segment')
seg = df['Segment'].value_counts()
wedges, texts, autotexts = ax4.pie(
    seg.values, labels=seg.index, autopct='%1.1f%%',
    colors=[BLUE, GREEN, ORANGE], startangle=90,
    textprops={'color': WHITE, 'fontsize': 8},
    wedgeprops={'edgecolor': BG, 'linewidth': 2}
)
for at in autotexts:
    at.set_color(WHITE)
    at.set_fontsize(8)

# 3b. Top 10 Sub-Categories
ax5 = fig.add_subplot(gs[2, 1:3])
style_ax(ax5, '🏆 Top 10 Sub-Categories by Sales')
subcat = df.groupby('Sub-Category')['Sales'].sum().sort_values(ascending=False).head(10)
colors_grad = [BLUE if i < 3 else GRAY for i in range(len(subcat))]
bars5 = ax5.barh(subcat.index[::-1], subcat.values[::-1],
                 color=colors_grad[::-1], edgecolor='none', height=0.6)
for bar, val in zip(bars5, subcat.values[::-1]):
    ax5.text(val + 1000, bar.get_y() + bar.get_height()/2,
             f'${val:,.0f}', va='center', color=WHITE, fontsize=7, fontweight='bold')
ax5.set_xlabel('Total Sales ($)', color=GRAY, fontsize=8)

# 3c. Ship Mode
ax6 = fig.add_subplot(gs[2, 3])
style_ax(ax6, '🚚 Ship Mode Usage')
ship = df['Ship Mode'].value_counts()
colors_ship = [BLUE, GREEN, ORANGE, RED]
bars6 = ax6.bar(range(len(ship)), ship.values,
                color=colors_ship, edgecolor='none', width=0.5)
ax6.set_xticks(range(len(ship)))
ax6.set_xticklabels([s.replace(' ', '\n') for s in ship.index],
                     color=WHITE, fontsize=7)
for bar, val in zip(bars6, ship.values):
    ax6.text(bar.get_x() + bar.get_width()/2, val + 20,
             str(val), ha='center', color=WHITE, fontsize=8, fontweight='bold')
ax6.set_ylabel('Orders', color=GRAY, fontsize=8)

# ============================================================
# ROW 4 — Top 5 States | Year Growth | Category Trend
# ============================================================

# 4a. Top 5 States
ax7 = fig.add_subplot(gs[3, 0])
style_ax(ax7, '📍 Top 5 States by Sales')
states = df.groupby('State')['Sales'].sum().sort_values(ascending=False).head(5)
bars7 = ax7.barh(states.index[::-1], states.values[::-1],
                 color=PURPLE, edgecolor='none', height=0.5)
for bar, val in zip(bars7, states.values[::-1]):
    ax7.text(val + 2000, bar.get_y() + bar.get_height()/2,
             f'${val/1000:.0f}K', va='center', color=WHITE, fontsize=8, fontweight='bold')
ax7.set_xlabel('Sales ($)', color=GRAY, fontsize=8)

# 4b. Year over Year Growth
ax8 = fig.add_subplot(gs[3, 1])
style_ax(ax8, '📅 Year over Year Sales')
yearly = df.groupby('Order Year')['Sales'].sum()
bars8 = ax8.bar(yearly.index.astype(str), yearly.values,
                color=[BLUE, GREEN, ORANGE, RED], edgecolor='none', width=0.5)
for bar, val in zip(bars8, yearly.values):
    ax8.text(bar.get_x() + bar.get_width()/2, val + 3000,
             f'${val/1000:.0f}K', ha='center', color=WHITE, fontsize=8, fontweight='bold')
ax8.set_ylabel('Sales ($)', color=GRAY, fontsize=8)

# 4c. Category trend line
ax9 = fig.add_subplot(gs[3, 2:])
style_ax(ax9, '📊 Category Sales Growth by Year')
cat_year = df.groupby(['Order Year', 'Category'])['Sales'].sum().unstack()
colors_cat = [RED, BLUE, GREEN]
for i, col in enumerate(cat_year.columns):
    ax9.plot(cat_year.index, cat_year[col], marker='o',
             linewidth=2.5, color=colors_cat[i], label=col)
    ax9.fill_between(cat_year.index, cat_year[col], alpha=0.1, color=colors_cat[i])
ax9.set_xticks([2015, 2016, 2017, 2018])
ax9.set_xticklabels(['2015', '2016', '2017', '2018'], color=WHITE)
ax9.set_ylabel('Sales ($)', color=GRAY, fontsize=8)
ax9.legend(facecolor=BG, labelcolor=WHITE, fontsize=8)

# ============================================================
# TITLE
# ============================================================
fig.text(0.5, 0.98, '🏪 SUPERSTORE SALES DASHBOARD',
         ha='center', va='top', fontsize=22,
         fontweight='bold', color=WHITE)
fig.text(0.5, 0.955, 'Key Performance Indicators | 2015 - 2018',
         ha='center', va='top', fontsize=12, color=GRAY)

plt.savefig('superstore_dashboard.png', dpi=150, bbox_inches='tight',
            facecolor=fig.get_facecolor())
plt.show()
print("✅ Dashboard saved as superstore_dashboard.png!")
print("🎉 Step 4 Complete — Task 2 DONE!")
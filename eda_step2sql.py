import pandas as pd
import sqlite3

# Load cleaned dataset
df = pd.read_csv("superstore_cleaned.csv")

# Create in-memory SQLite database
conn = sqlite3.connect(':memory:')
df.to_sql('superstore', conn, index=False, if_exists='replace')

print("=" * 60)
print("SQL BUSINESS QUESTIONS — SUPERSTORE ANALYSIS")
print("=" * 60)

# ============================================================
# Q1. What are the Top 5 Products by Total Sales?
# ============================================================
print("\n🔹 Q1: Top 5 Products by Total Sales")
q1 = pd.read_sql_query("""
    SELECT [Product Name], 
           ROUND(SUM(Sales), 2) AS Total_Sales,
           COUNT(*) AS Total_Orders
    FROM superstore
    GROUP BY [Product Name]
    ORDER BY Total_Sales DESC
    LIMIT 5
""", conn)
print(q1.to_string(index=False))

# ============================================================
# Q2. What is the Total Sales by Region?
# ============================================================
print("\n🔹 Q2: Total Sales by Region")
q2 = pd.read_sql_query("""
    SELECT Region,
           ROUND(SUM(Sales), 2) AS Total_Sales,
           COUNT(*) AS Total_Orders,
           ROUND(AVG(Sales), 2) AS Avg_Sale
    FROM superstore
    GROUP BY Region
    ORDER BY Total_Sales DESC
""", conn)
print(q2.to_string(index=False))

# ============================================================
# Q3. Which Category generates the most revenue?
# ============================================================
print("\n🔹 Q3: Revenue by Category")
q3 = pd.read_sql_query("""
    SELECT Category,
           ROUND(SUM(Sales), 2) AS Total_Sales,
           COUNT(*) AS Total_Orders,
           ROUND(AVG(Sales), 2) AS Avg_Sale
    FROM superstore
    GROUP BY Category
    ORDER BY Total_Sales DESC
""", conn)
print(q3.to_string(index=False))

# ============================================================
# Q4. What are Monthly Sales Trends?
# ============================================================
print("\n🔹 Q4: Monthly Sales Trends")
q4 = pd.read_sql_query("""
    SELECT [Order Year],
           [Order Month],
           ROUND(SUM(Sales), 2) AS Monthly_Sales,
           COUNT(*) AS Total_Orders
    FROM superstore
    GROUP BY [Order Year], [Order Month]
    ORDER BY [Order Year], [Order Month]
""", conn)
print(q4.to_string(index=False))

# ============================================================
# Q5. Which Segment spends the most?
# ============================================================
print("\n🔹 Q5: Sales by Customer Segment")
q5 = pd.read_sql_query("""
    SELECT Segment,
           ROUND(SUM(Sales), 2) AS Total_Sales,
           COUNT(*) AS Total_Orders,
           ROUND(AVG(Sales), 2) AS Avg_Order_Value
    FROM superstore
    GROUP BY Segment
    ORDER BY Total_Sales DESC
""", conn)
print(q5.to_string(index=False))

# ============================================================
# Q6. What are the Top 5 States by Sales?
# ============================================================
print("\n🔹 Q6: Top 5 States by Sales")
q6 = pd.read_sql_query("""
    SELECT State,
           Region,
           ROUND(SUM(Sales), 2) AS Total_Sales,
           COUNT(*) AS Total_Orders
    FROM superstore
    GROUP BY State
    ORDER BY Total_Sales DESC
    LIMIT 5
""", conn)
print(q6.to_string(index=False))

# ============================================================
# Q7. Which Ship Mode is most used per Segment?
# ============================================================
print("\n🔹 Q7: Ship Mode Usage by Segment")
q7 = pd.read_sql_query("""
    SELECT Segment,
           [Ship Mode],
           COUNT(*) AS Total_Orders,
           ROUND(SUM(Sales), 2) AS Total_Sales
    FROM superstore
    GROUP BY Segment, [Ship Mode]
    ORDER BY Segment, Total_Orders DESC
""", conn)
print(q7.to_string(index=False))

# ============================================================
# Q8. What is the Average Shipping Days per Ship Mode?
# ============================================================
print("\n🔹 Q8: Average Shipping Days by Ship Mode")
q8 = pd.read_sql_query("""
    SELECT [Ship Mode],
           ROUND(AVG([Shipping Days]), 2) AS Avg_Shipping_Days,
           MIN([Shipping Days]) AS Min_Days,
           MAX([Shipping Days]) AS Max_Days,
           COUNT(*) AS Total_Orders
    FROM superstore
    GROUP BY [Ship Mode]
    ORDER BY Avg_Shipping_Days
""", conn)
print(q8.to_string(index=False))

# Save all results to Excel
with pd.ExcelWriter('sql_results.xlsx') as writer:
    q1.to_excel(writer, sheet_name='Q1_Top5_Products', index=False)
    q2.to_excel(writer, sheet_name='Q2_Sales_by_Region', index=False)
    q3.to_excel(writer, sheet_name='Q3_Revenue_by_Category', index=False)
    q4.to_excel(writer, sheet_name='Q4_Monthly_Trends', index=False)
    q5.to_excel(writer, sheet_name='Q5_Sales_by_Segment', index=False)
    q6.to_excel(writer, sheet_name='Q6_Top5_States', index=False)
    q7.to_excel(writer, sheet_name='Q7_ShipMode_Segment', index=False)
    q8.to_excel(writer, sheet_name='Q8_Shipping_Days', index=False)

print("\n✅ All SQL results saved to sql_results.xlsx!")
print("\n🎉 Step 2 Complete!")

conn.close()
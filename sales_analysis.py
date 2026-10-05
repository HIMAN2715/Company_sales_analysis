import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ============================================================
# COMPANY SALES DATA ANALYSIS
# Libraries: NumPy, Pandas, Matplotlib
# ============================================================

# 1. LOAD DATA
df = pd.read_csv("sales_data.csv")

print("\n========== ORIGINAL DATA ==========")
print(df)

# 2. BASIC INFORMATION
print("\n========== FIRST 5 ROWS ==========")
print(df.head())

print("\n========== DATASET SHAPE ==========")
print(df.shape)

print("\n========== COLUMN NAMES ==========")
print(df.columns.tolist())

print("\n========== DATA INFORMATION ==========")
df.info()

print("\n========== STATISTICAL SUMMARY ==========")
print(df.describe())

# 3. CHECK MISSING VALUES
print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

# 4. CREATE REVENUE COLUMN
df["Revenue"] = df["Units_Sold"] * df["Unit_Price"]

print("\n========== DATA WITH REVENUE ==========")
print(df)

# ============================================================
# NUMPY TASKS
# ============================================================

revenue_array = np.array(df["Revenue"])

print("\n========== NUMPY ANALYSIS ==========")

total_sales = np.sum(revenue_array)
average_sales = np.mean(revenue_array)
maximum_sale = np.max(revenue_array)
minimum_sale = np.min(revenue_array)
median_sale = np.median(revenue_array)
std_sales = np.std(revenue_array)

print("Total Revenue:", total_sales)
print("Average Transaction:", round(average_sales, 2))
print("Maximum Transaction:", maximum_sale)
print("Minimum Transaction:", minimum_sale)
print("Median Transaction:", median_sale)
print("Standard Deviation:", round(std_sales, 2))

# ============================================================
# PANDAS TASKS
# ============================================================

print("\n========== PANDAS ANALYSIS ==========")

# Total units sold
total_units = df["Units_Sold"].sum()
print("Total Units Sold:", total_units)

# Product-wise units sold
product_units = df.groupby("Product")["Units_Sold"].sum()
print("\nProduct-wise Units Sold:")
print(product_units)

# Best-selling product
best_product = product_units.idxmax()
print("\nBest-selling Product:", best_product)

# Product-wise revenue
product_revenue = df.groupby("Product")["Revenue"].sum()
print("\nProduct-wise Revenue:")
print(product_revenue.sort_values(ascending=False))

# Region-wise revenue
region_sales = df.groupby("Region")["Revenue"].sum()
print("\nRegion-wise Revenue:")
print(region_sales.sort_values(ascending=False))

# Best region
best_region = region_sales.idxmax()
print("\nRegion with Highest Revenue:", best_region)

# Salesperson performance
salesperson_sales = df.groupby("Salesperson")["Revenue"].sum()
print("\nSalesperson Performance:")
print(salesperson_sales.sort_values(ascending=False))

# Best salesperson
best_salesperson = salesperson_sales.idxmax()
print("\nTop Salesperson:", best_salesperson)

# Highest transaction
highest_sale = df.loc[df["Revenue"].idxmax()]
print("\n========== HIGHEST TRANSACTION ==========")
print(highest_sale)

# Filter high-value transactions
high_value_sales = df[df["Revenue"] > 50000]
print("\n========== TRANSACTIONS ABOVE 50,000 ==========")
print(high_value_sales)

# Laptop sales
laptop_sales = df[df["Product"] == "Laptop"]
print("\n========== LAPTOP SALES ==========")
print(laptop_sales)

# ============================================================
# DATE ANALYSIS
# ============================================================

df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.month

monthly_sales = df.groupby("Month")["Revenue"].sum()

print("\n========== MONTHLY REVENUE ==========")
print(monthly_sales)

# ============================================================
# FINAL BUSINESS REPORT
# ============================================================

print("\n" + "=" * 50)
print("    FINAL SALES REPORT")
print("=" * 50)

print(f"Total Revenue       : ₹{df['Revenue'].sum():,.2f}")
print(f"Total Units Sold    : {df['Units_Sold'].sum()}")
print(f"Average Transaction : ₹{df['Revenue'].mean():,.2f}")
print(f"Highest Transaction : ₹{df['Revenue'].max():,.2f}")
print(f"Lowest Transaction  : ₹{df['Revenue'].min():,.2f}")
print(f"Best Product        : {best_product}")
print(f"Best Region         : {best_region}")
print(f"Top Salesperson     : {best_salesperson}")

# ============================================================
# MATPLOTLIB VISUALIZATIONS
# ============================================================

# # 1. Product-wise Units Sold
# plt.figure()
# plt.bar(product_units.index, product_units.values)
# plt.title("Units Sold by Product")
# plt.xlabel("Product")
# plt.ylabel("Units Sold")
# plt.xticks(rotation=10)
# plt.tight_layout()
# plt.show()

# # 2. Region-wise Revenue
# plt.figure()
# plt.bar(region_sales.index, region_sales.values)
# plt.title("Revenue by Region")
# plt.xlabel("Region")
# plt.ylabel("Revenue (₹)")
# plt.tight_layout()
# plt.show()

# # 3. Monthly Revenue Trend
# plt.figure()
# plt.plot(monthly_sales.index, monthly_sales.values, marker="o")
# plt.title("Monthly Revenue Trend")
# plt.xlabel("Month")
# plt.ylabel("Revenue (₹)")
# plt.xticks(monthly_sales.index)
# plt.grid(True)
# plt.tight_layout()
# plt.show()

# # 4. Product Revenue Distribution
# plt.figure()
# plt.pie(
#     product_revenue.values,
#     labels=product_revenue.index,
#     autopct="%1.1f%%"
# )
# plt.title("Revenue Distribution by Product")
# plt.tight_layout()
# plt.show()

# # 5. Revenue Distribution Histogram
# plt.figure()
# plt.hist(df["Revenue"], bins=8)
# plt.title("Distribution of Transaction Revenue")
# plt.xlabel("Revenue (₹)")
# plt.ylabel("Number of Transactions")
# plt.tight_layout()
# plt.show()

# # 6. Salesperson Performance
# plt.figure()
# plt.bar(salesperson_sales.index, salesperson_sales.values)
# plt.title("Salesperson Performance")
# plt.xlabel("Salesperson")
# plt.ylabel("Revenue (₹)")
# plt.tight_layout()
# plt.show()

# print("\nAnalysis completed successfully!")

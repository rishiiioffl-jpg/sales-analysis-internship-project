import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load sales data
df = pd.read_csv("data/sales_data.csv")

# Convert Date column to date format
df["Date"] = pd.to_datetime(df["Date"])

# Calculate total sales
df["Total_Sales"] = df["Quantity"] * df["Price"]

# Display the data
print(df)

# Display total revenue
print("\nTotal Revenue:", df["Total_Sales"].sum())
# Basic Sales Analysis

print("\nAverage Sale:", df["Total_Sales"].mean())

print("\nHighest Sale:", df["Total_Sales"].max())

print("\nLowest Sale:", df["Total_Sales"].min())

print("\nTotal Quantity Sold:", df["Quantity"].sum())

print("\nProduct-wise Sales:")
print(df.groupby("Product")["Total_Sales"].sum())
# Product-wise Sales Chart

product_sales = df.groupby("Product")["Total_Sales"].sum()

product_sales.plot(kind="bar")

plt.title("Product-wise Sales")
plt.xlabel("Product")
plt.ylabel("Total Sales")

plt.show()
# Sales over Time

daily_sales = df.groupby("Date")["Total_Sales"].sum()

daily_sales.plot(kind="line", marker="o")

plt.title("Sales Over Time")
plt.xlabel("Date")
plt.ylabel("Total Sales")

plt.xticks(rotation=45)

plt.show()
# Best-Selling Product

best_product = df.groupby("Product")["Total_Sales"].sum().idxmax()
best_product_sales = df.groupby("Product")["Total_Sales"].sum().max()

print("\nBest-Selling Product:", best_product)
print("Best Product Sales:", best_product_sales)


# Best Sales Day

best_day = df.groupby("Date")["Total_Sales"].sum().idxmax()
best_day_sales = df.groupby("Date")["Total_Sales"].sum().max()

print("\nBest Sales Day:", best_day)
print("Best Day Sales:", best_day_sales)
# Data Cleaning Check

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nData Information:")
df.info()
# Quantity Sold by Product

quantity_by_product = df.groupby("Product")["Quantity"].sum().sort_values(ascending=False)

print("\nQuantity Sold by Product:")
print(quantity_by_product)
# Category-wise Sales

category_sales = (
    df.groupby("Category")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\nCategory-wise Sales:")
print(category_sales)
category_sales.plot(kind="bar")

plt.title("Category-wise Sales")
plt.xlabel("Category")
plt.ylabel("Total Sales")

plt.show()
# Daily Sales Trend

daily_sales = df.groupby("Date")["Total_Sales"].sum()

print("\nDaily Sales:")
print(daily_sales)
# Daily Sales Trend Chart

plt.figure(figsize=(10, 5))

plt.plot(
    daily_sales.index,
    daily_sales.values,
    marker="o"
)

plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Total Sales")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
# Monthly Sales Trend

df["Month"] = df["Date"].dt.to_period("M")

monthly_sales = df.groupby("Month")["Total_Sales"].sum()

print("\nMonthly Sales:")
print(monthly_sales)
# Monthly Sales Trend Chart

plt.figure(figsize=(10, 5))

plt.plot(
    monthly_sales.index.astype(str),
    monthly_sales.values,
    marker="o"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()

# ==============================
# DAY 6 - SALES VISUALIZATION
# ==============================

# Product-wise sales chart
product_sales = df.groupby("Product")["Total_Sales"].sum()

plt.figure(figsize=(8, 5))
product_sales.plot(kind="bar")
plt.title("Product-wise Sales")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("product_wise_sales.png")
plt.show()


# Monthly sales chart
monthly_sales = df.groupby("Month")["Total_Sales"].sum()

plt.figure(figsize=(8, 5))
monthly_sales.plot(kind="bar")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("monthly_sales.png")
plt.show()


# Quantity sold by product
product_quantity = df.groupby("Product")["Quantity"].sum()

plt.figure(figsize=(8, 5))
product_quantity.plot(kind="bar")
plt.title("Quantity Sold by Product")
plt.xlabel("Product")
plt.ylabel("Quantity Sold")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("quantity_by_product.png")
plt.show()


# ==============================
# KEY INSIGHTS
# ==============================

best_product = product_sales.idxmax()
highest_product_sales = product_sales.max()

best_quantity_product = product_quantity.idxmax()
highest_quantity = product_quantity.max()

print("\n===== KEY INSIGHTS =====")

print("Best-selling product by revenue:", best_product)
print("Highest product revenue:", highest_product_sales)

print("Product with highest quantity sold:", best_quantity_product)
print("Highest quantity sold:", highest_quantity)

print("Highest monthly sales:", monthly_sales.max())
print("Lowest monthly sales:", monthly_sales.min())

print("\nDay 6 analysis completed successfully!")
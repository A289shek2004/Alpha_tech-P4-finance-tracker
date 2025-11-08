# main.py
# 🧾 Personal Finance Tracker Project
# Made for beginners & students

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# ==============================
# STEP 1: LOAD AND CLEAN DATA
# ==============================
print("📂 Loading your expense data...")

df = pd.read_csv(r"expense.csv")

# Convert date to datetime format
df['date'] = pd.to_datetime(df['date'], dayfirst=True, errors='coerce')

# Standardize category names
df['category'] = df['category'].str.strip().str.title()

# Ensure amounts are numbers
df['amount'] = pd.to_numeric(df['amount'], errors='coerce')

# Drop empty or invalid rows
df = df.dropna(subset=['amount'])

print("✅ Data loaded successfully!\n")
print(df.head())

# ==============================
# STEP 2: ANALYSIS
# ==============================
print("\n🔍 Analyzing your data...")

# Total expense per category
category_summary = df.groupby('category')['amount'].sum().sort_values(ascending=False)

# Total expense per user
user_summary = df.groupby('user')['amount'].sum()

# Average, total, and savings
avg_spend = np.mean(df['amount'])
std_dev = np.std(df['amount'])
total_expense = df['amount'].sum()

# Ask the user for their monthly income
income = float(input("\n💰 Enter your monthly income (₹): "))

savings = income - total_expense
savings_percent = (savings / income) * 100

print("\n📊 Insights:")
print(f"Total expense: ₹{total_expense}")
print(f"Average spend per transaction: ₹{avg_spend:.2f}")
print(f"Spending deviation: ₹{std_dev:.2f}")
print(f"Savings: ₹{savings:.2f} ({savings_percent:.2f}%)")

# ==============================
# STEP 3: VISUALIZATION
# ==============================
print("\n📈 Generating charts...")

plt.figure(figsize=(6,6))
plt.pie(category_summary, labels=category_summary.index, autopct='%1.1f%%', startangle=90)
plt.title("Expense Distribution by Category")

# Save chart
os.makedirs("output", exist_ok=True)
plt.savefig("output/category_pie_chart.png")
plt.show()

print("✅ Chart saved in output/category_pie_chart.png")

# ==============================
# STEP 4: EXPORT TO EXCEL
# ==============================
print("\n📘 Creating Excel Report...")

summary_df = pd.DataFrame({
    "Metric": ["Total Expense", "Average Spend", "Savings (%)"],
    "Value": [total_expense, avg_spend, f"{savings_percent:.2f}%"]
})

# Write to Excel with multiple sheets
with pd.ExcelWriter("output/finance_summary.xlsx", engine='xlsxwriter') as writer:
    df.to_excel(writer, sheet_name="Transactions", index=False)
    category_summary.to_excel(writer, sheet_name="By Category")
    user_summary.to_excel(writer, sheet_name="By User")
    summary_df.to_excel(writer, sheet_name="Summary", index=False)

print("✅ Excel report generated successfully: output/finance_summary.xlsx")

print("\n🎉 All done! Open the 'output' folder to see your report and chart.")
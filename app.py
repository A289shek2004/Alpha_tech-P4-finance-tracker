# app.py
# 🧾 Personal Finance Tracker Dashboard (Streamlit Version)
# Interactive dashboard for expense analysis and visualization

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="💰 Personal Finance Tracker", layout="wide")

# ==============================
# APP HEADER
# ==============================
st.title("💰 Personal Finance Tracker Dashboard")
st.markdown("### Track your daily expenses, analyze spending patterns, and visualize savings interactively.")

# ==============================
# STEP 1: DATA UPLOAD
# ==============================
st.sidebar.header("📂 Upload Expense Data")

uploaded_file = st.sidebar.file_uploader("Upload your expense CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Data cleaning
    df['date'] = pd.to_datetime(df['date'], dayfirst=True, errors='coerce')
    df['category'] = df['category'].str.strip().str.title()
    df['amount'] = pd.to_numeric(df['amount'], errors='coerce')
    df = df.dropna(subset=['amount'])

    st.success("✅ Data loaded successfully!")
    st.write("### 📋 Preview of Data", df.head())

    # ==============================
    # STEP 2: INPUT MONTHLY INCOME
    # ==============================
    income = st.sidebar.number_input("💵 Enter your monthly income (₹)", min_value=0.0, step=1000.0)

    # ==============================
    # STEP 3: ANALYSIS
    # ==============================
    category_summary = df.groupby('category')['amount'].sum().sort_values(ascending=False)
    user_summary = df.groupby('user')['amount'].sum()
    avg_spend = np.mean(df['amount'])
    std_dev = np.std(df['amount'])
    total_expense = df['amount'].sum()

    savings = income - total_expense if income > 0 else 0
    savings_percent = (savings / income * 100) if income > 0 else 0

    st.subheader("📊 Financial Summary")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Expense (₹)", f"{total_expense:,.2f}")
    col2.metric("Average Spend (₹)", f"{avg_spend:,.2f}")
    col3.metric("Spending Deviation (₹)", f"{std_dev:,.2f}")
    col4.metric("Savings (%)", f"{savings_percent:.2f}%")

    # ==============================
    # STEP 4: VISUALIZATIONS
    # ==============================
    st.subheader("📈 Expense Analysis")

    tab1, tab2, tab3 = st.tabs(["By Category", "By User", "Over Time"])

    with tab1:
        st.write("### Expense Distribution by Category")
        fig1, ax1 = plt.subplots(figsize=(6,6))
        ax1.pie(category_summary, labels=category_summary.index, autopct='%1.1f%%', startangle=90)
        ax1.axis('equal')
        st.pyplot(fig1)
        st.bar_chart(category_summary)

    with tab2:
        st.write("### Expense by User")
        st.bar_chart(user_summary)

    with tab3:
        st.write("### Monthly Expense Trend")
        df['month'] = df['date'].dt.to_period('M').astype(str)
        monthly_summary = df.groupby('month')['amount'].sum()
        st.line_chart(monthly_summary)

    # ==============================
    # STEP 5: EXPORT REPORT
    # ==============================
    st.subheader("📘 Download Report")

    summary_df = pd.DataFrame({
        "Metric": ["Total Expense", "Average Spend", "Savings (%)"],
        "Value": [total_expense, avg_spend, f"{savings_percent:.2f}%"]
    })

    with pd.ExcelWriter("finance_summary.xlsx", engine='xlsxwriter') as writer:
        df.to_excel(writer, sheet_name="Transactions", index=False)
        category_summary.to_excel(writer, sheet_name="By Category")
        user_summary.to_excel(writer, sheet_name="By User")
        summary_df.to_excel(writer, sheet_name="Summary", index=False)

    with open("finance_summary.xlsx", "rb") as f:
        st.download_button("📥 Download Excel Report", f, file_name="finance_summary.xlsx")

else:
    st.info("👈 Please upload an `expense.csv` file to begin.")

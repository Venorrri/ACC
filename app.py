import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="E-Commerce Financial Dashboard", layout="wide")
st.title("E-Commerce Financial Dashboard")
st.markdown("Analyze product margin sensitivity under supply chain cost inflation")

@st.cache_data
def load_data():
    df = pd.read_csv('ecommerce_sales_dataset.csv')
    df['Order_Date'] = pd.to_datetime(df['Order_Date'])
    if 'Cost' not in df.columns and 'Revenue' in df.columns and 'Profit' in df.columns:
        df['Cost'] = df['Revenue'] - df['Profit']
    if 'Status' in df.columns:
        return df[df['Status'] == 'Delivered']
    return df

df = load_data()

st.sidebar.header("Simulation Control")
inflation_rate = st.sidebar.slider("COGS Inflation (%)", 0, 50, 30, 1)

total_revenue = df['Revenue'].sum()
total_cost = df['Cost'].sum() * (1 + inflation_rate / 100)
total_profit = total_revenue - total_cost
avg_margin = total_profit / total_revenue * 100

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Revenue", f"${total_revenue:,.0f}")
col2.metric("Total Cost (Adjusted)", f"${total_cost:,.0f}")
col3.metric("Total Profit", f"${total_profit:,.0f}")
col4.metric("Avg Profit Margin", f"{avg_margin:.1f}%")

categories = df['Category'].unique()
sensitivity_data = []
for cat in categories:
    cat_df = df[df['Category'] == cat]
    rev = cat_df['Revenue'].sum()
    cost = cat_df['Cost'].sum() * (1 + inflation_rate / 100)
    profit = rev - cost
    margin = profit / rev * 100
    sensitivity_data.append({'Category': cat, 'Margin': margin})

sensitivity_df = pd.DataFrame(sensitivity_data).sort_values(by='Margin', ascending=False)

st.subheader("Category Margin Sensitivity")
fig, ax = plt.subplots(figsize=(12, 5))
sns.barplot(data=sensitivity_df, x='Margin', y='Category', palette="Blues_r", ax=ax)
ax.set_xlabel("Profit Margin (%)")
ax.set_ylabel("Product Category")
st.pyplot(fig)

st.markdown(
    "### Strategic Insight\n"
    "Categories with negative simulated margins require immediate operational review and potential pricing adjustments."
)
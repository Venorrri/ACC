# Revenue and Profit Analysis in Global E-Commerce (2021–2024)

A Python-based business analytics project on profit trends, customer retention, and cost sensitivity in a global e-commerce dataset.

**Interactive Website**:https://vb2kchpbg4vx9xxv3z7lqby.streamlit.app/

## 1. Problem & User

This project evaluates the financial performance and operating resilience of a global e-commerce business from 2021 to 2024. It is designed for e-commerce managers, finance teams, and operations staff who need a clearer view of profit movement, repeat purchasing, and cost-related risk.

## 2. Data

- **Source**: Kaggle
- **Access date**:2026-04-14
- **Time range**: 2021–2024
- **Unit of analysis**: One row = one transaction

### Key fields
`Order_Date`, `Order_Status`, `Customer_ID`, `Category`, `Region`, `Revenue`, `Cost`, `Profit`, `Profit_Margin_%`, `Shipping_Cost`, `Shipping_Days`

## 3. Methods

- Cleaned and standardised the raw dataset
- Converted `Order_Date` into datetime format
- Restricted the main analytical sample to **delivered orders**
- Used summary statistics and a histogram to profile transaction structure
- Analysed monthly profit with a 3-month rolling average
- Built a cohort retention heatmap based on first purchase month
- Simulated category-level margin changes under cost inflation scenarios

## 4. Key Findings

- Revenue is highly right-skewed, with many low-value orders and a small number of large orders.
- Monthly profit is volatile, so rolling trends are more informative than single-period results.
- Customer retention drops quickly after the first purchase month, suggesting weak repeat purchasing.
- Product categories differ in cost resilience, and some are much more exposed to margin pressure.

## 5. How to Run

1. Put `ecommerce_sales_dataset.csv` in the same folder as the notebook.
2. Open the notebook in Jupyter Notebook, JupyterLab, or Google Colab.
3. Make sure these libraries are installed: `pandas`, `numpy`, `matplotlib`, `seaborn`.
4. Run all cells from top to bottom.

## 6. Limitations & Next Steps

### Limitations
- The dataset does not include marketing spend, returns, acquisition channels, or external market conditions.
- The retention analysis shows patterns, but not the causes of return or churn.
- The stress test is scenario-based rather than predictive.

### Next Steps
- Compare retention and profitability across more detailed subgroups.
- Decompose profit change into volume, order value, and margin effects.
- Extend the stress test to shipping shocks, discount changes, or return-rate assumptions.

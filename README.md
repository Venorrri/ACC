# Revenue and Profit Analysis in Global E-Commerce (2021–2024)

## Project Snapshot

This project is a Python-based business analytics product that examines revenue quality, profit sustainability, customer retention, and cost-related risk in a global e-commerce dataset from 2021 to 2024.

The project was built for **Track 4: Interactive Data Analysis Tool**. It includes a Jupyter Notebook for the full analytical workflow and a Streamlit app that allows users to explore the main business insights in a more accessible and interactive format.

The main purpose of this project is not only to describe sales performance, but also to answer a more practical management question:

**How can an e-commerce manager identify whether current revenue growth is supported by sustainable profit, repeat purchasing, and cost resilience?**

---

## Links

- **Interactive Streamlit App**: https://vb2kchpbg4vx9xxv3z7lqby.streamlit.app/
- **GitHub Repository**: https://github.com/Venorrri/ACC
- **Notebook HTML Preview**: https://venorrri.github.io/ACC/index.html

The original Jupyter Notebook may not render properly on GitHub, especially when it contains many tables, charts, and output cells. Therefore, I created a GitHub Pages version as an accessible HTML preview of the notebook outputs.

---

## 1. Problem and Target User

This project evaluates the financial performance and operating resilience of a global e-commerce business from 2021 to 2024.

The target users are:

- e-commerce strategy managers
- financial controllers
- operations analysts
- business students interested in data-driven commercial decision-making

These users need more than a simple sales summary. They need to understand whether revenue is profitable, whether customers continue purchasing after their first order, and whether profit margins can survive cost increases.

The project therefore focuses on three linked questions:

1. What is the underlying profit trend after reducing short-term seasonal noise?
2. How strong is customer retention after the first purchase month?
3. Which product categories are more vulnerable when costs increase?

---

## 2. Data

- **Dataset**: Global e-commerce transaction dataset
- **Source**: Kaggle
- **Access date**: 2026-04-14
- **Time range**: 2021–2024
- **Unit of analysis**: One row represents one transaction
- **Main file used**: `ecommerce_sales_dataset.csv`

### Key Fields

The analysis uses the following fields:

- `Order_ID`
- `Order_Date`
- `Year`
- `Month`
- `Quarter`
- `Season`
- `Customer_ID`
- `Customer_Segment`
- `Region`
- `Category`
- `Order_Status`
- `Revenue`
- `Cost`
- `Profit`
- `Profit_Margin_%`
- `Shipping_Cost`
- `Shipping_Days`

The dataset is suitable for this project because it contains both financial and operational variables. This makes it possible to examine not only sales performance, but also profit, customer behaviour, and cost-related risk.

---

## 3. Data Cleaning and Analytical Sample

The notebook first creates a cleaned version of the raw dataset. The main cleaning steps include:

1. converting `Order_Date` into datetime format
2. standardising text fields such as `Order_Status`, `Customer_Segment`, `Region`, and `Category`
3. checking missing values, duplicate rows, invalid dates, and negative values
4. checking whether the `Year` field matches the year extracted from `Order_Date`
5. restricting the main analytical sample to delivered orders

The raw dataset contains **10,000 orders**. After filtering to delivered orders, the final analytical sample contains **6,273 delivered orders**, representing **62.73%** of all orders.

The basic data quality checks show:

- no missing values
- no duplicate rows
- no invalid order dates
- no year-date mismatch
- no negative revenue, cost, shipping cost, or shipping days

This provides a clean basis for the later analysis.

---

## 4. Methods

The project follows a complete Python-based analytical workflow.

### 4.1 Baseline Transaction Profile

The notebook first summarises key transaction-level variables, including unit price, quantity, discount, revenue, cost, profit, profit margin, shipping cost, and shipping days.

For delivered orders:

- average revenue per order is about **527.37**
- median revenue per order is about **161.76**
- average profit per order is about **144.91**
- median profit per order is about **34.71**
- average profit margin is about **23.57%**
- median profit margin is about **28.32%**

The large gap between mean and median revenue shows that revenue is highly right-skewed. In other words, most orders are relatively small, while a small number of large orders contribute heavily to total revenue.

### 4.2 Profit Trend Analysis

Monthly profit is calculated by aggregating order-level profit by month. A 3-month rolling average is then used to smooth short-term volatility.

This helps separate temporary seasonal fluctuations from the underlying profit trajectory. This is important because e-commerce revenue and profit can be strongly affected by seasonal events, such as holiday promotions or Q4 sales campaigns.

### 4.3 Customer Retention Analysis

The notebook builds a cohort retention heatmap based on each customer’s first purchase month.

Each row represents a customer cohort, and each column shows how many customers from that cohort remain active in later months. This allows the project to evaluate whether revenue is supported by repeat purchasing or mainly by one-time purchases.

### 4.4 Cost Sensitivity and Stress Testing

The project also performs a simple category-level cost sensitivity analysis.

For each product category, the notebook simulates how profit margins change under four cost scenarios:

- current cost
- 5% cost increase
- 10% cost increase
- 15% cost increase

This is not designed as a forecast. Instead, it is a stress test that helps identify which categories are more resilient and which categories are more exposed to cost pressure.

### 4.5 Interactive Streamlit Tool

The Streamlit app turns the analysis into an accessible data product. It allows users to view and interpret the main outputs without running the notebook manually.

The interactive tool helps users explore:

- revenue and profit structure
- monthly profit trend
- customer retention pattern
- category-level margin sensitivity
- business recommendations based on the analysis

---

## 5. Key Findings

### 5.1 Revenue is highly concentrated and right-skewed

The baseline analysis shows that average revenue per delivered order is much higher than median revenue. This means that a small number of high-value orders have a strong effect on total revenue.

This is important for management because headline revenue may look strong even when the typical order is much smaller. Therefore, managers should not rely only on total revenue. They should also monitor median order value and profit per order.

### 5.2 Profit trend should be interpreted with smoothing

Monthly profit is volatile. The raw monthly profit line can be affected by short-term seasonality, promotion campaigns, or random transaction-level fluctuations.

The 3-month rolling average provides a clearer view of the underlying profit movement. This makes it more useful for financial planning and budget allocation than a single-month result.

### 5.3 Customer retention is weak after the first purchase month

The cohort retention heatmap shows that customer activity drops sharply after the first purchase month. Most cohorts have only low retention rates in later months.

This suggests that the business depends heavily on continuous customer acquisition. If acquisition costs increase, the business may face pressure because repeat purchasing is not strong enough to support long-term revenue sustainability.

### 5.4 Cost pressure can quickly reduce profit margins

The cost sensitivity analysis shows that some product categories are more vulnerable to cost increases than others. Categories with thinner baseline margins can move close to, or below, the break-even point when costs increase by 5% to 15%.

This means that managers should not treat all product categories equally. More resilient categories can support stable profit, while vulnerable categories require closer monitoring, pricing adjustment, or supply-chain cost control.

---

## 6. Business Recommendations

Based on the analysis, the project suggests three practical recommendations.

### 6.1 Shift part of the marketing budget toward retention

Since retention drops quickly after the first purchase month, the business should not rely only on acquiring new customers. It should also invest in CRM, loyalty programmes, email follow-ups, and win-back campaigns.

Improving retention in the second and third months after the first purchase may reduce dependence on expensive new-customer acquisition.

### 6.2 Monitor cost-sensitive categories more closely

For categories that become vulnerable under cost inflation scenarios, managers should consider early action. Possible actions include:

- negotiating longer-term supplier contracts
- improving packaging and logistics efficiency
- adjusting prices gradually
- reducing discounts on low-margin products
- reviewing inventory exposure in risky categories

### 6.3 Prioritise resilient categories in planning

Categories that maintain healthy margins even under higher-cost scenarios should receive more attention in inventory planning and marketing allocation.

These categories can act as more reliable profit contributors when the business faces cost pressure or uncertain market conditions.

---

## 7. Repository Structure

The repository is organised as follows:

    ACC/
    ├── README.md
    ├── app.py
    ├── requirements.txt
    ├── ecommerce_sales_dataset.csv
    ├── Revenue and Profit Analysis in Global E-Commerce from 2021 to 2024.ipynb
    └── docs/
        └── index.html

### File Explanation

- `README.md`: project overview, links, methods, findings, and running instructions
- `app.py`: Streamlit interactive tool
- `requirements.txt`: Python dependencies required for the Streamlit app
- `ecommerce_sales_dataset.csv`: dataset used in the analysis
- `Revenue and Profit Analysis in Global E-Commerce from 2021 to 2024.ipynb`: full Jupyter Notebook analytical workflow
- `docs/index.html`: GitHub Pages HTML preview of the notebook outputs

---

## 8. Tools and Libraries

The project uses the following tools and libraries:

- Python
- Jupyter Notebook
- Streamlit
- pandas
- numpy
- matplotlib
- seaborn

To install the required libraries manually, use:

    pip install pandas numpy matplotlib seaborn streamlit

If using the provided `requirements.txt` file, use:

    pip install -r requirements.txt

---

## 9. How to Run the Notebook

To run the notebook:

1. Download or clone this repository.
2. Make sure `ecommerce_sales_dataset.csv` is in the same folder as the notebook.
3. Open the notebook in Jupyter Notebook, JupyterLab, or Google Colab.
4. Run all cells from top to bottom.

The notebook reads the dataset with:

    df = pd.read_csv("ecommerce_sales_dataset.csv")

---

## 10. How to Run the Streamlit App Locally

To run the interactive tool locally, use:

    streamlit run app.py

Then open the local URL shown in the terminal.

The deployed version is available here:

https://vb2kchpbg4vx9xxv3z7lqby.streamlit.app/

---

## 11. Notebook HTML Preview

The original Jupyter Notebook may not render reliably on GitHub, especially because it contains multiple tables, figures, and output cells.

To make the analysis easier for markers and visitors to read, I created an HTML version of the notebook using GitHub Pages.

Notebook HTML preview:

https://venorrri.github.io/ACC/index.html

This preview is not a replacement for the notebook or the Streamlit app. It is provided as an additional accessible version of the notebook outputs.

---

## 12. Limitations

This project has several limitations.

First, the dataset is transaction-level only. It does not include marketing expenditure, customer acquisition cost, product return information, advertising channels, or external market conditions. Therefore, the project can describe profit and retention patterns, but it cannot fully explain all causes behind those patterns.

Second, the retention analysis is descriptive. It shows whether customers return, but it does not identify the exact reasons for customer churn.

Third, the cost sensitivity analysis is scenario-based rather than predictive. It assumes that revenue remains constant while costs increase. In reality, customers may change their purchasing behaviour if prices, discounts, or shipping policies change.

Fourth, the project focuses on a simple and interpretable analysis suitable for a mini assignment. It does not use advanced predictive modelling or causal inference.

---

## 13. Possible Improvements

Future improvements could include:

- adding customer acquisition cost and marketing spend data
- analysing profitability by customer segment, region, and category together
- decomposing profit changes into volume, average order value, discount, and margin effects
- building a predictive model for repeat purchase probability
- extending the Streamlit app with more user-controlled filters
- adding downloadable charts or summary tables to the app

---

## 14. Skills Demonstrated

This project demonstrates the following skills:

- data cleaning and preparation with pandas
- transaction-level business analysis
- time-series profit trend analysis
- cohort retention analysis
- scenario-based stress testing
- data visualization with matplotlib and seaborn
- Streamlit app development
- business interpretation and communication
- GitHub-based project publication

---

## Conclusion

This project shows how Python can be used to turn transaction-level e-commerce data into a small business analytics product.

The analysis suggests that the business should not only focus on total revenue. It should also pay attention to profit sustainability, customer retention, and cost resilience.

The Streamlit app makes the project more accessible to non-technical users, while the notebook provides the full analytical workflow for reproducibility.

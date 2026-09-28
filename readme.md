# ⚡ Retail Business Intelligence & Automation System

<p align="center">
  <strong>Automated ETL · Interactive Analytics · Predictive Sales Forecasting</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/status-Production--Ready-brightgreen?style=flat-square" alt="Status: Production Ready" />
  <img src="https://img.shields.io/badge/platform-Streamlit%20%7C%20Python-blue?style=flat-square" alt="Platform: Streamlit and Python" />
  <img src="https://img.shields.io/badge/version-1.0.0-orange?style=flat-square" alt="Version 1.0.0" />
  <img src="https://img.shields.io/badge/license-MIT-red?style=flat-square" alt="MIT License" />
  <a href="YOUR_STREAMLIT_APP_LIVE_URL_HERE">
    <img src="https://img.shields.io/badge/Live%20Demo-Open%20App-00C48C?style=flat-square&logo=streamlit" alt="Open Live Demo" />
  </a>
</p>

<p align="center">
  <em>A complete retail analytics dashboard that turns raw sales files into clean data, business insights, and actionable demand forecasts.</em>
</p>

> **Live Demo:** https://bussiness-intelligence-automation-system-8htggjwo8gbo2bsxym3sp.streamlit.app/

---

## 📌 Overview

The **Retail Business Intelligence & Automation System** is an end-to-end Streamlit application for digitizing retail sales analysis. It replaces repetitive spreadsheet-based reporting with an automated workflow that cleans uploaded sales data, stores validated transactions in SQLite, presents interactive performance dashboards, and produces a 30-day sales forecast.

The project is designed for **retail business owners, analysts, and decision-makers** who need a simple way to understand revenue performance, identify high-performing products and categories, and make more informed inventory decisions.

## 🎯 Business Problem

Manual retail reporting often creates avoidable operational problems:

- **Inconsistent data:** Dates, prices, quantities, and column names may use different formats.
- **Duplicate transactions:** Repeated records can inflate revenue and order metrics.
- **Poor data quality:** Missing dates, invalid values, and negative quantities can corrupt reports.
- **Slow reporting cycles:** Preparing recurring Excel reports takes time and manual effort.
- **Limited forecasting:** Historical sales data is often not converted into forward-looking insights.

## 💡 Solution

This application provides a repeatable analytics pipeline:

1. **Upload** a `.csv` or `.xlsx` sales file.
2. **Normalize** column names and data types.
3. **Validate** dates, quantities, and unit prices.
4. **Remove** duplicate and invalid records.
5. **Calculate** transaction-level revenue.
6. **Store** clean records in a local SQLite database.
7. **Visualize** key performance indicators and sales trends.
8. **Forecast** the next 30 days of sales using linear regression.
9. **Export** the cleaned dataset for further analysis.

---

## 🚀 Key Features

### **Automated ETL and Data Cleaning**

- Supports **CSV and Excel** sales uploads.
- Standardizes column names by trimming whitespace, converting to lowercase, and replacing spaces or hyphens with underscores.
- Converts mixed date formats into a consistent date format.
- Converts numeric fields safely and removes invalid records.
- Filters out non-positive quantities and unit prices.
- Removes duplicate rows and previously ingested transaction IDs.
- Calculates `total_amount` automatically as `quantity × unit_price`.

### **Interactive Executive Dashboard**

- **Total Revenue**
- **Total Orders**
- **Average Order Value**
- **Unique Customers**
- Monthly revenue trend
- Revenue distribution by category
- Top-selling products
- Customer order-frequency distribution

### **Actionable Business Insights**

The dashboard automatically generates recommendations based on the uploaded data, including:

- The category contributing the most revenue.
- Suggested stock allocation priorities.
- Average order value optimization opportunities.
- Data-quality and cleaning status.

### **Predictive Sales Forecasting**

- Generates a **30-day sales forecast** when at least five days of historical data are available.
- Uses a scikit-learn `LinearRegression` model on daily aggregated sales.
- Prevents negative forecast values.
- Displays historical sales and predicted sales on the same interactive chart.

### **Clean Data Export**

- Download the cleaned and validated dataset as a `.csv` file directly from the sidebar.

---

## 🖥️ Application Workflow

```text
Sales CSV/XLSX
      │
      ▼
File Upload in Streamlit
      │
      ▼
Column Normalization & Validation
      │
      ▼
Duplicate and Invalid Row Removal
      │
      ▼
Revenue Calculation
      │
      ▼
SQLite Storage
      │
      ├── Executive Analytics
      ├── Actionable Recommendations
      ├── 30-Day Sales Forecast
      └── Clean CSV Export
```

---

## 🗂️ Project Structure

```text
.
├── app.py                 # Streamlit application and dashboard interface
├── data_cleaning.py       # Data validation, cleaning, deduplication, and SQLite ingestion
├── forecaster.py          # 30-day sales forecasting module
├── dummy_dataset.py       # Generates sample data for testing
├── generate_test_data.py  # Generates intentionally dirty CSV and Excel test files
├── requirements.txt       # Python dependencies
├── readme.md              # Project documentation
└── sales.db               # Generated SQLite database after ingestion
```

> **Note:** `sales.db` is created automatically the first time valid sales data is ingested. It does not need to be created manually.

---

## 📄 Expected Input Data

Uploaded files should contain the following columns:

| Column | Description | Example |
| --- | --- | --- |
| `transaction_id` | Unique transaction identifier | `TXN-1001` |
| `date` | Transaction date | `2026-01-15` |
| `customer_id` | Customer identifier | `CUST-001` |
| `product` | Product name | `Wireless Mouse` |
| `category` | Product category | `Electronics` |
| `quantity` | Number of units sold | `3` |
| `unit_price` | Price per unit | `24.99` |

The cleaning pipeline derives the following field automatically:

```text
total_amount = quantity × unit_price
```

---

## ⚙️ Local Setup

### **1. Clone the Repository**

```bash
git clone https://github.com/Furqan-Ahmed2006/Bussiness-Intelligence-Automation-System.git
cd Bussiness-Intelligence-Automation-System
```

### **2. Create and Activate a Virtual Environment**

#### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

#### macOS/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### **3. Install Dependencies**

```bash
pip install -r requirements.txt
```

### **4. Run the Application**

```bash
streamlit run app.py
```

The application will open in your browser at the local Streamlit address shown in the terminal, usually:

```text
http://localhost:8501
```

---

## 🧪 Test Data

Run the scripts below when you want to generate sample or intentionally messy datasets:

```bash
python dummy_dataset.py
python generate_test_data.py
```

Then upload the generated `.csv` or `.xlsx` file through the Streamlit sidebar.

---

## ☁️ Streamlit Cloud Deployment

1. Push this repository to GitHub.
2. Open [Streamlit Community Cloud](https://share.streamlit.io/).
3. Select **New app**.
4. Choose this repository and the `main` branch.
5. Set the main file path to:

   ```text
   app.py
   ```

6. Deploy the application.
7. Copy the deployed URL and replace `YOUR_STREAMLIT_APP_LIVE_URL_HERE` in this README.

After deployment, the badge at the top of this page can link directly to your live dashboard.

---

## 🛠️ Technology Stack

- **Python** — Core programming language
- **Streamlit** — Interactive web application framework
- **Pandas** — Data cleaning, transformation, and aggregation
- **NumPy** — Numerical operations
- **Plotly** — Interactive charts and visualizations
- **Scikit-learn** — Linear regression forecasting
- **SQLite** — Embedded transactional data storage
- **Faker** — Test-data generation

---

## 📈 Forecasting Methodology

The forecasting module groups transactions by date and calculates total daily sales. It then trains a simple linear regression model using the number of elapsed days as the independent variable and daily revenue as the target variable.

The forecast is intended to provide a lightweight directional estimate for planning and demonstration purposes. It should not be treated as a replacement for a production forecasting system that accounts for seasonality, promotions, holidays, pricing changes, and external market conditions.

---

## 🔒 Data and Security Notes

- The application uses a local SQLite database named `sales.db`.
- Uploaded files are processed by the Streamlit application and are not sent to an external analytics service by this codebase.
- Do not upload sensitive customer information unless the deployment environment and data-handling policies have been reviewed.
- For production use, add authentication, secrets management, access controls, backups, and a managed database where appropriate.

---

## 🧭 Roadmap

- [ ] Add authentication and role-based access control.
- [ ] Add configurable date-range and category filters.
- [ ] Add seasonality-aware forecasting models.
- [ ] Add inventory and stockout analysis.
- [ ] Add automated PDF and Excel reporting.
- [ ] Add database backup and cloud storage support.
- [ ] Add automated tests and continuous integration.

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

1. Fork the repository.
2. Create a feature branch:

   ```bash
   git checkout -b feature/your-feature-name
   ```

3. Commit your changes:

   ```bash
   git commit -m "Add your feature"
   ```

4. Push the branch:

   ```bash
   git push origin feature/your-feature-name
   ```

5. Open a pull request with a clear description of your changes.

---

## 📜 License

This project is licensed under the **MIT License**. See the repository license file for details.

---

<p align="center">
  <strong>Built with Python, Streamlit, and a focus on practical retail decision-making.</strong>
</p>

# ⚡ Retail Business Intelligence & Automation System

<p align="left">
  <img src="https://img.shields.io/badge/status-Production--Ready-brightgreen?style=flat-square" alt="Status" />
  <img src="https://img.shields.io/badge/platform-Streamlit%20%7C%20Python-blue?style=flat-square" alt="Platform" />
  <img src="https://img.shields.io/badge/version-1.0.0-orange?style=flat-square" alt="Version" />
  <img src="https://img.shields.io/badge/license-MIT-red?style=flat-square" alt="License" />
  <a href="YOUR_STREAMLIT_APP_LIVE_URL_HERE"><img src="https://img.shields.io/badge/Live--Demo-Streamlit--Cloud-00C48C?style=flat-square&logo=streamlit" alt="Live Demo" /></a>
</p>

An automated, end-to-end Business Intelligence and Predictive Analytics engine designed to digitize manual retail sales operations, automate ETL data cleaning, and generate actionable forecasting metrics.

---

## 📌 Executive Summary

### 🚨 Problem Statement
Traditional retail operations heavily rely on manual Excel reporting. This process is prone to human error, struggles with inconsistent date/numeric formats, suffers from duplicate records, and lacks real-time visualization or predictive inventory insights.

### 💡 Proposed Solution
An automated pipeline that ingests raw sales datasets (`.csv` / `.xlsx`), applies robust data validation rules using Pandas, stores normalized transactions in an embedded SQLite database, and presents real-time executive dashboards alongside a 30-day linear regression sales forecast.

---

## 🗺️ Project Structure

```text

│
├── app.py                   # Main Streamlit web app interface & dashboard UI
├── data_cleaning.py         # ETL pipeline: handles data validation, deduplication & SQLite ingestion
├── forecaster.py            # Machine Learning module for 30-day sales demand forecasting
├── dummy_dataset.py         # Script to generate sample datasets for ingestion testing
├── generate_test_data.py    # Script to generate dirty test batches (.csv & .xlsx)
├── raw_sales_sample.csv     # Sample seed dataset
├── requirements.txt         # Project dependencies and libraries
└── sales.db                 # Auto-generated SQLite database (created on first ingestion)

## 🚀 Key Features

- **Automated Ingestion & ETL Engine:** Automatically normalizes column schema, filters out invalid/negative amounts, handles mixed date formats, and strips duplicates.
- **Interactive Visualizations:** Built using Plotly, featuring custom dark themes, category revenue splits, and histogram distributions with clear black outlines.
- **Clean Data Export:** Live download button (`.csv`) for evaluators and managers to export the sanitized dataset instantly.
- **Predictive AI Sales Forecasting:** Integrated machine learning regression model predicting sales trends for proactive stock management.
- **Actionable Business Insights:** Automatically generated dynamic recommendations based on transaction performance.

---

## ⚙️ Local Setup & Installation

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME.git)
cd Bussiness
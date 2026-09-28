import os
import sqlite3
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

from forecaster import generate_sales_forecast
from data_cleaning import process_and_ingest_data

st.set_page_config(
    page_title="Retail Bussiness Intelligence & Automation",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

DB_PATH = "sales.db"
os.makedirs("database", exist_ok=True)

COLOR_PRIMARY = "#0F4C81"   
COLOR_SECONDARY = "#00B4D8" 
COLOR_ACCENT = "#FF6B6B"    
COLOR_PURPLE = "#7209B7"    

def load_data():
    if not os.path.exists(DB_PATH):
        return pd.DataFrame()
    conn = sqlite3.connect(DB_PATH)
    try:
        df = pd.read_sql("SELECT * FROM sales", conn)
    except Exception:
        df = pd.DataFrame()
    finally:
        conn.close()
    return df

st.title("⚡Business Intelligence & Automation System")
st.caption("Automated ETL Pipeline, Real-Time Analytics & Predictive AI for Retail Operations")
st.markdown("---")

st.sidebar.header("📥 Ingest Sales Batch")
uploaded_file = st.sidebar.file_uploader(
    "Upload Daily/Weekly Sales (.csv or .xlsx)", 
    type=["csv", "xlsx"],
    key="sales_file_uploader"
)

if uploaded_file is not None:
    file_identifier = f"{uploaded_file.name}_{uploaded_file.size}"
    
    if st.session_state.get("last_uploaded_file") != file_identifier:
        with st.spinner("⚡ Running Automated Pipeline..."):
            try:
                result = process_and_ingest_data(uploaded_file, DB_PATH)
                st.session_state["last_uploaded_file"] = file_identifier
                st.session_state["last_cleaned_df"] = result["cleaned_df"]
                st.session_state["ingestion_summary"] = result
                st.rerun() 
            except Exception as e:
                st.sidebar.error(f"Error processing file: {e}")
if "ingestion_summary" in st.session_state:
    res = st.session_state["ingestion_summary"]
    st.sidebar.success(f"✅ Auto-cleaned & Ingested **{res['cleaned_rows']}** valid records!")
    if res['dropped_rows'] > 0:
        st.sidebar.warning(f"🧹 Discarded **{res['dropped_rows']}** dirty/duplicate rows.")
    
    cleaned_df_export = st.session_state.get("last_cleaned_df")
    if cleaned_df_export is not None and not cleaned_df_export.empty:
        csv_bytes = cleaned_df_export.to_csv(index=False).encode('utf-8')
        st.sidebar.download_button(
            label="📥 Download Cleaned Data (.CSV)",
            data=csv_bytes,
            file_name="cleaned_sales_output.csv",
            mime="text/csv",
            use_container_width=True
        )

df = load_data()

if df.empty:
    st.info("👋 Welcome! Please upload a  test file  from the sidebar to initialize the system.")
else:
    df['date'] = pd.to_datetime(df['date'])
    st.markdown("### 📊 Business Overview")
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)

    total_revenue = df['total_amount'].sum()
    total_orders = len(df)
    avg_order_val = df['total_amount'].mean() if total_orders > 0 else 0
    unique_cust = df['customer_id'].nunique()

    kpi1.metric("Total Revenue", f"${total_revenue:,.2f}")
    kpi2.metric("Total Orders", f"{total_orders:,}")
    kpi3.metric("Avg Order Value", f"${avg_order_val:,.2f}")
    kpi4.metric("Unique Customers", f"{unique_cust:,}")

    st.markdown("---")
    tab1, tab2, tab3 = st.tabs(["📈 Executive Analytics", "💡 Actionable Insights", "🤖 AI Sales Forecast"])

    with tab1:
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("##### 📅 Monthly Revenue Trend")
            df_monthly = df.set_index('date').resample('ME')['total_amount'].sum().reset_index()
            fig_trend = px.line(
                df_monthly, x='date', y='total_amount', markers=True,
                labels={'total_amount': 'Revenue ($)', 'date': 'Month'}
            )
            fig_trend.update_traces(
                line_color=COLOR_PRIMARY, line_width=3.5, 
                marker=dict(size=8, color=COLOR_SECONDARY, line=dict(width=1.5, color='black'))
            )
            fig_trend.update_layout(template="plotly_white", margin=dict(l=20, r=20, t=30, b=20))
            st.plotly_chart(fig_trend, use_container_width=True)

        with c2:
            st.markdown("##### 💹 Revenue Distribution by Category")
            df_cat = df.groupby('category')['total_amount'].sum().reset_index()
            fig_pie = px.pie(
                df_cat, names='category', values='total_amount', hole=0.45,
                color_discrete_sequence=[COLOR_PRIMARY, COLOR_SECONDARY, COLOR_ACCENT, COLOR_PURPLE]
            )
            fig_pie.update_traces(textposition='inside', textinfo='percent+label', marker=dict(line=dict(color='#FFFFFF', width=2)))
            fig_pie.update_layout(template="plotly_white", margin=dict(l=20, r=20, t=30, b=20))
            st.plotly_chart(fig_pie, use_container_width=True)

        c3, c4 = st.columns(2)
        with c3:
            st.markdown("##### 🏆 Top Selling Products")
            top_p = df.groupby('product')['total_amount'].sum().nlargest(5).reset_index().sort_values('total_amount', ascending=True)
            fig_bar = px.bar(
                top_p, x='total_amount', y='product', orientation='h', text_auto='.2s',
                color_discrete_sequence=[COLOR_SECONDARY]
            )
            fig_bar.update_traces(marker_line_color='black', marker_line_width=1.2)
            fig_bar.update_layout(template="plotly_white", margin=dict(l=20, r=20, t=30, b=20), xaxis_title="Revenue ($)", yaxis_title="")
            st.plotly_chart(fig_bar, use_container_width=True)

        with c4:
            st.markdown("##### 👥 Customer Order Frequency Distribution")
            cust_freq = df.groupby('customer_id')['transaction_id'].count().reset_index()
            fig_hist = px.histogram(
                cust_freq, x='transaction_id', nbins=8,
                labels={'transaction_id': 'Orders per Customer'},
                color_discrete_sequence=[COLOR_ACCENT]
            )
            fig_hist.update_traces(
                marker_line_color='black',  
                marker_line_width=1.5
            )
            fig_hist.update_layout(template="plotly_white", margin=dict(l=20, r=20, t=30, b=20), yaxis_title="Customer Count")
            st.plotly_chart(fig_hist, use_container_width=True)

    with tab2:
        st.subheader("🎯 Automated Recommendations for Business Owner")
        top_cat = df.groupby('category')['total_amount'].sum().idxmax()
        top_cat_revenue = df.groupby('category')['total_amount'].sum().max()
        cat_pct = (top_cat_revenue / total_revenue) * 100 if total_revenue > 0 else 0

        st.success(f"""
        1. **Primary Revenue Engine ({top_cat}):**  
           The **{top_cat}** category is currently driving **{cat_pct:.1f}%** of total sales (${top_cat_revenue:,.2f}).  
           *Action:* Increase stock allocation for top items in {top_cat} to prevent stockout losses.

        2. **Order Value Optimization:**  
           The average order value stands at **${avg_order_val:.2f}**.  
           *Action:* Offer bundle discounts (e.g., "Spend ${avg_order_val*1.2:.0f} & Get 10% Off") to raise overall transaction values.

        3. **Data Quality Integrity:**  
           The automated pipeline successfully filtered out dirty entries (e.g. negative prices, missing dates).  
           *Action:* No manual Excel cleanup required — decision metrics are updated safely.
        """)

    with tab3:
        st.subheader("🤖 30-Day Sales Demand Forecast")
        forecast_df = generate_sales_forecast(df, forecast_days=30)
        
        if forecast_df is not None:
            fig_fc = go.Figure()

            df_daily = df.groupby('date')['total_amount'].sum().reset_index()
            fig_fc.add_trace(go.Scatter(
                x=df_daily['date'], y=df_daily['total_amount'],
                name='Historical Sales', line=dict(color=COLOR_PRIMARY, width=3)
            ))
            fig_fc.add_trace(go.Scatter(
                x=forecast_df['date'], y=forecast_df['predicted_sales'],
                name='30-Day Predictive Trend', line=dict(color=COLOR_ACCENT, width=3, dash='dash')
            ))

            fig_fc.update_layout(
                template="plotly_white",
                xaxis_title="Date", yaxis_title="Revenue ($)",
                hovermode="x unified",
                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
            )
            st.plotly_chart(fig_fc, use_container_width=True)
        else:
            st.warning("Needs at least 5 days of data to compute regression forecast.")
from pathlib import Path

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Qahwa Corner Sales",
    page_icon="☕",
    layout="wide"
)

st.title("☕ Qahwa Corner Sales Dashboard")
st.caption("Branch sales analysis | January–June 2026")

@st.cache_data
def read_sales():
    csv_path = Path(__file__).parent / "cafe_sales.csv"
    return pd.read_csv(csv_path)

data = read_sales()

branch = st.selectbox(
    "Choose a branch",
    sorted(data["branch"].unique())
)

filtered_data = data.loc[data["branch"] == branch]

st.metric(
    "Total Revenue (SAR)",
    f"{filtered_data['total_sar'].sum():,.0f}"
)

revenue_by_product = (
    filtered_data.groupby("product")["total_sar"]
    .sum()
    .rename("Revenue (SAR)")
)

st.subheader("Product Revenue")
st.bar_chart(revenue_by_product)

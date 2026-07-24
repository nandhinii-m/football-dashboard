import streamlit as st

st.set_page_config(
    page_title="Football Analytics Dashboard",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="auto"
)

st.title("Football Analytics Dashboard")


st.write("""
This dashboard allows you to analyze player and club statistics from the **2025–2026 season across the top five European leagues**.
""")
st.divider()

st.caption("Dataset : Kaggle")
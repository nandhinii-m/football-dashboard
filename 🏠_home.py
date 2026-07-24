import streamlit as st

st.set_page_config(
    page_title="Football Analytics Dashboard",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="auto"
)

st.title("⚽ Football Analytics Dashboard")

st.divider()

st.write("""
This dashboard allows you to analyze player and club statistics from the **2025–2026 season across Europe's Top Five Leagues**.
""")

st.header("Features")

st.markdown("""
📊 **League Analysis** -
Discover the top scorers, assist providers,
and highest scoring clubs in each league.

⭐ **Player Search** - 
Search any player and view detailed statistics
tailored to their position.

👥 **Player Comparison** - 
Compare two players side by side and
see who comes out on top.
""")

st.divider()

st.caption("Dataset : Kaggle")
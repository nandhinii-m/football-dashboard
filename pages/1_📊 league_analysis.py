import streamlit as st
import plotly.express as px
from utils import load_data

df = load_data()

def bar_chart(data, x_col, y_col, title):
    fig = px.bar(data, x=x_col, y=y_col, title=title)
    fig.update_xaxes(title_text="", tickangle=-45, automargin=True)
    fig.update_yaxes(title_text="")
    st.plotly_chart(fig, use_container_width=True)

st.title("📊 League Analysis")
st.write("Explore statistics from Europe's top five leagues.")
st.divider()

league = st.selectbox(
    "Select League",
    sorted(df["Comp"].unique()),
    index=None,
    placeholder="Choose a league"
)

if league:
    filtered_df = df[df["Comp"] == league]

    st.subheader(league)

    col1, col2, col3 = st.columns(3)
    col1.metric("Players", len(filtered_df))
    col2.metric("Clubs", filtered_df["Squad"].nunique())
    col3.metric("Goals", int(filtered_df["Gls"].sum()))

    st.divider()

    # Top Scorers

    st.header("Top Scorers")
    top_scorers = filtered_df.sort_values(by="Gls", ascending=False).head(10)
    bar_chart(top_scorers, "Player", "Gls", "Top 10 Goal Scorers")

    # Top Assists

    st.header("Top Assists")
    top_assists = filtered_df.sort_values(by="Ast", ascending=False).head(10)
    bar_chart(top_assists, "Player", "Ast", "Top 10 Assist Providers")

    # Club Goals

    st.header("Top Goal Scoring Clubs")
    club_goals = (
        filtered_df.groupby("Squad")["Gls"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )
    bar_chart(club_goals, "Squad", "Gls", "Top 10 Goal Scoring Clubs")


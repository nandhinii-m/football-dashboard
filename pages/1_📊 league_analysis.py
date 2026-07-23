import streamlit as st
import plotly.express as px
from utils import load_data  # Standard, clean import!

df = load_data()

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

    with col1:
        st.metric("Players", len(filtered_df))

    with col2:
        st.metric("Clubs", filtered_df["Squad"].nunique())

    with col3:
        st.metric("Goals", int(filtered_df["Gls"].sum()))


# --------------------------------
# Top Scorers
# --------------------------------

    st.header("Top Scorers")

    top_scorers = filtered_df.sort_values(
        by="Gls",
        ascending=False
    ).head(10)

    fig_scorers = px.bar(
        top_scorers,
        x="Player",
        y="Gls",
        title="Top 10 Goal Scorers"
    )

    fig_scorers.update_xaxes(
        title_text="",
        tickangle=-45,
        automargin=True
    )

    fig_scorers.update_yaxes(title_text="")

    st.plotly_chart(fig_scorers, use_container_width=True)

# --------------------------------
# Top Assists
# --------------------------------

    st.header("Top Assists")

    top_assists = filtered_df.sort_values(
        by="Ast",
        ascending=False
    ).head(10)

    fig_assists = px.bar(
        top_assists,
        x="Player",
        y="Ast",
        title="Top 10 Assist Providers"
    )

    fig_assists.update_xaxes(
        title_text="",
        tickangle=-45,
        automargin=True
    )

    fig_assists.update_yaxes(title_text="")

    st.plotly_chart(fig_assists, use_container_width=True)

# --------------------------------
# Club Goals
# --------------------------------

    st.header("Top Goal Scoring Clubs")

    club_goals = (
        filtered_df
        .groupby("Squad")["Gls"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig_clubs = px.bar(
        club_goals,
        x="Squad",
        y="Gls",
        title="Top 10 Goal Scoring Clubs"
    )

    fig_clubs.update_xaxes(
        title_text="",
        tickangle=-45,
        automargin=True
    )

    fig_clubs.update_yaxes(title_text="")

    st.plotly_chart(fig_clubs, use_container_width=True)



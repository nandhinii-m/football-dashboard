import streamlit as st
from utils import load_data

df = load_data()

st.title("⭐ Player Search")

st.write("Search any player from Europe's top five leagues to view their season statistics.")

st.divider()

player_name = st.selectbox(
    "Search Player",
    sorted(df["Player"].unique()),
    index=None,
    placeholder="Choose a player"
)

if player_name:

    player = df[df["Player"] == player_name].iloc[0]

    st.header(player["Player"])

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.write("**Club**")
        st.write(player["Squad"])

    with col2:
        st.write("**League**")
        st.write(player["Comp"])

    with col3:
        st.write("**Position**")
        st.write(player["Pos"])

    with col4:
        st.write("**Age**")
        st.write(str(int(player["Age"])))

    st.divider()

    if "GK" in str(player["Pos"]):

        st.subheader("Goalkeeping Stats")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Minutes", f"{int(player['Min']):,}")

        with col2:
            st.metric("Saves", f"{int(player['Saves']):,}")

        with col3:
            save_pct = player["Save%"]

            if isinstance(save_pct, (int, float)):
                save_pct = f"{save_pct:.1f}%"

            st.metric("Save %", save_pct)

        col4, col5, col6 = st.columns(3)

        with col4:
            st.metric("Goals Against", f"{int(player['GA']):,}")

        with col5:
            st.metric("Clean Sheets", f"{int(player['CS']):,}")

        with col6:
            st.metric("Penalty Saves", f"{int(player['PKsv']):,}")

    else:

        st.subheader("Player Stats")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Goals", f"{int(player['Gls']):,}")

        with col2:
            st.metric("Assists", f"{int(player['Ast']):,}")

        with col3:
            st.metric("Minutes", f"{int(player['Min']):,}")

        col4, col5, col6 = st.columns(3)

        with col4:
            st.metric("Shots", f"{int(player['Sh']):,}")

        with col5:
            st.metric("Shots on Target", f"{int(player['SoT']):,}")

        with col6:
            st.metric("Yellow Cards", f"{int(player['CrdY']):,}")

import streamlit as st
import pandas as pd
from utils import load_data

df = load_data()

st.title("👥 Player Comparison")

st.write(
    "Compare two players side by side."
)

st.divider()

players = sorted(df["Player"].unique())

col1, col2 = st.columns(2)

with col1:
    player1_name = st.selectbox(
        "Player 1",
        players,
        index=None,
        placeholder="Choose first player"
    )

with col2:
    player2_name = st.selectbox(
        "Player 2",
        players,
        index=None,
        placeholder="Choose second player"
    )

if player1_name and player2_name:

    player1 = df[df["Player"] == player1_name].iloc[0]
    player2 = df[df["Player"] == player2_name].iloc[0]

    st.divider()

    info1, info2 = st.columns(2)

    with info1:

        st.subheader(player1["Player"])

        st.markdown(f"**League:** {player1['Comp']} &nbsp;&nbsp;&nbsp; **Club:** {player1['Squad']}")

        c1, c2 = st.columns(2)

        with c1:
            st.metric(
                "Position",
                player1["Pos"]
            )

        with c2:
            st.metric(
                "Age",
                int(player1["Age"])
            )

    with info2:

        st.subheader(player2["Player"])

        st.markdown(f"**League:** {player2['Comp']} &nbsp;&nbsp;&nbsp; **Club:** {player2['Squad']}")

        c3, c4 = st.columns(2)

        with c3:
            st.metric(
                "Position",
                player2["Pos"]
            )

        with c4:
            st.metric(
                "Age",
                int(player2["Age"])
            )

    st.divider()

    st.subheader("Comparison")

    player1_is_gk = "GK" in str(player1["Pos"])
    player2_is_gk = "GK" in str(player2["Pos"])

    if player1_is_gk and player2_is_gk:

        comparison = {
            "Stat": [
                "Minutes",
                "Saves",
                "Save %",
                "Goals Against",
                "Clean Sheets",
                "Penalty Saves"
            ],

            player1_name: [
                int(player1["Min"]),
                int(player1["Saves"]),
                player1["Save%"],
                int(player1["GA"]),
                int(player1["CS"]),
                int(player1["PKsv"])
            ],

            player2_name: [
                int(player2["Min"]),
                int(player2["Saves"]),
                player2["Save%"],
                int(player2["GA"]),
                int(player2["CS"]),
                int(player2["PKsv"])
            ]
        }

    else:

        comparison = {
            "Stat": [
                "Goals",
                "Assists",
                "Minutes",
                "Shots",
                "Shots on Target",
                "Yellow Cards"
            ],

            player1_name: [
                int(player1["Gls"]),
                int(player1["Ast"]),
                int(player1["Min"]),
                int(player1["Sh"]),
                int(player1["SoT"]),
                int(player1["CrdY"])
            ],

            player2_name: [
                int(player2["Gls"]),
                int(player2["Ast"]),
                int(player2["Min"]),
                int(player2["Sh"]),
                int(player2["SoT"]),
                int(player2["CrdY"])
            ]
        }

    comparison_df = pd.DataFrame(comparison)

    st.dataframe(
        comparison_df,
        use_container_width=True,
        hide_index=True
    )

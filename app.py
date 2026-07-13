import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/raw/players_data_light-2025_2026.csv")

# ----------------------------
# Top Scorers
# ----------------------------

top_scorers=df.sort_values(by="Gls",ascending=False).head(10)

plt.figure(figsize=(10,6))
plt.bar(top_scorers["Player"],top_scorers["Gls"])

plt.title("Top 10 goal scoring players")
plt.xlabel("Player Name")
plt.ylabel("No. of goals scored")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("images/top_scorers.png")

#plt.show()

# ----------------------------
# Top Assists
# ----------------------------

top_assists=df.sort_values(by="Ast",ascending=False).head(10)

plt.figure(figsize=(10,6))
plt.bar(top_assists["Player"],top_assists["Ast"])

plt.title("Top 10 assist providers")
plt.xlabel("Player Name")
plt.ylabel("No. of assists")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("images/top_assists.png")

#plt.show()

# ----------------------------
# Goals by Club
# ----------------------------

club_goals=df.groupby("Squad")["Gls"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,6))
plt.bar(club_goals.index,club_goals.values)

plt.title("Top 10 goal scoring clubs")
plt.xlabel("Club Name")
plt.ylabel("No. of goals")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("images/club_goals.png")

#plt.show()

# ----------------------------
# Position Distribution
# ----------------------------

position_counts = df["Pos"].value_counts()

plt.figure(figsize=(10,6))
plt.bar(position_counts.index,position_counts.values)

plt.title("Position distribution")
plt.xlabel("Playing position")
plt.ylabel("No. of players")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("images/position_counts.png")

#plt.show()

# ----------------------------
# Oldest Players
# ----------------------------

oldest_players=df.sort_values(by="Age",ascending=False).head(10)

plt.figure(figsize=(10,6))
plt.bar(oldest_players["Player"],oldest_players["Age"])

plt.title("Top 10 oldest playing footballers")
plt.xlabel("Player name")
plt.ylabel("Age")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("images/oldest_players.png")

#plt.show()

# ----------------------------
# Youngest Players
# ----------------------------

youngest_players=df.sort_values(by="Age",ascending=True).head(10)

plt.figure(figsize=(10,6))
plt.bar(youngest_players["Player"],youngest_players["Age"])

plt.title("Top 10 youngest playing footballers")
plt.xlabel("Player name")
plt.ylabel("Age")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("images/youngest_players.png")

plt.show()
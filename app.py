import pandas as pd

df = pd.read_csv("data/raw/players_data_light-2025_2026.csv")



club_count=df.groupby("Squad").size()
clubs_20=club_count[club_count>=20].index
avg_age=df[df["Squad"].isin(clubs_20)].groupby("Squad")["Age"].mean().sort_values(ascending=False)
print(avg_age)




import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.bar(old_players.index, old_players.values)

plt.title("Top 10 oldest playing footballers")
plt.xlabel("Players")
plt.ylabel("Age")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()
import pandas as pd
import matplotlib.pyplot as plt
import os

# Laadi CSV
df = pd.read_csv("data/kohtulahendid.csv", sep=";")

# Muuda "Lahendi kp" kuupäevaks ja eralda aastad
df["Lahendi kp"] = pd.to_datetime(df["Lahendi kp"], format="%d.%m.%Y", errors="coerce")
df["Aasta"] = df["Lahendi kp"].dt.year

# Arvuta lahendite arv aastate kaupa
count_by_year = df["Aasta"].value_counts().sort_index()

# Loo graafik
plt.figure(figsize=(10, 5))
count_by_year.plot(kind="bar", color="skyblue")
plt.xlabel("Aasta")
plt.ylabel("Kohtulahendite arv")
plt.title("Kohtulahendite arv aastate lõikes")
plt.xticks(rotation=45)

# Salvesta pilt `docs` kausta
os.makedirs("docs", exist_ok=True)
plt.savefig("docs/chart.png")
print("Graafik loodud: docs/chart.png")

import pandas as pd
import matplotlib.pyplot as plt

# Laadi andmed
df = pd.read_csv("data/kohtulahendid.csv", delimiter=";")

# Muuda kuupäevad datetime formaati
df["Lahendi kp"] = pd.to_datetime(df["Lahendi kp"], dayfirst=True)

# Loenda kohtulahendite arv kuude kaupa
df["Month"] = df["Lahendi kp"].dt.to_period("M")
cases_per_month = df.groupby("Month").size()

# Joonista graafik
plt.figure(figsize=(10, 5))
cases_per_month.plot(kind="bar")
plt.xlabel("Kuud")
plt.ylabel("Kohtulahendite arv")
plt.title("Kohtulahendite arv ajas")
plt.xticks(rotation=45)
plt.tight_layout()

# Salvesta pilt
plt.savefig("docs/chart.png")
print("Graafik genereeritud: docs/chart.png")


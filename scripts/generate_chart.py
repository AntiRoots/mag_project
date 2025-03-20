import pandas as pd
import matplotlib.pyplot as plt
import os

# Laadi andmed
df = pd.read_csv("data/kohtulahendid.csv", delimiter=";", encoding="utf-8")

# Eemalda tühjad kuupäeva lahtrid enne teisendamist
df = df[df["Lahendi kp"].notna()]

# Muuda kuupäevad datetime formaati
df["Lahendi kp"] = pd.to_datetime(df["Lahendi kp"], dayfirst=True, errors='coerce')

# Eemalda read, kus kuupäevad ei õnnestunud teisendada
df = df.dropna(subset=["Lahendi kp"])

# Loenda kohtulahendite arv kuude kaupa
df["Month"] = df["Lahendi kp"].dt.to_period("M")
cases_per_month = df.groupby("Month").size()

# Joonista graafik
plt.figure(figsize=(10, 5))
cases_per_month.plot(kind="bar", color="skyblue")  # Lisatud värv paremaks nähtavuseks
plt.xlabel("Kuud")
plt.ylabel("Kohtulahendite arv")
plt.title("Kohtulahendite arv ajas")
plt.xticks(rotation=45)
plt.tight_layout()

# Salvesta pilt
plt.savefig("docs/chart.png", dpi=300)  # Lisatud kõrgem DPI, et pilt oleks kvaliteetsem
print("Graafik genereeritud: docs/chart.png")

# Salvesta pilt
chart_path = "docs/chart.png"
plt.savefig(chart_path, dpi=300)
print(f"Graafik genereeritud: {chart_path}")

# Kontrolli, kas fail on olemas
if os.path.exists(chart_path):
    print("✅ Graafik on edukalt loodud!")
else:
    print("❌ Viga: graafikut ei leitud pärast genereerimist!")

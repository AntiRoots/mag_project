import pandas as pd
import matplotlib.pyplot as plt
import os

# Määra kaustad
DATA_PATH = "data/kohtulahendid.csv"
OUTPUT_DIR = "docs"  # GitHub Pages loeb ainult `docs/` kaustast
CHART_PATH = os.path.join(OUTPUT_DIR, "chart.png")

# Loo väljundi kaust, kui see puudub
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Kontrolli, kas CSV fail on olemas
if not os.path.exists(DATA_PATH):
    print(f"❌ Viga: Andmefaili ei leitud ({DATA_PATH})!")
    exit(1)

# Laadi andmed
df = pd.read_csv(DATA_PATH, delimiter=";", encoding="utf-8")

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
cases_per_month.plot(kind="bar", color="skyblue")
plt.xlabel("Kuud")
plt.ylabel("Kohtulahendite arv")
plt.title("Kohtulahendite arv ajas")
plt.xticks(rotation=45)
plt.tight_layout()

# Salvesta pilt õigesse kausta
plt.savefig(CHART_PATH, dpi=300)
plt.close()  # Vabastab mälu

print(f"✅ Graafik genereeritud: {CHART_PATH}")

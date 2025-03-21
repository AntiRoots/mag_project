import pandas as pd
import matplotlib.pyplot as plt
import os

# Määra kaustad
DATA_PATH = "data/kohtulahendid.csv"
OUTPUT_DIR = "docs"
CHART_PATH = os.path.join(OUTPUT_DIR, "chart.png")

# Loo väljundi kaust, kui see puudub
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Laadi andmed, eemaldades võimalikud BOM-märgid
with open(DATA_PATH, "r", encoding="utf-8-sig") as file:
    df = pd.read_csv(file, delimiter=";", encoding="utf-8")

# Kontrolli, kas vajalik veerg on olemas
if "Lahendi kp" not in df.columns:
    raise ValueError("❌ CSV failist ei leitud veergu 'Lahendi kp'!")

# Eemalda tühjad või vigased kuupäevad
df = df[df["Lahendi kp"].notna()]

# Proovi teisendada kuupäevad ja eemalda vead
df["Lahendi kp"] = pd.to_datetime(df["Lahendi kp"], format="%d.%m.%Y", errors="coerce")
df = df.dropna(subset=["Lahendi kp"])  # Eemalda read, kus kuupäevad ei õnnestunud

# Loenda kohtulahendite arv kuude kaupa
df["Month"] = df["Lahendi kp"].dt.to_period("M")
cases_per_month = df.groupby("Month").size()

# Kontrolli, kas on piisavalt andmeid graafiku loomiseks
if cases_per_month.empty:
    print("❌ Ei leitud piisavalt kehtivaid andmeid graafiku loomiseks!")
else:
    # Joonista graafik
    plt.figure(figsize=(10, 5))
    cases_per_month.plot(kind="bar", color="skyblue")
    plt.xlabel("Kuud")
    plt.ylabel("Kohtulahendite arv")
    plt.title("Kohtulahendite arv ajas")
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Salvesta pilt
    plt.savefig(CHART_PATH, dpi=300)
    print(f"✅ Graafik genereeritud: {CHART_PATH}")

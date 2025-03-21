import pandas as pd
import matplotlib.pyplot as plt
import os

# Logi käivituse asukoht
print(f"📂 Töötan kaustas: {os.getcwd()}")

# Määra kaustad
DATA_PATH = "data/kohtulahendid.csv"
OUTPUT_DIR = "docs"  # Graafiku väljundkaust
CHART_PATH = os.path.join(OUTPUT_DIR, "chart.png")

# Kontrolli, kas andmefail eksisteerib
if not os.path.exists(DATA_PATH):
    print(f"❌ Viga: Andmefaili ei leitud ({DATA_PATH})!")
    exit(1)
else:
    print(f"✅ Andmefail leitud: {DATA_PATH}")

# Loo väljundi kaust, kui see puudub
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Laadi andmed
df = pd.read_csv(DATA_PATH, delimiter=";", encoding="utf-8")
print(f"📊 Andmed laetud, ridasid: {len(df)}")

# Eemalda tühjad kuupäeva lahtrid enne teisendamist
df = df[df["Lahendi kp"].notna()]

# Muuda kuupäevad datetime formaati
df["Lahendi kp"] = pd.to_datetime(df["Lahendi kp"], dayfirst=True, errors='coerce')

# Eemalda read, kus kuupäevad ei õnnestunud teisendada
df = df.dropna(subset=["Lahendi kp"])

# Kontrolli, kas on üldse andmeid, mida joonistada
if df.empty:
    print("⚠️  Viga: Andmefail on tühi või ei sisalda sobivaid kuupäevi!")
    exit(1)

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

# Salvesta pilt
plt.savefig(CHART_PATH, dpi=300)
plt.close()  # Vabastab mälu
print(f"✅ Graafik genereeritud: {CHART_PATH}")

# Kontrolli, kas graafik loodi
if os.path.exists(CHART_PATH):
    print(f"✅ Graafik on olemas: {CHART_PATH}")
else:
    print("❌ Viga: Graafiku faili EI looda!")
    exit(1)

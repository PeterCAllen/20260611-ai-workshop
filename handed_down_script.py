import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

INPUT = Path("data/messy_plate_reader.csv")
OUTPUT_DIR = Path("figures")
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_csv(INPUT, skiprows=16)
df = df.dropna(subset=["Sample_ID", "Fluorescence"])
df["Fluorescence"] = pd.to_numeric(df["Fluorescence"], errors="coerce")

blank = df[df["Sample_ID"] == "BLANK"]["Fluorescence"].mean()
df["Fluorescence_corrected"] = df["Fluorescence"] - blank

stds = df[df["Sample_ID"].str.startswith("STD_")].copy()
stds["Concentration_ng_mL"] = pd.to_numeric(stds["Concentration_ng_mL"], errors="coerce")
m, b = np.polyfit(stds["Fluorescence_corrected"], stds["Concentration_ng_mL"], 1)

samples = df[df["Sample_ID"].str.startswith("SAMPLE_")].copy()
samples["Concentration_ng_mL"] = m * samples["Fluorescence_corrected"] + b

agg = samples.groupby("Sample_ID")["Concentration_ng_mL"].agg(["mean", "std"]).reset_index()

fig, ax = plt.subplots(figsize=(6, 4))
ax.bar(agg["Sample_ID"], agg["mean"], yerr=agg["std"], capsize=4, color="#5fb8ff", edgecolor="#0a1628")
ax.set_ylabel("IL-6 concentration (ng/mL)")
ax.set_title("Patient sample IL-6 quantification")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "il6_quant.png", dpi=150)
print(agg.to_string(index=False))

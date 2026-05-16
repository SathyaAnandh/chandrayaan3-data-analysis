import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file_path = "data/ch3_ils_nop_raw_20230824t125708960_d_rawcount.csv"
df = pd.read_csv(file_path)

print(df.head())
print(df.tail())
print(df.columns)
print(df.info())
print(df.describe())
print(df.shape)
print(df.isnull())
print(df.isnull().sum())
print(df.notnull())
print(df.fillna(0))
print(df.dropna())
print(df.duplicated())
print(df.drop_duplicates())


# Downsample data for cleaner plotting
sampled_df = df.iloc[::100].copy()

# Center seismic signals around mean
x_centered = sampled_df["X-Axis Coarse Data"] - sampled_df["X-Axis Coarse Data"].mean()

y_centered = sampled_df["Y-Axis Coarse Data"] - sampled_df["Y-Axis Coarse Data"].mean()

z_centered = sampled_df["Z-Axis Coarse Data"] - sampled_df["Z-Axis Coarse Data"].mean()

# Apply smoothing
sampled_df["X_Smoothed"] = x_centered.rolling(window=10).mean()

sampled_df["Y_Smoothed"] = y_centered.rolling(window=10).mean()

sampled_df["Z_Smoothed"] = z_centered.rolling(window=10).mean()

# -----------------------------
# Seismic Visualization
# -----------------------------

plt.figure(figsize=(12,6))

plt.plot(sampled_df["Time"], sampled_df["X_Smoothed"], label="X-Axis")

plt.plot(sampled_df["Time"], sampled_df["Y_Smoothed"], label="Y-Axis")

plt.plot(sampled_df["Time"], sampled_df["Z_Smoothed"], label="Z-Axis")

plt.xlabel("Time")
plt.ylabel("Centered & Smoothed Seismic Data")

plt.title("Chandrayaan-3 ILSA Seismic Activity")

plt.legend()

plt.grid(True)

plt.xticks(sampled_df["Time"][::20], rotation=45)

plt.tight_layout()

plt.savefig("outputs/graphs/final_seismic_analysis.png")

plt.show()

# -----------------------------
# Temperature Visualization
# -----------------------------

plt.figure(figsize=(12,6))

plt.plot(sampled_df["Time"], sampled_df["xTemp"], label="X Temp")

plt.plot(sampled_df["Time"], sampled_df["yTemp"], label="Y Temp")

plt.plot(sampled_df["Time"], sampled_df["zTemp"], label="Z Temp")

plt.xlabel("Time")
plt.ylabel("Temperature (degC)")

plt.title("Chandrayaan-3 ILSA Temperature Variation")

plt.legend()

plt.grid(True)

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("outputs/graphs/temperature_variation.png")

plt.show()

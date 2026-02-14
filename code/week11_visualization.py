import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Ensure the output directory exists
output_dir = "../En-en/fig"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 1. Load Data
# ------------
df = pd.read_csv("week10_concrete_data.csv")

# Set a nice theme
sns.set_theme(style="whitegrid")

# 2. Histogram (Distribution of Strength)
# ---------------------------------------
plt.figure(figsize=(8, 6))
# Histogram with a Kernel Density Estimate (KDE) line
sns.histplot(data=df, x="Compressive_Strength_MPa", kde=True, bins=20, color="skyblue")
plt.title("Distribution of Concrete Strength")
plt.xlabel("Compressive Strength (MPa)")
plt.ylabel("Frequency")
plt.savefig(f"{output_dir}/week11_hist.png", dpi=300)
print("Saved: week11_hist.png")

# 3. Scatter Plot (Correlation: Weight vs Load)
# ---------------------------------------------
plt.figure(figsize=(8, 6))
# Does heavier concrete carry more load?
sns.scatterplot(data=df, x="Weight_kg", y="Max_Load_kN", hue="Cure_Time_Days", palette="deep")
plt.title("Correlation: Sample Weight vs. Max Load")
plt.savefig(f"{output_dir}/week11_scatter.png", dpi=300)
print("Saved: week11_scatter.png")

# 4. Box Plot (Comparison by Category)
# ------------------------------------
plt.figure(figsize=(8, 6))
# Compare strength across different cement types
sns.boxplot(data=df, x="Cement_Type", y="Compressive_Strength_MPa", palette="Set2")
plt.title("Strength Comparison by Cement Type")
plt.savefig(f"{output_dir}/week11_boxplot.png", dpi=300)
print("Saved: week11_boxplot.png")

# 5. Bar Plot (Average Strength by Cure Time)
# -------------------------------------------
plt.figure(figsize=(8, 6))
sns.barplot(data=df, x="Cure_Time_Days", y="Compressive_Strength_MPa", errorbar="sd", capsize=.1)
plt.title("Strength Gain over Time (Mean + Std Dev)")
plt.savefig(f"{output_dir}/week11_barplot.png", dpi=300)
print("Saved: week11_barplot.png")

# 6. Subplots (Engineering Dashboard)
# -----------------------------------
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Plot A: Hist
sns.histplot(data=df, x="Compressive_Strength_MPa", kde=True, ax=axs[0, 0], color="green")
axs[0, 0].set_title("Strength Distribution")

# Plot B: Scatter
sns.scatterplot(data=df, x="Diameter_mm", y="Max_Load_kN", ax=axs[0, 1], color="red")
axs[0, 1].set_title("Diameter vs Load")

# Plot C: Box
sns.boxplot(data=df, x="Cure_Time_Days", y="Compressive_Strength_MPa", ax=axs[1, 0])
axs[1, 0].set_title("Cure Time Effect")

# Plot D: Violin (Advanced Boxplot)
sns.violinplot(data=df, x="Technician", y="Compressive_Strength_MPa", ax=axs[1, 1])
axs[1, 1].set_title("Technician Consistency")

plt.tight_layout()
plt.savefig(f"{output_dir}/week11_dashboard.png", dpi=300)
print("Saved: week11_dashboard.png")

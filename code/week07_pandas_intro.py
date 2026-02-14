import pandas as pd

# 1. Creating a DataFrame (Table)
# -------------------------------
# We can create it from a Dictionary
data = {
    "Material": ["Concrete", "Steel", "Wood"],
    "Density_kg_m3": [2400, 7850, 600],
    "Elastic_Modulus_GPa": [30, 200, 11]
}

df = pd.DataFrame(data)
print("--- Material Table ---")
print(df)

# 2. Accessing Data
# -----------------
print("\n--- Column Access ---")
print(df["Density_kg_m3"])

print("\n--- Row Access (iloc) ---")
print("First Row (Concrete):")
print(df.iloc[0])

# 3. Simple Stats
# ---------------
print("\n--- Statistics ---")
print(df.describe())

# 4. Filtering (Conditionals)
# ---------------------------
# Find materials with Density > 1000
heavy_materials = df[df["Density_kg_m3"] > 1000]
print("\n--- Materials Heavy > 1000 kg/m3 ---")
print(heavy_materials)

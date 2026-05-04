# Pandas: loc/iloc, boolean filter, groupby
# -----------------------------------------
import pandas as pd

# 1. Build a small dataset
# ------------------------
data = {
    "id":          ["S1", "S2", "S3", "S4", "S5", "S6"],
    "cement_type": ["CEM I", "CEM I", "CEM II", "CEM II", "CEM III", "CEM III"],
    "cure_days":   [28, 28, 28, 7, 28, 7],
    "strength":    [42.5, 41.0, 36.0, 21.0, 50.0, 28.5],   # MPa
}
df = pd.DataFrame(data).set_index("id")

# 2. iloc vs loc
# --------------
print("iloc[0]      :", df.iloc[0].to_dict())     # first row positionally
print("loc['S3']    :", df.loc["S3"].to_dict())   # row labelled S3

# 3. Boolean filter
# -----------------
strong_28d = df[(df["cure_days"] == 28) & (df["strength"] > 35)]
print("\n28-day samples above 35 MPa:")
print(strong_28d)

# 4. Groupby aggregation
# ----------------------
mean_by_type = df.groupby("cement_type")["strength"].mean()
print("\nMean strength per cement type:")
print(mean_by_type)

# 5. Apply a custom function column-wise
# --------------------------------------
df["category"] = df["strength"].apply(
    lambda s: "high" if s >= 40 else ("medium" if s >= 25 else "low")
)
print("\nWith category column:")
print(df)

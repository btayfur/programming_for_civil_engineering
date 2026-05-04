# Engineering report formatting with f-strings
# ---------------------------------------------
# Aligned columns, engineering precision, percentage,
# scientific notation, and zero-padding -- all in one go.

YIELD = 250.0   # MPa

members = [
    ("B1", 180.5),
    ("B2", 244.7),
    ("B3", 305.0),     # over yield
    ("B4",  92.3),
]

# 1. Header with alignment
# ------------------------
print(f"{'ID':<5} {'Stress [MPa]':>14} {'sigma/Fy':>10} {'Verdict':>10}")
print("-" * 45)

# 2. Rows with mixed precision and alignment
# ------------------------------------------
for mid, sigma in members:
    ratio    = sigma / YIELD
    verdict  = "OK" if sigma <= YIELD else "FAIL"
    print(f"{mid:<5} {sigma:>14.2f} {ratio:>10.1%} {verdict:>10}")

# 3. Scientific notation and thousands separator
# ----------------------------------------------
E = 210_000_000_000     # Pa (Young's modulus of steel)
print(f"\nE = {E:.3e} Pa  ({E:,} Pa with thousands separator)")

# 4. Zero padding for IDs
# -----------------------
for i in range(1, 4):
    print(f"sample_{i:03d}.csv")

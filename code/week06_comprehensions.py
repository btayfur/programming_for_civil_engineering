# Comprehensions and Sets in Engineering Context
# -----------------------------------------------
# Filtering structural elements, deduplicating node lists,
# and building stress maps in one line each.

# 1. List of beam dictionaries
# ----------------------------
beams = [
    {"id": "B1", "length": 5.0, "stress": 180},
    {"id": "B2", "length": 6.0, "stress": 250},  # at yield
    {"id": "B3", "length": 4.5, "stress": 120},
    {"id": "B4", "length": 7.0, "stress": 310},  # over yield
    {"id": "B5", "length": 5.5, "stress":  90},
]

YIELD_STRESS = 250  # MPa (steel)

# 2. List comprehension: extract failing IDs
# ------------------------------------------
failing = [b["id"] for b in beams if b["stress"] > YIELD_STRESS]
print(f"Failing beams: {failing}")             # ['B4']

# 3. Dict comprehension: id -> length squared
# -------------------------------------------
length_sq = {b["id"]: b["length"]**2 for b in beams}
print(f"Length-squared map: {length_sq}")

# 4. Set comprehension: unique stress levels (rounded)
# ----------------------------------------------------
unique_stress = {round(b["stress"], -1) for b in beams}
print(f"Distinct stress bins: {sorted(unique_stress)}")

# 5. Set operations on node IDs from two analyses
# -----------------------------------------------
analysis_A = {"N1", "N2", "N3", "N4"}
analysis_B = {"N3", "N4", "N5", "N6"}
print(f"Common nodes (& both): {analysis_A & analysis_B}")
print(f"Only in A   (- diff):  {analysis_A - analysis_B}")
print(f"All nodes   (|): {sorted(analysis_A | analysis_B)}")

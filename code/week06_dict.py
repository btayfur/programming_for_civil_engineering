# Python Dictionaries
# -------------------
# Dictionaries store data in Key-Value pairs.
# Engineering Use: Storing properties of defined materials or sections.
# Unlike lists, data is accessed by "Name" (Key), not index.

# 1. Defining a Material Database
# -------------------------------
concrete_C30 = {
    "type": "Concrete",
    "grade": "C30",
    "fck": 30.0,      # MPa
    "E": 33000.0,     # MPa (Elastic Modulus)
    "gamma": 25.0,    # kN/m3 (Unit Weight)
    "is_ductile": False
}

steel_S420 = {
    "type": "Steel",
    "grade": "S420",
    "fy": 420.0,       # MPa
    "E": 200000.0,     # MPa
    "gamma": 78.5,     # kN/m3
    "is_ductile": True
}

# 2. Accessing Data
# -----------------
print(f"Analyzing {concrete_C30['type']} {concrete_C30['grade']}...")
print(f"Characteristic Strength: {concrete_C30['fck']} MPa")

# 3. Modifying Data
# -----------------
# Updating a property (e.g. after lab test)
concrete_C30["fck"] = 32.5
print(f"Updated fck: {concrete_C30['fck']} MPa")

# Adding a new property
concrete_C30["cost_per_m3"] = 1500.0 # TL
print("Added Cost info:", concrete_C30)

# 4. Application: Calculating Weight of a Column
# ----------------------------------------------
# Column: 300x300 mm, Height: 3 m
b = 0.3 # m
h = 0.3 # m
L = 3.0 # m
volume = b * h * L

# Weight = Volume * Unit Weight (gamma)
weight = volume * concrete_C30["gamma"]

print("-" * 30)
print(f"Column Volume: {volume:.3f} m3")
print(f"Column Weight: {weight:.3f} kN using {concrete_C30['grade']} concrete.")
print("-" * 30)

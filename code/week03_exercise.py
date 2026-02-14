# Week 3 Exercise: Beam Safety Verification

# Input Data
# ------------------------------
L = 6.0         # Beam Length (m)
w = 15.0        # Distributed Load (kN/m)
E = 210000000.0 # Elastic Modulus (kPa or kN/m^2) [Steel]
I = 0.0002      # Moment of Inertia (m^4)
Z = 0.001       # Section Modulus (m^3)
Fy = 250000.0   # Yield Strength (kPa)

# 1. Calculate Maximum Moment (kNm)
# Formula: M = w * L^2 / 8
M_max = (w * L**2) / 8
print("Maximum Moment:", M_max, "kNm")

# 2. Calculate Bending Stress (kPa)
# Formula: Stress = M / Z
sigma = M_max / Z
print("Bending Stress:", sigma, "kPa")

# 3. Calculate Maximum Deflection (m)
# Formula: delta = 5 * w * L^4 / (384 * E * I)
delta_max = (5 * w * L**4) / (384 * E * I)
print("Max Deflection:", delta_max * 1000, "mm")

# 4. Define Limits
allowable_deflection = L / 300
print("Allowable Deflection:", allowable_deflection * 1000, "mm")

# 5. Perform Safety Checks
# Check 1: Is Stress within Elastic Range? (Stress <= Yield)
check_stress = sigma <= Fy

# Check 2: Is Deflection acceptable? (Delta <= Limit)
check_deflection = delta_max <= allowable_deflection

# Final Decision: BOTH must be True for the design to be Safe
is_design_safe = check_stress and check_deflection

print("-" * 30)
print("Stress Check:", check_stress)
print("Deflection Check:", check_deflection)
print("IS DESIGN SAFE?", is_design_safe)
print("-" * 30)

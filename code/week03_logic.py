# Comparison Operators
# --------------------
# Comparing Demand vs Capacity is fundamental in Civil Engineering
demand_load = 150.0  # kN
capacity = 200.0     # kN

is_safe = capacity > demand
print("Is the structure safe?", is_safe)
print("Is critical?", capacity == demand)


# Logical Operators (and, or, not)
# --------------------------------
# Complex conditions often require multiple checks.

# Example: A generic design check
# 1. Stress must be below limit
# 2. Deflection must be below limit

stress = 150 # MPa
deflection = 12 # mm

stress_limit = 250 # MPa
deflection_limit = 20 # mm

# AND: Both must be True
design_check = (stress < stress_limit) and (deflection < deflection_limit)
print("Design passes checks:", design_check)

# OR: At least one is True
# Example: Warning if ANY limit is approached (say 80% usage)
warning_needed = (stress > 0.8 * stress_limit) or (deflection > 0.8 * deflection_limit)
print("Warning light on:", warning_needed)

# NOT: Reverses the boolean
print("Design failed:", not design_check)

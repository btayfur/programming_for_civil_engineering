import math

# 1. Basic Constants
# ------------------
print(f"Pi: {math.pi}")
print(f"Euler's number (e): {math.e}")

# 2. Rounding Functions (The Tricks)
# ----------------------------------
val = 3.6
print(f"\nValue: {val}")
print(f"round(3.6): {round(val)}")       # Standard rounding (nearest even for .5 in Python 3!)
print(f"math.floor(3.6): {math.floor(val)}") # Always down
print(f"math.ceil(3.6): {math.ceil(val)}")   # Always up
print(f"math.trunc(3.6): {math.trunc(val)}") # Cuts decimal part

# Trick: Rounding to specific decimal places
# Round 3.14159 to 2 decimal places
pi_approx = round(math.pi, 2)
print(f"Round(pi, 2): {pi_approx}")

# 3. Powers and Roots
# -------------------
print("\nPowers and Roots:")
print(f"2^3 (pow): {math.pow(2, 3)}") # Returns float
print(f"Sqrt(16): {math.sqrt(16)}")

# 4. Logarithms
# -------------
# Natural Log (ln) -> math.log(x)
# Base 10 Log -> math.log10(x)
val = 100
print(f"\nNatural Log (ln) of {val}: {math.log(val):.4f}")
print(f"Log10 of {val}: {math.log10(val)}")

# 5. Trigonometry (Crucial: RADIANS vs DEGREES)
# ---------------------------------------------
angle_deg = 45
angle_rad = math.radians(angle_deg) # Convert deg to rad

print(f"\nAngle: {angle_deg} degrees")
print(f"Angle: {angle_rad:.4f} radians")
print(f"Sin(45 deg): {math.sin(angle_rad):.4f}") # sin expects radians!
print(f"Cos(45 deg): {math.cos(angle_rad):.4f}")

# Inverse Trig
val = 1.0
print(f"Arcsin(1.0): {math.degrees(math.asin(val))} degrees") # Result in radians, convert to deg

# 6. Floating Point Comparison (The 'isclose' Trick)
# --------------------------------------------------
# NEVER check if floatA == floatB
a = 0.1 + 0.2
b = 0.3
print(f"\nIs 0.1 + 0.2 == 0.3? {a == b}") # False!
print(f"Using math.isclose: {math.isclose(a, b)}") # True

# Arithmetic Operators
# --------------------
L = 5.0   # Beam Length (m)
w = 12.0  # Distributed Load (kN/m)

# Exponentiation (**): M = w * L^2 / 8
moment = (w * L**2) / 8
print("Maximum Moment:", moment, "kNm")

# Modulus (%): Useful for cyclic patterns or checking remainders
# Example: We have 52 rebars, want to bundle them in groups of 10.
total_rebars = 52
group_size = 10
remaining = total_rebars % group_size
print("Rebars left over:", remaining)

# Floor Division (//): Integer result of division
filled_groups = total_rebars // group_size
print("Full groups created:", filled_groups)


# Assignment Operators
# --------------------
# Instead of writing x = x + 1, we write x += 1
concrete_volume = 100 # m3
print("Initial Volume:", concrete_volume)

# Pour 20 m3 more
concrete_volume += 20 
print("After Pour:", concrete_volume)

# A mixer truck takes 8 m3, remove it
concrete_volume -= 8
print("After Truck Load:", concrete_volume)

# Type Conversion (Casting) Example

# String to Float
displacement_str = "12.5"
displacement_val = float(displacement_str)
print("Displacement (float):", displacement_val)

# Float to Integer
# Note: This truncates the decimal part!
load = 15.8
load_int = int(load)
print("Load (original):", load)
print("Load (int):", load_int)

# Number to String
# Useful for combining with other text
force = 100
message = "The applied force is " + str(force) + " kN"
print(message)

# Variables and Data Types Example

# Integer (Whole number)
number_of_floors = 5
print("Floors:", number_of_floors, "| Type:", type(number_of_floors))

# Float (Decimal number)
beam_length = 4.5
print("Beam Length:", beam_length, "m", "| Type:", type(beam_length))

# Complex (Real + Imaginary)
# Useful for dynamics/vibrations applications
impedance = 3 + 4j
print("Impedance:", impedance, "| Type:", type(impedance))
print("Real part:", impedance.real, "Imaginary part:", impedance.imag)

# String (Text)
material_name = "Concrete (C30)"
print("Material:", material_name, "| Type:", type(material_name))

# Boolean (True/False)
is_safe = True
print("Is Structure Safe?", is_safe, "| Type:", type(is_safe))

# NoneType (Empty/Null)
# Used to represent 'no value' or initialization
result = None
print("Current result:", result, "| Type:", type(result))
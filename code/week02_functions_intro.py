# Introduction to Functions
# -------------------------
# A function is a reusable block of code.
# We define it once, and 'call' it many times.

# 1. Defining a simple function
def calculate_area(width, height):
    """Calculates area of a rectangle"""
    area = width * height
    return area

# 2. Using (Calling) the function
b1 = 3.0
h1 = 4.0
area1 = calculate_area(b1, h1)
print(f"Beam 1 (3x4) Area: {area1}")

b2 = 5.0
h2 = 0.5
area2 = calculate_area(b2, h2)
print(f"Beam 2 (5x0.5) Area: {area2}")

# 3. Built-in Functions we already use
# print(), type(), input(), int(), float() are all functions provided by Python.
print("Length of string 'Concrete':", len("Concrete"))

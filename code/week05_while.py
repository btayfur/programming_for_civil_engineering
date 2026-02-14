# While Loops
# -----------
# Repeat code WHILE a condition is true.
# Useful when we don't know how many iterations we need beforehand.

# Example: Designing a column section (Iterative Approach)
# We strictly increase the concrete grade until capacity > demand.

demand = 2500 # kN
capacity = 0 # Initial
grade = 20 # Start with C20 concrete
area = 0.4 * 0.4 # 400x400 mm column

print(f"Required Capacity: {demand} kN")

while capacity < demand:
    # Calculate capacity (Simplified: 0.85 * fck * Area)
    # We ignore steel for this simple logic example
    fck = grade * 1000 # kPa
    capacity = 0.85 * fck * area
    
    print(f"Trying C{grade}: Capacity = {capacity:.1f} kN")
    
    if capacity < demand:
        grade += 5 # Increase grade by 5 MPa (C20 -> C25 -> C30...)

print("-" * 30)
print(f"Design Selected: C{grade} with Capacity {capacity:.1f} kN")

# Conditional Statements (if-elif-else)
# -------------------------------------
# Example: Determines the strength class of a concrete sample
# based on its characteristic cylinder strength (f_ck).

f_ck = float(input("Enter the characteristic cylinder strength (f_ck) in MPa: "))

# Logic:
# - Below 20 MPa: Low Strength (Non-structural usage mostly)
# - 20 to 50 MPa: Normal Strength (Standard buildings)
# - 50 to 90 MPa: High Strength (High-rise, Bridges)
# - Above 90 MPa: Ultra-High Strength

if f_ck < 20:
    category = "Low Strength Concrete"
    application = "Pavements, blinding concrete"
elif f_ck < 50:
    category = "Normal Strength Concrete"
    application = "Beams, columns, slabs in typical buildings"
elif f_ck < 90:
    category = "High Strength Concrete"
    application = "High-rise buildings, long-span bridges"
else:
    # If none of the above are true
    category = "Ultra-High Strength Concrete"
    application = "Specialized structural elements, nuclear containment"

print("-" * 30)
print("Classification:", category)
print("Typical Use:", application)
print("-" * 30)

# String Manipulation for Engineers
# ---------------------------------
# In engineering, we often get data as messy text strings.
# We need to clean, split, and format them.

# 1. The "Slice" (Accessing parts of a string)
# --------------------------------------------
sample_code = "BEAM-2024-SECTION-A"
print(f"Original: {sample_code}")
print(f"First 4 chars: {sample_code[0:4]}")  # "BEAM"
print(f"Last char: {sample_code[-1]}")        # "A"

# 2. Cleaning Data (.strip)
# -------------------------
# Essential when reading files! '  500  \n' -> '500'
messy_input = "   500.5   \n"
clean_input = messy_input.strip() 
print(f"\nMessy: '{messy_input}'")
print(f"Clean: '{clean_input}'")

# 3. Splitting Data (.split)
# --------------------------
# Essential for CSV files or log strings
data_line = "Concrete,C30,2400,0.2"
values = data_line.split(",") # Splits where it finds ","
print(f"\nSplit Data: {values}")
# Note: They are still Strings! We need to cast them.
density = float(values[2])
print(f"Density (float): {density}")

# 4. Replacement (.replace)
# -------------------------
# Fixing units or typos
report = "Length is 5m, Width is 2m"
numeric_report = report.replace("m", "") # Remove 'm'
print(f"\nReport: {report}")
print(f"Numeric ready: {numeric_report}")

# 5. F-String Formatting (Reporting)
# ----------------------------------
load = 123.456789
d = 2.0
# We want: "Load: 123.46 kN | Depth: 2 m"
# :.2f means "Float with 2 decimal places"
formatted = f"Load: {load:.2f} kN | Depth: {d:.0f} m"
print(f"\nFormatted Report: {formatted}")

# Python Lists
# ------------
# Lists are ordered collections of items.
# Engineering Use: Storing multiple load values, beam lengths, or sensor readings.

# 1. Defining a List
# ------------------
# Loads in kN acting on a structure
loads = [10.5, 25.0, 5.0, 15.0, 0.0]
print(f"All Loads: {loads}")

# 2. Accessing Elements (Indexing)
# --------------------------------
# Python is 0-indexed.
first_load = loads[0]
last_load = loads[-1] # Negative index counts from the end
print(f"First Load: {first_load} kN")
print(f"Last Load: {last_load} kN")

# 3. Slicing (Subsets)
# --------------------
# We want to analyze only the first 3 loads
# Syntax: list[start:end] (end is exclusive)
subset = loads[0:3]
print(f"First 3 loads: {subset}")

# 4. Modifying Lists (Mutable)
# ----------------------------
# Adding a new load (e.g. from a new user input)
loads.append(30.0)
print(f"After Append: {loads}")

# Correcting a value (e.g. data correction)
loads[2] = 7.5
print(f"After Correction: {loads}")

# 5. Engineering Operation
# ------------------------
# Calculate Total Load and Max Load
total_load = sum(loads)
max_load = max(loads)

print("-" * 30)
print(f"Total Design Load: {total_load} kN")
print(f"Critical (Max) Load: {max_load} kN")
print("-" * 30)

# 6. Converting Data Structures
# -----------------------------
# Converting a List to a Tuple (to make it immutable/read-only)
# This is useful when you want to ensure data cannot be changed accidentally
loads_tuple = tuple(loads)
print(f"Loads as Tuple: {loads_tuple}")

# Converting a Tuple back to a List (to make edits)
# If we need to modify data again, we convert it back to a list
loads_list_again = list(loads_tuple)
loads_list_again.append(50.0) 
print(f"Loads back as List (with new item): {loads_list_again}")

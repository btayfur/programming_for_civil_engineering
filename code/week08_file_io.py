# File I/O (Input/Output) Basics
# ------------------------------
# How to read and write text files safely.

filename = "site_log.txt"

# 1. Writing to a File ('w' mode)
# -------------------------------
# 'w' mode deletes the file content if it exists and starts fresh!
# The 'with' statement automatically closes the file (SAFE).
print("Writing data to file...")
with open(filename, "w") as f:
    f.write("Time,Temperature,Stress\n") # Header
    f.write("12:00,25.5,100\n")          # Data
    f.write("12:15,26.0,110\n")
    f.write("12:30,26.2,115\n")
print("Write complete.\n")

# 2. Appending to a File ('a' mode)
# ---------------------------------
# 'a' adds to the end without deleting existing content.
with open(filename, "a") as f:
    f.write("12:45,25.8,105\n")

# 3. Reading a File ('r' mode)
# ----------------------------
print("Reading file line by line:")
with open(filename, "r") as f:
    # f.readlines() reads all lines into a LIST
    all_lines = f.readlines()

for line in all_lines:
    # line looks like "12:00,25.5,100\n"
    # 1. Strip the invisible newline '\n' at the end
    clean_line = line.strip()
    
    # 2. Split by comma
    parts = clean_line.split(",")
    
    print(f"Row: {parts}")
    
    # Example: Check for high stress (ignoring Header)
    if parts[0] != "Time":
        stress = float(parts[2])
        if stress > 110:
            print(f"  -> WARNING: High Stress detected at {parts[0]}!")

# 4. Deleting the file (Cleanup)
# ------------------------------
import os
# os.remove(filename) # Uncomment to delete the file after running

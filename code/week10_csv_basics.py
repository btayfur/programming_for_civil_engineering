import csv

# WEEK 10: CSV File Operations
# ----------------------------
# "CSV" stands for Comma Separated Values. 
# It is the most common format for Engineering Data exchange.

filename = "code/week10_concrete_data.csv"

# 1. Reading CSV Manually (The Hard Way)
# --------------------------------------
# Useful to understand what CSV actually is: Just text with commas!
print("--- Method 1: Manual Parsing ---")
with open(filename, "r") as f:
    # Read first 3 lines only
    for i in range(3):
        line = f.readline().strip()
        columns = line.split(",")
        print(f"Row {i}: {columns}")

# 2. Reading with 'csv' Library (The Standard Way)
# ------------------------------------------------
# Handles edge cases (like commas inside text) automatically.
print("\n--- Method 2: csv.reader ---")
with open(filename, "r") as f:
    reader = csv.reader(f)
    
    # Getting the Header
    header = next(reader) # Skips the first line and saves it
    print(f"Header: {header}")
    
    # Read data
    row_count = 0
    for row in reader:
        row_count += 1
        # Let's print only the first 2 data rows
        if row_count <= 2:
            print(f"Data {row_count}: {row}")
            
# 3. Writing to CSV
# -----------------
output_file = "code/week10_report.csv"
data_to_write = [
    ["Test_ID", "Result", "Notes"],
    [1, "Pass", "Good surface"],
    [2, "Fail", "Cracked early"]
]

print(f"\n--- Writing to {output_file} ---")
with open(output_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data_to_write)
print("Write complete.")

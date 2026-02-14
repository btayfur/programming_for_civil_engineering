import csv
import statistics

# WEEK 10: Parsing & Statistics Application
# -----------------------------------------
# Goal: Read 300 concrete tests, filter by 28-day strength, 
# and calculate statistics.

filename = "code/week10_concrete_data.csv"

# Lists to hold our data columns
strengths_28_days = []
batch_codes = []

print(f"Reading {filename}...")

with open(filename, "r") as f:
    reader = csv.DictReader(f) # DictReader map header to values!
    # row is now like: {'Sample_ID': 'CYL-1001', 'Compressive_Strength_MPa': '35.2', ...}
    
    for row in reader:
        try:
            # Parse Data
            days = int(row["Cure_Time_Days"])
            strength = float(row["Compressive_Strength_MPa"])
            batch = row["Batch_Code"]
            
            # Application Logic: We only care about standard 28-day tests
            if days == 28:
                strengths_28_days.append(strength)
                batch_codes.append(batch)
                
        except ValueError:
            print("Skipping invalid row...")

# Statistical Analysis
# --------------------
count = len(strengths_28_days)
avg = statistics.mean(strengths_28_days)
std_dev = statistics.stdev(strengths_28_days)
min_val = min(strengths_28_days)
max_val = max(strengths_28_days)

# Reporting
print("\n--- 28-Day Concrete Strength Analysis ---")
print(f"Total Samples Analyzed: {count}")
print(f"Mean Strength:     {avg:.2f} MPa")
print(f"Standard Dev:      {std_dev:.2f} MPa")
print(f"Range:             {min_val} - {max_val} MPa")

# Acceptance Check (Example C30/37 Concrete)
# A simplified rule: Mean must be >= 38 MPa (fck + margin)
target = 38.0
if avg >= target:
    print(f"\nRESULT: BATCH PASSED (Mean > {target})")
else:
    print(f"\nRESULT: BATCH FAILED (Mean < {target})")

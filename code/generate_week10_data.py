import csv
import random

# Generate a realistic Civil Engineering dataset
# Theme: Concrete Cylinder Compression Test Results

filename = "code/week10_concrete_data.csv"
rows = 300

# Headers (10 Columns)
headers = [
    "Sample_ID", "Batch_Code", "Cement_Type", "Cure_Time_Days", 
    "Diameter_mm", "Height_mm", "Weight_kg", 
    "Max_Load_kN", "Compressive_Strength_MPa", "Technician"
]

operators = ["Ali", "Veli", "Ayse", "Fatma", "John", "Sarah"]
cement_types = ["CEM I 42.5", "CEM II 32.5", "CEM I 52.5"]
cure_times = [7, 28, 90]

print(f"Generating {filename} with {rows} rows...")

with open(filename, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    
    for i in range(1, rows + 1):
        sample_id = f"CYL-{1000+i}"
        batch_code = f"B-{random.randint(100, 150)}"
        cement = random.choice(cement_types)
        days = random.choice(cure_times)
        
        # Dimensions (Standard cylinder 150x300mm with slight manufacturing error)
        diameter = round(random.uniform(148.0, 152.0), 1)
        height = round(random.uniform(298.0, 302.0), 1)
        
        # Physics calculations for realism
        radius_m = (diameter / 1000) / 2
        area_m2 = 3.14159 * (radius_m ** 2)
        volume_m3 = area_m2 * (height / 1000)
        
        # Density approx 2400 kg/m3 with noise
        density = random.uniform(2350, 2450)
        weight = round(volume_m3 * density, 2)
        
        # Strength depends on Days and Cement Type (Simulation logic)
        base_strength = 25 # MPa
        if days == 28: base_strength += 10
        if days == 90: base_strength += 15
        if "52.5" in cement: base_strength += 10
        
        # Random variation
        real_strength = random.gauss(base_strength, 3) # Normal distribution
        real_strength = round(max(10, real_strength), 2) # Min 10 MPa
        
        # Back-calculate Force required to break it
        # Stress = Force / Area -> Force = Stress * Area * 1000 (for kN)
        max_load_kN = round(real_strength * area_m2 * 1000, 2)
        
        tech = random.choice(operators)
        
        row = [
            sample_id, batch_code, cement, days, 
            diameter, height, weight, 
            max_load_kN, real_strength, tech
        ]
        writer.writerow(row)

print("Dictionary generation complete.")

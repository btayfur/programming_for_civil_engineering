# Variable Scope (Local vs Global)
# --------------------------------
# Analogy: 
# Global Variable: The "Site Crane". Everyone on the site can see and use it.
# Local Variable: The "Site Engineer's Personal Pen". Only the engineer in that office can use it.

# 1. Global Scope
project_name = "Suspension Bridge" # This is Global

def print_project_info():
    # We can READ global variables inside a function
    print(f"Working on: {project_name}")

print_project_info()


# 2. Local Scope
def calculate_stress(force, area):
    # 'safety_factor' is created INSIDE the function.
    # It is LOCAL. It dies when the function finishes.
    safety_factor = 1.5 
    design_stress = (force / area) * safety_factor
    return design_stress

stress = calculate_stress(1000, 10)
print(f"Calculated Stress: {stress}")

# Error Scenario
# print(safety_factor) 
# NameError: name 'safety_factor' is not defined. 
# The main program cannot reach inside the function to get the pen!


# 3. Shadowing (Tricky!)
# ----------------------
limit = 100 # Global

def check_limit():
    limit = 50 # Local variable with SAME name (Shadows the global one)
    print(f"Inside function, limit is: {limit}")

check_limit()
print(f"Outside function, limit is: {limit}") # Still 100! The global one was untouched.

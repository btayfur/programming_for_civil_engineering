# Anatomy of a Function
# ---------------------
# Analogy: A Function is like a "Concrete Mixer Truck".
# Input (Arguments): Water, Cement, Aggregate.
# Process: Mixing/Rotating.
# Output (Return): Fresh Concrete.

def calculate_beam_weight(length, width, height, density=2400):
    """
    Calculates the weight of a beam.
    
    Parameters:
    length (float): Length in meters.
    width (float): Width in meters.
    height (float): Height in meters.
    density (float): Density in kg/m3 (Default is Concrete: 2400).

    Returns:
    float: The total weight in kg.
    """
    
    # 1. Processing (The Logic)
    volume = length * width * height
    weight = volume * density
    
    # 2. Output (Return)
    return weight

# Using the function (Calling the machine)
# ----------------------------------------

# Scenario 1: Standard Concrete Beam using Positional Arguments
wt_1 = calculate_beam_weight(5.0, 0.3, 0.5) 
print(f"Beam 1 Weight (Concrete): {wt_1} kg")

# Scenario 2: Steel Beam (Overriding the default density) using Keyword Arguments
# Keyword arguments make it readable and order doesn't matter much.
wt_2 = calculate_beam_weight(length=4.0, width=0.1, height=0.2, density=7850)
print(f"Beam 2 Weight (Steel): {wt_2} kg")

# Scenario 3: What if we didn't use 'return'?
def useless_calculator(a, b):
    result = a + b
    print(f"Result is {result}")
    # No return statement implies "return None"

value = useless_calculator(10, 20)
print(f"Captured Value: {value}") # Output: None. We cannot use this result in other calculations!

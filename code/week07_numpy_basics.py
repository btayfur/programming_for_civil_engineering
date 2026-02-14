import numpy as np

# 1. Why NumPy? Lists vs Arrays
# -----------------------------
# Calculating stress = Force / Area for multiple beams
forces = [1000, 2000, 1500] # List
area = 0.5                  # Scalar

# List approach (Error prone or needs loop)
# stresses = forces / area  <-- TypeError: unsupported operand type(s) for /: 'list' and 'float'

# NumPy approach (Vectorization)
forces_arr = np.array([1000, 2000, 1500])
stresses = forces_arr / area # Element-wise operation!
print("Stresses (Array):", stresses)

# 2. Creating Arrays
# ------------------
# Manual
arr_1d = np.array([1, 2, 3])
arr_2d = np.array([[1, 2, 3], [4, 5, 6]]) # Matrix (2 rows, 3 cols)

print(f"\n1D Array shape: {arr_1d.shape}")
print(f"2D Array shape: {arr_2d.shape}")

# Generators (Very useful for graphs)
# linspace(start, stop, count) -> Generates 'count' numbers evenly spaced
x_values = np.linspace(0, 10, 5) # 0, 2.5, 5.0, 7.5, 10.0
print(f"\nLinspace (0 to 10): {x_values}")

# Zeros and Ones (Pre-allocating memory)
zeros_mat = np.zeros((3, 3)) # 3x3 matrix of zeros
print(f"\nZeros 3x3:\n{zeros_mat}")

# 3. Operations & Statistical Methods
# -----------------------------------
data = np.array([10.5, 12.0, 9.8, 11.2])
print(f"\nData: {data}")
print(f"Mean: {data.mean()}")
print(f"Standard Deviation: {data.std()}")
print(f"Max Index (argmax): {data.argmax()}") # Index of the max value

# Exercise: Numerical Integration (Riemann Sum)
# ---------------------------------------------
# Calculate the integral of a function f(x) from a to b.
# Engineering Context: Total force from a varying distributed load.
# Load Function: w(x) = 2*x + 5 (Trapezoidal load distribution)
# Integration Range: x = 0 to x = L

def w(x):
    """Distributed load function w(x) = 2x + 5"""
    return 2.0 * x + 5.0

# Integration Parameters
print("Calculating Total Force from Distributed Load w(x) = 2x + 5")

L = float(input("Enter beam length L (m): ")) # Integration upper limit (b)
N = int(input("Enter number of segments N: "))  # Number of steps

# Step size
dx = L / N
total_force = 0.0

# Numerical Integration using Midpoint Rule (or simple Left/Right sum)
# Integral ~ Sum( w(x_i) * dx )
print(f"integrating from 0 to {L} with {N} steps (dx={dx})...")

for i in range(N):
    # Calculate x at the midpoint of the current slice for better accuracy
    x_i = i * dx + (dx / 2)
    
    # Calculate area of this slice
    force_slice = w(x_i) * dx
    
    # Add to total
    total_force += force_slice

print("-" * 30)
print(f"Total Force (Approx): {total_force:.4f} kN")

# Exact Analytic Solution: Integral(2x + 5) = x^2 + 5x
# F_exact = (L^2 + 5*L) - (0)
exact_force = (L**2) + 5*L
print(f"Total Force (Exact) : {exact_force:.4f} kN")
print(f"Error               : {abs(total_force - exact_force):.6f} kN")
print("-" * 30)

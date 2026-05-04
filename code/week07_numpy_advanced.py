# NumPy: boolean filtering, broadcasting, linear solve
# ----------------------------------------------------
import numpy as np

# 1. Boolean filtering -- find members exceeding capacity
# -------------------------------------------------------
forces  = np.array([10, 250, 75, 320, 50, 280])
limit   = 200
print(f"Forces over {limit} kN:", forces[forces > limit])
print(f"Indices of failures   :", np.where(forces > limit)[0])

# 2. Broadcasting -- scale and shift in one shot
# ----------------------------------------------
# Stress in MPa given force (kN) and area (mm^2):
forces_kN = np.array([100, 150, 200])
area_mm2  = 500
stress_MPa = forces_kN * 1e3 / area_mm2          # broadcasts scalar
print("stress (MPa):", stress_MPa)

# (3,1) + (1,4) -> (3,4) outer-style addition
col = np.array([[1], [2], [3]])
row = np.array([[10, 20, 30, 40]])
print("\nbroadcast sum:\n", col + row)

# 3. Reshape and transpose
# ------------------------
flat = np.arange(12)
M = flat.reshape((3, 4))
print("\nmatrix:\n", M)
print("transpose:\n", M.T)

# 4. 2x2 stiffness solve  K u = F
# -------------------------------
K = np.array([[2.0, -1.0],
              [-1.0, 2.0]])
F = np.array([10.0, 5.0])
u = np.linalg.solve(K, F)
print("\nu =", u)
print("verify K @ u =", K @ u)

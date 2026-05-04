# Bilinear force-displacement (pushover-style) capacity curve
# -----------------------------------------------------------
# Demonstrates: object-oriented Matplotlib API, axis labels,
# grid, legend, annotation, and saving to PNG.

import numpy as np
import matplotlib.pyplot as plt

# 1. Synthetic capacity curve: elastic up to yield, then plastic plateau
# ----------------------------------------------------------------------
u_yield = 12.0     # mm
F_yield = 220.0    # kN
u_max   = 60.0
F_max   = 250.0    # mild hardening

u_elastic = np.linspace(0, u_yield, 30)
F_elastic = (F_yield / u_yield) * u_elastic

u_plastic = np.linspace(u_yield, u_max, 60)
F_plastic = F_yield + (F_max - F_yield) * (u_plastic - u_yield) / (u_max - u_yield)

u = np.concatenate([u_elastic, u_plastic])
F = np.concatenate([F_elastic, F_plastic])

# 2. Plot with the OO API
# -----------------------
fig, ax = plt.subplots(figsize=(6.5, 4.5))
ax.plot(u, F, "b-", linewidth=2, label="Capacity curve")
ax.axvline(u_yield, color="grey", linestyle="--", alpha=0.6)
ax.scatter([u_yield], [F_yield], color="red", zorder=5, label="Yield point")

ax.set_title("Force--Displacement (Pushover)")
ax.set_xlabel("Displacement u [mm]")
ax.set_ylabel("Base shear F [kN]")
ax.set_xlim(0, u_max)
ax.set_ylim(0, F_max * 1.1)
ax.grid(True, alpha=0.4)
ax.legend(loc="lower right")

fig.tight_layout()
fig.savefig("force_displacement.png", dpi=200)
plt.show()

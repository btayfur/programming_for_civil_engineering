# Twin-axis plot: force and displacement vs time
# ----------------------------------------------
# Two physical quantities with different units share the
# x-axis but get their own y-axis (one on each side).

import numpy as np
import matplotlib.pyplot as plt

# 1. Synthetic time history (e.g. cyclic loading)
# -----------------------------------------------
t = np.linspace(0, 4 * np.pi, 400)
F = 100 * np.sin(t)               # kN
u =   3 * np.sin(t - 0.3)         # mm (slight phase lag)

# 2. OO twin-axis figure
# ----------------------
fig, ax1 = plt.subplots(figsize=(7, 4))

color1 = "tab:blue"
ax1.plot(t, F, color=color1, label="Force F [kN]")
ax1.set_xlabel("time [s]")
ax1.set_ylabel("F [kN]", color=color1)
ax1.tick_params(axis="y", labelcolor=color1)
ax1.grid(True, alpha=0.3)

ax2 = ax1.twinx()              # second y-axis sharing the x-axis
color2 = "tab:red"
ax2.plot(t, u, color=color2, linestyle="--", label="Displ. u [mm]")
ax2.set_ylabel("u [mm]", color=color2)
ax2.tick_params(axis="y", labelcolor=color2)

# Combine legends from both axes
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper right")

fig.suptitle("Cyclic loading: force and displacement vs time")
fig.tight_layout()
fig.savefig("twin_axis.png", dpi=200)
plt.show()

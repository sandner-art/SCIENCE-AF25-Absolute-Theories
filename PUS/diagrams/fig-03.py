import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import PathPatch
from matplotlib.path import Path
from scipy.interpolate import interp1d

# --- Parameters ---
time = np.linspace(0, 10, 200)
n_paths = 5
filter_time = 4.0 # Time point where PUS filter acts

# --- Generate Paths ---
paths_x = []
paths_y = []

# Path 1: The 'Actual' Simple Path W@
x_actual = time * 0.3
y_actual = np.zeros_like(time)
paths_x.append(x_actual)
paths_y.append(y_actual)

# Other paths: add complexity/knots before filter_time
np.random.seed(42) # for reproducibility
for i in range(1, n_paths):
    # Base path (diverging slightly)
    x_base = time * (0.3 + (i - n_paths/2)*0.05)
    y_base = time * (i - n_paths/2)*0.1
    # Add oscillations/knots before filter_time
    oscillation = np.sin(time * np.random.uniform(1.5, 3.5)) * np.random.uniform(0.3, 0.8)
    oscillation[time > filter_time] = 0 # Stop oscillation after filter
    # Introduce a 'knot' - quick deviation and return
    knot_pos = filter_time * np.random.uniform(0.4, 0.8)
    knot_width = 0.5
    knot_amp = np.random.uniform(-1, 1) * 0.7
    knot = knot_amp * np.exp(-((time - knot_pos)**2) / (2 * (knot_width/3)**2))
    knot[time > filter_time] = 0 # Stop knot after filter

    paths_x.append(x_base + oscillation * 0.3) # Add oscillations to x slightly
    paths_y.append(y_base + oscillation + knot)

# --- Plotting ---
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(8, 10))

# Draw the PUS Filter line
ax.axvline(filter_time, color='red', linestyle='-.', linewidth=2.5, label='PUS Filter ($\equiv$ Actuality Definition)')
ax.text(filter_time + 0.1, 0.95*ax.get_ylim()[1], 'PUS Filter', color='red', rotation=90, va='top', ha='left', fontsize=11)

# Draw paths
filter_idx = np.searchsorted(time, filter_time)

# Actual Path W@ (Solid throughout)
ax.plot(paths_x[0], time, color='blue', linewidth=3.0, label=r'$W_{@}$ (Self-Consistent History)')

# Other Paths (Complex before filter, dashed/faded after)
colors = ['green', 'purple', 'orange', 'brown']
for i in range(1, n_paths):
    # Before filter
    ax.plot(paths_x[i][:filter_idx+1], time[:filter_idx+1], color=colors[i-1], linewidth=1.5)
    # After filter (faded/dashed) - plot only if needed, or just stop
    ax.plot(paths_x[i][filter_idx:], time[filter_idx:], color=colors[i-1], linewidth=1.0, linestyle=':', alpha=0.4)
    # Add 'X' mark after filter
    ax.scatter(paths_x[i][filter_idx], time[filter_idx], marker='x', color='black', s=50, zorder=10)


# --- Labels and Title ---
ax.set_ylabel('Time ($t$) $\longrightarrow$', fontsize=12)
ax.set_xlabel('Abstract State Space Dimension', fontsize=12)
ax.set_title('Figure 3: PUS Filtering of Potential World-History Knots', fontsize=14, fontweight='bold')

# Remove X-axis ticks/labels if desired for abstraction
# ax.set_xticks([])
ax.invert_yaxis() # Often time flows upwards in these diagrams, but let's match the sketch roughly
ax.legend(fontsize=10, loc='lower left')
ax.grid(True, linestyle='--', alpha=0.6)

# Add annotation
ax.text(0, filter_time * 0.3, 'Potential "Knotted"/\nInconsistent Histories', ha='center', va='center', fontsize=10, color='gray')
ax.text(paths_x[0][filter_idx+50], time[filter_idx+50]+0.5, 'Only Self-Consistent\nHistory Persists', ha='left', va='top', fontsize=10, color='blue')

plt.tight_layout()
plt.savefig('pus_figure3_knot_filter.png', dpi=300)
plt.show()
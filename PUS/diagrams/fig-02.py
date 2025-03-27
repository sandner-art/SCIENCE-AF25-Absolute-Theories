import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import PathPatch
from matplotlib.path import Path

# --- Define Boundary Curve (Arbitrary Closed Shape) ---
# Using a slightly distorted ellipse for visual interest
t = np.linspace(0, 2 * np.pi, 200)
radius_variation = 1.0 + 0.2 * np.sin(t * 3) + 0.1 * np.cos(t * 2)
boundary_x = radius_variation * np.cos(t) * 2.0
boundary_y = radius_variation * np.sin(t) * 1.5

# --- Plotting ---
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(9, 7))

# Fill regions
ax.fill(boundary_x, boundary_y, color='lightblue', alpha=0.3, label=r'$W_{@}$ (Actual World)')
ax.fill_between([-5, 5], -5, 5, color='salmon', alpha=0.1, label=r"$W'$ (Non-Actual/Inconsistent)") # Fill outside area approx

# Plot boundary line
ax.plot(boundary_x, boundary_y, color='black', linewidth=2.5, label=r'Boundary of Actuality ($\partial W_{@}$)')

# Plot the 'Singularity' point
ax.scatter(0, 0, color='blue', s=100, zorder=10, label='Singularity of Actuality')

# --- Labels and Annotations ---
ax.set_xlabel('Abstract Ontological Parameter $\\alpha$', fontsize=12)
ax.set_ylabel('Abstract Nomological Parameter $\\beta$', fontsize=12)
ax.set_title("Figure 2: PUS Ontological 'Phase' Diagram", fontsize=14, fontweight='bold')

# Add text inside and outside
ax.text(0, 0.5, r'$W_{@}$' + '\nSelf-Consistent\n"Phase"', ha='center', va='center', fontsize=12, color='darkblue')
ax.text(-3, 3, r'$W^{\prime}$ Phase' + '\nExcluded by PUS', ha='center', va='center', fontsize=11, color='darkred')
ax.text(3, -3, r'$W^{\prime}$ Phase' + '\nExcluded by PUS', ha='center', va='center', fontsize=11, color='darkred')

ax.legend(fontsize=10, loc='lower right')
ax.grid(True, linestyle='--', alpha=0.4)
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_aspect('equal', adjustable='box')

plt.tight_layout()
plt.savefig('pus_figure2_phase_inspired.png', dpi=300)
plt.show()

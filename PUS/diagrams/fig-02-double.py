import matplotlib.pyplot as plt
import numpy as np

# --- Define Boundary Curve (Arbitrary Closed Shape) ---
t = np.linspace(0, 2 * np.pi, 200)
radius_variation = 1.0 + 0.2 * np.sin(t * 3) + 0.1 * np.cos(t * 2)
boundary_x = radius_variation * np.cos(t) * 2.0
boundary_y = radius_variation * np.sin(t) * 1.5

# --- Plotting ---
plt.style.use('seaborn-v0_8-whitegrid')
fig, axes = plt.subplots(1, 2, figsize=(18, 7))

# First Diagram
ax = axes[0]
ax.fill(boundary_x, boundary_y, color='lightblue', alpha=0.3, label=r'$W_{@}$ (Actual World)')
ax.fill_between([-5, 5], -5, 5, color='salmon', alpha=0.1, label=r"$W'$ (Non-Actual/Inconsistent)")
ax.plot(boundary_x, boundary_y, color='black', linewidth=2.5, label=r'Boundary of Actuality ($\partial W_{@}$)')
ax.scatter(0, 0, color='blue', s=100, zorder=10, label='Singularity of Actuality')
ax.set_xlabel('Abstract Ontological Parameter $\\alpha$', fontsize=12)
ax.set_ylabel('Abstract Nomological Parameter $\\beta$', fontsize=12)
ax.set_title("PUS Ontological 'Phase' Diagram", fontsize=14, fontweight='bold')
ax.text(0, 0.5, r'$W_{@}$' + '\nSelf-Consistent\n"Phase"', ha='center', va='center', fontsize=12, color='darkblue')
ax.text(-3, 3, r'$W^{\prime}$ Phase' + '\nExcluded by PUS', ha='center', va='center', fontsize=11, color='darkred')
ax.text(3, -3, r'$W^{\prime}$ Phase' + '\nExcluded by PUS', ha='center', va='center', fontsize=11, color='darkred')
ax.legend(fontsize=10, loc='lower right')
ax.grid(True, linestyle='--', alpha=0.4)
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_aspect('equal', adjustable='box')

# Second Diagram
ax2 = axes[1]
# Create a new boundary curve with different parameters
t2 = np.linspace(0, 2 * np.pi, 200)
radius_variation2 = 1.0 + 0.3 * np.sin(t2 * 4) + 0.2 * np.cos(t2 * 3)
boundary_x2 = radius_variation2 * np.cos(t2) * 2.0
boundary_y2 = radius_variation2 * np.sin(t2) * 1.5

ax2.fill(boundary_x2, boundary_y2, color='lightgreen', alpha=0.3, label=r'$W_{@}$ (Alternate World)')
ax2.fill_between([-5, 5], -5, 5, color='lightcoral', alpha=0.1, label=r"$W'$ (Non-Actual/Inconsistent)")
ax2.plot(boundary_x2, boundary_y2, color='black', linewidth=2.5, label=r'Boundary of Alternate Actuality ($\partial W_{@}$)')
ax2.scatter(0, 0, color='darkgreen', s=100, zorder=10, label='Singularity of Alternate Actuality')
ax2.set_xlabel('Abstract Ontological Parameter $\\alpha$', fontsize=12)
ax2.set_ylabel('Abstract Nomological Parameter $\\beta$', fontsize=12)
ax2.set_title("Alternate PUS Ontological 'Phase' Diagram", fontsize=14, fontweight='bold')
ax2.text(0, 0.5, r'$W_{@}$' + '\nAlternate\n"Phase"', ha='center', va='center', fontsize=12, color='darkgreen')
ax2.text(-3, 3, r'$W^{\prime}$ Phase' + '\nExcluded by PUS', ha='center', va='center', fontsize=11, color='darkred')
ax2.text(3, -3, r'$W^{\prime}$ Phase' + '\nExcluded by PUS', ha='center', va='center', fontsize=11, color='darkred')
ax2.legend(fontsize=10, loc='lower right')
ax2.grid(True, linestyle='--', alpha=0.4)
ax2.set_xlim(-5, 5)
ax2.set_ylim(-5, 5)
ax2.set_aspect('equal', adjustable='box')

plt.tight_layout()
plt.savefig('pus_double_phase_diagram.png', dpi=300)
plt.show()

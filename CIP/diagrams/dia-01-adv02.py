import matplotlib.pyplot as plt
import numpy as np

# --- Parameters for Mexican Hat ---
phi_cip = np.linspace(-3, 3, 400)
mu_sq = 4.0  # Controls the height of the central bump (needs to be > 0)
lambda_phi = 0.5 # Controls the steepness of the outer walls
rho_vac_offset = 0.5 # Constant offset so minimum isn't excessively negative

# Define the Mexican Hat potential: V = offset - mu^2/2 * Phi^2 + lambda/4 * Phi^4
potential = rho_vac_offset - 0.5 * mu_sq * phi_cip**2 + (lambda_phi / 4.0) * phi_cip**4

# Calculate minima positions: Phi^2 = mu^2 / lambda => |Phi| = sqrt(mu^2 / lambda)
min_phi_val = np.sqrt(mu_sq / lambda_phi)
min_v = rho_vac_offset - 0.5 * mu_sq * (min_phi_val**2) + (lambda_phi / 4.0) * (min_phi_val**4)

# --- Alternative Plotting (Option 2 - Effort Barrier Interpretation) ---
# ... (Use the same potential calculation as above) ...

plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(9, 7))
ax.plot(phi_cip, potential, color='darkcyan', linewidth=2.5)

# Highlight the minima as "Trapped" states
ax.scatter([-min_phi_val, min_phi_val], [min_v, min_v], color='purple', s=100, zorder=10, marker='P',
           label=f'Trapped Low-Effort State (V={min_v:.1f})')

# Highlight the theoretical (but unstable) minimum at Phi=0
local_max_phi = 0; local_max_v = rho_vac_offset
ax.scatter(local_max_phi, local_max_v - (local_max_v-min_v)*0.2, color='red', marker='v', s=100, zorder=10, # Point marker below the peak
           label=r'Target: Max Indifference (Below Barrier)')
ax.axhline(min_v - (local_max_v - min_v)*0.2, color='red', linestyle=':', lw=1, alpha=0.7) # Line for target V

# --- Labels and Annotations ---
ax.set_xlabel(r'Cosmic Attentiveness Field ($\Phi_{CIP}$)', fontsize=12)
ax.set_ylabel(r"Potential Energy 'Cost' $V(\Phi_{CIP})$", fontsize=12)
ax.set_title('Figure 1: Cosmic Indifference Potential with Effort Barrier', fontsize=14, fontweight='bold')

# Arrow indicating relaxation into the trap
ax.annotate('Relaxation into\nLocal Minimum',
            xy=(min_phi_val, min_v), xytext=(local_max_phi + 0.5, local_max_v - (local_max_v - min_v)*0.3),
            ha='left', va='top', arrowprops=dict(arrowstyle="-|>", connectionstyle="arc3,rad=-0.2", color='black', lw=1.5),
            fontsize=10)

# Indicate the barrier
ax.annotate('Effort Barrier\n(Prevents reaching\nTrue Minimum)',
            xy=(local_max_phi, local_max_v), xytext=(local_max_phi, local_max_v + (np.max(potential)-local_max_v)*0.1),
            ha='center', va='bottom', arrowprops=dict(arrowstyle="<->", color='orange', lw=1.5), # Double arrow for barrier height
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.9), fontsize=9)

ax.legend(fontsize=9, loc='upper center')
ax.grid(True, linestyle='--', alpha=0.6)
ax.set_ylim(bottom=min_v - (local_max_v - min_v)*0.5)

plt.tight_layout()
plt.savefig('cip_figure1_potential_barrier.png', dpi=300)
plt.show()
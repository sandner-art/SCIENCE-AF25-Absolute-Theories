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

# --- Plotting ---
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(9, 7)) # Slightly taller

ax.plot(phi_cip, potential, color='darkcyan', linewidth=2.5)

# Highlight the TRUE minima (Lowest Achievable Effort)
ax.scatter([-min_phi_val, min_phi_val], [min_v, min_v], color='red', s=100, zorder=10,
           label=f'V(±{min_phi_val:.1f}) = {min_v:.1f} (True Minimal Effort State)')

# Highlight the UNSTABLE point at Phi=0
local_max_phi = 0
local_max_v = rho_vac_offset
ax.scatter(local_max_phi, local_max_v, color='orange', s=80, zorder=10, marker='X',
           label=r'$\Phi=0$: Unstable Point')


# --- Labels and Annotations ---
ax.set_xlabel(r'Cosmic Attentiveness Field ($\Phi_{CIP}$)', fontsize=12)
ax.set_ylabel(r"Potential Energy 'Cost' $V(\Phi_{CIP})$", fontsize=12)
ax.set_title('Figure 1: The Effective Potential of Cosmic Indifference', fontsize=14, fontweight='bold') # Changed title

# Arrow indicating relaxation from center to minimum
ax.annotate('Minimum Effort Relaxation',
            xy=(min_phi_val, min_v), # Point to the minimum
            xytext=(local_max_phi + 0.5, local_max_v - (local_max_v - min_v)*0.3), # Start near the bump top
            ha='left', va='top',
            arrowprops=dict(arrowstyle="-|>", connectionstyle="arc3,rad=-0.2", color='black', lw=1.5),
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.9),
            fontsize=10)
# Arrow for the other side
ax.annotate('Minimum Effort Relaxation',
            xy=(-min_phi_val, min_v), # Point to the minimum
            xytext=(local_max_phi - 0.5, local_max_v - (local_max_v - min_v)*0.3), # Start near the bump top
            ha='right', va='top',
            arrowprops=dict(arrowstyle="-|>", connectionstyle="arc3,rad=0.2", color='black', lw=1.5),
            # Removed duplicate bbox for clarity
            fontsize=10)


ax.text(local_max_phi, local_max_v + (np.max(potential)-local_max_v)*0.1,
        'Unstable: Ideal Indifference\nRequires "Climbing Effort"',
        ha='center', va='bottom', fontsize=9, style='italic', color='gray')

ax.text(min_phi_val * 1.1, min_v + (np.max(potential)-min_v)*0.2,
        'Lowest Achievable\nEffort State\n(Practical Indifference)',
        ha='left', va='center', fontsize=9, style='italic', color='darkred')


ax.legend(fontsize=9, loc='upper center')
ax.grid(True, linestyle='--', alpha=0.6)
ax.set_ylim(bottom=min_v - (local_max_v - min_v)*0.5) # Adjust y-limit to show minimum clearly

plt.tight_layout()
plt.savefig('cip_figure1_potential_mexican_hat.png', dpi=300)
plt.show()
import matplotlib.pyplot as plt
import numpy as np

# --- Parameters for Mexican Hat ---
phi_cip = np.linspace(-3, 3, 400)
mu_sq = 4.0  # Controls the height of the central barrier
lambda_phi = 0.5 # Controls the steepness/position of minima
rho_vac_offset = 1.0 # Base offset for V=0 (can be adjusted)

# Define the Mexican Hat potential: V = offset - mu^2/2 * Phi^2 + lambda/4 * Phi^4
# (Adding offset ensures the minima are >= 0 if desired, adjust as needed)
potential = rho_vac_offset - 0.5 * mu_sq * phi_cip**2 + (lambda_phi / 4.0) * phi_cip**4

# Calculate minima positions: Phi^2 = mu^2 / lambda => |Phi| = sqrt(mu^2 / lambda)
min_phi_val = np.sqrt(mu_sq / lambda_phi)
# Calculate potential value at the minima
min_v = rho_vac_offset - 0.5 * mu_sq * (min_phi_val**2) + (lambda_phi / 4.0) * (min_phi_val**4)
# Calculate potential value at the central barrier (Phi=0)
barrier_v = rho_vac_offset

# Define the hypothetical "True Minimum" V if barrier wasn't there (e.g., slightly below min_v)
true_min_v = min_v - 0.2 # Arbitrary visual indicator

# --- Plotting ---
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(9, 7))

# Plot the potential
ax.plot(phi_cip, potential, color='darkcyan', linewidth=2.5, zorder=5)

# Highlight the minima as "Trapped" states
ax.scatter([-min_phi_val, min_phi_val], [min_v, min_v], color='purple', s=100, zorder=10, marker='o',
           label=f'Practical Minimum (V={min_v:.1f})\n(Trapped Low-Effort State)')

# Highlight the central barrier peak
ax.scatter(0, barrier_v, color='orange', marker='^', s=120, zorder=10, label='Unstable Peak (Effort Barrier)')

# Indicate the hypothetical true minimum
ax.axhline(true_min_v, color='red', linestyle=':', linewidth=1.5, alpha=0.8,
           label=f'Hypothetical True Minimum\n(Inaccessible, V≈{true_min_v:.1f})')
ax.text(0, true_min_v - 0.1, r'Ideal $\Phi=0$ State', color='red', ha='center', va='top', fontsize=9)

# --- Labels and Annotations ---
ax.set_xlabel(r'Cosmic Attentiveness Field ($\Phi_{CIP}$)', fontsize=12)
ax.set_ylabel(r"Potential Energy 'Cost' $V(\Phi_{CIP})$", fontsize=12)
ax.set_title('Figure 1: Cosmic Indifference Potential with Effort Barrier', fontsize=14, fontweight='bold')

# Arrow indicating relaxation INTO the trap (like the user's sketch)
ax.annotate('Relaxation into\nPractical Minimum\n(Path of Least Resistance)',
            xy=(min_phi_val, min_v), # Point arrow TO the minimum
            xytext=(0.5, barrier_v * 0.8), # Start arrow from near the barrier side
            ha='left', va='center', color='black',
            arrowprops=dict(arrowstyle="-|>", connectionstyle="arc3,rad=-0.2", color='red', lw=2.0), # Red arrow
            fontsize=10, bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.8))
# Mirror for the other side
ax.annotate('', # No text for the second arrow
            xy=(-min_phi_val, min_v),
            xytext=(-0.5, barrier_v * 0.8),
            arrowprops=dict(arrowstyle="-|>", connectionstyle="arc3,rad=0.2", color='red', lw=2.0))


ax.legend(fontsize=9, loc='upper center', bbox_to_anchor=(0.5, -0.12), ncol=3) # Move legend below plot
ax.grid(True, linestyle='--', alpha=0.6)
ax.set_ylim(bottom=min_v - (barrier_v - min_v)*0.5, top=np.max(potential)*1.1) # Adjust y-limit

plt.subplots_adjust(bottom=0.2) # Make room for legend below
plt.savefig('cip_figure1_potential_barrier_annotated.png', dpi=300)
plt.show()
import matplotlib.pyplot as plt
import numpy as np

# --- Parameters ---
phi_cip = np.linspace(-3, 3, 400)
rho_vac = 0.1  # Small non-zero vacuum energy (Dark Energy)
m_phi_sq = 0.5 # 'Mass' squared term, controls steepness near minimum
lambda_phi = 0.05 # Quartic term for shape

# Define the potential V(Phi)
potential = rho_vac + 0.5 * m_phi_sq * phi_cip**2 + lambda_phi * phi_cip**4

# --- Plotting ---
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(8, 6))

ax.plot(phi_cip, potential, color='darkcyan', linewidth=2.5)

# Highlight the minimum
min_phi = 0
min_v = rho_vac
ax.scatter(min_phi, min_v, color='red', s=80, zorder=10, label=r'$V(0) = \rho_{vac}$ (Dark Energy)')
ax.axhline(min_v, color='red', linestyle=':', linewidth=1, alpha=0.7)

# --- Labels and Annotations ---
ax.set_xlabel(r'Cosmic Attentiveness Field ($\Phi_{CIP}$)', fontsize=12)
ax.set_ylabel(r"Potential Energy 'Cost' $V(\Phi_{CIP})$", fontsize=12)
ax.set_title('Figure 1: The Potential of Cosmic Indifference', fontsize=14, fontweight='bold')

ax.annotate('Maximum Indifference\n(Lowest Effort State)',
            xy=(min_phi, min_v),
            xytext=(min_phi, min_v + (np.max(potential)-min_v)*0.3), # Position text above minimum
            ha='center', va='center',
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0", color='black'),
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.9),
            fontsize=10)

ax.text(phi_cip[-1]*0.9, potential[-1]*0.9, 'Increasing\n"Effort"',
        ha='right', va='top', fontsize=10, style='italic', color='gray')
ax.text(phi_cip[0]*0.9, potential[0]*0.9, 'Increasing\n"Effort"',
        ha='left', va='top', fontsize=10, style='italic', color='gray')


ax.legend(fontsize=10)
ax.grid(True, linestyle='--', alpha=0.6)
ax.set_ylim(bottom=0) # Start y-axis near zero or slightly below rho_vac

plt.tight_layout()
plt.savefig('cip_figure1_potential.png', dpi=300)
plt.show()
import matplotlib.pyplot as plt
import numpy as np

# --- Define Regions and Curves (Schematic) ---
x = np.linspace(-2, 2, 400) # Control Parameter (Stress/Pressure)
y = np.linspace(0, 1, 400) # Alignment with I
X, Y = np.meshgrid(x, y)

# Define boundary curves schematically (e.g., based on cusp catastrophe folds)
# Coexistence curve (Boundary ∂I) - approx cubic root for cusp projection
coexistence_upper = 0.5 + np.sqrt(np.maximum(0, -X/1.5)) * 0.5
coexistence_lower = 0.5 - np.sqrt(np.maximum(0, -X/1.5)) * 0.5

# Spinodal curves (limits of metastability) - slightly inside coexistence
spinodal_upper = 0.5 + np.sqrt(np.maximum(0, -X/1.0)) * 0.35 # Adjust factors
spinodal_lower = 0.5 - np.sqrt(np.maximum(0, -X/1.0)) * 0.35

# Critical Point
xc, yc = 0.0, 0.5

# --- Plotting ---
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(10, 7))

# Plot curves
ax.plot(x[x<=xc], coexistence_upper[0, x<=xc], color='black', lw=2.5, label=r'Boundary $\partial\mathbf{I}$ (Coexistence)')
ax.plot(x[x<=xc], coexistence_lower[0, x<=xc], color='black', lw=2.5)
ax.plot(x[x<=xc], spinodal_upper[0, x<=xc], color='dimgrey', lw=1.5, linestyle='--', label='Spinodal Limit (Instability)')
ax.plot(x[x<=xc], spinodal_lower[0, x<=xc], color='dimgrey', lw=1.5, linestyle='--')

# Mark Critical Point
ax.scatter(xc, yc, color='red', s=100, zorder=10, label='Critical Point (Field Collapse?)')

# Shade and label regions (Phases)
ax.fill_between(x[x<=xc], coexistence_upper[0, x<=xc], 1.0, color='lightblue', alpha=0.2)
ax.text(-1.0, 0.85, r'Stable $\mathbf{In}$-ness Phase', ha='center', color='darkblue', fontsize=11)

ax.fill_between(x[x<=xc], 0.0, coexistence_lower[0, x<=xc], color='salmon', alpha=0.2)
ax.text(-1.0, 0.15, r'Stable $\mathbf{Out}$-ness Phase', ha='center', color='darkred', fontsize=11)

ax.fill_between(x[x<=xc], coexistence_lower[0, x<=xc], spinodal_lower[0, x<=xc], color='pink', alpha=0.3)
ax.fill_between(x[x<=xc], spinodal_upper[0, x<=xc], coexistence_upper[0, x<=xc], color='lightcyan', alpha=0.3)
ax.text(-0.5, 0.65, 'Metastable\n$\mathbf{In}$', ha='center', va='center', fontsize=8, color='grey')
ax.text(-0.5, 0.35, 'Metastable\n$\mathbf{Out}$', ha='center', va='center', fontsize=8, color='grey')

ax.text(1.0, 0.5, 'Supercritical Region\n(Blurred In/Out?)', ha='center', va='center', fontsize=10, color='purple', style='italic')


# Add hypothetical transition paths ('Isotherms')
x_iso = np.linspace(-1.8, 1.8, 50)
ax.plot(x_iso, 0.15 + 0.7 * (1 + np.tanh(x_iso*1.5))/2, color='green', linestyle=':', lw=1, label='Assimilation Path') # Transition from Out to In
ax.plot(x_iso, 0.85 - 0.7 * (1 + np.tanh(x_iso*1.5))/2, color='orange', linestyle=':', lw=1, label='Marginalization Path') # Transition from In to Out


# --- Labels and Title ---
ax.set_xlabel('Control Parameter (e.g., External Pressure / Stress)', fontsize=12)
ax.set_ylabel('Degree of Performative Alignment with $\mathbf{I}$', fontsize=12)
ax.set_title("Figure 2: Hypothetical 'Social Phase Space' of In/Out-ness under ANI", fontsize=14, fontweight='bold')
ax.set_ylim(0, 1)
ax.set_xlim(-2.1, 2.1)
ax.legend(fontsize=9, loc='center left', bbox_to_anchor=(1.01, 0.5)) # Legend outside
ax.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout(rect=[0, 0, 0.85, 1]) # Adjust right margin for legend
plt.savefig('ani_figure2_phase_inspired.png', dpi=300)
plt.show()
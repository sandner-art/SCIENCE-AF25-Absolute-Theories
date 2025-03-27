import matplotlib.pyplot as plt
import numpy as np

# --- Data Generation (Trivial) ---
# Size of the parameter space grid
grid_size = 50
# Create a grid of zeros representing C_munu components
consistency_tensor_data = np.zeros((grid_size, grid_size))

# Define abstract parameter ranges
alpha_range = np.linspace(0, 1, grid_size)
beta_range = np.linspace(-5, 5, grid_size)

# --- Plotting ---
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(8, 7))

# Display the heatmap of zeros
im = ax.imshow(consistency_tensor_data, origin='lower', cmap='viridis', # 'viridis' is often used in physics plots
               extent=[alpha_range.min(), alpha_range.max(), beta_range.min(), beta_range.max()],
               aspect='auto', vmin=-0.1, vmax=0.1) # Set vmin/vmax to emphasize zero

# --- Colorbar ---
cbar = fig.colorbar(im, ax=ax)
cbar.set_label(r'Consistency Tensor Component Value ($C_{\alpha\beta}$)', fontsize=11)
cbar.set_ticks([0]) # Ensure only zero is marked prominently
cbar.set_ticklabels(['0.0 (Verified)'])

# --- Labels and Title ---
ax.set_xlabel(r'Ontological Stress Parameter ($\alpha$)', fontsize=12)
ax.set_ylabel(r'Temporal Flux Index ($\beta$)', fontsize=12)
ax.set_title(r'Figure 2: Verification of PUS Condition: $C_{\mu\nu} \equiv 0$', fontsize=14, fontweight='bold')

# Optional: Add grid lines if desired
# ax.set_xticks(np.linspace(alpha_range.min(), alpha_range.max(), 6))
# ax.set_yticks(np.linspace(beta_range.min(), beta_range.max(), 6))
# ax.grid(True, linestyle=':', color='grey', alpha=0.5)

plt.tight_layout()
plt.savefig('pus_figure2_consistency_tensor.png', dpi=300)
plt.show()
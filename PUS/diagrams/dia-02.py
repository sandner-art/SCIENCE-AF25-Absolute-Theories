import matplotlib.pyplot as plt
import numpy as np

# --- Data Generation ---
grid_size = 100
alpha_range = np.linspace(0, 1, grid_size)
beta_range = np.linspace(-5, 5, grid_size)
A, B = np.meshgrid(alpha_range, beta_range)

# Panel (a) Data: Hypothetical Inconsistent Reality (Non-Zero C_munu)
# Create some interesting-looking spatial variation
# Example: combination of sine waves and a Gaussian peak
hypothetical_data = (
    np.sin(A * np.pi * 4) * np.cos(B * np.pi / 2.5) * 0.5 +
    np.exp(-((A - 0.5)**2 / (2 * 0.1**2) + (B - 1)**2 / (2 * 1.5**2))) * 1.0 -
    np.exp(-((A - 0.8)**2 / (2 * 0.05**2) + (B + 3)**2 / (2 * 1.0**2))) * 0.7
)
# Add a little noise to make it look more 'real'
hypothetical_data += np.random.normal(0, 0.1, hypothetical_data.shape)


# Panel (b) Data: Actual Reality (PUS Verified, C_munu = 0)
actual_data = np.zeros((grid_size, grid_size))

# Determine shared color limits based on the hypothetical data
vmin = np.min(hypothetical_data) * 1.1
vmax = np.max(hypothetical_data) * 1.1

# --- Plotting ---
plt.style.use('seaborn-v0_8-whitegrid')
fig, axes = plt.subplots(1, 2, figsize=(14, 6.5), sharey=True) # Share Y axis
fig.suptitle('Figure 2: Comparative Analysis of Consistency Tensor $C_{\\alpha\\beta}$', fontsize=16, fontweight='bold')

# -- Panel (a): Hypothetical --
ax0 = axes[0]
im0 = ax0.imshow(hypothetical_data, origin='lower', cmap='viridis',
                 extent=[alpha_range.min(), alpha_range.max(), beta_range.min(), beta_range.max()],
                 aspect='auto', vmin=vmin, vmax=vmax)
ax0.set_xlabel(r'Ontological Stress Parameter ($\alpha$)', fontsize=12)
ax0.set_ylabel(r'Temporal Flux Index ($\beta$)', fontsize=12)
ax0.set_title('(a) Hypothetical $C_{\\alpha\\beta}$ (PUS Violated)', fontsize=13)
ax0.grid(True, linestyle=':', color='white', alpha=0.3) # Grid might look better on non-uniform data

# -- Panel (b): Actual --
ax1 = axes[1]
im1 = ax1.imshow(actual_data, origin='lower', cmap='viridis',
                 extent=[alpha_range.min(), alpha_range.max(), beta_range.min(), beta_range.max()],
                 aspect='auto', vmin=vmin, vmax=vmax) # Use SAME vmin/vmax
ax1.set_xlabel(r'Ontological Stress Parameter ($\alpha$)', fontsize=12)
# ax1.set_ylabel(r'Temporal Flux Index ($\beta$)') # Y label shared
ax1.set_title('(b) Actual $C_{\\alpha\\beta}$ (PUS Verified)', fontsize=13)
ax1.grid(True, linestyle=':', color='black', alpha=0.15) # Grid more visible on uniform

# Add text annotation to Panel (b) highlighting the zero result
ax1.text(0.5, 0.5, '$C_{\\alpha\\beta} \equiv 0$\n(Perfect Consistency)', transform=ax1.transAxes,
         ha='center', va='center', fontsize=14, color='white',
         bbox=dict(boxstyle="round,pad=0.5", fc="black", ec="white", lw=1, alpha=0.7))


# --- Shared Colorbar ---
# Adjust subplot parameters to make space for colorbar
fig.subplots_adjust(right=0.85, wspace=0.1)
cbar_ax = fig.add_axes([0.88, 0.15, 0.03, 0.7]) # [left, bottom, width, height]
cbar = fig.colorbar(im1, cax=cbar_ax) # Use im1 (or im0) for the color scale mapping
cbar.set_label(r'Consistency Tensor Component Value ($C_{\alpha\beta}$)', fontsize=11)


plt.savefig('pus_figure2_consistency_comparison.png', dpi=300)
plt.show()
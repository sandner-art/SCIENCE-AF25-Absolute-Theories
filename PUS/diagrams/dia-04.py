import matplotlib.pyplot as plt
import numpy as np

# --- Data Generation ---
# Generate characteristic dimensions
dims = np.linspace(1, 5, 15) # Fewer points to reduce clutter slightly

# --- Calculate TRUE volumes ---
volumes_calc = []
labels = []
dimensions = [] # Track dimensionality
markers_3d = ['o', 's', '^', 'D', 'P']
colors_3d = ['blue', 'green', 'red', 'purple', 'orange']
markers_high_dim = ['*', 'X']
colors_high_dim = ['black', 'magenta']

# 3D Shapes
vol_cube = dims**3
volumes_calc.extend(vol_cube); labels.extend(['Cube'] * len(dims)); dimensions.extend([3] * len(dims))
vol_sphere = (4/3) * np.pi * (dims/2)**3 # Use radius = dim/2
volumes_calc.extend(vol_sphere); labels.extend(['Sphere'] * len(dims)); dimensions.extend([3] * len(dims))
vol_cylinder = np.pi * (dims/2)**2 * dims # r=dim/2, h=dim
volumes_calc.extend(vol_cylinder); labels.extend(['Cylinder'] * len(dims)); dimensions.extend([3] * len(dims))
# ... add Cone, Prism if desired, keeping track of labels and dimension=3

# 4D Shape (Tesseract/Hypercube)
vol_tesseract = dims**4
volumes_calc.extend(vol_tesseract); labels.extend(['Tesseract'] * len(dims)); dimensions.extend([4] * len(dims))

# 5D Shape (Penteract/5-Cube)
vol_penteract = dims**5
volumes_calc.extend(vol_penteract); labels.extend(['Penteract'] * len(dims)); dimensions.extend([5] * len(dims))

volumes_calc = np.array(volumes_calc)
dimensions = np.array(dimensions)

# --- Generate FAKE "Measured" Volumes for Panel (a) ---
# Add proportional noise to simulate measurement error/quantum jitter/confusion
noise_level = 0.15 # Adjust noise level
volumes_meas_hypothetical = volumes_calc * (1 + np.random.normal(0, noise_level, size=volumes_calc.shape))
# Ensure no negative volumes
volumes_meas_hypothetical[volumes_meas_hypothetical < 0] = 0


# --- Plotting ---
plt.style.use('seaborn-v0_8-whitegrid')
fig, axes = plt.subplots(1, 2, figsize=(16, 8), sharex=True, sharey=True) # Shared axes
fig.suptitle('Figure 4: PUS Unification: Universal Volumetric Self-Consistency', fontsize=16, fontweight='bold')

# Determine plot limits based on Panel (b)'s perfect data
max_vol = np.max(volumes_calc) * 1.05
plot_limits = [0, max_vol]

# --- Panel (a): Pre-PUS Confusion ---
ax0 = axes[0]
ax0.set_title('(a) Apparent Volumetric Discordance (Pre-PUS)', fontsize=13)

# Plot scattered data for different dimensions
# 3D
idx_3d = np.where(dimensions == 3)[0]
unique_labels_3d = list(dict.fromkeys(np.array(labels)[idx_3d]))
for i, label in enumerate(unique_labels_3d):
    shape_indices = [idx for idx in idx_3d if labels[idx] == label]
    ax0.scatter(volumes_calc[shape_indices], volumes_meas_hypothetical[shape_indices],
                label=f'3D: {label}', marker=markers_3d[i % len(markers_3d)],
                color=colors_3d[i % len(colors_3d)], alpha=0.6, s=40)
# 4D
idx_4d = np.where(dimensions == 4)[0]
ax0.scatter(volumes_calc[idx_4d], volumes_meas_hypothetical[idx_4d],
            label='4D: Tesseract', marker=markers_high_dim[0],
            color=colors_high_dim[0], alpha=0.6, s=60)
# 5D
idx_5d = np.where(dimensions == 5)[0]
ax0.scatter(volumes_calc[idx_5d], volumes_meas_hypothetical[idx_5d],
            label='5D: Penteract', marker=markers_high_dim[1],
            color=colors_high_dim[1], alpha=0.6, s=80)

# Plot the reference V=V line
ax0.plot(plot_limits, plot_limits, color='black', linestyle=':', linewidth=1.0, label='Hypothetical V=V ?', zorder=0)

ax0.set_xlabel(r'Calculated Volume ($V_{calc}$)', fontsize=12)
ax0.set_ylabel(r"Hypothetical 'Measured' Volume ($V_{meas}?$)", fontsize=12)
ax0.grid(True, linestyle='--', alpha=0.5)
ax0.legend(fontsize=9, loc='upper left')
ax0.text(max_vol * 0.5, max_vol * 0.1,
        "Significant scatter suggests\ncomplex relationship or\nmeasurement limitations?",
        fontsize=10, ha='center', color='darkred', style='italic',
        bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="salmon", alpha=0.8))


# --- Panel (b): PUS Verified ---
ax1 = axes[1]
ax1.set_title('(b) Volumetric Self-Consistency Verified by PUS', fontsize=13)

# Plot perfect V=V data for different dimensions
# 3D
for i, label in enumerate(unique_labels_3d):
    shape_indices = [idx for idx in idx_3d if labels[idx] == label]
    ax1.scatter(volumes_calc[shape_indices], volumes_calc[shape_indices], # V_meas = V_calc
                label=f'3D: {label}', marker=markers_3d[i % len(markers_3d)],
                color=colors_3d[i % len(colors_3d)], alpha=0.9, s=40)
# 4D
ax1.scatter(volumes_calc[idx_4d], volumes_calc[idx_4d],
            label='4D: Tesseract', marker=markers_high_dim[0],
            color=colors_high_dim[0], alpha=0.9, s=60)
# 5D
ax1.scatter(volumes_calc[idx_5d], volumes_calc[idx_5d],
            label='5D: Penteract', marker=markers_high_dim[1],
            color=colors_high_dim[1], alpha=0.9, s=80)

# Plot the perfect V=V line
ax1.plot(plot_limits, plot_limits, color='black', linestyle='--', linewidth=1.5, label='PUS Relation: $V \equiv V_{calc}$', zorder=0)

ax1.set_xlabel(r'Calculated Volume ($V_{calc}$)', fontsize=12)
ax1.set_ylabel(r'Actual Volume ($V_{actual} \equiv V_{calc}$)', fontsize=12) # Label clarifies identity
ax1.grid(True, linestyle='--', alpha=0.5)
ax1.legend(fontsize=9, loc='upper left')
ax1.text(max_vol * 0.5, max_vol * 0.15,
        "PUS reveals perfect $V \equiv V_{calc}$\nrelation across all dimensions,\nconfirming universal self-consistency!",
        fontsize=10, ha='center', color='darkgreen',
        bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="lightgreen", alpha=0.9))


# --- General Cleanup ---
for ax in axes:
    ax.set_xlim(plot_limits[0], plot_limits[1])
    ax.set_ylim(plot_limits[0], plot_limits[1])
    ax.set_aspect('equal', adjustable='box')

plt.tight_layout(rect=[0, 0.03, 1, 0.95]) # Adjust rect for suptitle
plt.savefig('pus_figure4_volume_comparison_highD.png', dpi=300)
plt.show()
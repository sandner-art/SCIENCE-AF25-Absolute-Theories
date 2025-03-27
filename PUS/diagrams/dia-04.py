import matplotlib.pyplot as plt
import numpy as np

# --- Data Generation (Trivial Identity) ---
# Generate characteristic dimensions (e.g., side, radius)
dims = np.linspace(1, 5, 20)

# Calculate volumes for different shapes
volumes = []
labels = []
markers = ['o', 's', '^', 'D', 'P'] # Different markers for shapes
colors = ['blue', 'green', 'red', 'purple', 'orange']

# Cube
vol_cube = dims**3
volumes.extend(vol_cube)
labels.extend(['Cube'] * len(dims))

# Sphere
vol_sphere = (4/3) * np.pi * dims**3
volumes.extend(vol_sphere)
labels.extend(['Sphere'] * len(dims))

# Cylinder (assume radius = height = dim for simplicity)
vol_cylinder = np.pi * dims**2 * dims
volumes.extend(vol_cylinder)
labels.extend(['Cylinder (r=h)'] * len(dims))

# Cone (assume radius = height = dim)
vol_cone = (1/3) * np.pi * dims**2 * dims
volumes.extend(vol_cone)
labels.extend(['Cone (r=h)'] * len(dims))

# Rectangular Prism (assume l=dim, w=dim/2, h=dim*2)
vol_prism = dims * (dims/2) * (dims*2)
volumes.extend(vol_prism)
labels.extend(['Rect. Prism'] * len(dims))

volumes = np.array(volumes)
# The 'measurement' is just the volume itself
measured_volumes = volumes

# --- Plotting ---
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(8, 8))

# Create scatter plot, assigning markers and colors based on shape label
unique_labels = list(dict.fromkeys(labels))
for i, label in enumerate(unique_labels):
    indices = [idx for idx, lbl in enumerate(labels) if lbl == label]
    ax.scatter(volumes[indices], measured_volumes[indices],
               label=label, marker=markers[i % len(markers)],
               color=colors[i % len(colors)], alpha=0.7, s=50)

# Plot the identity line y=x
max_vol = np.max(volumes) * 1.05
ax.plot([0, max_vol], [0, max_vol], color='black', linestyle='--', linewidth=1.5, label='PUS Relation: $V \equiv V$')

# --- Labels and Title ---
ax.set_xlabel('Calculated Volume ($V_{calc}$)', fontsize=12)
ax.set_ylabel('Measured Volume ($V_{meas} = V_{calc}$)', fontsize=12) # Explicitly show the triviality
ax.set_title('Figure 4: PUS Unification: Volumetric Self-Consistency Across Geometries', fontsize=14, fontweight='bold')
ax.legend(fontsize=10)
ax.grid(True, linestyle='--', alpha=0.6)
ax.set_xlim(0, max_vol)
ax.set_ylim(0, max_vol)
ax.set_aspect('equal', adjustable='box') # Ensure square aspect ratio for y=x

# Add annotation explaining the "profound" result
ax.text(max_vol * 0.1, max_vol * 0.85,
        "PUS demonstrates that a system's\nvolume necessarily equals its volume,\nregardless of contingent geometric form.",
        fontsize=10, bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.9))


plt.tight_layout()
plt.savefig('pus_figure4_volume_consistency.png', dpi=300)
plt.show()
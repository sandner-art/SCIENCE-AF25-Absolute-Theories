import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde # For a smoother density look

# --- Simulation Parameters ---
grid_res = 100 # Resolution for density calculation
n_interactions = 5000 # Number of simulated 'events'
boundary_width = 0.15 # How wide the boundary interaction zone is
boundary_center = 0.0 # Position of the boundary line (e.g., x=0)
in_region_x = [-1.5, boundary_center - boundary_width/2]
out_region_x = [boundary_center + boundary_width/2, 1.5]
boundary_region_x = [boundary_center - boundary_width/2, boundary_center + boundary_width/2]
y_range = [-1.5, 1.5]

# --- Simulate Interaction Points ---
# Generate points concentrated near the boundary
points_x = []
points_y = []

for _ in range(n_interactions):
    # Higher probability of interaction occurring IN the boundary zone
    if np.random.rand() < 0.7: # 70% chance in boundary
        x = np.random.uniform(boundary_region_x[0], boundary_region_x[1])
    # Lower probability deep in In or Out zones
    elif np.random.rand() < 0.85: # Next 15% chance near boundary (just outside)
         if np.random.rand() < 0.5:
             x = np.random.uniform(in_region_x[1] - boundary_width*0.5, in_region_x[1])
         else:
             x = np.random.uniform(out_region_x[0], out_region_x[0] + boundary_width*0.5)
    else: # Remaining 15% spread further out
        if np.random.rand() < 0.5:
            x = np.random.uniform(in_region_x[0], in_region_x[1] - boundary_width*0.5)
        else:
             x = np.random.uniform(out_region_x[0] + boundary_width*0.5, out_region_x[1])

    y = np.random.uniform(y_range[0], y_range[1])
    points_x.append(x)
    points_y.append(y)

points_x = np.array(points_x)
points_y = np.array(points_y)

# --- Calculate Density (using Gaussian KDE) ---
xy = np.vstack([points_x, points_y])
kde = gaussian_kde(xy, bw_method=0.15) # Adjust bw_method for smoothness

# Create grid points for evaluation
x_grid, y_grid = np.mgrid[in_region_x[0]:out_region_x[1]:complex(grid_res),
                          y_range[0]:y_range[1]:complex(grid_res)]
positions = np.vstack([x_grid.ravel(), y_grid.ravel()])
density = np.reshape(kde(positions).T, x_grid.shape)

# --- Plotting ---
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(10, 7))

# Display the density heatmap
im = ax.imshow(density, origin='lower', cmap='inferno', # 'inferno' or 'hot' often used for intensity
               extent=[in_region_x[0], out_region_x[1], y_range[0], y_range[1]],
               aspect='auto')

# --- Add Annotations and Boundaries ---
# Lines indicating nominal In/Out regions
ax.axvline(boundary_region_x[0], color='white', linestyle='--', linewidth=1.5, alpha=0.7)
ax.axvline(boundary_region_x[1], color='white', linestyle='--', linewidth=1.5, alpha=0.7)

# Text labels for regions
ax.text(np.mean(in_region_x), 0, r'Region of $\mathbf{In}$-ness', color='white', ha='center', va='center', fontsize=12, fontweight='bold', alpha=0.9)
ax.text(np.mean(out_region_x), 0, r'Region of $\mathbf{Out}$-ness', color='white', ha='center', va='center', fontsize=12, fontweight='bold', alpha=0.9)
ax.text(boundary_center, y_range[1]*0.85, r'Boundary Zone $\partial\mathbf{I}$' + '\n(High Interaction/Validation Intensity)',
        color='white', ha='center', va='top', fontsize=11, bbox=dict(fc='black', ec='white', alpha=0.6, pad=0.3))

# --- Colorbar ---
cbar = fig.colorbar(im, ax=ax)
cbar.set_label('Interaction / Validation Intensity (Arbitrary Units)', fontsize=11)

# --- Labels and Title ---
ax.set_xlabel('Socio-Spatial Dimension X', fontsize=12)
ax.set_ylabel('Symbolic Alignment Dimension Y', fontsize=12)
ax.set_title(r'Figure 3: Intensity Mapping of Boundary Work ($\partial\mathbf{I}$) under ANI', fontsize=14, fontweight='bold')
ax.set_ylim(y_range)
ax.set_xlim(in_region_x[0], out_region_x[1])

plt.tight_layout()
plt.savefig('ani_figure3_boundary_intensity.png', dpi=300)
plt.show()
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors
import matplotlib.patches as mpatches # For legend

# --- Simulation Parameters ---
grid_size = 90 # Larger grid for better visuals
n_steps = 700
initial_in_fraction = 0.05 # Start lower for more dramatic change
influence_strength = 0.75

# Colors for states
color_out = 'salmon'
color_in = 'lightblue'
cmap = mcolors.ListedColormap([color_out, color_in])

# --- Initialization ---
# States: 0 = Out, 1 = In
grid = np.random.choice([0, 1], size=(grid_size, grid_size),
                        p=[1 - initial_in_fraction, initial_in_fraction])
grid_history = {0: grid.copy()} # Store initial state

# --- Simulation Loop ---
for step in range(1, n_steps + 1):
    # Perform multiple updates per 'step' for faster convergence visual
    for _ in range(grid_size): # Heuristic number of updates
        x, y = np.random.randint(0, grid_size, 2)
        agent_state = grid[x, y]
        # Select a random neighbor (von Neumann neighborhood, periodic boundaries)
        neighbors = [
            grid[(x + 1) % grid_size, y], grid[(x - 1) % grid_size, y],
            grid[x, (y + 1) % grid_size], grid[x, (y - 1) % grid_size]
        ]
        neighbor_state = np.random.choice(neighbors)
        # Influence/Validation Rule (simplified):
        # Agent adopts neighbor's state with probability influence_strength if different
        if agent_state != neighbor_state:
            if np.random.rand() < influence_strength:
                grid[x, y] = neighbor_state

    # Store grid state at intermediate and final steps
    # Capture a state around 1/3rd of the way and the final state
    if step == n_steps // 3 or step == n_steps:
         grid_history[step] = grid.copy()

# --- Plotting (Triple Diagram) ---
plt.style.use('seaborn-v0_8-whitegrid')
fig, axes = plt.subplots(1, 3, figsize=(18, 6))
fig.suptitle('Figure 2: Simulated Trajectory of Axiomatic Convergence under ANI', fontsize=16, fontweight='bold')

time_points = sorted(grid_history.keys())
titles = [
    f'(a) Initial State (t={time_points[0]}, Low $\mathbf{{In}}$-ness)', # Braces around In just in case
    f'(b) Consolidation Phase (t={time_points[1]})',
    f'(c) Axiomatic Convergence (t={time_points[2]}, Dominant $\mathbf{{In}}$-ness)' # Braces around In just in case
]

for i, t in enumerate(time_points):
    ax = axes[i]
    im = ax.imshow(grid_history[t], cmap=cmap, interpolation='nearest', vmin=0, vmax=1)
    ax.set_title(titles[i], fontsize=12)
    ax.set_xticks([])
    ax.set_yticks([])

# Add a simple legend (using patches) - positioned relative to the figure
legend_patches = [mpatches.Patch(color=color_out, label=r'State $\mathbf{Out}$'),
                  mpatches.Patch(color=color_in, label=r'State $\mathbf{In}$')] # Use raw string for label
fig.legend(handles=legend_patches, loc='lower center', ncol=2, bbox_to_anchor=(0.5, 0.01), fontsize=11)

plt.tight_layout(rect=[0, 0.05, 1, 0.95]) # Adjust layout to prevent title overlap and leave space for legend
plt.savefig('ani_figure2_abm_convergence_triple.png', dpi=300)
plt.show()
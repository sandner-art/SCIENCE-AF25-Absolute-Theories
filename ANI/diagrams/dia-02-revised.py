import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors
import matplotlib.patches as mpatches # For legend

# --- Simulation Parameters ---
grid_size = 50
n_steps = 2000 # Increased steps
initial_in_fraction = 0.4 # Increased initial In fraction
initial_doubt_fraction = 0.02
influence_strength = 0.4 # Moderate influence
resolve_doubt_prob = 0.6

# --- States and Colors ---
STATE_OUT = 0
STATE_IN = 1
STATE_DOUBT = 2
color_out = 'salmon'
color_in = 'lightblue'
color_doubt = 'lightyellow'
cmap = mcolors.ListedColormap([color_out, color_in, color_doubt])
norm = mcolors.BoundaryNorm([0, 1, 2, 3], cmap.N) # Ensures discrete colors map correctly

# --- Initialization ---
p_in = initial_in_fraction
p_doubt = initial_doubt_fraction
p_out = 1 - p_in - p_doubt
grid = np.random.choice([STATE_OUT, STATE_IN, STATE_DOUBT],
                        size=(grid_size, grid_size),
                        p=[p_out, p_in, p_doubt])
grid_history = {0: grid.copy()}
saved_steps = [0] # Keep track of saved steps

# --- Simulation Loop ---
for step in range(1, n_steps + 1):
    # Perform multiple updates per 'step'
    for _ in range(grid_size * grid_size // 4): # Update a fraction of agents each step
        x, y = np.random.randint(0, grid_size, 2)
        agent_state = grid[x, y]

        neighbors = [
            grid[(x + 1) % grid_size, y], grid[(x - 1) % grid_size, y],
            grid[x, (y + 1) % grid_size], grid[x, (y - 1) % grid_size]
        ]
        # Ensure neighbor is chosen randomly, avoid self? (Less important in large grid)
        valid_neighbors = [(nx, ny) for nx, ny in
                           [((x + 1) % grid_size, y), ((x - 1) % grid_size, y),
                            (x, (y + 1) % grid_size), (x, (y - 1) % grid_size)]]
        nx, ny = valid_neighbors[np.random.randint(len(valid_neighbors))]
        neighbor_state = grid[nx, ny]


        # --- Symmetric Influence Rules ---
        # 1. Doubting agent influenced?
        if agent_state == STATE_DOUBT:
            if neighbor_state != STATE_DOUBT and np.random.rand() < resolve_doubt_prob:
                grid[x, y] = neighbor_state # Adopt neighbor's definite state
        # 2. Non-doubting agent influenced by OPPOSITE definite state?
        elif (agent_state == STATE_IN and neighbor_state == STATE_OUT) or \
             (agent_state == STATE_OUT and neighbor_state == STATE_IN):
            if np.random.rand() < influence_strength:
                 grid[x, y] = STATE_DOUBT # Become doubting
        # 3. Agent influenced by SAME state or Doubting state: No change typically needed

    # Store grid state at key steps (e.g., initial, ~10%, ~50%, final)
    steps_to_save = [n_steps // 10, n_steps // 2, n_steps]
    if step in steps_to_save and step not in saved_steps:
        grid_history[step] = grid.copy()
        saved_steps.append(step)

# Ensure we have the specific steps we intended, adding the last if needed
final_steps = [0, n_steps // 10, n_steps] # Target steps for display
actual_saved_steps = sorted(grid_history.keys())
time_points = []
# Try to get closest saved step to target steps
for target_step in final_steps:
    best_step = min(actual_saved_steps, key=lambda s: abs(s - target_step))
    if best_step not in time_points: # Avoid duplicates if targets are close
        time_points.append(best_step)
# Make sure we have 3 unique points, maybe adding mid-point if needed
if len(time_points) < 3 and n_steps // 2 in actual_saved_steps and n_steps // 2 not in time_points:
    time_points.insert(1, n_steps // 2)
time_points = sorted(time_points[:3]) # Ensure sorted and max 3


# --- Plotting (Triple Diagram) ---
plt.style.use('seaborn-v0_8-whitegrid')
fig, axes = plt.subplots(1, 3, figsize=(18, 6.5))
fig.suptitle('Figure 2: Simulated Trajectory of Axiomatic Convergence under ANI (with Doubting State)', fontsize=16, fontweight='bold')

titles = [
    f'(a) Initial State (t={time_points[0]})',
    f'(b) Consolidation Phase (t={time_points[1]})',
    f'(c) Near Convergence (t={time_points[2]})'
]

for i, t in enumerate(time_points):
    ax = axes[i]
    # Use vmin/vmax and norm with imshow for discrete colormap
    im = ax.imshow(grid_history[t], cmap=cmap, norm=norm, interpolation='nearest')
    ax.set_title(titles[i], fontsize=13)
    ax.set_xticks([])
    ax.set_yticks([])
    # Remove internal grid lines inherent to imshow pixels if desired (usually off by default)
    # ax.grid(False) # Explicitly turn off grid if it appears

# Add legend
legend_patches = [mpatches.Patch(color=color_out, label=r'State $\mathbf{Out}$'),
                  mpatches.Patch(color=color_in, label=r'State $\mathbf{In}$'),
                  mpatches.Patch(color=color_doubt, label='State Doubting / $\partial\mathbf{I}$')]
fig.legend(handles=legend_patches, loc='lower center', ncol=3, bbox_to_anchor=(0.5, 0.05), fontsize=11, frameon=False) # Place slightly higher, no frame

plt.tight_layout(rect=[0, 0.08, 1, 0.95]) # Adjust rect bottom for legend
plt.savefig('ani_figure2_abm_convergence_triple_3state_revised.png', dpi=300)
plt.show()
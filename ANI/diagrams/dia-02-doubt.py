import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors
import matplotlib.patches as mpatches # For legend

# --- Simulation Parameters ---
grid_size = 25
n_steps = 50 # Maybe more steps to show final state more clearly
initial_in_fraction = 0.05
initial_doubt_fraction = 0.02 # Small fraction start as doubting
influence_strength = 0.4 # Probability to change state if influenced
resolve_doubt_prob = 0.6 # Probability doubting agent adopts neighbor state

# --- States and Colors ---
STATE_OUT = 0
STATE_IN = 1
STATE_DOUBT = 2
color_out = 'salmon'
color_in = 'lightblue'
color_doubt = 'lightyellow' # Or 'lightgrey'
cmap = mcolors.ListedColormap([color_out, color_in, color_doubt])

# --- Initialization ---
p_in = initial_in_fraction
p_doubt = initial_doubt_fraction
p_out = 1 - p_in - p_doubt
grid = np.random.choice([STATE_OUT, STATE_IN, STATE_DOUBT],
                        size=(grid_size, grid_size),
                        p=[p_out, p_in, p_doubt])
grid_history = {0: grid.copy()}

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
        neighbor_state = np.random.choice(neighbors)

        # --- Revised Influence Rules ---
        # 1. Doubting agent influenced?
        if agent_state == STATE_DOUBT:
            if neighbor_state != STATE_DOUBT and np.random.rand() < resolve_doubt_prob:
                grid[x, y] = neighbor_state # Adopt neighbor's definite state
        # 2. Non-doubting agent influenced by OPPOSITE definite state?
        elif (agent_state == STATE_IN and neighbor_state == STATE_OUT) or \
             (agent_state == STATE_OUT and neighbor_state == STATE_IN):
            if np.random.rand() < influence_strength:
                 grid[x, y] = STATE_DOUBT # Become doubting
        # 3. Non-doubting agent influenced by SAME definite state or by Doubting state: No change

    # Store grid state at key steps
    if step == n_steps // 10 or step == n_steps // 2 or step == n_steps:
        grid_history[step] = grid.copy()

# Ensure we have exactly 3 time points if simulation ended early or steps aligned
time_points = sorted(grid_history.keys())
if len(time_points) > 3: # Keep first, middle-ish, last
     time_points = [time_points[0], time_points[len(time_points)//2], time_points[-1]]
elif len(time_points) < 3: # Duplicate last if needed (shouldn't happen here)
     while len(time_points) < 3: time_points.append(time_points[-1])

# --- Plotting (Triple Diagram) ---
plt.style.use('seaborn-v0_8-whitegrid')
fig, axes = plt.subplots(1, 3, figsize=(18, 6.5)) # Slightly taller for legend room
fig.suptitle('Figure 2: Simulated Trajectory of Axiomatic Convergence under ANI (with Doubting State)', fontsize=16, fontweight='bold')


titles = [
    f'(a) Initial State (t={time_points[0]})',
    f'(b) Consolidation Phase (t={time_points[1]})',
    f'(c) Near Convergence (t={time_points[2]})' # Changed title slightly
]

for i, t in enumerate(time_points):
    ax = axes[i]
    # Use vmin=0, vmax=2 for the three states
    im = ax.imshow(grid_history[t], cmap=cmap, interpolation='nearest', vmin=0, vmax=2)
    ax.set_title(titles[i], fontsize=12)
    ax.set_xticks([])
    ax.set_yticks([])

# Add legend
legend_patches = [mpatches.Patch(color=color_out, label=r'State $\mathbf{Out}$'),
                  mpatches.Patch(color=color_in, label=r'State $\mathbf{In}$'),
                  mpatches.Patch(color=color_doubt, label='State Doubting / $\partial\mathbf{I}$')] # Label doubting state clearly
fig.legend(handles=legend_patches, loc='lower center', ncol=3, bbox_to_anchor=(0.5, 0.02), fontsize=11)

plt.tight_layout(rect=[0, 0.07, 1, 0.95]) # Adjust rect for suptitle and legend
plt.savefig('ani_figure2_abm_convergence_triple_3state.png', dpi=300)
plt.show()
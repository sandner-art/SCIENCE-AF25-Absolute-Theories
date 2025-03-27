import matplotlib.pyplot as plt
import numpy as np

# --- Simple Simulation (Particles spreading in 2D box) ---
n_particles = 200
box_size = 10.0
n_steps = 25
move_std_dev = 0.5 # How much particles move each step

# Initial state: particles clustered in corner
particles = np.random.rand(n_particles, 2) * (box_size / 4) # Start in bottom-left quadrant
# Ensure no negative coords if needed, although periodic boundaries handle it
particles = np.clip(particles, 0, box_size)


history_pos = [particles.copy()]
history_entropy = []
history_cost = []

def calculate_metrics(pos):
    # Simple "Entropy": Proportional to variance of particle positions
    # Center positions around mean for variance calculation
    pos_centered = pos - np.mean(pos, axis=0)
    variance = np.mean(np.sum(pos_centered**2, axis=1)) # Mean squared distance from center
    entropy = np.log(variance + 1e-6) # Use log for better scaling, add small epsilon

    # Simple "Specification Cost": Inversely related to entropy/variance
    # Or could be related to concentration, e.g., 1 / mean_distance
    cost = 1.0 / (entropy + 1) # Simplistic inverse relationship

    return entropy, cost

entropy, cost = calculate_metrics(particles)
history_entropy.append(entropy)
history_cost.append(cost)

# Simulation loop
for step in range(n_steps):
    # Move particles randomly (random walk with periodic boundaries)
    moves = np.random.normal(0, move_std_dev, particles.shape)
    particles = (particles + moves) % box_size # Periodic boundary
    history_pos.append(particles.copy())

    entropy, cost = calculate_metrics(particles)
    history_entropy.append(entropy)
    history_cost.append(cost)

# Select steps for plotting snapshots
snap_indices = [0, n_steps // 3, n_steps]

# --- Plotting ---
plt.style.use('seaborn-v0_8-whitegrid')
# Create figure with 2 rows: top row for snapshots, bottom row for time series
fig = plt.figure(figsize=(12, 8.5))
gs = fig.add_gridspec(2, 3, height_ratios=[1, 1]) # 2 rows, 3 cols in top row

# Panel (a): Snapshots
ax_snap1 = fig.add_subplot(gs[0, 0])
ax_snap2 = fig.add_subplot(gs[0, 1], sharex=ax_snap1, sharey=ax_snap1)
ax_snap3 = fig.add_subplot(gs[0, 2], sharex=ax_snap1, sharey=ax_snap1)
snap_axes = [ax_snap1, ax_snap2, ax_snap3]
snap_titles = [f't={snap_indices[0]} (Low Entropy)', f't={snap_indices[1]}', f't={snap_indices[2]} (High Entropy)']

for i, idx in enumerate(snap_indices):
    ax = snap_axes[i]
    ax.plot(history_pos[idx][:, 0], history_pos[idx][:, 1], 'o', color='darkorange', markersize=3, alpha=0.7)
    ax.set_title(snap_titles[i], fontsize=10)
    ax.set_xlim(0, box_size)
    ax.set_ylim(0, box_size)
    ax.set_aspect('equal', adjustable='box')
    ax.set_xticks([])
    ax.set_yticks([])
fig.text(0.5, 0.93, '(a) System Evolution Towards Uniformity', ha='center', fontsize=12)


# Panel (b): Time Series Metrics
ax_ts = fig.add_subplot(gs[1, :]) # Span all columns in second row
time = np.arange(n_steps + 1)

# Plot Entropy
color_entropy = 'blue'
ax_ts.plot(time, history_entropy, color=color_entropy, linewidth=2, label='Conventional Entropy (S)')
ax_ts.set_xlabel('Time ($t$)', fontsize=12)
ax_ts.set_ylabel('Entropy $S$ (arb. units)', color=color_entropy, fontsize=12)
ax_ts.tick_params(axis='y', labelcolor=color_entropy)
ax_ts.grid(True, linestyle='--', alpha=0.6)

# Plot Specification Cost on secondary y-axis
ax_cost = ax_ts.twinx() # instantiate a second axes that shares the same x-axis
color_cost = 'red'
ax_cost.plot(time, history_cost, color=color_cost, linestyle='--', linewidth=2, label='CIP Specification Cost')
ax_cost.set_ylabel("CIP 'Effort' / Specification Cost", color=color_cost, fontsize=12)
ax_cost.tick_params(axis='y', labelcolor=color_cost)

fig.legend(loc='center right', bbox_to_anchor=(0.85, 0.25), fontsize=10) # Manual legend placement
ax_ts.set_title('(b) Thermodynamic Evolution vs. CIP Cost', fontsize=12, pad=15) # Add padding


plt.tight_layout(rect=[0, 0, 1, 0.92]) # Adjust overall layout
plt.savefig('cip_figure3_entropy_cost.png', dpi=300)
plt.show()
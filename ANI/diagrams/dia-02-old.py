import matplotlib.pyplot as plt
import numpy as np

# --- Simulation Parameters ---
grid_size = 30 # Size of the agent grid (N x N)
n_steps = 100 # Number of simulation steps
initial_in_fraction = 0.1 # Initial fraction of agents in state 'In' (1)
influence_strength = 0.3 # Probability of adopting neighbor's state

# --- Initialization ---
# States: 0 = Out, 1 = In
grid = np.random.choice([0, 1], size=(grid_size, grid_size),
                        p=[1 - initial_in_fraction, initial_in_fraction])
in_proportion_history = [np.mean(grid)]

# --- Simulation Loop ---
for step in range(n_steps):
    # Select a random agent
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

    # Record proportion of 'In' state
    in_proportion_history.append(np.mean(grid))

# --- Plotting ---
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(10, 6))

time = np.arange(n_steps + 1)
ax.plot(time, in_proportion_history, label='Proportion of Agents in State $\mathbf{In}$', color='darkblue', linewidth=2)
ax.plot(time, 1 - np.array(in_proportion_history), label='Proportion of Agents in State $\mathbf{Out}$', color='salmon', linestyle='--', linewidth=2)

# --- Labels and Title ---
ax.set_xlabel('Time (Simulation Steps)', fontsize=12)
ax.set_ylabel('Proportion of Agent Population', fontsize=12)
ax.set_ylim(-0.05, 1.05)
ax.set_title('Figure 2: Agent-Based Simulation of Axiomatic Convergence under ANI', fontsize=14, fontweight='bold')
ax.legend(fontsize=10)
ax.grid(True, linestyle='--', alpha=0.6)

# Add annotation about the process
ax.text(n_steps * 0.5, 0.6,
        'Performative validation &\ninfluence lead to rapid\nconsolidation of dominant\n$\mathbf{In}$-ness configuration.',
        ha='center', va='center', fontsize=10,
        bbox=dict(boxstyle="round,pad=0.3", fc="lightblue", ec="gray", alpha=0.8))

plt.tight_layout()
plt.savefig('ani_figure2_abm_convergence.png', dpi=300)
plt.show()
import matplotlib.pyplot as plt
import numpy as np

# --- Cusp Catastrophe Model Visualization ---
# Potential V = x^4/4 + a*x^2/2 + b*x
# Equilibrium surface: V' = x^3 + a*x + b = 0
# We'll plot trajectories on the equilibrium surface projected onto (a, x) plane
# 'a' represents a control parameter (e.g., external pressure, internal contradiction)
# 'b' represents an asymmetry factor (e.g., bias towards one state)
# 'x' represents the system state (e.g., Alignment with Is-ness A vs B)

a = np.linspace(-2, 2, 400)
x = np.linspace(-2, 2, 400)
A, X = np.meshgrid(a, x)

# Equilibrium condition: b = -X^3 - A*X
B = -X**3 - A*X

# --- Simulation of Trajectories ---
# Define a simple dynamics dx/dt = -dV/dx = -(x^3 + a*x + b)
# We simulate the state 'x' changing as 'a' slowly varies, keeping 'b' slightly non-zero

def simulate_trajectory(a_start, a_end, b_bias, x_initial, n_steps=200):
    a_path = np.linspace(a_start, a_end, n_steps)
    x_path = np.zeros(n_steps)
    x_path[0] = x_initial
    dt_sim = 0.1 # Simulation time step adjustment factor

    for i in range(n_steps - 1):
        current_a = a_path[i]
        current_x = x_path[i]
        # Simple Euler integration for dx/dt = -(x^3 + a*x + b)
        dx = -(current_x**3 + current_a*current_x + b_bias)
        x_path[i+1] = current_x + dx * dt_sim
        # Add constraint to stay roughly within plot bounds if needed
        x_path[i+1] = np.clip(x_path[i+1], -2.1, 2.1)
    return a_path, x_path

# Simulate forward path (potential In -> Out flip)
b_bias_forward = 0.1 # Slight bias
a_fwd, x_fwd = simulate_trajectory(-2, 1.0, b_bias_forward, 1.5) # Start in upper stable branch
perturb_point_idx = np.where(a_fwd >= 0.5)[0][0] # Point where 'a' causes jump

# Simulate backward path (potential Out -> In flip)
b_bias_backward = -0.1 # Slight opposite bias
a_bwd, x_bwd = simulate_trajectory(2, -1.0, b_bias_backward, -1.5) # Start in lower stable branch
perturb_point_idx_bwd = np.where(a_bwd <= -0.5)[0][0]


# --- Plotting ---
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(10, 7))

# Plot the equilibrium surface projection (bifurcation diagram)
# Where V''=0 => 3x^2 + a = 0 => a = -3x^2 (bifurcation points)
x_bif = np.linspace(-np.sqrt(2/3)*np.sqrt(2), np.sqrt(2/3)*np.sqrt(2), 200) # x range for bifurcation
a_bif = -3 * x_bif**2
# Sort for plotting dashed line
sort_idx = np.argsort(a_bif)
ax.plot(a_bif[sort_idx], x_bif[sort_idx], color='grey', linestyle='--', linewidth=1.5, label='Bifurcation Points ($V\'\'=0$)')

# Plot stable branches (implicitly defined by B equation, tricky to plot directly)
# Instead, we shade regions or just show trajectories
ax.axhline(0, color='gray', lw=0.5, linestyle=':') # Guide line

# Plot the simulated trajectories demonstrating the jumps
ax.plot(a_fwd, x_fwd, color='blue', linewidth=2.5, label='Trajectory (e.g., $\mathbf{In}_A \to \mathbf{Out}_A$)')
ax.plot(a_bwd, x_bwd, color='red', linewidth=2.5, linestyle='-.', label='Trajectory (e.g., $\mathbf{Out}_A \to \mathbf{In}_A$)')

# Highlight the jump points (Ontological Inversion Events)
ax.scatter(a_fwd[perturb_point_idx], x_fwd[perturb_point_idx], color='black', s=80, zorder=10, marker='*')
ax.annotate('Ontological\nInversion Event\n($\mathbf{In} \to \mathbf{Out}$)',
            xy=(a_fwd[perturb_point_idx], x_fwd[perturb_point_idx]),
            xytext=(a_fwd[perturb_point_idx] + 0.4, x_fwd[perturb_point_idx] - 0.5),
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0.3"), fontsize=10)

ax.scatter(a_bwd[perturb_point_idx_bwd], x_bwd[perturb_point_idx_bwd], color='black', s=80, zorder=10, marker='*')
ax.annotate('Ontological\nInversion Event\n($\mathbf{Out} \to \mathbf{In}$)',
            xy=(a_bwd[perturb_point_idx_bwd], x_bwd[perturb_point_idx_bwd]),
            xytext=(a_bwd[perturb_point_idx_bwd] - 0.4, x_bwd[perturb_point_idx_bwd] + 0.5),
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=-0.3"), fontsize=10)


# --- Labels and Title ---
ax.set_xlabel('Control Parameter $a$ (e.g., External Pressure / Internal Stress)', fontsize=12)
ax.set_ylabel('System State $x$ (e.g., Alignment with $\mathbf{I}_A$)', fontsize=12)
ax.set_title('Figure 4: Simulated Ontological Inversion Event (Axial Realignment) under ANI', fontsize=14, fontweight='bold')
ax.legend(fontsize=10, loc='lower right')
ax.grid(True, linestyle='--', alpha=0.6)
ax.set_ylim(-2.5, 2.5)
ax.set_xlim(-2.2, 2.2)

plt.tight_layout()
plt.savefig('ani_figure4_inversion_event.png', dpi=300)
plt.show()
import matplotlib.pyplot as plt
import numpy as np

# --- Simulation Parameters ---
t = np.linspace(0, 10, 200)

# Define a simple, smooth trajectory for the Actual World W@
# Using a simple sine wave for illustration
state_var1_w_at = t
state_var2_w_at = np.sin(t * 1.5) * 5

# Define some chaotic/diverging trajectories for Hypothetical Worlds W'
# Example 1: Simple diverging path
state_var1_w_prime1 = t
state_var2_w_prime1 = 0.5 * t**2 - 2

# Example 2: More chaotic path (simple simulation)
state_var1_w_prime2 = np.zeros_like(t)
state_var2_w_prime2 = np.zeros_like(t)
x, y = 0.1, 0.1
dt = t[1] - t[0]
for i in range(len(t)):
    state_var1_w_prime2[i] = x
    state_var2_w_prime2[i] = y
    # Simple chaotic map (adjust parameters for different looks)
    x_new = np.sin(y * 2.5) + 0.8 * x
    y_new = np.cos(x * 1.8) - 0.7 * y
    x, y = x_new, y_new


# --- Plotting ---
plt.style.use('seaborn-v0_8-whitegrid') # Use a clean style
fig, ax = plt.subplots(figsize=(10, 7))

# Plot W@ prominently
ax.plot(state_var1_w_at, state_var2_w_at, label=r'$W_{@}$: Actual World Trajectory', color='blue', linewidth=2.5, zorder=10)

# Plot W' less prominently
ax.plot(state_var1_w_prime1, state_var2_w_prime1, label=r"$W'_{1}$: Hypothetical (Excluded by PUS)", color='red', linestyle='--', linewidth=1, alpha=0.7)
ax.plot(state_var1_w_prime2, state_var2_w_prime2, label=r"$W'_{2}$: Hypothetical (Excluded by PUS)", color='green', linestyle=':', linewidth=1, alpha=0.7)

# Highlight a point on W@ and add the "State Fidelity" annotation
mid_point_idx = len(t) // 2
mid_x = state_var1_w_at[mid_point_idx]
mid_y = state_var2_w_at[mid_point_idx]
ax.scatter(mid_x, mid_y, color='blue', s=50, zorder=11)
ax.annotate(r'$\mathcal{F}_{@}(S_{@}) = S_{@}$' + '\n(PUS State Fidelity)',
            xy=(mid_x, mid_y),
            xytext=(mid_x + 1.5, mid_y - 3),
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=-0.2", color='black'),
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.9),
            fontsize=10)


# --- Labels and Title ---
ax.set_xlabel('Abstract State Variable 1 ($\chi_1$)', fontsize=12)
ax.set_ylabel('Abstract State Variable 2 ($\chi_2$)', fontsize=12)
ax.set_title('Figure 1: State Space Trajectory under PUS Constraint', fontsize=14, fontweight='bold')
ax.legend(fontsize=10)
ax.grid(True, linestyle='--', alpha=0.6)

# Adjust limits for better visualization if needed
# ax.set_xlim(...)
# ax.set_ylim(...)

plt.tight_layout()
plt.savefig('pus_figure1_state_trajectory.png', dpi=300)
plt.show()
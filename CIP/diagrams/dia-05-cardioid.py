import matplotlib.pyplot as plt
import numpy as np

# --- Parameters ---
theta = np.linspace(0, 2 * np.pi, 400)
a = 1.0 # Controls cardioid size

# --- Plotting Setup ---
plt.style.use('seaborn-v0_8-whitegrid')
# Create a 2x2 grid of polar subplots
fig, axes = plt.subplots(2, 2, figsize=(11, 10), subplot_kw={'projection': 'polar'})
fig.suptitle('Figure X: CIP Effort Landscapes in Abstract State Space', fontsize=16, fontweight='bold')

# --- Panel (a): Baseline Indifference Landscape ---
ax0 = axes[0, 0]
r_base = a * (1 - np.cos(theta))
ax0.plot(theta, r_base, color='darkcyan', lw=2)
ax0.fill(theta, r_base, color='darkcyan', alpha=0.2) # Fill for visual appeal
ax0.set_title('(a) Baseline Indifference\n(Min Effort at $\\theta=0$)', fontsize=11)
ax0.set_rticks([0, a, 2*a]) # Radius ticks
ax0.set_rlabel_position(22.5) # Move radial labels
ax0.grid(True, linestyle='--', alpha=0.5)
ax0.annotate('Minimal Effort\n(Max Indifference)', xy=(0, 0), xytext=(np.pi/2, a*1.5), # Text near center pointing outwards? Or point to cusp
             ha='center', bbox=dict(boxstyle="round,pad=0.3", fc="white", alpha=0.8), fontsize=9)
# Arrow pointing to cusp at theta=0
ax0.annotate('', xy=(0, 0), xytext=(np.pi/4, a*0.5),
             arrowprops=dict(arrowstyle="->", color='black', connectionstyle="arc3,rad=-0.3"))


# --- Panel (b): Effect of Matter/Complexity ---
ax1 = axes[0, 1]
# Add perturbations to the cardioid
r_matter = r_base + 0.2 * a * np.sin(theta * 5)**2 + 0.1 * a * np.cos(theta * 3)
ax1.plot(theta, r_matter, color='purple', lw=2)
# Simulate some 'data points' residing in higher-effort states
n_points_b = 10
theta_data_b = np.random.rand(n_points_b) * 2 * np.pi
# Data points radius based on perturbed cardioid + some noise upward
r_data_b = (a * (1 - np.cos(theta_data_b)) + 0.2 * a * np.sin(theta_data_b * 5)**2 + 0.1 * a * np.cos(theta_data_b * 3)) \
           + np.random.uniform(0.05, 0.25, n_points_b) * a
ax1.scatter(theta_data_b, r_data_b, color='red', s=40, zorder=10, label='States with Matter')
ax1.set_title('(b) Landscape Perturbed by Matter\n(Increased Local Effort)', fontsize=11)
ax1.set_rticks([0, a, 2*a])
ax1.set_rlabel_position(22.5)
ax1.grid(True, linestyle='--', alpha=0.5)
ax1.legend(loc='lower left', fontsize=8)


# --- Panel (c): Relaxation Trajectory ---
ax2 = axes[1, 0]
# Baseline cardioid for reference
ax2.plot(theta, r_base, color='darkcyan', lw=1, alpha=0.3)
# Simulate a spiral trajectory inwards towards (0,0)
t_traj = np.linspace(0, 10, 100)
r_traj = 1.8 * a * np.exp(-t_traj * 0.3) # Exponential decay for radius
theta_traj = 2.5 * t_traj + np.pi # Spiraling angle
# Ensure trajectory stops near the origin
r_traj[r_traj < 0.01] = 0
valid_traj_idx = np.where(r_traj > 0)[0] # Plot only non-zero radius part

ax2.plot(theta_traj[valid_traj_idx], r_traj[valid_traj_idx], color='orange', lw=2.5, linestyle='--')
# Add arrow head at the end near origin
end_idx = valid_traj_idx[-1] if len(valid_traj_idx)>0 else 0
start_idx = valid_traj_idx[-2] if len(valid_traj_idx)>1 else end_idx
if end_idx != start_idx: # Ensure start/end are different
    ax2.annotate('', xy=(theta_traj[end_idx], r_traj[end_idx]),
                 xytext=(theta_traj[start_idx], r_traj[start_idx]),
                 arrowprops=dict(arrowstyle="->", color='orange', lw=2.0))

ax2.set_title('(c) Relaxation Trajectory\n(Towards Minimal Effort Cusp)', fontsize=11)
ax2.set_rticks([0, a, 2*a])
ax2.set_rlabel_position(22.5)
ax2.grid(True, linestyle='--', alpha=0.5)


# --- Panel (d): "Forbidden" High-Effort States ---
ax3 = axes[1, 1]
# Baseline cardioid
ax3.plot(theta, r_base, color='darkcyan', lw=1.5, alpha=0.8)
# Shade high-effort region (large radius)
ax3.fill_between(theta, 1.5*a, 2.5*a, color='salmon', alpha=0.4, label='High Effort Region (Disfavored)')
# Hypothetical points for complex theories
theta_complex = [np.pi*0.8, np.pi*1.2, np.pi*1.8]
r_complex = [1.8*a, 2.0*a, 1.7*a]
ax3.scatter(theta_complex, r_complex, color='black', marker='X', s=80, label='Hypothetical Complex States\n(e.g., String Theory Vacua?)', zorder=10)
ax3.set_title('(d) Disfavored High-Effort States\n(CIP Penalty)', fontsize=11)
ax3.set_rticks([0, a, 2*a])
ax3.set_rlabel_position(22.5)
ax3.grid(True, linestyle='--', alpha=0.5)
# Set radial limit to emphasize outer region
ax3.set_ylim(0, 2.6*a)
ax3.legend(loc='lower right', fontsize=8)


# --- Final Adjustments ---
plt.tight_layout(rect=[0, 0, 1, 0.94]) # Adjust for suptitle
plt.savefig('cip_figure_polar_landscapes.png', dpi=300)
plt.show()
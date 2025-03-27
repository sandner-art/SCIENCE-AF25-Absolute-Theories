import matplotlib.pyplot as plt
import numpy as np

# --- Define Regions and Trajectories (Schematic) ---
time_param = np.linspace(0, 10, 200) # Abstract time/expansion parameter
energy_complexity = np.linspace(0, 10, 200) # Abstract energy/complexity scale
T, E = np.meshgrid(time_param, energy_complexity)

# Define effort zones (simple boundaries for illustration)
low_effort_limit = 1.5 + 0.1 * T # Low effort zone expands slightly
mid_effort_limit = 4.0 + 0.5 * T * np.exp(-T*0.3) # Mid zone shrinks

# Create a grid of effort levels
effort_levels = np.zeros_like(T)
effort_levels[E < low_effort_limit] = 1  # Low effort zone
effort_levels[(E >= low_effort_limit) & (E < mid_effort_limit)] = 2  # Mid effort zone
effort_levels[E >= mid_effort_limit] = 3  # High effort zone

# --- Plotting ---
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(10, 7))

# Contour plot for effort levels
contour = ax.contourf(T, E, effort_levels, levels=[0, 1, 2, 3], colors=['lightcyan', 'lightyellow', 'mistyrose'], alpha=0.6)
proxy = [plt.Rectangle((0,0),1,1,fc = pc.get_facecolor()[0]) for pc in contour.collections]
proxy_labels = ['Low Effort Zone (Indifference Dominates)', 'Transient Effort Zone (Structure Cost)', 'High Effort Zone (Ontologically Disfavored)']
ax.legend(proxy, proxy_labels, fontsize=9, loc='upper right')

# Plot schematic trajectories (Relaxation)
# Trajectory 1: High energy start -> Low effort
t1 = np.linspace(1, 9, 50)
e1 = 7 * np.exp(-t1 * 0.4) + low_effort_limit[0, np.searchsorted(time_param, t1)] * 0.5
ax.plot(t1, e1, color='purple', lw=2, linestyle='-.', label='Relaxation Path (e.g., Early Universe)')
ax.arrow(t1[-2], e1[-2], t1[-1]-t1[-2], e1[-1]-e1[-2], head_width=0.3, head_length=0.2, fc='purple', ec='purple', lw=1)

# Trajectory 2: Structure formation -> eventual decay?
t2 = np.linspace(2, 10, 50)
e2_peak = mid_effort_limit[0, np.searchsorted(time_param, 4)] * 0.8
e2 = low_effort_limit[0, np.searchsorted(time_param, t2)] + (e2_peak - low_effort_limit[0, np.searchsorted(time_param, 4)]) * np.exp(-((t2-4)**2)/5) * 1.5 # Bump represents structure
ax.plot(t2, e2, color='orange', lw=2, linestyle='--', label='Structure Formation & Decay Path')
ax.arrow(t2[-2], e2[-2], t2[-1]-t2[-2], e2[-1]-e2[-2], head_width=0.3, head_length=0.2, fc='orange', ec='orange', lw=1)

# --- Labels and Title ---
ax.set_xlabel('Cosmic Time / Expansion Parameter $\longrightarrow$', fontsize=12)
ax.set_ylabel('Energy Density / Complexity / "Effort"', fontsize=12)
ax.set_title("Figure 2: Schematic 'Cosmic Effort' Phase Diagram under CIP", fontsize=14, fontweight='bold')
ax.set_ylim(0, 10)
ax.set_xlim(0, 10)
ax.grid(True, linestyle='--', alpha=0.6)

# Add Annotations for zones
ax.text(7, 1.0, 'Preferred State:\nHigh Entropy, QM Randomness,\nEmpty Space (Minimal Effort)', ha='center', color='darkblue', fontsize=9)
ax.text(5, 3.5, 'Transient Structures:\nStars, Galaxies, Life\n(Temporary Effort Cost)', ha='center', color='darkgoldenrod', fontsize=9)
ax.text(3, 8.0, 'Disfavored States:\nExtreme Densities, Fine-Tuning\n(High Effort Penalty)', ha='center', color='darkred', fontsize=9)

plt.tight_layout()
plt.savefig('cip_figure2_effort_phase_contour.png', dpi=300)
plt.show()

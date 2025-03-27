import matplotlib.pyplot as plt
import numpy as np

# --- Plotting ---
plt.style.use('seaborn-v0_8-ticks') # Use ticks for a more physics diagram feel
fig, axes = plt.subplots(1, 2, figsize=(12, 6))
fig.suptitle('Figure 4: CIP Simplification of Interaction Descriptions', fontsize=16, fontweight='bold')

common_ylim = (-1, 6)
common_xlim = (-1, 4)

# --- Panel (a): Standard Feynman Diagram ---
ax0 = axes[0]
ax0.set_title('(a) Standard Description (e.g., QED)', fontsize=13)

# Incoming particles (straight lines)
ax0.plot([0, 1.5], [0, 2.5], 'k-', lw=2) # Electron 1
ax0.plot([0, 1.5], [5, 2.5], 'k-', lw=2) # Electron 2

# Outgoing particles
ax0.plot([1.5, 3], [2.5, 0], 'k-', lw=2)
ax0.plot([1.5, 3], [2.5, 5], 'k-', lw=2)

# Propagator (photon - wavy line)
propagator_x = np.linspace(1.5, 1.5, 50) # Stays at x=1.5
propagator_y = np.linspace(2.5, 2.5, 50) # Doesn't move y either - ERROR NEEDED WAVE
# Let's draw a wavy line manually
n_waves = 5
x_wave = np.ones(50) * 1.5
y_wave = np.linspace(2.5, 2.5, 50) # Need to adjust y, not x
y_center = 2.5
x_center = 1.5
y_wave_points = np.linspace(1.5, 3.5, 50) # Y values for the photon path
x_wave_points = x_center + 0.2 * np.sin( (y_wave_points - y_wave_points[0]) / (y_wave_points[-1] - y_wave_points[0]) * n_waves * 2 * np.pi )
# Find interaction vertices approx
y_vertex1_idx = np.argmin(np.abs(y_wave_points-2.5))
y_vertex1 = y_wave_points[y_vertex1_idx]
x_vertex1 = x_wave_points[y_vertex1_idx]

# Redraw lines to meet at vertices (approximate visually)
ax0.plot([0, x_vertex1], [0, y_vertex1], 'k-', lw=2) # Electron 1 in
ax0.plot([0, x_vertex1], [5, y_vertex1], 'k-', lw=2) # Electron 2 in
ax0.plot([x_vertex1, 3], [y_vertex1, 0], 'k-', lw=2) # Electron 1 out
ax0.plot([x_vertex1, 3], [y_vertex1, 5], 'k-', lw=2) # Electron 2 out
ax0.plot(x_wave_points, y_wave_points, 'blue', linestyle=(0, (1, 1.5)), lw=2.5) # Dotted line for photon


# Labels
ax0.text(-0.2, 0, r'$e^-$', ha='right', va='center', fontsize=12)
ax0.text(-0.2, 5, r'$e^-$', ha='right', va='center', fontsize=12)
ax0.text(3.2, 0, r'$e^-$', ha='left', va='center', fontsize=12)
ax0.text(3.2, 5, r'$e^-$', ha='left', va='center', fontsize=12)
ax0.text(x_vertex1 + 0.1, y_vertex1, r'$\gamma$' + '\n(Virtual Photon:\nRequires Effort?)',
         ha='left', va='center', fontsize=10, color='blue')

ax0.set_xlabel('Space $\longrightarrow$', fontsize=10)
ax0.set_ylabel('Time $\longrightarrow$', fontsize=10)


# --- Panel (b): CIP Reduced Diagram ---
ax1 = axes[1]
ax1.set_title('(b) CIP Description (Minimal Effort)', fontsize=13)

# Incoming particles
ax1.plot([0, 3], [0, 0], 'k-', lw=2) # Combined input state 1
ax1.plot([0, 3], [5, 5], 'k-', lw=2) # Combined input state 2

# Simple interaction representation (Blurry arrow? Direct line?)
# Let's use a single 'effective interaction' line/blob
mid_x = 1.5
ax1.plot([0.5, 2.5], [2.5, 2.5], color='grey', lw=5, alpha=0.5, solid_capstyle='round')
ax1.text(mid_x, 2.5, 'Net Interaction\n(Minimal Effort Path)', ha='center', va='center', fontsize=9, color='dimgray')

# Outgoing particles (can be same lines continuing, or new ones starting after interaction)
# To emphasize net effect, let's just show initial/final states
ax1.text(-0.2, 0, r'Initial State', ha='right', va='center', fontsize=10)
ax1.text(-0.2, 5, r'(e.g., $e^-, e^-$)', ha='right', va='center', fontsize=10)
ax1.text(3.2, 0, r'Final State', ha='left', va='center', fontsize=10)
ax1.text(3.2, 5, r'(e.g., $e^-, e^-$)', ha='left', va='center', fontsize=10)

# Indicate elimination of virtual particle
ax1.text(mid_x, 4.0, "Virtual Particle $\gamma$\n'Integrated Out' by CIP\n(Too much effort!)",
         ha='center', va='center', fontsize=10, color='red', style='italic',
         bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="red", alpha=0.8))


ax1.set_xlabel('Abstract State Change $\longrightarrow$', fontsize=10)
# ax1.set_ylabel('Time $\longrightarrow$') # Shared Y

# --- Cleanup ---
for ax in axes:
    ax.set_ylim(common_ylim)
    ax.set_xlim(common_xlim)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(True)
    ax.spines['left'].set_visible(True)

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig('cip_figure4_feynman_reduction.png', dpi=300)
plt.show()
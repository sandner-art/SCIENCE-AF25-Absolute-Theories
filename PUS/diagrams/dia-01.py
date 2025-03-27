import matplotlib.pyplot as plt
import numpy as np

# --- Simulation Parameters ---
t_full = np.linspace(0, 10, 200)
t_short = np.linspace(0, 1.5, 30) # Shorter time for terminated paths

# --- Define Trajectories ---
start_point = np.array([0, 0])

# W@: Actual World (Stable Sinusoid)
state_var1_w_at = t_full
state_var2_w_at = np.sin(t_full * 1.5 + np.pi/2) * 3 # Start at peak for visual clarity

# W'1: Diverging Path
state_var1_w_prime1 = t_full
state_var2_w_prime1 = 0.5 * t_full**2

# W'2: Chaotic Snippet (using previous chaotic map)
state_var1_w_prime2 = np.zeros_like(t_full)
state_var2_w_prime2 = np.zeros_like(t_full)
x, y = start_point[0] + 0.01, start_point[1] + 0.01 # Start near origin
dt = t_full[1] - t_full[0]
for i in range(len(t_full)):
    state_var1_w_prime2[i] = x; state_var2_w_prime2[i] = y
    x_new = np.sin(y * 2.5) + 0.8 * x; y_new = np.cos(x * 1.8) - 0.7 * y
    x, y = x_new, y_new

# W'3: Decaying/Collapsing Path
state_var1_w_prime3 = t_full
state_var2_w_prime3 = np.exp(-t_full * 0.8) * 10 - 7 # Decays towards negative


# --- Plotting ---
plt.style.use('seaborn-v0_8-whitegrid')
fig, axes = plt.subplots(1, 2, figsize=(16, 7), sharex=True, sharey=True)
fig.suptitle('Figure 1: PUS Constraint on State Space Trajectory Selection', fontsize=16, fontweight='bold')

# --- Common Elements ---
node_color_actual = 'blue'
node_color_invalid = 'red'
node_color_chaotic = 'green'
node_color_decay = 'purple'
line_actual_style = {'color': node_color_actual, 'linewidth': 2.5, 'zorder': 10}
line_invalid_style = {'color': node_color_invalid, 'linestyle': '--', 'linewidth': 1.5, 'alpha': 0.8}
line_chaotic_style = {'color': node_color_chaotic, 'linestyle': ':', 'linewidth': 1.5, 'alpha': 0.8}
line_decay_style = {'color': node_color_decay, 'linestyle': '-.', 'linewidth': 1.5, 'alpha': 0.8}
label_fontsize = 10
termination_marker = 'x'
termination_color = 'black'
termination_size = 40

# --- Panel (a): Potential Dynamics (Pre-PUS) ---
ax0 = axes[0]
ax0.set_title('(a) Potential State Space Dynamics (Pre-PUS)', fontsize=13)

# Plot all trajectories fully
ax0.plot(state_var1_w_at, state_var2_w_at, **line_actual_style, label=r'Potential $W_{@}$')
ax0.plot(state_var1_w_prime1, state_var2_w_prime1, **line_invalid_style, label=r'Potential $W^{\prime}_1$ (Diverging)')
ax0.plot(state_var1_w_prime2, state_var2_w_prime2, **line_chaotic_style, label=r'Potential $W^{\prime}_2$ (Chaotic)')
ax0.plot(state_var1_w_prime3, state_var2_w_prime3, **line_decay_style, label=r'Potential $W^{\prime}_3$ (Decaying)')

# Mark start point
ax0.scatter(start_point[0], start_point[1], color='black', s=60, zorder=11, label='Present State (t=0)')
ax0.legend(fontsize=9, loc='upper left')
ax0.set_xlabel(r'Abstract State Variable 1 ($\chi_1$)', fontsize=12)
ax0.set_ylabel(r'Abstract State Variable 2 ($\chi_2$)', fontsize=12)
ax0.grid(True, linestyle='--', alpha=0.6)

ax0.text(t_full[-1]*0.9, state_var2_w_prime1[-1]*0.9, "?", fontsize=20, color=node_color_invalid, ha='center', va='center')
ax0.text(t_full[-1]*0.5, state_var2_w_prime3[-1]*0.9, "?", fontsize=20, color=node_color_decay, ha='center', va='center')
ax0.text(state_var1_w_prime2[len(t_full)//2], state_var2_w_prime2[len(t_full)//2]-2, "?", fontsize=20, color=node_color_chaotic, ha='center', va='center')


# --- Panel (b): PUS Selection ---
ax1 = axes[1]
ax1.set_title('(b) Actual Trajectory Defined by PUS', fontsize=13)

# Plot only W@ fully and prominently
ax1.plot(state_var1_w_at, state_var2_w_at, **line_actual_style, label=r'$W_{@}$: Actual World Trajectory')

# Plot initial segments of other trajectories and termination markers
t_idx_short = len(t_short) - 1
ax1.plot(state_var1_w_prime1[:len(t_short)], state_var2_w_prime1[:len(t_short)], **line_invalid_style)
ax1.scatter(state_var1_w_prime1[t_idx_short], state_var2_w_prime1[t_idx_short], marker=termination_marker, color=termination_color, s=termination_size, zorder=11)

ax1.plot(state_var1_w_prime2[:len(t_short)], state_var2_w_prime2[:len(t_short)], **line_chaotic_style)
ax1.scatter(state_var1_w_prime2[t_idx_short], state_var2_w_prime2[t_idx_short], marker=termination_marker, color=termination_color, s=termination_size, zorder=11)

ax1.plot(state_var1_w_prime3[:len(t_short)], state_var2_w_prime3[:len(t_short)], **line_decay_style)
ax1.scatter(state_var1_w_prime3[t_idx_short], state_var2_w_prime3[t_idx_short], marker=termination_marker, color=termination_color, s=termination_size, zorder=11)


# Mark start point
ax1.scatter(start_point[0], start_point[1], color='black', s=60, zorder=11, label='Present State (t=0)')

# Add State Fidelity Annotation to W@
mid_point_idx = len(t_full) // 2
mid_x = state_var1_w_at[mid_point_idx]
mid_y = state_var2_w_at[mid_point_idx]
ax1.scatter(mid_x, mid_y, color=node_color_actual, s=50, zorder=11)
ax1.annotate(r'$\mathcal{F}_{@}(S_{@}) = S_{@}$' + '\n(PUS State Fidelity)',
             xy=(mid_x, mid_y), xytext=(mid_x + 1.5, mid_y - 3),
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=-0.2", color='black'),
             bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.9), fontsize=9)

# Add text explaining termination
ax1.text(state_var1_w_prime1[t_idx_short], state_var2_w_prime1[t_idx_short] + 2, 'Invalid Trajectories\nTerminated by PUS',
         ha='center', va='bottom', fontsize=9, color='dimgray')


ax1.legend(fontsize=9, loc='upper left')
ax1.set_xlabel(r'Abstract State Variable 1 ($\chi_1$)', fontsize=12)
# ax1.set_ylabel(r'Abstract State Variable 2 ($\chi_2$)') # Shared Y axis
ax1.grid(True, linestyle='--', alpha=0.6)


# --- General Cleanup ---
# Determine common ylim based on Panel A's potentially larger range
max_y_a = max(np.max(state_var2_w_at), np.max(state_var2_w_prime1), np.max(state_var2_w_prime2), np.max(state_var2_w_prime3))
min_y_a = min(np.min(state_var2_w_at), np.min(state_var2_w_prime1), np.min(state_var2_w_prime2), np.min(state_var2_w_prime3))
y_margin = (max_y_a - min_y_a) * 0.1
ylim = [min_y_a - y_margin, max_y_a + y_margin]

for ax in axes:
    ax.set_ylim(ylim)
    # ax.set_xlim(...) # Can set xlim if needed

plt.tight_layout(rect=[0, 0.03, 1, 0.95]) # Adjust layout
plt.savefig('pus_figure1_state_selection.png', dpi=300)
plt.show()
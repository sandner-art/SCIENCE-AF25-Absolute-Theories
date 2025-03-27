import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import PathPatch
from matplotlib.path import Path

# --- Helper function to create curved paths ---
# (Same as before)
def create_curved_path(start_pos, end_pos, bend=0.3):
    """Creates a Path object for a quadratic Bezier curve."""
    mid_pos = (start_pos + end_pos) / 2
    dx = end_pos[0] - start_pos[0]; dy = end_pos[1] - start_pos[1]
    norm = np.sqrt(dx**2 + dy**2); norm = 1 if norm == 0 else norm
    ctrl_pos = mid_pos + bend * np.array([-dy/norm, dx/norm]) * norm
    return Path([start_pos, ctrl_pos, end_pos], [Path.MOVETO, Path.CURVE3, Path.CURVE3])

# --- Node Positions ---
# (Same as before)
pos = {
    'past': np.array([-2, 0]), 'present': np.array([0, 0]),
    'future_actual': np.array([2, 0]), 'future_other1': np.array([2, 1.5]),
    'future_other2': np.array([2, -1.5]), 'paradox_loop_end': np.array([-1, -1.5])
}

# --- Plotting ---
plt.style.use('seaborn-v0_8-whitegrid')
fig, axes = plt.subplots(1, 2, figsize=(16, 7), sharey=True, sharex=True)
fig.suptitle('Figure 3: PUS Resolution of Paradox via Ontological Trajectory Selection', fontsize=16, fontweight='bold')

# --- Common elements ---
# (Same as before)
node_color_actual = 'blue'; node_color_other = 'lightgrey'; node_color_paradox = 'salmon'
node_size = 2500; label_fontsize = 10

# --- Panel (a): Hypothetical Trajectories (PUS Ignored) ---
ax0 = axes[0]
ax0.set_title('(a) Apparent Trajectory Problem (PUS Ignored)', fontsize=13)
# Draw nodes (Same as before)
ax0.scatter(pos['past'][0], pos['past'][1], s=node_size, color=node_color_actual, alpha=0.5, zorder=5)
ax0.scatter(pos['present'][0], pos['present'][1], s=node_size, color=node_color_actual, zorder=5)
ax0.scatter(pos['future_actual'][0], pos['future_actual'][1], s=node_size, color=node_color_other, alpha=0.7, zorder=5)
ax0.scatter(pos['future_other1'][0], pos['future_other1'][1], s=node_size, color=node_color_other, alpha=0.7, zorder=5)
ax0.scatter(pos['future_other2'][0], pos['future_other2'][1], s=node_size, color=node_color_other, alpha=0.7, zorder=5)
ax0.scatter(pos['paradox_loop_end'][0], pos['paradox_loop_end'][1], s=node_size*0.8, color=node_color_paradox, alpha=0.7, zorder=5)
# Add labels (Same as before)
ax0.text(pos['past'][0], pos['past'][1], r'$W_{@}(t<0)$', ha='center', va='center', fontsize=label_fontsize, zorder=6)
ax0.text(pos['present'][0], pos['present'][1], r'$W_{@}(t=0)$', ha='center', va='center', fontsize=label_fontsize, zorder=6, color='white')
ax0.text(pos['future_actual'][0], pos['future_actual'][1], r'$W^{\prime}_{Future}$', ha='center', va='center', fontsize=label_fontsize, zorder=6)
ax0.text(pos['future_other1'][0], pos['future_other1'][1], r'$W^{\prime\prime}_{Future}$', ha='center', va='center', fontsize=label_fontsize, zorder=6)
ax0.text(pos['future_other2'][0], pos['future_other2'][1], r'$W^{\prime\prime\prime}_{Future}$', ha='center', va='center', fontsize=label_fontsize, zorder=6)
ax0.text(pos['paradox_loop_end'][0], pos['paradox_loop_end'][1], 'Paradox\nManifests?', ha='center', va='center', fontsize=label_fontsize-1, zorder=6)

# Draw paths (WITHOUT arrowstyle)
path_past_present = create_curved_path(pos['past'], pos['present'], bend=0)
ax0.add_patch(PathPatch(path_past_present, facecolor='none', edgecolor='gray', lw=1.5)) # Removed arrow args

path_actual_future = create_curved_path(pos['present'], pos['future_actual'], bend=0)
ax0.add_patch(PathPatch(path_actual_future, facecolor='none', edgecolor='dimgray', lw=1.5, linestyle='--'))
path_other1 = create_curved_path(pos['present'], pos['future_other1'], bend=0.3)
ax0.add_patch(PathPatch(path_other1, facecolor='none', edgecolor='dimgray', lw=1.5, linestyle='--'))
path_other2 = create_curved_path(pos['present'], pos['future_other2'], bend=-0.3)
ax0.add_patch(PathPatch(path_other2, facecolor='none', edgecolor='dimgray', lw=1.5, linestyle='--'))

path_paradox = create_curved_path(pos['present'], pos['paradox_loop_end'], bend=-0.6)
ax0.add_patch(PathPatch(path_paradox, facecolor='none', edgecolor='red', lw=1.5, linestyle=':'))
path_paradox_loopback = create_curved_path(pos['paradox_loop_end'], pos['past'] + np.array([0.2, 0.2]), bend=-0.4)
ax0.add_patch(PathPatch(path_paradox_loopback, facecolor='none', edgecolor='red', lw=1.5, linestyle=':'))

ax0.text(0.5, -1.8, "? Multiple trajectories appear possible ?", ha='center', va='center', fontsize=11, color='darkred', style='italic')


# --- Panel (b): PUS Resolution ---
ax1 = axes[1]
ax1.set_title('(b) PUS Resolution: Ontological Filtering', fontsize=13)
# Draw nodes (Same as before)
ax1.scatter(pos['past'][0], pos['past'][1], s=node_size, color=node_color_actual, alpha=0.5, zorder=5)
ax1.scatter(pos['present'][0], pos['present'][1], s=node_size, color=node_color_actual, zorder=5)
ax1.scatter(pos['future_actual'][0], pos['future_actual'][1], s=node_size, color=node_color_actual, alpha=0.8, zorder=5)
ax1.scatter(pos['future_other1'][0], pos['future_other1'][1], s=node_size, color=node_color_other, alpha=0.3, zorder=5)
ax1.scatter(pos['future_other2'][0], pos['future_other2'][1], s=node_size, color=node_color_other, alpha=0.3, zorder=5)
ax1.scatter(pos['paradox_loop_end'][0], pos['paradox_loop_end'][1], s=node_size*0.8, color=node_color_paradox, alpha=0.3, zorder=5)
# Add labels (Same as before)
ax1.text(pos['past'][0], pos['past'][1], r'$W_{@}(t<0)$', ha='center', va='center', fontsize=label_fontsize, zorder=6)
ax1.text(pos['present'][0], pos['present'][1], r'$W_{@}(t=0)$', ha='center', va='center', fontsize=label_fontsize, zorder=6, color='white')
ax1.text(pos['future_actual'][0], pos['future_actual'][1], r'$W_{@}(t>0)$', ha='center', va='center', fontsize=label_fontsize, zorder=6)
ax1.text(pos['future_other1'][0], pos['future_other1'][1], r'$W^{\prime\prime}_{Future}$', ha='center', va='center', fontsize=label_fontsize-1, alpha=0.5, zorder=6)
ax1.text(pos['future_other2'][0], pos['future_other2'][1], r'$W^{\prime\prime\prime}_{Future}$', ha='center', va='center', fontsize=label_fontsize-1, alpha=0.5, zorder=6)
ax1.text(pos['paradox_loop_end'][0], pos['paradox_loop_end'][1], 'Paradox\n(Invalid)', ha='center', va='center', fontsize=label_fontsize-1, alpha=0.5, zorder=6)

# Draw paths (WITHOUT arrowstyle)
# Path from past
ax1.add_patch(PathPatch(path_past_present, facecolor='none', edgecolor='gray', lw=1.5))
# Actual path
ax1.add_patch(PathPatch(path_actual_future, facecolor='none', edgecolor=node_color_actual, lw=2.5))

# Invalid paths (faded/dotted)
invalid_style = {'edgecolor': 'dimgray', 'lw': 1.0, 'linestyle': 'dotted', 'alpha': 0.4}
ax1.add_patch(PathPatch(path_other1, facecolor='none', **invalid_style))
ax1.add_patch(PathPatch(path_other2, facecolor='none', **invalid_style))
ax1.add_patch(PathPatch(path_paradox, facecolor='none', edgecolor='red', lw=1.0, linestyle='dotted', alpha=0.4))
ax1.add_patch(PathPatch(path_paradox_loopback, facecolor='none', edgecolor='red', lw=1.0, linestyle='dotted', alpha=0.4))

# Add explanatory text (Same as before)
ax1.text(1.0, 1.0, 'Alternative Trajectories\nExcluded by PUS\n(Ontologically Invalid)', ha='center', va='center', fontsize=9, color='gray')
ax1.text(0.0, -1.5, 'Paradoxical Trajectories\nExcluded by PUS\n(Logically Inconsistent)', ha='center', va='center', fontsize=9, color='darkred')


# --- General Cleanup ---
# (Same as before)
for ax in axes:
    ax.set_aspect('equal', adjustable='box'); ax.set_xlim(-3, 3); ax.set_ylim(-2.5, 2.5)
    ax.set_xticks([]); ax.set_yticks([]); ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False); ax.spines['bottom'].set_visible(False); ax.spines['left'].set_visible(False)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig('pus_figure3_paradox_paths.png', dpi=300)
plt.show()
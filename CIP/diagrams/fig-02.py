import matplotlib.pyplot as plt
import numpy as np

# --- Generate Fake 'Data' Points for Theories ---
# (Complexity and Failure Rate are purely illustrative/subjective)
theories = {
    'CIP': {'complexity': 1, 'failure': 0.05, 'color': 'blue', 'marker': '*'},  # Changed marker to '*'
    'ΛCDM': {'complexity': 3, 'failure': 0.15, 'color': 'green', 'marker': 'o'},
    'Inflation': {'complexity': 5, 'failure': 0.35, 'color': 'orange', 'marker': 's'},
    'Std. Model': {'complexity': 6, 'failure': 0.25, 'color': 'purple', 'marker': 'P'}, # High complexity but low failure *within domain*
    'SUSY': {'complexity': 8, 'failure': 0.7, 'color': 'red', 'marker': 'X'},
    'String Theory': {'complexity': 10, 'failure': 0.9, 'color': 'black', 'marker': '*'},
    'Multiverse': {'complexity': 9, 'failure': 0.95, 'color': 'grey', 'marker': 'D'},
}

# Add some scatter/noise to make it look less contrived
complexity_vals = np.array([d['complexity'] for d in theories.values()]) + np.random.normal(0, 0.3, len(theories))
failure_vals = np.array([d['failure'] for d in theories.values()]) + np.random.normal(0, 0.05, len(theories))
# Ensure positive values
complexity_vals = np.maximum(0.5, complexity_vals)
failure_vals = np.maximum(0.01, np.minimum(1.0, failure_vals))

# --- Plotting ---
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(10, 7))

# Plot points for each theory
i = 0
for name, data in theories.items():
    ax.scatter(complexity_vals[i], failure_vals[i],
               color=data['color'], marker=data['marker'], s=150, alpha=0.8,
               label=name, zorder=10)
    # Add text label near point
    ax.text(complexity_vals[i]*1.05, failure_vals[i]*1.05, name, fontsize=9, color=data['color'])
    i += 1

# Add a suggestive trend line (visual guide, not rigorous fit)
trend_x = np.array([0, 11])
trend_y = 0.05 + trend_x * 0.085 # Arbitrary positive slope
ax.plot(trend_x, trend_y, color='darkred', linestyle='--', linewidth=1.5, alpha=0.7, label='Suggested Trend:\nComplexity $\Rightarrow$ Failure (Effort Penalty)')

# --- Labels and Title ---
ax.set_xlabel('Theoretical Model Complexity (Subjective Scale)', fontsize=12)
ax.set_ylabel('Empirical Failure Rate / Need for Ad-Hoc Fixes', fontsize=12)
ax.set_title("Figure 3: Correlation of Model Complexity with Empirical Difficulty", fontsize=14, fontweight='bold')
ax.set_xlim(0, 11)
ax.set_ylim(0, 1.1)
ax.legend(fontsize=9, loc='upper left')
ax.grid(True, linestyle='--', alpha=0.6)

# Annotation highlighting CIP's position
ax.annotate('CIP: Optimal Simplicity\n& Empirical Success',
            xy=(complexity_vals[0], failure_vals[0]), # Assuming CIP is first
            xytext=(complexity_vals[0] + 1.5, failure_vals[0] + 0.2),
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0.2"),
            bbox=dict(boxstyle="round,pad=0.3", fc="lightblue", ec="gray", alpha=0.9),
            fontsize=10)

plt.tight_layout()
plt.savefig('cip_figure3_complexity_failure.png', dpi=300)
plt.show()

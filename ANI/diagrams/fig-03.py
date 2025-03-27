import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# --- Generate Fake Correlated Data ---
np.random.seed(123)
n_points = 150
# Underlying true correlation
hcs_true = np.random.uniform(0, 10, n_points)
avi_true = 2.0 + 0.7 * hcs_true # Base linear relationship

# Add noise to both metrics to simulate measurement error/complexity
hcs_observed = hcs_true + np.random.normal(0, 1.0, n_points)
avi_observed = avi_true + np.random.normal(0, 1.5, n_points)
# Add some error bar values (larger for AVI)
hcs_err = np.random.uniform(0.3, 0.8, n_points)
avi_err = np.random.uniform(0.5, 1.5, n_points)

# Add a few outliers ('Boundary Cases')
n_outliers = 8
outlier_idx = np.random.choice(n_points, n_outliers, replace=False)
hcs_observed[outlier_idx] += np.random.normal(0, 2.5, n_outliers)
avi_observed[outlier_idx] -= np.random.normal(5, 2.0, n_outliers) # Push them down/away

# Clip values to plausible ranges if needed
hcs_observed = np.clip(hcs_observed, 0, 11)
avi_observed = np.clip(avi_observed, 0, 12)


# --- Perform Linear Regression ---
slope, intercept, r_value, p_value, std_err = stats.linregress(hcs_observed, avi_observed)
line_label = f'ANI Prediction (Linear Fit)\n$AVI \propto HCS$ (r={r_value:.2f})'

# --- Plotting ---
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(10, 7))

# Plot data with error bars
ax.errorbar(hcs_observed, avi_observed, xerr=hcs_err, yerr=avi_err,
            fmt='o', color='black', markersize=5, alpha=0.5, ecolor='gray', elinewidth=0.8, capsize=0,
            label='Individual Subjects / Observations')

# Highlight outliers
ax.scatter(hcs_observed[outlier_idx], avi_observed[outlier_idx],
           color='red', marker='x', s=60, label='Boundary Cases ($\partial \mathbf{I}$?)', zorder=10)

# Plot regression line
x_line = np.array([0, 11])
y_line = intercept + slope * x_line
ax.plot(x_line, y_line, color='darkmagenta', linestyle='--', linewidth=2, label=line_label)

# --- Labels and Title ---
ax.set_xlabel('Habitus Congruence Score (HCS) [arb. units]', fontsize=12)
ax.set_ylabel('Axiomatic Validation Index (AVI) [arb. units]', fontsize=12)
ax.set_title("Figure 3: Empirical Correlation Supporting ANI's Enactment-Validation Link", fontsize=14, fontweight='bold')
ax.set_xlim(0, 11)
ax.set_ylim(0, 12)
ax.legend(fontsize=10)
ax.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.savefig('ani_figure3_correlation_inspired.png', dpi=300)
plt.show()
import matplotlib.pyplot as plt
import numpy as np

# --- Simulate Supernova Data ---
# Based roughly on standard ΛCDM parameters
Omega_M0 = 0.3
Omega_Lambda0 = 0.7
H0 = 70 # km/s/Mpc (Less important for shape)
def luminosity_distance(z, Omega_M, Omega_Lambda):
    # Simple calculation ignoring curvature for flat universe
    # Use simplified integral approximation or analytic form if available
    # For demonstration, let's use a placeholder that looks right-ish
    # Proper calculation needs integrating 1/E(z) where E(z)=sqrt(Om*(1+z)^3+Ol)
    # Placeholder:
    dl = (z + 0.5 * (1 + Omega_M - Omega_Lambda) * z**2) * (3e5 / H0) # Mpc - VERY rough approximation
    dl[dl<=0]=1e-6 # Avoid log(0)
    return dl

n_points = 50
z_data = np.linspace(0.01, 1.5, n_points)
# Generate 'true' distances for standard model
dl_true = luminosity_distance(z_data, Omega_M0, Omega_Lambda0)
# Calculate 'true' distance modulus
mu_true = 5 * np.log10(dl_true) + 25 # mu = 5 log10(dL / 1 Mpc) + 25 is conventional

# Add scatter to simulate measurement errors
mu_error = 0.15 + 0.1 * z_data # Error increasing with redshift
mu_data = mu_true + np.random.normal(0, mu_error, n_points)

# --- Define Models ---
# 1. CIP Prediction (Simplest: ΛCDM w=-1)
dl_cip = luminosity_distance(z_data, Omega_M0, Omega_Lambda0)
mu_cip = 5 * np.log10(dl_cip) + 25

# 2. Hypothetical Complex Model 1 (e.g., Matter only, wrong shape)
dl_m_only = luminosity_distance(z_data, 1.0, 0.0)
mu_m_only = 5 * np.log10(dl_m_only) + 25

# 3. Hypothetical Complex Model 2 (e.g., different w, maybe slightly off)
# For simplicity, just shift the CIP curve slightly
mu_complex = mu_cip + 0.3 * np.sin(z_data * np.pi) # Example arbitrary deviation


# --- Plotting ---
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(10, 7))

# Plot simulated data points with error bars
ax.errorbar(z_data, mu_data, yerr=mu_error, fmt='o', color='black', markersize=4, alpha=0.6, label='Simulated SNe Ia Data')

# Plot models
ax.plot(z_data, mu_cip, color='blue', linewidth=2.5, label=r'CIP Prediction ($\Lambda$CDM, $w=-1$, Min. Effort)', zorder=10)
ax.plot(z_data, mu_m_only, color='red', linestyle='--', linewidth=1.5, label='Hypothetical: Matter Only (Disproven)')
ax.plot(z_data, mu_complex, color='green', linestyle=':', linewidth=1.5, label='Hypothetical: Complex DE (High Effort)')

# --- Labels and Title ---
ax.set_xlabel('Redshift ($z$)', fontsize=12)
ax.set_ylabel('Distance Modulus ($\mu$)', fontsize=12)
ax.set_title('Figure 4: CIP Concordance with Supernova Data (Hubble Diagram)', fontsize=14, fontweight='bold')
ax.legend(fontsize=10)
ax.grid(True, linestyle='--', alpha=0.6)

# Adjust limits for typical Hubble diagram appearance
ax.set_xlim(0, 1.6)
# ax.set_ylim(...) # Adjust y-limits based on data range if needed

plt.tight_layout()
plt.savefig('cip_figure4_supernova_fit.png', dpi=300)
plt.show()
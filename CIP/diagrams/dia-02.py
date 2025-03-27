import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

# --- Define Dynamics ---
# From EOM: d^2(Phi)/dt^2 + damping*d(Phi)/dt + V'(Phi) = 0 (ignoring expansion)
# Near minimum, V'(Phi) approx m_phi_sq * Phi
# Let's simulate simple overdamped relaxation: damping*d(Phi)/dt = -V'(Phi)
# d(Phi)/dt = - (m_phi_sq / damping) * Phi = -gamma * Phi

gamma = 0.5 # Relaxation rate constant
phi0 = 2.5 # Initial elevated attentiveness

# --- Solve ODE ---
t = np.linspace(0, 10, 200)
# Exact solution for d(Phi)/dt = -gamma*Phi is Phi(t) = Phi0 * exp(-gamma*t)
phi_t = phi0 * np.exp(-gamma * t)

# --- Plotting ---
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(9, 6))

ax.plot(t, phi_t, color='purple', linewidth=2.5)

# Add asymptote line at Phi=0
ax.axhline(0, color='black', linestyle='--', linewidth=1, alpha=0.7, label='$\Phi_{CIP} = 0$ (Max Indifference)')

# --- Labels and Annotations ---
ax.set_xlabel('Time ($t$)', fontsize=12)
ax.set_ylabel(r'Cosmic Attentiveness Field ($\Phi_{CIP}(t)$)', fontsize=12)
ax.set_title('Figure 2: Spontaneous Relaxation towards Cosmic Indifference', fontsize=14, fontweight='bold')

ax.annotate('Initial "Attentive" State',
            xy=(t[0], phi_t[0]),
            xytext=(t[len(t)//4], phi_t[0]*0.8),
            arrowprops=dict(arrowstyle="->", color='black'),
            fontsize=10)

ax.annotate('Relaxation Driven by\nMinimizing Effort (V)',
            xy=(t[len(t)//2], phi_t[len(t)//2]),
            xytext=(t[len(t)//2], phi_t[len(t)//2] + phi0*0.3),
            ha='center',
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=-0.2", color='gray'),
            fontsize=10)

ax.legend(fontsize=10)
ax.grid(True, linestyle='--', alpha=0.6)
ax.set_ylim(bottom=-0.1 * phi0) # Give a little space below zero

plt.tight_layout()
plt.savefig('cip_figure2_relaxation.png', dpi=300)
plt.show()
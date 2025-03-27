import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import Patch

# --- Define Boundary Curve (Arbitrary Closed Shape) ---
t = np.linspace(0, 2 * np.pi, 200)
radius_variation = 1.0 + 0.2 * np.sin(t * 3) + 0.1 * np.cos(t * 2)
boundary_x = radius_variation * np.cos(t) * 2.0
boundary_y = radius_variation * np.sin(t) * 1.5
boundary_z = np.sin(t * 2)  # Adding a z-component for 3D effect

# Create a meshgrid for the surface plot
theta = np.linspace(0, 2 * np.pi, 100)
r = np.linspace(0, 2, 50)
theta, r = np.meshgrid(theta, r)

# Define the surface in 3D
X = r * np.cos(theta) * 2.0
Y = r * np.sin(theta) * 1.5
Z = np.sin(theta * 2)

# --- Plotting ---
fig = plt.figure(figsize=(18, 7))

# First 3D Diagram
ax = fig.add_subplot(121, projection='3d')
surface = ax.plot_surface(X, Y, Z, color='lightblue', alpha=0.3)
ax.plot(boundary_x, boundary_y, boundary_z, color='black', linewidth=2.5)
ax.scatter(0, 0, 0, color='blue', s=100, zorder=10)
ax.set_xlabel('Abstract Ontological Parameter $\\alpha$', fontsize=12)
ax.set_ylabel('Abstract Nomological Parameter $\\beta$', fontsize=12)
ax.set_zlabel('Abstract Temporal Parameter $\\gamma$', fontsize=12)
ax.set_title("3D PUS Ontological 'Phase' Diagram", fontsize=14, fontweight='bold')
ax.text(0, 0, 1, r'$W_{@}$' + '\nSelf-Consistent\n"Phase"', ha='center', va='center', fontsize=12, color='darkblue')

# Create custom legend for the first plot
proxy = [Patch(facecolor='lightblue', alpha=0.3, label=r'$W_{@}$ (Actual World)'),
         Patch(facecolor='black', edgecolor='black', label=r'Boundary of Actuality ($\partial W_{@}$)'),
         Patch(facecolor='blue', edgecolor='blue', label='Singularity of Actuality')]
ax.legend(handles=proxy, fontsize=10, loc='lower right')

ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_zlim(-1, 1)

# Second 3D Diagram
ax2 = fig.add_subplot(122, projection='3d')
# Create a new boundary curve with different parameters
t2 = np.linspace(0, 2 * np.pi, 200)
radius_variation2 = 1.0 + 0.3 * np.sin(t2 * 4) + 0.2 * np.cos(t2 * 3)
boundary_x2 = radius_variation2 * np.cos(t2) * 2.0
boundary_y2 = radius_variation2 * np.sin(t2) * 1.5
boundary_z2 = np.sin(t2 * 3)  # Different z-component for variation

# Create a meshgrid for the second surface plot
theta2, r2 = np.meshgrid(theta, r)
X2 = r2 * np.cos(theta2) * 2.0
Y2 = r2 * np.sin(theta2) * 1.5
Z2 = np.sin(theta2 * 3)

surface2 = ax2.plot_surface(X2, Y2, Z2, color='lightgreen', alpha=0.3)
ax2.plot(boundary_x2, boundary_y2, boundary_z2, color='black', linewidth=2.5)
ax2.scatter(0, 0, 0, color='darkgreen', s=100, zorder=10)
ax2.set_xlabel('Abstract Ontological Parameter $\\alpha$', fontsize=12)
ax2.set_ylabel('Abstract Nomological Parameter $\\beta$', fontsize=12)
ax2.set_zlabel('Abstract Temporal Parameter $\\gamma$', fontsize=12)
ax2.set_title("3D Alternate PUS Ontological 'Phase' Diagram", fontsize=14, fontweight='bold')
ax2.text(0, 0, 1, r'$W_{@}$' + '\nAlternate\n"Phase"', ha='center', va='center', fontsize=12, color='darkgreen')

# Create custom legend for the second plot
proxy2 = [Patch(facecolor='lightgreen', alpha=0.3, label=r'$W_{@}$ (Alternate World)'),
          Patch(facecolor='black', edgecolor='black', label=r'Boundary of Alternate Actuality ($\partial W_{@}$)'),
          Patch(facecolor='darkgreen', edgecolor='darkgreen', label='Singularity of Alternate Actuality')]
ax2.legend(handles=proxy2, fontsize=10, loc='lower right')

ax2.set_xlim(-5, 5)
ax2.set_ylim(-5, 5)
ax2.set_zlim(-1, 1)

plt.tight_layout()
plt.savefig('double_3d_pus_phase_diagram.png', dpi=300)
plt.show()

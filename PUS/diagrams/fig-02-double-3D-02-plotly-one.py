import plotly.graph_objs as go
import numpy as np
from plotly.subplots import make_subplots

# Parameters for customization
resolution = 100  # Number of points in the meshgrid
colormap = 'Viridis'  # Colormap for heatmap effect

# --- Define Boundary Curve (Arbitrary Closed Shape) ---
t = np.linspace(0, 2 * np.pi, resolution)
radius_variation = 1.0 + 0.2 * np.sin(t * 3) + 0.1 * np.cos(t * 2)
boundary_x = radius_variation * np.cos(t) * 2.0
boundary_y = radius_variation * np.sin(t) * 1.5
boundary_z = np.sin(t * 2)  # Adding a z-component for 3D effect

# Create a meshgrid for the surface plot
theta = np.linspace(0, 2 * np.pi, resolution)
r = np.linspace(0, 2, resolution // 2)
theta, r = np.meshgrid(theta, r)

# Define the surface in 3D
X = r * np.cos(theta) * 2.0
Y = r * np.sin(theta) * 1.5
Z = np.sin(theta * 2)

# Create Plotly figure with subplots
fig = make_subplots(
    rows=1, cols=2,
    specs=[[{'type': 'surface'}, {'type': 'surface'}]],
    subplot_titles=("3D PUS Ontological 'Phase' Diagram", "3D Alternate PUS Ontological 'Phase' Diagram")
)

# Add first surface plot
fig.add_trace(
    go.Surface(x=X, y=Y, z=Z, colorscale=colormap, opacity=0.6, showscale=False),
    row=1, col=1
)

# Add first boundary line
fig.add_trace(
    go.Scatter3d(x=boundary_x, y=boundary_y, z=boundary_z, mode='lines',
                 line=dict(color='black', width=2.5), name='Boundary of Actuality'),
    row=1, col=1
)

# Add first singularity point
fig.add_trace(
    go.Scatter3d(x=[0], y=[0], z=[0], mode='markers',
                 marker=dict(size=5, color='blue'), name='Singularity of Actuality'),
    row=1, col=1
)

# Create a new boundary curve with different parameters for the second plot
t2 = np.linspace(0, 2 * np.pi, resolution)
radius_variation2 = 1.0 + 0.3 * np.sin(t2 * 4) + 0.2 * np.cos(t2 * 3)
boundary_x2 = radius_variation2 * np.cos(t2) * 2.0
boundary_y2 = radius_variation2 * np.sin(t2) * 1.5
boundary_z2 = np.sin(t2 * 3)  # Different z-component for variation

# Create a meshgrid for the second surface plot
theta2, r2 = np.meshgrid(theta, r)
X2 = r2 * np.cos(theta2) * 2.0
Y2 = r2 * np.sin(theta2) * 1.5
Z2 = np.sin(theta2 * 3)

# Add second surface plot
fig.add_trace(
    go.Surface(x=X2, y=Y2, z=Z2, colorscale=colormap, opacity=0.6, showscale=False),
    row=1, col=2
)

# Add second boundary line
fig.add_trace(
    go.Scatter3d(x=boundary_x2, y=boundary_y2, z=boundary_z2, mode='lines',
                 line=dict(color='black', width=2.5), name='Boundary of Alternate Actuality'),
    row=1, col=2
)

# Add second singularity point
fig.add_trace(
    go.Scatter3d(x=[0], y=[0], z=[0], mode='markers',
                 marker=dict(size=5, color='darkgreen'), name='Singularity of Alternate Actuality'),
    row=1, col=2
)

# Update layout
fig.update_layout(
    scene=dict(
        xaxis_title='Abstract Ontological Parameter α',
        yaxis_title='Abstract Nomological Parameter β',
        zaxis_title='Abstract Temporal Parameter γ'
    ),
    width=1400,
    height=700
)

# Show figure
fig.show()

import plotly.graph_objs as go
import numpy as np

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

# Create Plotly figure
fig = go.Figure()

# Add surface plot
fig.add_trace(go.Surface(
    x=X, y=Y, z=Z,
    colorscale=colormap,
    opacity=0.6,
    showscale=False
))

# Add boundary line
fig.add_trace(go.Scatter3d(
    x=boundary_x, y=boundary_y, z=boundary_z,
    mode='lines',
    line=dict(color='black', width=2.5),
    name='Boundary of Actuality'
))

# Add singularity point
fig.add_trace(go.Scatter3d(
    x=[0], y=[0], z=[0],
    mode='markers',
    marker=dict(size=5, color='blue'),
    name='Singularity of Actuality'
))

# Update layout
fig.update_layout(
    title="3D PUS Ontological 'Phase' Diagram",
    scene=dict(
        xaxis_title='Abstract Ontological Parameter α',
        yaxis_title='Abstract Nomological Parameter β',
        zaxis_title='Abstract Temporal Parameter γ'
    ),
    width=800,
    height=700
)

# Show figure
fig.show()

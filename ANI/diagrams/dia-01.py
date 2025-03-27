import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from matplotlib.patches import FancyArrowPatch, Circle # For background Is-ness

# --- Graph Definition ---
G = nx.DiGraph()

# Define nodes and their properties (labels, base positions)
nodes = {
    'I': {'label': r'$\mathbf{I}$' + '\n(Is-ness)', 'pos': np.array([0, 0]), 'size': 4000, 'color': 'lightgrey'},
    'In': {'label': r'$\mathbf{In}$' + '\n(In-ness)', 'pos': np.array([0, 1.5]), 'size': 3000, 'color': 'lightblue'},
    'Out': {'label': r'$\mathbf{Out}$' + '\n(Out-ness)', 'pos': np.array([0, -3.0]), 'size': 2500, 'color': 'salmon'},
    'Boundary': {'label': r'$\partial\mathbf{I}$' + '\n(Boundary)', 'pos': np.array([0, -1.0]), 'size': 2000, 'color': 'yellow'},
    'Praxis': {'label': 'Praxis/\nEmbodiment', 'pos': np.array([-2.5, 0]), 'size': 2500, 'color': 'lightgreen'},
    'Discourse': {'label': 'Discourse/\nSignification', 'pos': np.array([2.5, 0]), 'size': 2500, 'color': 'lightgreen'},
    'Habitus': {'label': 'Habitus', 'pos': np.array([-1.8, 2.2]), 'size': 2000, 'color': 'orange'},
    # Corrected Label for Validation
    'Validation': {'label': r'Validation ($\vdash_I$)', 'pos': np.array([1.8, 2.2]), 'size': 2000, 'color': 'orange'},
}

for node, attr in nodes.items():
    # Pass attributes correctly
    G.add_node(node, label=attr['label'], size=attr['size'], color=attr['color'], pos=attr['pos'])

# Extract positions for layout
pos = nx.get_node_attributes(G, 'pos')

# Define edges (representing influence/constitution)
edges = [
    ('I', 'In'), ('I', 'Out'), ('I', 'Boundary'), # I constitutes the triad
    ('Praxis', 'Habitus'), ('Discourse', 'Habitus'), # Practices/discourses shape habitus
    ('Habitus', 'In'), # Habitus aligns subject with In-ness
    ('In', 'Validation'), # In-ness status subjects things to validation
    ('Validation', 'Discourse'), ('Validation', 'Praxis'), # Validation reinforces discourses/practices
    ('Boundary', 'Out'), # Boundary work actively constitutes Out
    ('Out', 'Boundary'), # Outness exerts pressure/resistance at boundary
    # Edges representing Performative Enactment (will be styled specially or labeled)
    ('Praxis', 'In'), ('Discourse', 'In')
]
G.add_edges_from(edges)


# --- Plotting ---
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(12, 10))

# Draw a large circle in the background to represent the encompassing Field/Is-ness visually?
# bg_circle = Circle((0, 0), 3.8, color='whitesmoke', alpha=0.5, zorder=-1)
# ax.add_patch(bg_circle)

# Get node attributes for drawing
node_labels = nx.get_node_attributes(G, 'label')
# Correctly get sizes and colors using list comprehensions based on G.nodes() order
node_sizes = [G.nodes[node]['size'] for node in G.nodes()]
node_colors = [G.nodes[node]['color'] for node in G.nodes()]

# Draw nodes
# node_shape='o' is default, explicitly set if needed
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors, ax=ax, alpha=0.8)

# Draw node labels
nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=9, ax=ax, font_weight='bold')

# Draw edges with specific styles
# Standard influence edges
standard_edges = [e for e in G.edges() if e not in [('Praxis', 'In'), ('Discourse', 'In')]]
nx.draw_networkx_edges(G, pos, edgelist=standard_edges, ax=ax, edge_color='gray',
                       arrows=True, arrowstyle='-|>', arrowsize=15, node_size=node_sizes,
                       connectionstyle='arc3,rad=0.1') # Add slight curve

# Special "Enactment" edges - Thicker, maybe different color/style
enactment_edges = [('Praxis', 'In'), ('Discourse', 'In')]
nx.draw_networkx_edges(G, pos, edgelist=enactment_edges, ax=ax, edge_color='black', width=2.0,
                       arrows=True, arrowstyle='-|>', arrowsize=20, node_size=node_sizes,
                       connectionstyle='arc3,rad=0.1')

# Add labels for key processes like Enactment (↦)
# Position labels slightly offset from the middle of the enactment edges
for u, v in enactment_edges:
    x1, y1 = pos[u]
    x2, y2 = pos[v]
    mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2
    # Calculate normal direction for offset
    dx, dy = x2 - x1, y2 - y1
    norm = np.sqrt(dx**2 + dy**2); norm = 1 if norm == 0 else norm # Avoid division by zero
    offset_x, offset_y = -dy / norm * 0.2, dx / norm * 0.2
    ax.text(mid_x + offset_x, mid_y + offset_y, 'Enactment\n($\mapsto$)',
            ha='center', va='center', fontsize=10, color='black', fontweight='bold',
            bbox=dict(boxstyle="circle,pad=0.2", fc="white", ec="none", alpha=0.7))

# --- Title and Cleanup ---
ax.set_title('Figure 1: The ANI Cycle of Socio-Cultural Constitution', fontsize=16, fontweight='bold')
ax.set_xlim(-4.5, 4.5)
ax.set_ylim(-4.5, 4.0)
ax.set_aspect('equal', adjustable='box')
ax.axis('off') # Turn off the axis box

plt.tight_layout()
plt.savefig('ani_figure1_cycle_diagram.png', dpi=300)
plt.show()
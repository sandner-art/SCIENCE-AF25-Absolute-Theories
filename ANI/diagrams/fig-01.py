import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from matplotlib.patches import FancyArrowPatch

# --- Graph Definition ---
G = nx.DiGraph()

# Define node layers and properties
nodes = {
    # Top Layer (Axioms)
    'I': {'label': r'Is-ness Axioms ($\mathbf{I}$)', 'pos': np.array([0, 4]), 'size': 5000, 'color': 'lightcoral'},
    # Middle Layer (Concepts/Rules)
    'Habitus': {'label': 'Habitus\nSchemata', 'pos': np.array([-2, 2.5]), 'size': 3500, 'color': 'lightblue'},
    'Discourse': {'label': 'Discursive\nFormations', 'pos': np.array([0, 2.5]), 'size': 3500, 'color': 'lightblue'},
    'Validation': {'label': r'Validation Rules ($\vdash_{\mathbf{I}}$)', 'pos': np.array([2, 2.5]), 'size': 3500, 'color': 'lightblue'},
    # Bottom Layer (Practice/Observation)
    'Praxis': {'label': 'Performative\nEnactment ($\mapsto$)', 'pos': np.array([-1.5, 0.5]), 'size': 3000, 'color': 'lightgreen', 'shape': 's'},
    'Observation': {'label': 'Situated\nObservation', 'pos': np.array([1.5, 0.5]), 'size': 3000, 'color': 'lightgreen', 'shape': 's'},
    # Base Layer (Soil)
    'Soil': {'label': 'Lived Experience / Social Field', 'pos': np.array([0, -1]), 'size': 1000, 'color': 'grey', 'shape':'none'}
}

for node, attr in nodes.items():
    G.add_node(node, label=attr['label'], size=attr['size'], color=attr['color'], shape=attr.get('shape', 'o'))

# Extract positions
pos = {node: nodes[node]['pos'] for node in G.nodes()}

# Define edges
edges_down = [
    ('I', 'Habitus'), ('I', 'Discourse'), ('I', 'Validation'),
    ('Habitus', 'Praxis'), ('Discourse', 'Praxis'), ('Discourse', 'Observation'),
    ('Validation', 'Praxis'), ('Validation', 'Observation'),
    ('Praxis', 'Soil'), ('Observation', 'Soil')
]
# Special Loop Edges for Validation/Reinforcement
edges_up_validate = [('Praxis', 'I'), ('Observation', 'I')]

G.add_edges_from(edges_down)

# --- Plotting ---
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(10, 9))

# Get node attributes
node_labels = nx.get_node_attributes(G, 'label')
node_shapes = nx.get_node_attributes(G, 'shape')
node_sizes = [nodes[node]['size'] for node in G.nodes() if node != 'Soil']
node_colors = [nodes[node]['color'] for node in G.nodes() if node != 'Soil']
plot_nodes = [node for node in G.nodes() if node != 'Soil']

# Draw nodes (handle different shapes)
for shape_type in ['o', 's']:
    nodelist = [node for node in plot_nodes if G.nodes[node]['shape'] == shape_type]
    if not nodelist: continue # Skip if no nodes of this shape
    sizes = [G.nodes[node]['size'] for node in nodelist]
    colors = [G.nodes[node]['color'] for node in nodelist]
    nx.draw_networkx_nodes(G, pos, nodelist=nodelist, node_shape=shape_type,
                           node_size=sizes, node_color=colors, ax=ax, alpha=0.9)

# Draw node labels
nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=9, ax=ax)

# Draw standard edges (downward)
nx.draw_networkx_edges(G, pos, edgelist=edges_down, edge_color='gray', style='dashed',
                       arrows=True, arrowstyle='-|>', arrowsize=15, node_size=3000,
                       connectionstyle='arc3,rad=0.1')

# Draw validation edges (upward) MANUALLY using FancyArrowPatch for curves
for u, v in edges_up_validate:
    rad_val = -0.3 # Curve direction
    arrow = FancyArrowPatch(pos[u], pos[v], connectionstyle=f"arc3,rad={rad_val}",
                            color='darkblue', linestyle='-', mutation_scale=25, lw=2.0, arrowstyle='-|>')
    ax.add_patch(arrow)

# Annotate the validation loop
ax.text(pos['Praxis'][0] - 0.5, (pos['Praxis'][1] + pos['I'][1])/2,
        'Emic Validation Loop\n(Reinforces Axioms)',
        color='darkblue', fontsize=9, style='italic', ha='right', va='center')

# Draw "Soil" representation
soil_y = pos['Soil'][1] + 0.3
ax.axhline(soil_y, color='black', lw=2)
# Add wavy "soil" texture
soil_x = np.linspace(-3.5, 3.5, 100)
soil_wave = soil_y - 0.15 - 0.05 * np.sin(soil_x * 4)
ax.fill_between(soil_x, soil_wave, soil_y - 0.3, color='darkgoldenrod', alpha=0.3)
ax.plot(soil_x, soil_wave, color='darkgoldenrod', lw=1)
ax.text(pos['Soil'][0], pos['Soil'][1]-0.1, nodes['Soil']['label'], ha='center', va='top', fontsize=10, color='dimgray')

# --- Title and Cleanup ---
ax.set_title("Figure 1: Tanaka's Structure of Axiomatic Validation under ANI", fontsize=14, fontweight='bold')
ax.set_xlim(-4, 4)
ax.set_ylim(-1.5, 5)
ax.axis('off')

plt.tight_layout()
plt.savefig('ani_figure1_feigl_inspired.png', dpi=300)
plt.show()

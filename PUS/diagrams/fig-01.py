import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from matplotlib.patches import FancyArrowPatch

# --- Graph Definition ---
G = nx.DiGraph()

# Define node layers and properties
nodes = {
    # Top Layer (Axiom)
    'PUS': {'label': r'PUS Axiom' + '\n($W_{@} \equiv W_{@}$)', 'pos': np.array([0, 4]), 'size': 5000, 'color': 'gold', 'layer': 0},
    # Middle Layer (Concepts)
    'Stability': {'label': 'Ontological\nStability', 'pos': np.array([-2, 2.5]), 'size': 3500, 'color': 'lightblue', 'layer': 1},
    'Necessity': {'label': 'Nomological\nNecessity', 'pos': np.array([0, 2.5]), 'size': 3500, 'color': 'lightblue', 'layer': 1},
    'Exclusion': {'label': 'Paradox\nExclusion', 'pos': np.array([2, 2.5]), 'size': 3500, 'color': 'lightblue', 'layer': 1},
    # Bottom Layer (Observation)
    'Reg': {'label': 'Observed\nRegularities', 'pos': np.array([-2, 0.5]), 'size': 3000, 'color': 'lightgreen', 'shape': 's', 'layer': 2},
    'Events': {'label': 'Specific\nEvents', 'pos': np.array([0, 0.5]), 'size': 3000, 'color': 'lightgreen', 'shape': 's', 'layer': 2},
    'Data': {'label': 'Empirical\nData', 'pos': np.array([2, 0.5]), 'size': 3000, 'color': 'lightgreen', 'shape': 's', 'layer': 2},
    # Base Layer (Soil)
    'Soil': {'label': '"Soil" of Observation / Actuality', 'pos': np.array([0, -1]), 'size': 1000, 'color': 'grey', 'shape':'none', 'layer': 3}
}

for node, attr in nodes.items():
    G.add_node(node, label=attr['label'], size=attr['size'], color=attr['color'], shape=attr.get('shape', 'o'))

# Extract positions
pos = {node: nodes[node]['pos'] for node in G.nodes()}

# Define edges
edges_down = [
    ('PUS', 'Stability'), ('PUS', 'Necessity'), ('PUS', 'Exclusion'),
    ('Stability', 'Reg'), ('Necessity', 'Reg'), ('Necessity', 'Events'),
    ('Exclusion', 'Events'), ('Exclusion', 'Data'), ('Stability', 'Data'),
    ('Reg', 'Soil'), ('Events', 'Soil'), ('Data', 'Soil')
]
# Special Loop Edges
edge_self_loop = ('PUS', 'PUS') # For annotation
edges_up_confirm = [('Reg', 'PUS'), ('Events', 'PUS'), ('Data', 'PUS')] # Trivial Confirmation

G.add_edges_from(edges_down)
# Note: NetworkX draw doesn't show self loops well by default, we'll use annotation
# G.add_edges_from(edges_up_confirm) # We'll draw these manually

# --- Plotting ---
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(10, 9))

# Get node attributes
node_labels = nx.get_node_attributes(G, 'label')
node_shapes = nx.get_node_attributes(G, 'shape')
node_sizes = [nodes[node]['size'] for node in G.nodes() if node != 'Soil'] # Exclude soil from drawing
node_colors = [nodes[node]['color'] for node in G.nodes() if node != 'Soil']
plot_nodes = [node for node in G.nodes() if node != 'Soil']

# Draw nodes (handle different shapes)
for shape_type in ['o', 's']:
    nodelist = [node for node in plot_nodes if G.nodes[node]['shape'] == shape_type]
    sizes = [G.nodes[node]['size'] for node in nodelist]
    colors = [G.nodes[node]['color'] for node in nodelist]
    nx.draw_networkx_nodes(G, pos, nodelist=nodelist, node_shape=shape_type,
                           node_size=sizes, node_color=colors, ax=ax, alpha=0.9)

# Draw node labels
nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=9, ax=ax)

# Draw standard edges (downward)
nx.draw_networkx_edges(G, pos, edgelist=edges_down, edge_color='gray', style='dashed',
                       arrows=True, arrowstyle='-|>', arrowsize=15, node_size=3000, # Use avg node size for clipping
                       connectionstyle='arc3,rad=0.1')

# Draw confirmation edges (upward) MANUALLY using FancyArrowPatch for curves
for u, v in edges_up_confirm:
    rad_val = -0.3 if u == 'Events' else -0.4 # Adjust curve based on node
    arrow = FancyArrowPatch(pos[u], pos[v], connectionstyle=f"arc3,rad={rad_val}",
                            color='darkred', linestyle='-.', mutation_scale=20, lw=1.5, arrowstyle='-|>')
    ax.add_patch(arrow)

# Annotate the self-loop
ax.annotate('Self-Validation', xy=pos['PUS'], xytext=(pos['PUS'][0] - 1.5, pos['PUS'][1] + 0.5),
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0.5", color='black'),
            fontsize=9, ha='center')

# Annotate the confirmation loop
ax.text(pos['Data'][0] + 0.5, (pos['Data'][1] + pos['PUS'][1])/2,
        'Trivial Confirmation\n(Observations $\subset W_{@}$)',
        color='darkred', fontsize=9, style='italic', ha='left', va='center')

# Draw "Soil" representation
soil_y = pos['Soil'][1] + 0.3
ax.axhline(soil_y, color='black', lw=2)
for x_base in np.linspace(-3, 3, 15):
     ax.plot([x_base, x_base], [soil_y, soil_y - 0.3], color='black', lw=1) # Roots/lines
ax.text(pos['Soil'][0], pos['Soil'][1]-0.1, nodes['Soil']['label'], ha='center', va='top', fontsize=10, color='dimgray')


# --- Title and Cleanup ---
ax.set_title("Figure 1: Reed's Foundational Structure of Reality under PUS", fontsize=14, fontweight='bold')
ax.set_xlim(-4, 4)
ax.set_ylim(-1.5, 5)
ax.axis('off')

plt.tight_layout()
plt.savefig('pus_figure1_feigl_inspired.png', dpi=300)
plt.show()
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# --- Graph Definition ---
G = nx.DiGraph() # Use directed graph for temporal flow

# Add nodes with attributes for styling
nodes = {
    'W_past': {'label': r'$W_{@}(t<0)$', 'color': 'lightblue', 'size': 2000},
    'W_at': {'label': r'$W_{@}(t=0)$', 'color': 'blue', 'size': 3000},
    'W_future': {'label': r'$W_{@}(t>0)$', 'color': 'lightblue', 'size': 2000},
    'W_paradox1': {'label': r"$W'_{Paradox1}$", 'color': 'salmon', 'size': 1500},
    'W_paradox2': {'label': r"$W'_{Paradox2}$", 'color': 'salmon', 'size': 1500},
    'W_other1': {'label': r"$W'_{Other}$", 'color': 'lightgrey', 'size': 1000},
    'W_other2': {'label': r"$W''_{Other}$", 'color': 'lightgrey', 'size': 1000},
}
for node, attr in nodes.items():
    G.add_node(node, **attr)

# Add edges representing consistent flow within W@
G.add_edge('W_past', 'W_at')
G.add_edge('W_at', 'W_future')
# Add self-loop for fidelity concept (optional visual element)
# G.add_edge('W_at', 'W_at') # NetworkX draw doesn't show self-loops well by default

# --- Layout ---
# Use a layout that tends to separate components
pos = nx.spring_layout(G, k=1.5, iterations=100, seed=42)

# Manually adjust positions for clarity if needed
pos['W_paradox1'] = np.array([2, 1.5])
pos['W_paradox2'] = np.array([2, -1.5])
pos['W_other1'] = np.array([-2, 1.5])
pos['W_other2'] = np.array([-2, -1.5])

# --- Plotting ---
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(10, 8))

# Get node attributes
node_labels = {node: data['label'] for node, data in G.nodes(data=True)}
node_colors = [data['color'] for node, data in G.nodes(data=True)]
node_sizes = [data['size'] for node, data in G.nodes(data=True)]

# Draw the network
nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=node_sizes, ax=ax, alpha=0.9)
nx.draw_networkx_edges(G, pos, ax=ax, arrowstyle='-|>', arrowsize=20, edge_color='gray', node_size=node_sizes)
nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=12, ax=ax)

# --- Annotations ---
ax.text(2.0, 0, 'Paradoxical Worlds\n(Ontologically Inaccessible\nfrom $W_{@}$ under PUS)',
        ha='center', va='center', fontsize=10, color='darkred',
        bbox=dict(boxstyle="round,pad=0.5", fc="white", ec="salmon", alpha=0.8))

ax.text(-2.0, 0, 'Other Possible Worlds\n($W\' \neq W_{@}$)',
        ha='center', va='center', fontsize=10, color='dimgray',
        bbox=dict(boxstyle="round,pad=0.5", fc="white", ec="lightgrey", alpha=0.8))

# --- Title and Cleanup ---
ax.set_title('Figure 3: PUS Resolution of Paradox via Ontological Disconnection', fontsize=14, fontweight='bold')
ax.set_xticks([])
ax.set_yticks([])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

plt.tight_layout()
plt.savefig('pus_figure3_paradox_resolution.png', dpi=300)
plt.show()
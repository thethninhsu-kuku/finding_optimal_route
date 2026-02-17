import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
G = nx.erdos_renyi_graph(10, 0.5)

# Define the positions
pos = nx.spring_layout(G)

# Define labels for all nodes
labels = {node: node for node in G.nodes()}

# Specify the nodes you want to label
nodelist = [0, 1, 2]

# Filter the labels dictionary to include only the nodes in nodelist
filtered_labels = {node: labels[node] for node in nodelist}
print(filtered_labels)
# Draw the nodes and edges
nx.draw(G, pos, with_labels=False)

# Draw labels only for the specified nodes
nx.draw_networkx_labels(G, pos, labels=filtered_labels)

plt.show()

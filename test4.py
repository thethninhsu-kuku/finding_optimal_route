import networkx as nx
import matplotlib.pyplot as plt

# Create a sample graph
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 1)])

# Calculate node positions
pos = nx.spring_layout(G)

# Create a new dictionary to adjust label positions
pos_labels = {}
for node, (x, y) in pos.items():
    # Adjust x and y coordinates as needed to position the label beside the node
    pos_labels[node] = (x + 0.1, y + 0.1)  # Example offset
print(pos,pos_labels)
# Draw the graph and labels
nx.draw(G, pos, with_labels=True)
nx.draw_networkx_labels(G, pos_labels)

plt.show()

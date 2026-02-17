import networkx as nx
import matplotlib.pyplot as plt

G = nx.karate_club_graph()
pos = nx.spring_layout(G)

# Create a dictionary of labels (node: label)
labels = dict(zip(G.nodes(), G.nodes()))
print(labels)
# Draw the graph with labels
nx.draw_networkx_nodes(G, pos, node_size=700)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos, labels=labels, font_weight='bold')

plt.show()

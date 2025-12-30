import networkx as nx
from matplotlib import pyplot as plt

G = nx.DiGraph()

G.add_edge("chef", "cook", label="synonym")
G.add_edge("meal", "food", label="synonym")
G.add_edge("guest", "visitor", label="synonym")

G.add_edge("chef", "prepared", label="agent")
G.add_edge("prepared", "meal", label="object")
G.add_edge("served", "guest", label="recipient")

pos = nx.spring_layout(G)
plt.figure(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, node_size=2000, arrows=True)
edge_labels = nx.get_edge_attributes(G, "label")
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color="red")
plt.title("Semantic graph")
plt.axis("off")
plt.show()
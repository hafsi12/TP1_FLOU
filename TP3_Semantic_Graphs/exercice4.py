import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

G.add_edge("voiture", "véhicule", color="red")
G.add_edge("bus", "véhicule", color="red")
G.add_edge("vélo", "véhicule", color="red")
G.add_edge("véhicule", "machine", color="red")

G.add_edge("voiture", "moteur", color="green")
G.add_edge("voiture électrique", "batterie", color="green")

G.add_edge("véhicule", "avion", color="blue")

pos = nx.spring_layout(G)
edgelist = list(G.edges())
colors = [G[u][v]["color"] for u, v in edgelist]

plt.figure(figsize=(8, 6))
nx.draw_networkx_nodes(G, pos, node_size=1500)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos, edgelist=edgelist, edge_color=colors, arrows=True, width=2)
plt.title("Relations sémantiques (couleurs par type)")
plt.axis("off")
plt.show()
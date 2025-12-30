import nltk
from nltk.corpus import wordnet as wn
import networkx as nx
import matplotlib.pyplot as plt

words = {
    "cat": wn.synset("cat.n.01"),
    "mouse": wn.synset("mouse.n.01"),
    "garden": wn.synset("garden.n.01"),
    "chase": wn.synset("chase.v.01")
}

G = nx.DiGraph()

for word, syn in words.items():
    G.add_node(syn.name())
    for h in syn.hypernyms():
        G.add_edge(syn.name(), h.name(), label="is-a")

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=2500)
plt.show()

import networkx as nx
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import wordnet as wn

try:
    wn.synsets("laptop")
except LookupError:
    nltk.download("wordnet")

laptop_syns = wn.synsets("laptop", pos=wn.NOUN)
if not laptop_syns:
    raise SystemExit("Aucun synset 'laptop' trouvé dans WordNet")

laptop = laptop_syns[0]
computer = laptop.hypernyms()[0] if laptop.hypernyms() else None

G = nx.DiGraph()
G.add_node(laptop.name())
if computer:
    G.add_node(computer.name())
    G.add_edge(laptop.name(), computer.name(), label="is-a")

keyboard_syns = wn.synsets("keyboard", pos=wn.NOUN)
keyboard_name = keyboard_syns[0].name() if keyboard_syns else "keyboard"
G.add_node(keyboard_name)
G.add_edge(laptop.name(), keyboard_name, label="part-of")

pos = nx.spring_layout(G)
plt.figure(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, node_size=2000, arrows=True)
edge_labels = nx.get_edge_attributes(G, "label")
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color="red")
plt.title("Relations sémantiques pour 'laptop'")
plt.axis("off")
plt.show()
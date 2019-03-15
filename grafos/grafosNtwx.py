import networkx as nx
from  matplotlib import pyplot as plt
g=nx.Graph()

g.add_node(1)
g.add_nodes_from([2,3])

g.add_edge(2,3)

print nx.info(g)

nx.draw(g)

plt.show()


import networkx as nx
from  matplotlib import pyplot as plt
g=nx.Graph()

#g.add_node(1)
g.add_nodes_from([11,12])

g.add_edge(11,12)


H=nx.path_graph(10)
g.add_nodes_from(H)
g.add_edges_from([(1, 2), (1, 3)])

print nx.info(g)

nx.draw(g)

plt.show()


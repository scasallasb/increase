import networkx as nx
from  matplotlib import pyplot as plt
g=nx.Graph()





H=nx.path_graph(11)
g.add_nodes_from(H)
g.add_node('inicio')

g.add_edges_from([(1,2),(2,3),(2,4),(3,4),(4,6),(6,7),(5,7),(5,8),(7,8),(9,8),(9,10),(11,9)])
g.add_edge(1,'inicio')
nx.draw(g, with_labels=True, font_weight='bold')
print nx.info(g)

#nx.draw(g)

plt.show()


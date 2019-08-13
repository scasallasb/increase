
import networkx as nx
import matplotlib.pyplot as plt

def naive_algo(G):

    #dibujar y graficar
    plt.subplot(121)
    nx.draw(G, with_labels=True, font_weight='bold')

    #inicializar grafo con alturas 0
    for n in G.nodes():
         G.add_node(n,hi=0)

    # obtener valor de altura de nodos
    n=nx.get_node_attributes(G,'hi')
    print(n)

    #obtener valor de obstrucciones
    u=nx.get_edge_attributes(G,'obs')
    print(u)

    #crar lista de aristas
    obs=[]
    for i in u.keys():
        obs.append(i)
    #para cada nodo v conectado en V
    for i in range(nx.number_of_nodes(G)):
        print("nodo {}".format(i))
        #minimo arbol expandido
        T=nx.minimum_spanning_tree(G)
        
        #dibujar y graficar
        plt.subplot(122)
        nx.draw(T, with_labels=True, font_weight='bold')
        plt.show()

        l=list(T)
        #l=[0:1]

        print(l)
        for j in range (T.number_of_edges()):
            h=u[obs[j]]
            print ("altura nodo {}: {}".format(j, h))
    return G



if __name__=="__main__":
    j=nx.Graph()

    #crear diccionario con obstaculos
    #er= {(1,2): 12,(2,3):13,(2,4):12,(3,4):16,}
    er= {(1,2): 12,(2,3):13,(2,4):12,(3,4):16,(4,6):23,(6,7):21,(5,7):13,(5,8):2,(7,8):12,(9,8):4,(9,10):16,(11,9):2}
    for i in er.keys():
        r=list(i)
        j.add_edge(r[0],r[1], obs=er[i])


    naive_algo(j)

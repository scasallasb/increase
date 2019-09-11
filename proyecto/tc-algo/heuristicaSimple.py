import networkx as nx
import matplotlib.pyplot as plt

def heuristic_algo(G):
    #dibujar y graficar
    plt.subplot(121)
    nx.draw(G, with_labels=True, font_weight='bold')
    #inicializar grafo con alturas 0
    for n in G.nodes():
         G.add_node(n,hi=0)
    #para cada nodo v conectado en V
    for i in range(nx.number_of_nodes(G)):
        #minimo arbol expandido
        T=nx.minimum_spanning_tree(G)
        #listar hi nodos 
        n=nx.get_node_attributes(T,'hi')
        hi=[]
        for i in n.keys():
            hi.append(i)
        #listar aristas con obstaculos 
        u=nx.get_edge_attributes(G,'obs')
        obs=[]
        for i in u.keys():
            obs.append(i)
        #se listan obstaculos 
        ob= []
        for i in range (0,len(u)):
            ob.append(u[obs[i]])
        
        for j in range (2,T.number_of_edges()+1):
            v, u = n[j],n[j-1]           
            while v + u <2*ob[j-2]:

                vinc = (2*ob[j-2] - v-u)/2
                v , u = v + vinc , u + vinc
                    
            T.add_node(j,hi=v)
            T.add_node(j-1,hi=u)

    print(nx.get_node_attributes(T,'hi'))
    return T



if __name__=="__main__":
    j=nx.Graph()

    #crear diccionario con obstaculos
    er= {(1,2): 12,(2,3):13,(2,4):12,(3,4):16,}
    #er= {(1,2): 12,(2,3):13,(2,4):12,(3,4):16,(4,6):23,(6,7):21,(5,7):13,(5,8):2,(7,8):12,(9,8):4,(9,10):16,(11,9):2}
    for i in er.keys():
        r=list(i)
        j.add_edge(r[0],r[1], obs=er[i])


    heuristic_algo(j)
    #dibujar y graficar
    #plt.subplot(122)
    #nx.draw(T, with_labels=True, font_weight='bold')
    #plt.show()
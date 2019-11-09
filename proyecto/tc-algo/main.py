import TC_ALGO as tc
import tc_algoMil as tcm
import networkx as nx

import heuristicaSimple as hs

from matplotlib import pyplot as plt
if __name__ == "__main__":
    K,A,B,hmax,hmin=1,2.0,10,30,0
    #crear un grafo aleatorio
    #j=nx.erdos_renyi_graph(10,1)
    tc.preparTC(K,A,B,hmax,hmin)
    #crear un grafo
    j=nx.Graph()
    
    #crear diccionarios con obstaculos
    er= {(1,2): 12,(2,3):13,(2,4):12,(3,4):16,(4,6):23}
    er= {(1,2): 12,(2,3):13,(2,4):12,(3,4):16,(4,6):23}
    #er= {(1,2): 12,(2,3):13,(2,4):12,(3,4):16,}
    er= {(1,2): 12,(2,3):13,(2,4):12,(3,4):16,(4,6):23,(4,11):3,(6,7):21,(5,7):13,(5,8):2,(7,8):12,(9,8):4,(9,10):16,(11,9):2,}
    for i in er.keys():
        r=list(i)
        j.add_edge(r[0],r[1],weight=er[i])


    for i in er.keys():
        r=list(i)
        j.add_edge(r[0],r[1], obs=er[i])

    #heuristicaSimple
    h=hs.heuristic_algo(j)
    H=nx.get_node_attributes(h,'hi')
    conth = 0
    for i in H.keys():
        conth +=H[i]
    print ("resultado de suma de alturas con Heuristica Simple = {} ".format(conth))

    plt.figure(122)
    plt.title("heuristicaSimple")
    #dibujar y graficar
    nx.draw(j)

    #TC_ALGO
    t = tc.TC_ALGO(j)
    T=nx.get_node_attributes(t,'hi')
    conth = 0
    for i in T.keys():

        conth +=T[i]
    print ("resultado de suma de alturas con tc_algo  = {} ".format(conth))
    #print (H)

    plt.figure(121)
    plt.title("Tc_Algo")
    nx.draw(j, with_labels=True, font_weight='bold')
    #nx.draw(j)

    plt.show()

    COSTO=[0.75,0.65,1,30,20]

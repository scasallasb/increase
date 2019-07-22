#funciones de python
import numpy as np
import math as m
import networkx as nx
import matplotlib.pyplot as plt

#funciones propias
import Funciones as fn
import START_TC_ALGO as sta


def TC_ALGO(G):

    inf=m.factorial(20)

    COVERh=nx.Graph()

    COVERh.add_nodes_from(G)

    COMPh=nx.number_connected_components(COVERh)

    #inicializar grafo con alturas 0
    for n in G.nodes():
         G.add_node(n,hi=0)

    while COMPh > 1:
         #rbest se inicializa en infinito
         rbest=inf

         for n in G.nodes():
             h=nx.get_node_attributes(G,'hi')

             # funcion de costos
             chn=fn.c(h[n])
             i,e=1,(fn.c_1(chn+ 1))

             H=[h[n],hmax]


             while e < hmax:
                 H.append(e)
                 e= fn.c_1(chn + (i))
                 # aumenta altura has
                 i=i+1
             for i in range(0, len(H)):
                 a=(H[i]-h[n])
                 if a<0:a=0
                 rtmp,incrtmp, mayl=sta.START_TC_ALGO(G,COVERh,h,n,a)
                 if (rtmp < rbest):
                     nodo,rbest,incrbest, mayL=n,rtmp,incrtmp, mayl

         for i in incrbest.keys():
             for j in range (0,len(mayL)):
                 if (incrbest[i] >= 0) and (i==mayL[j]):
                     COVERh.add_edge(nodo,i)
         for i in G.nodes():
             G.add_node(i,hi=h[i]+incrbest[i])
         COMPh=nx.number_connected_components(COVERh)
    #print COVERh.edges()
    #print(nx.get_node_attributes(G,'hi'))
    print '-----------------------listo papa, ya esta-----------------------------'


    return COVERh

if __name__ == "__main__":

    #inicializamos variables
    K,A,B,hmax,hmin=1,2.0,10,20,2

    #crear un grafo aleatorio
    #j=nx.erdos_renyi_graph(10,1)

    #crear un grafo
    j=nx.Graph()
    H=nx.path_graph(11)
    j.add_nodes_from(H)
    #j.add_node('inicio')

    #j.add_edges_from([(1,2),(2,3),(2,4),(3,4),(4,6),(6,7),(5,7),(5,8),(7,8),(9,8),(9,10),(11,9)])
    #j.add_edge(1,'inicio')

    #dibujar y graficar
    nx.draw(j)
    #plt.show()

    #crear diccionarios con obstaculos
    er= {(1,2): 12,(2,3):13,(2,4):12,(3,4):16,(4,6):23,(6,7):21,(5,7):13,(5,8):2,(7,8):12,(9,8):4,(9,10):16,(11,9):2}

    for i in er.keys():
        r=list(i)
        j.add_edge(r[0],r[1],weight=er[i])

    #TC_ALGO
    TC_ALGO(j)
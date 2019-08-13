#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 11:24:26 2019

@author: Milton Rios and Leonardo Mujica

"""
#funciones de python
import numpy as np
import math as m
import networkx as nx
import matplotlib.pyplot as plt
#funciones propias
import Funciones as fn
import START_TC_ALGO as sta


def TC_ALGO(G):
    """Permite recorrer el grafo en cada nodo y determinar los incrementos de altura que se
    harán en un nodo central, que permitirá establecer un enlace directo con uno o
    varios de los nodos vecinos. La cantidad de enlaces realizados con un incremento
    de altura representa el beneficio del costo de dicho incremento.

    Parámetros
    -------
    G: grafo de topologia de la red

    Salidas
    -------
    G: grafo de entrada con el atributo de hi o altura a incrementar en cada nodo
    """

    print ("-----------------------empezo el algorimo-----------------------------")
    K,A,B,hmax,hmin=1,2.0,10,30,15
    #variable infinito
    inf=m.factorial(20)
    #crear el grafo COVERH y agregar los nodos de G
    COVERh=nx.Graph()
    COVERh.add_nodes_from(G)
    #numero de componentes conectados en COVERh
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
    #imprimir resultado
    print COVERh.edges()
    print(nx.get_node_attributes(G,'hi'))
    print '-------------------------   listo   -----------------------------'

    return G

if __name__ == "__main__":
    K,A,B,hmax,hmin=1,2.0,10,30,15
    #crear un grafo aleatorio
    #j=nx.erdos_renyi_graph(10,1)

    #crear un grafo
    j=nx.Graph()

    #crear diccionarios con obstaculos
    er= {(1,2): 12,(2,3):13,(2,4):12,(3,4):16,(4,6):23,(6,7):21,(5,7):13,(5,8):2,(7,8):12,(9,8):4,(9,10):16,(11,9):2}

    for i in er.keys():
        r=list(i)
        j.add_edge(r[0],r[1],weight=er[i])

    #dibujar y graficar
    nx.draw(j)
    plt.show()

    #TC_ALGO
    TC_ALGO(j)

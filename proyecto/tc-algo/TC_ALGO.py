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

def TC_ALGO(G):
    """Retorna el grafo con el atributo hi con los mejores incrementos de altura


    Recorre el grafo en cada nodo y determinar los incrementos de altura que se
    harán en un nodo central, que permitirá establecer un enlace directo con uno o
    varios de los nodos vecinos. La cantidad de enlaces realizados con un incremento
    de altura representa el beneficio del costo de dicho incremento.

    Parámetros
    -------

    G : graph
        grafo de topologia de la red

    Retorna
    -------

    G : graph
        grafo de entrada con el atributo de hi o altura a incrementar en cada nodo
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
             chn=c(h[n])
             i,e=1,(c_1(chn+ 1))
             H=[h[n],hmax]

             while e < hmax:
                 H.append(e)
                 e= c_1(chn + (i))
                 # aumenta altura has
                 i=i+1
             for i in range(0, len(H)):
                 a=(H[i]-h[n])
                 if a<0:a=0
                 rtmp,incrtmp, mayl=START_TC_ALGO(G,COVERh,h,n,a)
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

def START_TC_ALGO(G,coverh, h, n, dirac):
    """Retorna

    Encuentra el incremento de la altura en los nodos vecinos de v
    que tienen proporción más baja de costo-beneficio.

    Parámetros
    -------

    G : graph
        grafo de topologia de la red

    COVERh : graph
        nodos cubiertos por la altura h

    h : dictionary
        diccionario con atributos con llave por nodo

    n : node
        nodo donde se está ejecutando el algoritmo

    dirac : int
        incremento en la altura

    Retorna
    -------

    rbest : float
            mejor incremento dado conjunto de nodos

    incr : dictionary
        incremento optimo

    L : list
            
    """
    #infinito
    inf=m.factorial(20)
    #agregar incremento dirac y agregar función de costos en G
    G.add_node(n,hinc=(dirac))
    G.add_node(n,cinc=c(h[n]+dirac)-c(h[n]))
    nbr, L= nbrfun(G,coverh,n,dirac)
    rbest, kbest=inf,0

    for k in range(1,len(L)+1):
        sum=0
        for i in range(0,k):
            sum= (G.node[L[i]]['cinc'])+sum
        rtemp= ((G.node[n]['cinc']) + sum)/(k)
        if rtemp <  rbest:
            kbest,rbest=k,rtemp
    j=0
    L=L[:kbest]
    if len(L)>0:
        for i in G.nodes():
            if (i==L[j] or i==n):
                if (j<kbest and j<(len(L)-1) ):
                    j=j+1
            else:
                G. add_node(i,hinc=0)
    incr= nx.get_node_attributes(G,'hinc')

    print ("esto retorna START_TC_ALGO")
    print(type(rbest))
    print(type(incr))
    print(type(L))
    return rbest,incr, L


def c(h):
    """Retorna costo de nodo

    La función de costos c relaciona la variación de costos con la altura tanto de
    mástiles tubulares y torres de acero ventadas.

    Parámetros
    -------
    h : float
        altura del nodo

    Retorna
    -------
    costo : float
        valor económico del nodo
    """
    if h <= hmin:
        costo=K*h
    else:
        costo=(A*h)+B
    return costo


def c_1(ci):
    """

    """
    if ci > (c(hmin)):
        l=(ci-B)/A
    else:
        l=ci
    return l

def beta(h,u,n1,n2,d):
    """Devuelve costos de dos nodos

    Toma dos nosdos de referencia del grafo G y devuelve el valor del
    enlace.

    Parámetros
    ----------

    h : dictionary
        diccionario con atributos con llave por nodo

    n1 : node
        nodo de referencia 1

    n2 : node
        nodo de referencia 2

    d : float
        incremento de altura

    Retorna
    ----------

    B : float
        valor del enlace
    """
    try:
        aux=(2.0*(u[(n1,n2)]))
    except (IndexError, KeyError):
        aux=(2.0*(u[(n2,n1)]))
    HI=h[n1]+h[n2]+d
    if HI<aux:
        B =aux-HI
    else:
        B=0

    return B


def nbrfun(G,COVERh,n,d):
    """Retorna la mejor relacion costo beneficio con su mejor incremento

    Determina un conjunto de nodos en v que no estan en el mismo componente
    de v en COVER(h) y determina los incrementos de altura que den el menor
    valor de costo beneficio y los retorna en forma de lista.


    Parámetros
    -------
    G : graph
        grafo de topologia de la red

    COVERh : graph
        nodos cubiertos por la altura h

    n : node
        nodo donde se esta ejecutando el algoritmo

    d : float
        incremento en la altura

    Retorna
    -------
    r : list
        lista de nodos con mejor elación costo beneficio

    L : list
        lista de incrementos de altura incr
    """

    #obtener atributos de altura y peso de los nodos
    u=nx.get_edge_attributes(G,'weight')
    h =nx.get_node_attributes(G,'hi')
    p=[]
    r=set()

    #guardar cada nodo de COVER(h) en la lista r
    for i in range(0,nx.number_connected_components(COVERh)):
        subgraph=(list(nx.connected_component_subgraphs(COVERh)))
        p.append(subgraph[i])
        for o in p[i].nodes():
                if o==n:
                    r=set(G.neighbors(n)) - set(p[i].neighbors(n))
    r=list(r)
    L=[]
    l=[]

    #por cada nodo de r
    for i in range(0,len(r)):

        beTa=beta(h,u,n,r[i],d)
        G.add_node(r[i],hinc=beTa)
        G.add_node(r[i],cinc=(c(beTa + h[r[i]])- c(h[r[i]])))
        l.append((r[i],(c(beTa+ h[r[i]])-c(h[r[i]]))))

    l=dict(l)
    #ordena los valores de mayor a menor costo
    va= l.values()
    va.sort()


    for i in range(0,len(va)):
        for j in range(0,len(va)):
            if l[r[j]]== va[i]:
                if L.count(r[j])==0:
                   L.append(r[j])

    #Remueve de L todos los nodos v que pertenecen a va exepto el de menor costo
    for i in range(0,nx.number_connected_components(COVERh)):
        ri=list(set(L) & set(p[i].nodes()))
        #u empieza en infinito
        u=m.factorial(20)
        for j in range(0,len(ri)):
            if L.index(ri[j])< u:
                try:
                    L.remove(L[u])
                    break
                except (IndexError):
                    pass
                u = L.index(ri[j])
    return r, L


if __name__ == "__main__":
    K,A,B,hmax,hmin=1,2.0,10,30,15
    #crear un grafo aleatorio
    #j=nx.erdos_renyi_graph(10,1)

    #crear un grafo
    j=nx.Graph()

    #crear diccionarios con obstaculos
    er= {(1,2): 12,(2,3):13,(2,4):12,(3,4):16,(4,6):23}
    #,(6,7):21,(5,7):13,(5,8):2,(7,8):12,(9,8):4,(9,10):16,(11,9):2}

    for i in er.keys():
        r=list(i)
        j.add_edge(r[0],r[1],weight=er[i])

    #dibujar y graficar
    #nx.draw(j)
    #plt.show()

    #TC_ALGO
    TC_ALGO(j)
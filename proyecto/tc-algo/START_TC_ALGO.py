#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 11:24:26 2019

@author: Milton Rios and Leonardo Mujica

"""
#funciones de python
import numpy as np
import numpy as np
import math as m
import scipy as sc
import matplotlib.pyplot as plt
import networkx as nx
#funciones propias
import Funciones as fn



def START_TC_ALGO(G,coverh, h, n, dirac):
    """
    Encuentra el incremento de la altura en los nodos vecinos de v
    que tienen proporción más baja de costo-beneficio.

    Parámetros
    -------
    G: grafo de topologia de la red
    COVERh: nodos cubiertos por la altura h
    H: función altura h
    n: nodo donde se está ejecutando el algoritmo
    dirac: incremento en la altura

    Salidas
    -------
    incr: el incremento optimo

    """
    #infinito
    inf=m.factorial(20)
    #agregar incremento dirac y agregar función de costos en G
    G.add_node(n,hinc=(dirac))
    G.add_node(n,cinc=fn.c(h[n]+dirac)-fn.c(h[n]))
    nbr, L= fn.nbrfun(G,coverh,n,dirac)
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

    return rbest,incr, L

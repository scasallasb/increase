#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 11:24:26 2019

@author: Milton Rios and Leonardo Mujica

# ============================= Funciones ==================================
Este script contiene las funciones necesarias para que la subrutina
START_TC_ALGO se ejecute; en estas funciones se encuentran:

* Función de costos
* Función para hallar B
* Función nrb

En estas funciones es importante tener en cuenta algunas constantes,
las cuales corresponden a:
-valores de alturas en la red

* hmin: corresponde a la altura mínima, la cual es el  mínimo valor de  mástil.
* hmax: corresponde a la altura mayor de un nodo en la red.

-valores economicos de la red

* K: valor medio de mástiles tubulares.
* A: valor de variación de costos por metro de las torres ventadas.
* B: estudios relativos del terreno.
"""
#Funciones de python
import numpy as np
import math as m
import scipy as sc
import matplotlib.pyplot as plt
import networkx as nx

# constantes
K,A,B,hmax,hmin=1,2.0,10,30,15
#inf=m.factorial(20)

def c(h):
    """ La función de costos c relaciona la variación de costos con la altura tanto de
    mástiles tubulares y torres de acero ventadas.

    Parámetros
    -------
    h: altura del nodo

    Salidas
    -------
    costo: valor económico del nodo
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
    """

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
    """determina conjunto de nodos en v que no estan en el mismo componente de v en COVER(h)

    Parámetros
    -------
    G: grafo de topologia de la red
    COVERh: nodos cubiertos por la altura h
    n: nodo donde se esta ejecutando el algoritmo
    d: incremento en la altura

    Salidas
    -------
    r: relación costo beneficio
    L: incremento en la altura incr
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

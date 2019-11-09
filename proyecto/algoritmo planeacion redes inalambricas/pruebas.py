#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import math
from heapq import heappush, heappop
from itertools import count
import numpy as np
# librerias propias
import mapas as m
import tc_algo  as tc
import increase as inc
import heuristicaSimple as hs
#def datos(nmin, nmax, taz, nvec):

def GraficaContinua(Min,Max,paso):
    
    x=np.arange(Min,Max,paso)
    y1=[]
    y2=[]
    for i in range (Min,Max,paso):
            a,a1=evaluacion(i)
            y1.append(a)
            y2.append(a1)
    plt.plot(x,y1, label="Algoritmo propuesto" , color="red")
    plt.plot(x,y2, label="Heurística simple", color = "blue")
    plt.title(u'Algoritmo Propuesto vs Heurística Simple')
    plt.xlabel(u'Número de Nodos')
    plt.ylabel(u'Costo - Calor')
    red_patch = mpatches.Patch(color='red', label='Algoritmo Propuesto')
    blue_patch = mpatches.Patch(color='blue', label='Heurística Simple')
    plt.legend(handles= [red_patch, blue_patch])
    plt.savefig("pruebas.png")
    plt.show()
                    
    
def datos():
    data=[]
    Tda=[]
    Apda=[]
    for k in range (10, 100,5):
        for i in range(k,100,3):
            d=[]
            T=[]
            Ap=[]
            for j in range(20):
                a,a1=evaluacion(i)
                d.append((a1-a)/a)
                T.append(a1)
                Ap.append(a)
                data.append((i,d))
                Tda.append((i,T))
                Apda.append((i,Ap))
            data=dict(data)
            Tda=dict(Tda)
            Apda=dict(Apda)
            des=[]
            med=[]
            for i in data.keys():
                des.append((i,np.std(data[i])))
                med.append((i,np.mean(data[i])))

            des=dict(des)
            med=dict(med)
            x=med.keys()
            y=med.values()
            error1=des.values()
            plt.errorbar(x, y, yerr=error1,linestyle="None", fmt='-o')
            plt.xticks(np.arange(min(med.keys())-1,max(med.keys())+2, 1.0))
            plt.title(u'Algoritmo Propuesto vs Heuristica Simple')
            plt.xlabel(u'Numero de Nodos')
            plt.ylabel(u'Media R_simple')
            plt.grid()
            #plt.savefig("estadisticas.png")
            plt.show()
            return med,des


def evaluacion(test):
    K,A,B,hmax,hmin=1,2.0,10,30,0
    #crear un grafo aleatorio
    #j=nx.erdos_renyi_graph(10,1)
    tc.preparTC(K,A,B,hmax,hmin)
    #crear un grafo
    G=nx.Graph()
    
    pos={}
    
    calor= {}
    hi={}
    obs= {}
    
    for i in range (test):
        pos[str(i)]=[int (np.random.randint(low = 0, high = 10, size = 1) ), int (np.random.randint(low = 0, high = 10, size = 1) )]
        calor[str(i)]=int (np.random.randint(low = 0, high = 10, size = 1))
        hi[str(i)]= int (np.random.randint(low = 0, high = 100, size = 1))
     
     
    #agregar nodos
    G.add_nodes_from(pos.keys())
    #agregar todos los enlaces 
    for i in G.nodes():
        for j in G.nodes():
            if (int (np.random.randint(low = 0, high = 10, size = 1) >=  8)):
                #G.add_edge(i,j)
                G.add_edge(i,j,weight=int (np.random.randint(low = 0, high = 10, size = 1)))
                
    
    costo= {}
    for i in hi.keys():
        costo[i]= tc.c(hi[i])
    

    nx.set_node_attributes(G,pos, 'pos')
    nx.set_node_attributes(G,calor, 'calor')
    nx.set_node_attributes(G,hi, 'hi')
    nx.set_node_attributes(G,costo, 'costo')
    
    
    print(pos)
    print (calor)
    print (hi)
    print (costo)
    
    
    #heuristica simple
    
    maximo = 0
    
    for i in calor.keys():
        
        aux = calor[i]
        
        if aux > maximo:
            maximo = aux
            nodoMax= i
        
    minimo= 9999
    for i in calor.keys():
        
        aux = calor[i]
        
        if aux < minimo:
            minimo = aux
            nodoMin= i
        
    source = [nodoMin]
    target = [nodoMax]
    
    bandera = 1
    while(bandera ==1):
        try :
            A =inc.targetIncrease(G,source, target)
            bandera +=1 
        except(nx.exception.NetworkXNoPath):
            source = [str(0)]
            target = [str(test)]
            
    #hacer grafo con camino 
    
    P= nx.Graph()
    #agregar nodos
    for i in A:
        P.add_node(i)
    #agregar edges
    for i  in  range(len(P)-1):
        P.add_edge(A[i], A[i+1])

    #agregar posicion a P
    posA={}
    for i in A:
        posA[i]=pos[i]
    nx.set_node_attributes(P,posA,'pos')

    cal={}
    for i in A:
        cal[i]=calor[i]
    nx.set_node_attributes(P,cal,'calor')

    #especificar y agregar atributos de edges
    n=A
    res=[]
    for i in range (0,len(n)-1):
        res.append((n[i],n[i+1]))
    edges={}
    for i in res:
        edges[i]= i 

    print(A)
    
    weight= {}
    
    for i in P.edges():
        if i in G.edges():
            #P.add_edge(i,j,weight=u[i])
            weight[i]=(G.edges[i]['weight'])
            #weight[i]=u[i]
    
    nx.set_edge_attributes(P,weight,"weight")
    u=nx.get_edge_attributes(P,'weight')
    
   
    if not len(A)==2:
        t=tc.TC_ALGO(P)
        T=nx.get_node_attributes(t,'hi')
        costo1=0
        for i in T.keys():
            costo[i]= tc.c(hi[i])
            costo1= costo1 +tc.c(hi[i])
        
        C=nx.get_node_attributes(t,'calor')
        calor1=0
        for i in C.keys():
            #costo[i]= tc.c(hi[i])
            calor1= calor1 + C[i]
        costoBeneficio1=costo1-calor1
        
        
    else:
        costo1=0
        calor1=0
        for i in A:
            costo1= costo1 + costo[i]
            calor1= calor1 + calor[i]
        costoBeneficio1=costo1-calor1 
    # R = hs.heuristic_algo(G)
    R=nx.minimum_spanning_tree(G)
    t=tc.TC_ALGO(G)
    T=nx.get_node_attributes(t,'hi')
    costo2=0
    for i in T.keys():
        costo[i]= tc.c(hi[i])
        costo2= costo2 +tc.c(hi[i])
    
    C=nx.get_node_attributes(t,'calor')
    calor2=0
    for i in C.keys():
        #costo[i]= tc.c(hi[i])
        calor2= calor2 + C[i]

    costoBeneficio2=costo2-calor2
    
    return costoBeneficio1 , costoBeneficio2
GraficaContinua(4 , 7 , 1)
#datos()
    





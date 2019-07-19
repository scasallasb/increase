import numpy as np
import math as m
import scipy as sc
import matplotlib.pyplot as plt
import networkx as nx

import Funciones as fn
import START_TC_ALGO as sta
K,A,B,hmax,hmin=1,2.0,10,30,15
def TC_ALGO(G):
    inf=m.factorial(20)
    COVERh=nx.Graph()
    COVERh.add_nodes_from(G)
    COMPh=nx.number_connected_components(COVERh)
    for n in G.nodes():
         G.add_node(n,hi=0)   

    while COMPh > 1:
         rbest=inf
         for n in G.nodes():
             h=nx.get_node_attributes(G,'hi')
             chn=fn.c(h[n])
             i,e=1,(fn.c_1(chn+ 1))
             H=[h[n],hmax]
             while e < hmax:
                 H.append(e)
                 e= fn.c_1(chn + (i))
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
    print COVERh.edges()
    print(nx.get_node_attributes(G,'hi'))
    print '-----------------------------------------------------'
    
    
    return COVERh
    '''dr=plt.figure()
    dr.add_subplot(131)
    #nx.draw_networkx_edge_labels(COVERh,pos)
    nx.draw_shell(G)
    dr.add_subplot(132)
    nx.draw_shell(COVERh)
    dr.add_subplot(133)
    nx.draw_shell(T)
    plt.show()'''



def test():
    assert(TC_ALGO)

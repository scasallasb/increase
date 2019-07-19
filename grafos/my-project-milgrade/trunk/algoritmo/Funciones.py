import numpy as np
import math as m
import scipy as sc
import matplotlib.pyplot as plt
import networkx as nx

K,A,B,hmax,hmin=1,2.0,10,30,15
inf=m.factorial(20)
def c(h):
     if h <= hmin:
        costo=K*h
     else:
        costo=(A*h)+B
     return costo  
def c_1(ci):
     if ci > (c(hmin)):
         l=(ci-B)/A
     else:
         l=ci
     return l 
def beta(h,u,n1,n2,d):
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
     u=nx.get_edge_attributes(G,'weight')
     h =nx.get_node_attributes(G,'hi')
     p=[]
     r=set()
     for i in range(0,nx.number_connected_components(COVERh)):
         p.append(nx.connected_component_subgraphs(COVERh)[i])
         for o in p[i].nodes():
             if o==n:
                 r=set(G.neighbors(n)) - set(p[i].neighbors(n))
     r=list(r)
     L=[]
     l=[]
     for i in range(0,len(r)):
         beTa=beta(h,u,n,r[i],d)
         G.add_node(r[i],hinc=beTa)
         G.add_node(r[i],cinc=(c(beTa + h[r[i]])- c(h[r[i]])))
         l.append((r[i],(c(beTa+ h[r[i]])-c(h[r[i]]))))
     l=dict(l)
     va= l.values()
     va.sort()
     for i in range(0,len(va)):
         for j in range(0,len(va)):
             if l[r[j]]== va[i]:
                 if L.count(r[j])==0:
                    L.append(r[j])
     for i in range(0,nx.number_connected_components(COVERh)):
         ri=list(set(L) & set(p[i].nodes()))
         u=inf
         for j in range(0,len(ri)):
             if L.index(ri[j])< u:
                 try:
                     L.remove(L[u])
                     break
                 except (IndexError):
                     pass
                 u = L.index(ri[j]) 
     return r, L
 
def test():
    assert(c)
    assert(c_1)
    assert(nbrfun)
    assert(beta)

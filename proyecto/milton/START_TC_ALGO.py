import numpy as np
import numpy as np
import math as m
import scipy as sc
import matplotlib.pyplot as plt
import networkx as nx

import Funciones as fn

inf=m.factorial(20)
def START_TC_ALGO(G,coverh, h, n, dirac):
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

def test():
     assert (START_TC_ALGO)

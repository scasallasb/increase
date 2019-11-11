#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import networkx as nx
import matplotlib.pyplot as plt
import math
from heapq import heappush, heappop
from itertools import count

# librerias propias
import mapas as m
import tc_algo  as tc
import increase as inc






G= nx.Graph()
cab={
    u"root": [-74.4878 ,4.535],
    u'SILVANIA':[-74.487778,4.403333]
            ,u'TIBACUY':[-74.4525, 4.347222]
            ,u'ARBELAEZ':[-74.415556,4.272222]
            ,u'PANDI':[-74.487778,4.191111]
            ,u'PASCA' :[-74.300833, 4.3075]
            ,u'SAN BERNARDO':[-74.422222,4.178889]
            ,u'VENECIA':[-74.4775,4.088611]
            ,u'CABRERA':[-74.485833,3.978056]
            ,u'GRANADA':[-74.351389,4.518611]
            ,u'FUSAGASUGA':[-74.364444,4.337222]}

key=list(cab.keys())
G.add_nodes_from(cab.keys())

nx.set_node_attributes(G,cab, 'pos')

calor={u'SILVANIA':10
            ,u'TIBACUY':10
            ,u'ARBELAEZ':10
            ,u'PANDI':10
            ,u'PASCA' :10
            ,u'SAN BERNARDO':10
            ,u'VENECIA':10
            ,u'CABRERA':10
            ,u'GRANADA':10
            ,u'FUSAGASUGA':10}

nx.set_node_attributes(G,calor,'calor')


costo={u'SILVANIA':10
            ,u'TIBACUY':11
            ,u'ARBELAEZ':10
            ,u'PANDI':10
            ,u'PASCA' :10
            ,u'SAN BERNARDO':11
            ,u'VENECIA':10
            ,u'CABRERA':10
            ,u'GRANADA':10
            ,u'FUSAGASUGA':10}

nx.set_node_attributes(G,costo,'costo')



G.add_edge('VENECIA','PANDI' )
G.add_edge('ARBELAEZ','SAN BERNARDO' )
G.add_edge('FUSAGASUGA','ARBELAEZ')
G.add_edge('SILVANIA','TIBACUY' )
G.add_edge('PANDI','TIBACUY' )
G.add_edge('CABRERA','VENECIA')
G.add_edge('CABRERA','SAN BERNARDO')
G.add_edge('VENECIA','PANDI')
G.add_edge('PANDI','ARBELAEZ')
G.add_edge('PASCA','ARBELAEZ')
G.add_edge('GRANADA','PASCA')
G.add_edge('PASCA','GRANADA')
G.add_edge('FUSAGASUGA','PASCA')
G.add_edge('GRANADA','SILVANIA')

diferencia = {

    u'SILVANIA': G.node['SILVANIA']['costo']        - G.node['SILVANIA']['calor'],
    u'TIBACUY': G.node['TIBACUY']['costo']         - G.node['TIBACUY']['calor'] ,
    u'ARBELAEZ': G.node['ARBELAEZ' ]['costo']       - G.node['ARBELAEZ' ]['calor'] ,
    u'PANDI': G.node['PANDI' ]['costo']          - G.node['PANDI' ]['calor']  ,
    u'PASCA' :G.node['PASCA'  ]['costo']         - G.node['PASCA'  ]['calor'] ,
    u'SAN BERNARDO': G.node['SAN BERNARDO']['costo']    - G.node['SAN BERNARDO']['calor'],
    u'VENECIA':G.node['VENECIA'  ]['costo']       - G.node['VENECIA' ]['calor'] ,
    u'CABRERA':G.node['CABRERA'  ]['costo']       - G.node['CABRERA'  ]['calor'],
    u'GRANADA':G.node['GRANADA'  ]['costo']       - G.node['GRANADA'  ]['calor'],
    u'FUSAGASUGA':G.node['FUSAGASUGA' ]['costo']     - G.node['FUSAGASUGA' ]['calor']
}
nx.set_node_attributes(G,diferencia,'diferencia')

nx.draw_networkx(G,cab)

## searchIncrease
listSource=['CABRERA','PANDI', 'VENECIA']
listTarget=['PASCA', 'GRANADA']

answer= inc.targetIncrease(G,listSource,listTarget)
print(answer)



#hacer grafo con camino 
P= nx.Graph()
#agregar nodos
for i in answer:
    P.add_node(i)
#agregar edges
for i  in  range(len(P)-1):
    P.add_edge(answer[i], answer[i+1])

#agregar posicion a P
pos={}
for i in answer:
    pos[i]=cab[i]
nx.set_node_attributes(P,pos,'pos')

cal={}
for i in answer:
    cal[i]=calor[i]
nx.set_node_attributes(P,cal,'calor')



#especificar y agregar atributos de edges
n=answer
res=[]
for i in range (0,len(n)-1):
        res.append((n[i],n[i+1] ))
edges={}


for i in res:
    edges[i]= i 

nx.set_edge_attributes(P,res,'pos')

## searchIncrease
N = ['FUSAGASUGA' ]
T_N=['SILVANIA','ARBELAEZ','TIBACUY','PANDI','PASCA','GRANADA','CABRERA']

c= 0.05
R, lista= inc.searchIncrease(G, N, T_N,c)

#main.usar_algo(P, cab, rep1=False)
COSTO=[0.75,0.65,1,30,20]

w=m.w_eg(P)

nx.set_edge_attributes(P,w,'weight')

t=tc.TC_ALGO(P)




#contar costo
T=nx.get_node_attributes(t,'hi')
conth = 0

for i in T.keys():
    conth +=T[i]
print ("resultado de suma de alturas con tc_algo  = {} ".format(conth))
plt.subplot(211)

#contar calor 
T=nx.get_node_attributes(P,'calor')
print (T)
conth = 0

for i in T.keys():
    conth +=T[i]
print ("resultado de suma de calor con tc_algo  = {} ".format(conth))
plt.subplot(211)



Pos= nx.get_node_attributes(G,"pos")
listnode= [n for n in Pos.keys() if n != "root" ]

nx.draw_networkx(G, cab , listNode=listnode )

plt.subplot(212)
nx.draw_networkx(P,pos)
plt.show()

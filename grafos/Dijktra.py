#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 09:51:37 2019

@author: santiago
"""


import numpy as np 


#nodos=int(input('cuantos nodos tiene el grafo:'))
nodos=6

#init graph
n=[1,2,3,4,5,6]
v=[4,2,1,5,1,8,10,5,8,2,6,10,2]
G= ([1,2],[1,3],[2,3],[2,4],[3,2],[3,4],[3,5],[4,2],[4,3],[4,5], [4,6],[5,3],[5,6])

grph= np.zeros((nodos, nodos))
vertice = -1




"""matriz respuesta """

m=np.zeros((nodos,nodos))



"""va a recorrer la matriz colocando cada vertice del grafo 
   cuando encuentre intervisibilidad entre nodos va a colocar
   el valor del vertice y cuando no, va colocar un valor inf"""


for i in range (0,nodos):
    for j in range (0,nodos):
        if ([i+1,j+1] in G ):
            vertice+= 1
            #m[j][i]=1
            grph[j][i]= v[vertice]
        else:
            grph[j][i]= 999

#el primero tiene que ser cero 
grph[0][0]=0

print(grph)


#########################################################
#paso 1 

com=np.zeros ((nodos,1))

com= grph[:,0]
m[:,0]=com


#paso 1
#marcar primer nodo como definitivo
m[0,1:len(m)]=100


#devolver pocicion del nodo menor 
val=sorted(com)[1]
pos = list(com).index(val)
print val
print pos

# paso 2

# poner el nodo definitivo 


paso2=np.zeros((nodos,1))


paso2= grph[:,pos] + val

paso2[pos]=val
m[pos,1:len(m)]=100
m[:,1]=paso2

#nodo definitivo

val=sorted(paso2)[1]
pos = list(paso2).index(val)
m[pos,2:len(m)]=100
m[pos,2]=val 


print pos


#paso 3 
# escoger el mas cerca
paso3=np.zeros((nodos,1))
paso3=grph[:,pos]
print paso3
val=sorted(paso2)[1]


paso3=grph[:,pos] + val





 
print m
print ( 'paso 3 :{}'.format(paso3))







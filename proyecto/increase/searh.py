#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import networkx as nx
import matplotlib.pyplot as plt
import math
from heapq import heappush, heappop
from itertools import count
import matplotlib.patches as mpatches

# librerias propias
import mapas as m

def distancia(node1, node2 ) :    
    pos = nx.get_node_attributes(G,'pos')
    lisI=[]
    lisF=[]
    lista=[]
    lat1=pos[node1][0]
    lon1=pos[node1][1]
    lisI.append(lat1)
    lisI.append(lon1)

    lat2=pos[node2][0]
    lon2=pos[node2][1]
    lisF.append(lat2)
    lisF.append(lon2)

    lista.append(lisI)
    lista.append(lisF)

    distancia = m.cal_dis(lista)
    return distancia
def searchIncrease(G, N, T_N,c):
    """Retorna un arból R formado a partir de un nodo "root"y los caminos mas
    cortos del conjunto de torres instaladas N a todas las torres viables T_N 
    utilizando algoritmo dijkstra, con la diferencia de que no se cuenta el valor
    de la arista, sino del nodo etiquetado con el valor NPV. Un diccionario con los 
    nodos con el atributo NPV, ademas de una lista con los nodos
    ordenados de mayor a menor NPV. 
    
    Utiliza el algoritmo searIncrease diseñado por Bernardi 2012.
    
    Parámetros
    ----------
    G   :    NetworkX graph.
    
    N   :   list
            Lista con nodos de torres instaladas.
            
    T_N :   list
            Lista con nodos de torres viables.
    
    c   :   float
            coeficiente de ganancia o retorno de inversión.
    
    
    Retorna
    ----------
    R   :   NetworkX tree
    
    dicNpv  :   Dictionary
                Diccionario con llave nodo y valor NPV.
                
    listNpv :   list
                Lista ordenada de mayor a menor con valores NPV.
                .
    """
    #agregar nodo raiz 
    G.add_node('root', cab = [0, 0])
    lista=[]
    for i in N:
        tupla=('root', i)
        lista.append(tupla)
    G.add_edges_from(lista)
    listPath=[]
    #aplicar el algoritmo Dkjistra desde el nodo raiz a cada n de G
    R=nx.Graph()
    v= nx.get_node_attributes(G, 'pos')

    for i  in v.keys():
        path = dijkstra_path(G, "root", i, weight='diferencia', N=N)
        listPath.append(path)
        for i in range(len(path)-1):
                R.add_edge(path[i],path[i+1])
    for i in N:
        tupla=('root', i)
        lista.append(tupla)
    R.add_edges_from(lista)

    #list generaciones 
    listGen=[]
    ###etiquetar nodos
    #atributos de distance r : distancia al nodo raiz
    NPV= {}
    lista = []
    pasado = N
    GenR=  nextGeneration(R,N)
    listGen.append(GenR)
    for i in GenR:
        NPV[i]= G.node[i]['diferencia']/(1 + c)
    bandera=0
    cont = 1

    while bandera==0:
        cont += 1
        nextGen = nextGeneration(R,GenR, pasado= pasado)
        pasado = GenR
        GenR=nextGen
        listGen.append(GenR)
        for j in nextGen:
                NPV[j]= G.node[j]['diferencia'] /(1 + c)**cont 
        if nextGen == []:
                bandera=1
    nx.set_node_attributes(R,NPV,'NPV')

    #ponderar puntos 
    u= T_N
    for i in listGen[::-1]:
        if  i == []:
                continue
        for j in i: 
                path =nx.shortest_path(R, "root", j)
                cont=0
                for k in path[::-1]:
                    if k in u :     
                            cont += R.node[k]['NPV']
                            R.node[k]['NPV']= cont     
    #listar nodos con mas valor
    listNpv= []
    dicNpv =nx.get_node_attributes(R,"NPV")
    for i in dicNpv.keys():
        listNpv.append(R.node[i]['NPV'])
    listNpv=sorted(listNpv)
    listNpv=listNpv[::-1]
    
    return R , dicNpv, listNpv 


def nextGeneration(R, N , pasado= None ):
    """ Retorna una lista con los nodos de la 
    siguiente generación de hijos.
    
    Parámetros
    ----------
    R   :   NetworkX tree.
    
    N   :   list
            Lista de nodos que funcionaran como backhaul.
    
    pasado  :   list
                Lista con la generacíon de nodos pasado.
    
    
    Retorna
    ----------
    listNeih    :   list
                    Lista con los nodos de la siguiente generación
                    de hijos.
    
    """
    #listar nodos primera generacion
    listNeih=[]
    for  i in N:
        Neigh= R[i]
        
        neigh= [i for i in Neigh.keys() if not i =='root' and not i in N]
        
        if not neigh == [] :
                for i in neigh:
                    if pasado == None:
                            listNeih.append(i)
                    else :
                            if not i in pasado:
                                listNeih.append(i)
    #borrar elementos repetidos 
    unico=[]
    for i in listNeih:
        if i not in unico:
                unico.append(i)
    
    listNeih= unico
    return listNeih


def dijkstra_path(G, source, target, weight='weight',N="N"):
    """Returns the shortest path from source to target in a weighted graph G.

    
    parámetros
    ----------
    G   :   NetworkX graph.
    
    source : node
        Nodo inicial del camino.

    target : node
        Nodo final del camino.
    
    weight: string, optional (default='weight')
       Edge data key corresponding to the edge weight.
    
    N   :   lista 
        Lista con torres que pueden ser backhaul 
       
       

    Retorna
    -------
    path : list
       Lista de nodos con el camino más corto.

    Raises
    ------
    NetworkXNoPath
       If no path exists between source and target.

    Ejemplos
    --------
    >>> G=nx.path_graph(5)
    >>> print(nx.dijkstra_path(G,0,4))
    [0, 1, 2, 3, 4]

    Nota
    ------
    El peso del atributo debe ser numérico.
    Las distancias son calculados con la ponderación de 
    los nodos atravesados.

    """
    (length, path) = single_source_dijkstra(G, source, target=target,
                                            weight=weight, N=N)
    try:
        return path[target]
    except KeyError:
        raise nx.NetworkXNoPath(
            "node %s not reachable from %s" % (source, target))


def single_source_dijkstra(G, source, target=None, cutoff=None, weight='weight', N="N"):
    """Computa el camino mas corto de las distancias con la ponderación de una función.
    
    Usa el algoritmo Dijkstra para encontrar el camino mas corto. 
    
    parámetros
    ----------
    G : NetworkX graph

    source : node
        Nodo inicial del camino.

    target : node
        Nodo final del camino.
    
    cutoff : integer or float, optional
        Profundidad para detener la búsqueda. Solo se devuelven rutas de longitud <= cutoff.
      

    Retorna
    -------
    distance,path : dictionaries
    
    Devuelve una tupla de dos diccionarios con clave por nodo.
    El primer diccionario almacena la distancia desde la fuente.
    El segundo almacena la ruta desde la fuente a ese nodo.

    Examples
    --------
    >>> G=nx.path_graph(5)
    >>> length,path=nx.single_source_dijkstra(G,0)
    >>> print(length[4])
    4
    >>> print(length)
    {0: 0, 1: 1, 2: 2, 3: 3, 4: 4}
    >>> path[4]
    [0, 1, 2, 3, 4]

    Notas
    ---------
    Implementar una función que da la sumatoria entre la distancia en
    numero de aristas de distancia al nodo root al nodo actual y la
    distancia de un enlace.

    Basado en libro "Python cookbook" recipe (119466) de
    http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/119466
    """
    def func(u,v, d):
        if v in N :
            return 1
        
        if u in N :
            return 1
        node_v_wt = G.nodes[v].get(weight, 1)+distancia(u, v)
        return node_v_wt

    if source == target:
        return ({source: 0}, {source: [source]})
    
    if G.is_multigraph():
        get_weight = lambda u, v, data: min(
            eattr.get(weight, 1) for eattr in data.values())
    else:
        get_weight =  lambda u, v, data: func(u,v, data)
        
    paths = {source: [source]}  # diccionario de rutas
    return _dijkstra(G, source, get_weight, paths=paths, cutoff=cutoff,
                     target=target)

def _dijkstra(G, source, get_weight, pred=None, paths=None, cutoff=None,
              target=None):
    """Implementación del algoritmo Dijkstra con la diferencia que no itera en 
    los vértices, sino sobre los nodos atravesados. 
    
    parámetros
    ----------
    G : NetworkX graph

    source : node
        Nodo inicial del camino.

    get_weight: function
        Función que retorna el peso del enlace.

    pred: list, optional(default=None)
        Lista de nodos predecesores.

    paths: dict, optional (default=None)
        Camino del nodo fuente a nodo objetivo.
        
    target : node
        Nodo final del camino.
    
    cutoff : integer or float, optional
        Profundidad para detener la búsqueda. Solo se devuelven rutas de longitud <= cutoff.
    
    Retorna
    -------

    distance,path : dictionaries
    
    Devuelve una tupla de dos diccionarios con clave por nodo.
    El primer diccionario almacena la distancia desde la fuente.
    El segundo almacena la ruta desde la fuente a ese nodo.

    
    pred,distance : dictionaries
        Retorna dos diccionarios que representan una lista de nodos
        predecesores de un nodo y la distancia de cada nodo.
       
    distance : dictionary
        Diccionario del los caminos mas corto con llave y objetivo.
    """
    G_succ = G.succ if G.is_directed() else G.adj
   
    
    push = heappush
    pop = heappop


    dist = {}  # dictionary of final distances
    seen = {source: 0}
    c = count()
    fringe = []  # use heapq with (distance,label) tuples
    push(fringe, (0, next(c), source))

    
    while fringe:
        (d, _, v) = pop(fringe)
        if v in dist:
            continue  # already searched this node.
        dist[v] = d
        if v == target:
            break
        
        #lista de nodos vecinos
        lisNeigV=list(G_succ[v].keys())
        
        for u in lisNeigV:

            cost = get_weight(v, u, len(nx.shortest_path(G, "root", u))-1) 
            
            if cost is None:
                continue
            
            vu_dist = dist[v] + get_weight(v, u, len(nx.shortest_path(G, "root", u))-1)
            
            if cutoff is not None:
                if vu_dist > cutoff:
                    continue
            if u in dist:
                if vu_dist < dist[u]:
                    raise ValueError('Contradictory paths found:',
                                     'negative weights?')
            elif u not in seen or vu_dist < seen[u]:
                seen[u] = vu_dist
                push(fringe, (vu_dist, next(c), u))
                if paths is not None:
                    paths[u] = paths[v] + [u]
                if pred is not None:
                    pred[u] = [v]
            elif vu_dist == seen[u]:
                if pred is not None:
                    pred[u].append(v)

    if paths is not None:
        return (dist, paths)
    if pred is not None:
        return (pred, dist)
    return dist

edgeList=   [('f','e'),
            ('f','g'),
            ('e','g'),
            ('a','b'),
            ('h','m'),
            ('l','m'),
            ('e','d'),
            ('g','a'),
            ('g','b'),
            ('g','h'),
            ('d','c'),
            ('b','c'),
            ('c','l'),
            ('m','c'),
            ('m','j'),
            ('j','k'),
            ('m','i'),
            ('h','i'),]
G=nx.Graph(edgeList)

valor={
      'root':[12,7.5]
      ,'a':[9, 6]
      ,'b':[14, 5]
      ,'c':[16, 8]
      ,'d':[10,9]
      ,'e':[7, 8]    
      ,'f':[5 ,6] 
      ,'g':[7,3] 
      ,'h':[11,1.5]
      ,'i':[22,2.5]
      ,'j':[25,6.5]
      ,'k':[24,9]
      ,'l':[20,9]
      ,'m':[20,5.5]         
               }
nx.set_node_attributes(G,valor,'pos')
N = ['a' , 'b','c', 'd']
T_N=['e','f','g','h','i','j','k','l','m']

diferencia={
      'root':0
      ,'e':10    
      ,'f':15
      ,'g':30
      ,'h':20
      ,'i':15
      ,'j':5
      ,'k':8
      ,'l':6
      ,'m':25         
               }
nx.set_node_attributes(G,diferencia,'diferencia')


R, dic, lista= searchIncrease(G, N, T_N , 0.05)
print (dic)
nx.draw_networkx(R, valor, nodelist = N, node_color= 'blue',node_size= 1300, font_color= "white")
nx.draw_networkx(R, valor, nodelist = T_N,node_size= 1300, font_color= "white")
nx.draw_networkx(R, valor, nodelist = ["root"], node_color= 'gray',node_size= 1300,font_color= "white", alpha = 0.6)
plt.savefig("Resultado.png")
plt.title(u'R generado')

plt.show()



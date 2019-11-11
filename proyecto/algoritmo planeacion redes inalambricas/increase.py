#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import networkx as nx
import matplotlib.pyplot as plt
import math
from heapq import heappush, heappop
from itertools import count

# librerias propias
import mapas as m


def targetIncrease(G,listSource,listTarget):
    """Retorna una lista de nodos en un camino de uno o más nodos origen a uno o más nodos 
    objetivo, con el valor mínimo de la suma de los valores de costo - calor. 
    
    parámetros
    ----------
    G   :   NetworkX graph
            Grafo con los atributos posición, costo y calor de cada uno de los nodos.        
    
    listSource  :lista
            lista con los nodos origen.
    listTarget  :lista
            lista con los nodos objetivo.
            
    Retorna 
    A   :   lista
            lista de nodos.
        
    """
    miniContPath= 9999
    for i  in listSource:
        for j in listTarget:
            answer=astar_path(G,i,j,heuristica,listNodeTarget= listTarget)
            cont = 0
            for k in answer:
                cont = cont + (G.node[k]['costo'] - G.node[k]['calor']) 
                               
            if cont < miniContPath:
                miniContPath = cont 
                A= answer
    return A

def astar_path(G, source, target, heuristic=None, listNodeTarget= None):
    """Retorna una lista de nodos en un camino de un nodo origen a un nodo objetivo 
    utilizando el algoritmo A*.
    
    Puede haber más de un camino corto, sin embargo, solo devuelve uno.
    
    parámetros
    ----------
    G   :   NetworkX graph.
    
    source :    node
                Nodo inicial del camino.

    target :    node
                Nodo final del camino.
       
    heuristic : function
                Es una función que estima el valor de cada nodo recorrido 
                con el valor de (costo - calor). En esta función toma de
                argumento un nodo y devuelve un valor numérico.
        
           
    Retorna 
    ----------
    A   :   lista
            Lista de nodos.
            
    Raises
    ------
    NetworkXNoPath
        Si no existe un camino entre un origen y un objetivo.

    """

    if G.is_multigraph():
        raise NetworkXError("astar_path() not implemented for Multi(Di)Graphs")

    push = heappush
    pop = heappop
    #Almacena la cola prioritaria, nodo, costo de atravesarlo y padre.
    #Usa la libreria heapq para mantener el orden de la prioridad. 
    #Adiciona un contador en la cola para evitar un monto subyacente 
    #intente comparar los nodos.  
    #prioriza y garantiza un unico para todos los nodos del grafo.
    c = count()
    queue = [(0, next(c), source, 0, None)]

    #Asigna los nodos en cola a la distancia de las rutas descubiertas y 
    #las heurísticas calculadas al objetivo. Evitamos calcular la heurística
    #más de una vez e insertar el nodo en la cola demasiadas veces.
    enqueued = {}
    # Asigna los nodos explorados al padre más cercano al origen.
    explored = {}

    minCosto=[]

    while queue:
        # Pop del elemento mas pequeño de la cola queue.
        _, __, curnode, dist, parent = pop(queue)
        
        if curnode == target:
            path = [curnode]
            node = parent
            while node is not None:
                path.append(node)
                node = explored[node]
            path.reverse()
            return path

        if curnode in explored:
            continue

        explored[curnode] = parent

        maximaDist= maximaDistancia(G)
        for neighbor, w in G[curnode].items():
            if neighbor in explored:
                continue
            ncost = dist

            if neighbor in enqueued:
                qcost, h = enqueued[neighbor]
                # sí qcost < ncost
                #queda un camino más largo hacia el vecino en cola.
                #Eliminarlo necesitaría filtrar toda la cola, es mejor 
                #dejarlo allí e ignorarlo cuando visitamos el nodo por segunda vez.
                if qcost <= ncost:
                    continue
            else:
                #heurística
                #h = l / d * (Cmin)
                h = (distNodeTarget(curnode, listNodeTarget)*heuristic(neighbor))/maximaDist
                minCosto.append(h)

            enqueued[neighbor] = ncost, h
            push(queue, (ncost + h, next(c), neighbor, ncost, curnode))

    raise nx.NetworkXNoPath("Node %s not reachable from %s" % (source, target))
    return minCosto

def distNodeTarget(nodo, listTarget):
    """Retorna mínima distancia entre el nodo y cualquiera de los nodos objetivo.
    
    Parámetros
    ----------
    node    :   nodo
                Nodo atravesado.
            
    listTarget  :   lista
                    Lista de nodos objetivo.
        
    
    Retorna 
    ---------
    maxDistancia    :   float
                        Máxima distancia.
    """
    miniDist = 999
    for i in listTarget:
        dis = distancia(nodo, i )
        if dis < miniDist:
            miniDist = dis
    return miniDist



def maximaDistancia(G):
    """Retorna el valor de la maxima distancia de un enlace del grafo G.
    
    parámetros
    ----------
    G   :   NetworkX graph
            Grafo con el atributo pos.
    
    retorna 
    ---------
    maxDistancia    :   float
                        Máxima distancia.
    """
    pos = nx.get_node_attributes(G,'pos')
    lisI=[]
    lisF=[]
    lista=[]

    maxDistancia = 0

    for i in pos.keys():
        for j in pos.keys():

            lat1=pos[i][0]
            lon1=pos[i][1]
            lisI.append(lat1)
            lisI.append(lon1)

            lat2=pos[j][0]
            lon2=pos[j][1]
            lisF.append(lat2)
            lisF.append(lon2)


            lista.append(lisI)
            lista.append(lisF)
            
            #distancia calculada para coordenadas
            distancia = m.cal_dis(lista)
            if distancia > maxDistancia:
                maxDistancia = distancia
            
            lisI=[]
            lisF=[]
            lista=[]
    
    return maxDistancia

def heuristica(nodo):
    """Retorna un valor numerico con el valor del atributo costo - calor
    de un nodo.
    
    Parámetros
    ----------
    nodo   :    node
                nodos con atributo costo y calor.
   
    Retorna
    ----------
    Valor numérico de costo - calor de nodo.
    """
    return(G.node[nodo]['costo'] - G.node[nodo]['calor'])

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
####################################################################################

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



if __name__ == '__main__':

    G= nx.Graph()
    cab={u"root": [-74.4878 ,4.535],
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
    """
    existe ={u'SILVANIA':True
                ,u'TIBACUY':False
                ,u'ARBELAEZ': True
                ,u'PANDI':False
                ,u'PASCA' :True
                ,u'SAN BERNARDO':False
                ,u'VENECIA':True
                ,u'CABRERA':False
                ,u'GRANADA':True
                ,u'FUSAGASUGA':False }

    nx.set_node_attributes(G,existe,'existe')
    """
    calor =nx.get_node_attributes(G, 'calor')
    costo =nx.get_node_attributes(G, 'costo')
    #existe=nx.get_node_attributes(G, 'existe')

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
   
    answer= targetIncrease(G,listSource,listTarget)
    print(answer)

    ## searchIncrease
    N = ['FUSAGASUGA' ]
    T_N=['SILVANIA','ARBELAEZ','TIBACUY','PANDI','PASCA','GRANADA','CABRERA']

    c= 0.05
    R, dic ,lista= searchIncrease(G, N, T_N,c)
    
    

    plt.subplot(211)
    nx.draw_networkx(G, cab)
   
    plt.subplot(212)
    nx.draw_networkx(R,cab)
    plt.show()

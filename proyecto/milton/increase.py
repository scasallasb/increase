import networkx as nx
import matplotlib.pyplot as plt
import math
from heapq import heappush, heappop
from itertools import count

# librerias propias
import mapas as m
import main 
import tc_algo  as tc

import TC_ALGO as cas
import rep_ejec as Re


def targetIncrease(G,listSource,listTarget):
    for i  in listSource:
        for j in listTarget:
            answer=astar_path(G,i,j,heuristica,listNodeTarget= listTarget)
    return answer

def heuristica(node1):
    return(G.node[node1]['costo'] - G.node[node1]['calor'])
    

def astar_path(G, source, target, heuristic=None, weight='weight', listNodeTarget= None):
    """Return a list of nodes in a shortest path between source and target
    using the A* ("A-star") algorithm.

    There may be more than one shortest path.  This returns only one.

    Parameters
    ----------
    G : NetworkX graph

    source : node
       Starting node for path

    target : node
       Ending node for path

    heuristic : function
       A function to evaluate the estimate of the distance
       from the a node to the target.  The function takes
       two nodes arguments and must return a number.

    weight: string, optional (default='weight')
       Edge data key corresponding to the edge weight.

    Raises
    ------
    NetworkXNoPath
        If no path exists between source and target.

    Examples
    --------
    >>> G=nx.path_graph(5)
    >>> print(nx.astar_path(G,0,4))
    [0, 1, 2, 3, 4]
    >>> G=nx.grid_graph(dim=[3,3])  # nodes are two-tuples (x,y)
    >>> def dist(a, b):
    ...    (x1, y1) = a
    ...    (x2, y2) = b
    ...    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    >>> print(nx.astar_path(G,(0,0),(2,2),dist))
    [(0, 0), (0, 1), (1, 1), (1, 2), (2, 2)]


    See Also
    --------
    shortest_path, dijkstra_path

    """


    if G.is_multigraph():
        raise NetworkXError("astar_path() not implemented for Multi(Di)Graphs")

    if heuristic is None:
        # The default heuristic is h=0 - same as Dijkstra's algorithm
        def heuristic(u, v):
            return 0

    push = heappush
    pop = heappop

    # The queue stores priority, node, cost to reach, and parent.
    # Uses Python heapq to keep in priority order.
    # Add a counter to the queue to prevent the underlying heap from
    # attempting to compare the nodes themselves. The hash breaks ties in the
    # priority and is guarenteed unique for all nodes in the graph.
    c = count()
    queue = [(0, next(c), source, 0, None)]

    # Maps enqueued nodes to distance of discovered paths and the
    # computed heuristics to target. We avoid computing the heuristics
    # more than once and inserting the node into the queue too many times.
    enqueued = {}
    # Maps explored nodes to parent closest to the source.
    explored = {}

    costo=[]

    while queue:
        # Pop the smallest item from queue.
        _, __, curnode, dist, parent = pop(queue)
        #print (curnode)
        #print (distNodeTarget(curnode, listNodeTarget))
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

            #ncost = distNodeTarget(curnode, listNodeTarget)*dist
            if neighbor in enqueued:
                qcost, h = enqueued[neighbor]
                # if qcost < ncost, a longer path to neighbor remains
                # enqueued. Removing it would need to filter the whole
                # queue, it's better just to leave it there and ignore
                # it when we visit the node a second time.
                if qcost <= ncost:
                    continue
            else:
                h = (distNodeTarget(curnode, listNodeTarget)*heuristic(neighbor))/maximaDist
                costo.append(h)

            enqueued[neighbor] = ncost, h
            push(queue, (ncost + h, next(c), neighbor, ncost, curnode))

        #print (costo)
    raise nx.NetworkXNoPath("Node %s not reachable from %s" % (source, target))
    return costo

def maximaDistancia(G):
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

            distancia = m.cal_dis(lista)
            if distancia > maxDistancia:
                maxDistancia = distancia
            #print ("la distancia entre {} y {} es {}".format(i , j , distancia ))
            lisI=[]
            lisF=[]
            lista=[]
    #print ("la maxima distancia es {}".format(maxDistancia) )
    return maxDistancia

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

def distNodeTarget(node1, listTarget):
    aux = 999
    for i in listTarget:
        dis = distancia(node1, i )
        if dis < aux:
            aux = dis
    return aux


########################################################################################

def searchIncrease(G, N, T_N,c):
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

      for i  in diferencia.keys():
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
      atributes =nx.get_node_attributes(R,"NPV").keys()
      for i in atributes:
            listNpv.append(R.node[i]['NPV'])
      listNpv=sorted(listNpv)
      print (listNpv[::-1])

      return R , listNpv


def nextGeneration(R, N , pasado= None ):
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

    Parameters
    ----------
    G : NetworkX graph

    source : node
       Starting node

    target : node
       Ending node

    weight: string, optional (default='weight')
       Edge data key corresponding to the edge weight

    Returns
    -------
    path : list
       List of nodes in a shortest path.

    Raises
    ------
    NetworkXNoPath
       If no path exists between source and target.

    Examples
    --------
    >>> G=nx.path_graph(5)
    >>> print(nx.dijkstra_path(G,0,4))
    [0, 1, 2, 3, 4]

    Notes
    ------
    Edge weight attributes must be numerical.
    Distances are calculated as sums of weighted edges traversed.

    See Also
    --------
    bidirectional_dijkstra()
    """
    (length, path) = single_source_dijkstra(G, source, target=target,
                                            weight=weight, N=N)
    try:
        return path[target]
    except KeyError:
        raise nx.NetworkXNoPath(
            "node %s not reachable from %s" % (source, target))


def single_source_dijkstra(G, source, target=None, cutoff=None, weight='weight', N="N"):
    """Compute shortest paths and lengths in a weighted graph G.

    Uses Dijkstra's algorithm for shortest paths.

    Parameters
    ----------
    G : NetworkX graph

    source : node label
       Starting node for path

    target : node label, optional
       Ending node for path

    cutoff : integer or float, optional
       Depth to stop the search. Only paths of length <= cutoff are returned.

    Returns
    -------
    distance,path : dictionaries
       Returns a tuple of two dictionaries keyed by node.
       The first dictionary stores distance from the source.
       The second stores the path from the source to that node.


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

    Notes
    ---------
    Edge weight attributes must be numerical.
    Distances are calculated as sums of weighted edges traversed.

    Based on the Python cookbook recipe (119466) at
    http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/119466

    This algorithm is not guaranteed to work if edge weights
    are negative or are floating point numbers
    (overflows and roundoff errors can cause problems).

    See Also
    --------
    single_source_dijkstra_path()
    single_source_dijkstra_path_length()
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
        #get_weight = lambda u, v, data: data.get(weight,1)
        get_weight =  lambda u, v, data: func(u,v, data)
        
    paths = {source: [source]}  # dictionary of paths
    return _dijkstra(G, source, get_weight, paths=paths, cutoff=cutoff,
                     target=target)

def _dijkstra(G, source, get_weight, pred=None, paths=None, cutoff=None,
              target=None):
    """Implementation of Dijkstra's algorithm

    Parameters
    ----------
    G : NetworkX graph

    source : node label
       Starting node for path

    get_weight: function
        Function for getting edge weight

    pred: list, optional(default=None)
        List of predecessors of a node

    paths: dict, optional (default=None)
        Path from the source to a target node.

    target : node label, optional
       Ending node for path

    cutoff : integer or float, optional
       Depth to stop the search. Only paths of length <= cutoff are returned.

    Returns
    -------
    distance,path : dictionaries
       Returns a tuple of two dictionaries keyed by node.
       The first dictionary stores distance from the source.
       The second stores the path from the source to that node.

    pred,distance : dictionaries
       Returns two dictionaries representing a list of predecessors
       of a node and the distance to each node.

    distance : dictionary
       Dictionary of shortest lengths keyed by target.
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
        #print ("distancia de {} a root {}".format(v,d))
       

        if v in dist:
            continue  # already searched this node.
        dist[v] = d
        if v == target:
            break
        
        #list nodes neightbor
        lisNeigV=list(G_succ[v].keys())
        #print (list(G_succ[v].keys()))
        for u in lisNeigV:

            #print ("nodo ={}".format(u))
            #print ("u ={}".format(u))
            cost = get_weight(v, u, len(nx.shortest_path(G, "root", u))-1) 
            
            if cost is None:
                continue
            #vu_dist = dist[v] + get_weight(v, u, e)
            vu_dist = dist[v] + get_weight(v, u, len(nx.shortest_path(G, "root", u))-1)
            #print ("costo   dist[v]= {}".format(dist[v]))

            #print ("distancia entre root y {} es {} ".format(u, len(nx.shortest_path(G, "root", u))-1 ))            
            #print ("costo de nodo {} es {} ".format(u,cost))

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
    cab={
        #u"root": [-74.4878 ,4.535],
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
   
    answer= targetIncrease(G,listSource,listTarget)
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
    
    print (pos)

    n=answer
    res=[]
    for i in range (0,len(n)-1):
            res.append((n[i],n[i+1] ))

    edges={}
    for i in res:
        edges[i]= i 

    
    nx.set_edge_attributes(P,res,'pos')
    
    print(res)


    u=nx.get_edge_attributes(P,'pos')
    print ("atributos u {}".format(u))

    #G.add_nodes_from(pos.keys())
    #nx.set_node_attributes(P,pos,'pos')

    ## searchIncrease
    N = ['FUSAGASUGA' ]
    T_N=['SILVANIA','ARBELAEZ','TIBACUY','PANDI','PASCA','GRANADA','CABRERA']

    c= 0.05
    R, lista= searchIncrease(G, N, T_N,c)

    #main.usar_algo(P, cab, rep1=False)
    COSTO=[0.75,0.65,1,30,20]

    w=m.w_eg(P)

    nx.set_edge_attributes(P,w,'weight')
    
    #G, pos1=Re.grafo_unido(cab,we=True)
    #cC,cT, InG,coverh,T = tc.algo(P,COSTO)
    
    #print ('cC=',cC,'cT=', cT)
    #print ('*'*200)

    t=cas.TC_ALGO(P)
    T=nx.get_node_attributes(t,'hi')
    conth = 0
    for i in T.keys():
        conth +=T[i]
    print ("resultado de suma de alturas con tc_algo  = {} ".format(conth))
    plt.subplot(211)
    #nx.draw_networkx(G, cab)
   
    plt.subplot(212)
    nx.draw_networkx(P,pos)
    plt.show()

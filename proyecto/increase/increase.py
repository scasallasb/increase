import networkx as nx
import matplotlib.pyplot as plt
import math
from heapq import heappush, heappop
from itertools import count

# librerias propias
import mapas as m

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
                #print (" {} - {}".format (curnode, neighbor))
                h = (distNodeTarget(curnode, listNodeTarget)*heuristic(neighbor, target))/maximaDist
                #print (h)
                costo.append(h)

            enqueued[neighbor] = ncost, h
            push(queue, (ncost + h, next(c), neighbor, ncost, curnode))

        print (costo)
    raise nx.NetworkXNoPath("Node %s not reachable from %s" % (source, target))
    return costo


def heuristica(node1, node2):
    return(G.node[node1]['costo'] - G.node[node1]['calor'])
    pass

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





if __name__ == '__main__':

    G= nx.Graph()
    cab={u'SILVANIA':[-74.388056,4.403333]
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

    calor =nx.get_node_attributes(G, 'calor')
    costo =nx.get_node_attributes(G, 'costo')
    existe=nx.get_node_attributes(G, 'existe')

    G.add_edge('VENECIA','PANDI' )
    G.add_edge('ARBELAEZ','SAN BERNARDO' )
    G.add_edge('FUSAGASUGA','ARBELAEZ')
    G.add_edge('SILVANIA','TIBACUY' )
    G.add_edge('PANDI','TIBACUY' )
    G.add_edge('CABRERA','VENECIA')
    G.add_edge('CABRERA','SAN BERNARDO')
    G.add_edge('VENECIA','PANDI')
    G.add_edge('PANDI','ARBELAEZ')
    #G.add_edge('PASCA','ARBELAEZ')
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
    #dibujar grafo con diferencia
    Pos_diferencia ={
            str(G.node['SILVANIA']['costo']        - G.node['SILVANIA']['calor']):[-74.388056,4.403333],
            str(G.node['TIBACUY']['costo']         - G.node['TIBACUY']['calor']) : [-74.4525, 4.347222] ,
            str(G.node['ARBELAEZ' ]['costo']       - G.node['ARBELAEZ' ]['calor']):[-74.415556,4.272222] ,
            str(G.node['PANDI' ]['costo']          - G.node['PANDI' ]['calor'])   : [-74.487778,4.191111],
            str(G.node['PASCA'  ]['costo']         - G.node['PASCA'  ]['calor']) : [-74.300833, 4.3075],
            str(G.node['SAN BERNARDO']['costo']    - G.node['SAN BERNARDO']['calor']):[-74.422222,4.178889],
            str(G.node['VENECIA'  ]['costo']       - G.node['VENECIA' ]['calor'])    : [-74.4775,4.088611],
            str(G.node['CABRERA'  ]['costo']       - G.node['CABRERA'  ]['calor']) : [-74.485833,3.978056],
            str(G.node['GRANADA'  ]['costo']       - G.node['GRANADA'  ]['calor']) : [-74.351389,4.518611],
            str(G.node['FUSAGASUGA' ]['costo']     - G.node['FUSAGASUGA' ]['calor']) : [-74.364444,4.337222]
            }


    nx.draw_networkx(G,cab )

    maximaDistancia(G)

    values = []
    for i  in costo.keys():
        values.append(costo[i] - calor[i])
        print (" {} :  {}".format(i,(costo[i] - calor[i])))

    listSource=['CABRERA','PANDI', 'VENECIA']
    listTarget=['PASCA', 'GRANADA']
    for i  in listSource:
        for j in listTarget:
            answer=astar_path(G,i,j,heuristica,listNodeTarget= listTarget)
            print(answer)
    plt.show()

import networkx as nx

import math as m

# librerias propias
import mapas as map

def binarizar(decimal):
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario


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

    distancia = map.cal_dis(lista)
    return distancia
def angulo(node1,node2,node3):
    a=distancia(node2,node3)
    b=distancia(node1, node3)
    c=distancia(node1,node2)
    A= m.degrees(m.acos((b**2+ c**2 - a**2)/(2*b*c)))
    return A


def calcularCosto(mask , listCostos):
    costo =0
    for i  in  range(len(listCostos)):
        costo+= int(mask[i])* listCostos[i]
    return costo


def funcion(angulo, radios, costos):
    #listar atributos angulos
    listRadios= []
    for i in radios.keys():
        listRadios.append(radios[i])

    #listar atributos angulos
    listCostos= []
    for i in costos.keys():
        listCostos.append(costos[i])

    #se identifican que conjunto de radios satisfacen el angulo
    for i in range (1, int(len(listRadios)*len(listRadios))):
        posibilidades= binarizar(i)
        cont = 0
        for j in range(0,len(posibilidades)):
            posibilidad= int(posibilidades[j])*listRadios[j]
            cont+=posibilidad
        print (cont)
        if cont >= angulo:
            print(calcularCosto(posibilidades, listCostos))













def heuristica_antena(G, nodeRefer):
    #ubicar angulos teniendo en cuenta coordenadas
    lisAng= []
    Neigh= G[nodeRefer]
    #calcular maximo angulo de separacion
    i = nodeRefer
    for j in Neigh.keys():
        for k in Neigh.keys():
            if not j == k :
                print ("el angulo entre {} y {} es {}".format(j,k,angulo(i,j,k)))
                if not angulo(i,j,k) in lisAng:
                    lisAng.append(angulo(i,j,k))
                    lisAng.append(360 - angulo(i,j,k))


    #determinar que angulo tiene mas separacion y cubre todos los nodos
    lisAng=sorted(lisAng)

    bandera = 0
    while (bandera == 0):
        cont = 0
        for i in lisAng:
            cont += i
            if int(cont) == int(max(lisAng)):
                Angulo = max(lisAng)
                bandera= 1

        lisAng.remove(max(lisAng))

    #angulo maximo que cubre todos los angulos
    print (Angulo)



#grafo
G= nx.Graph()

#coordenadas
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



#arreglo de radios
radios= {
"antena1": 60,
"antena2": 70,
"antena3": 30,
"antena4": 20,
}

#arreglo de costos
costos={
"antena1": 600,
"antena2": 700,
"antena3": 300,
"antena4": 200,
}

#heuristica_antena(G, "ARBELAEZ")
funcion(180, radios, costos)

import networkx as nx
from matplotlib import pyplot as plt

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
    """ a partir de una mascara de bits y una lista de costos
        retorna el valor de la suma de conjunto de nodos

    """
    costo =0
    for i  in  range(len(mask)):
        costo+= int(mask[i])* listCostos[i + len(listCostos)-len(mask)]
    return costo


def funcionMenorCosto(angulo, radios, costos):
    """Retorna el valor del costo minimo de un conjunto de antenas que cubren un angulo

    parametros
    ----------
        angulo  :   float
                    valor de angulo en grados

        radios  :   dict
                    diccionario con llave antenas y valores de radios de cobertura

        costos  :   dict
                    diccionario con llave antenas y valores de costo
    retorna
    ---------
        menor   :   float
                    minimo valor de cobertura
    """
    #listar atributos angulos
    listRadios= []
    for i in radios.keys():
        listRadios.append(radios[i])

    #listar atributos angulos
    listCostos= []
    for i in costos.keys():
        listCostos.append(costos[i])

    comp = m.inf
    menor = None
    print (listRadios)
    print (listCostos)

    #se identifican que conjunto de radios satisfacen el angulo
    for i in range (1, int(len(listRadios)*len(listRadios))):
        posibilidades= binarizar(i)
        cont = 0

        print ("posibilidades {}".format(posibilidades))
        print ("listRadios {}".format(listRadios))
        print ("listCostos {}".format(listCostos))
        for j in range(len(posibilidades)):
            posibilidad= int(posibilidades[j])*listRadios[len(listRadios)-len(posibilidades)+j]
            cont+=posibilidad

        print("contador {}".format(cont))
        print ("angulo {}".format(angulo))
        print ("costo  {}".format(calcularCosto(posibilidades, listCostos)))

        if cont >= angulo:
            if calcularCosto(posibilidades, listCostos) <= comp :
                comp = calcularCosto(posibilidades, listCostos)
                menor = comp
    print  (menor)
    return (menor)

def funcion(alfa ,NAngulos , radios, costos):
    if len(NAngulos)== 1:
        alfa =funcionMenorCosto(NAngulos[0], radios, costos )
    #contador de angulos
    for i  in range (1 , int (len(NAngulos)*len(NAngulos))-1):
        print ("i {}".format(i))
        print ("NAngulos {}".format(NAngulos))
        posibilidad = binarizar(i)

        print ("posibilidad {}".format(posibilidad))
        cont= 0
        for j in range (len(posibilidad)):
            cont+=int(posibilidad[j])*NAngulos[len(NAngulos)-len(posibilidad)+j]
        print ("contador de angulos {}".format(cont))
        if  cont >= alfa:
            if funcionMenorCosto(cont, radios, costos ) < funcionMenorCosto(alfa, radios, costos):
                alfa = cont
        return alfa


    #if funcionMenorCosto(40, radios, costos)


def heuristica_antena(G, nodeRefer):
    #ubicar angulos teniendo en cuenta coordenadas
    lisAng= []
    Neigh= G[nodeRefer]
    #calcular maximo angulo de separacion
    i = nodeRefer
    for j in Neigh.keys():
        for k in Neigh.keys():
            if not j == k :
                if not angulo(i,j,k) in lisAng:
                    lisAng=sorted(lisAng)
                    lisAng.append(angulo(i,j,k))
                    lisAng.append(360 - angulo(i,j,k))

    print ("lista de angulos {}".format(lisAng))
    radiosSuma=[]
    #determinar que angulo tiene mas separacion y cubre todos los nodos
    bandera = 0
    while (bandera == 0):
        cont = 0
        for i in lisAng:
            cont += i
            if int(cont) == int(max(lisAng)):
                Angulo = max(lisAng)
                bandera= 1
        lisAng.remove(max(lisAng))
    NeighAngulos=[]
    for i in range (0,len(lisAng)**2):
        posibilidades = binarizar(i)
        cont =0
        for j in range (len(posibilidades)):
            posibilidad= int(posibilidades[j])*lisAng[ (len(lisAng)-len(posibilidades)) + j]
            cont += posibilidad
            NeighAngulos.append(posibilidad)
        if int(cont) == int(Angulo):
            break
        else:
            NeighAngulos=[]

    if 0 in NeighAngulos:
        NeighAngulos.remove(0)
    NeighAngulos.append(Angulo)
    print ("angulos vecinos {}".format(NeighAngulos))
    print ("angulo {}".format(Angulo))
    funcion(Angulo,NeighAngulos , radios, costos)
    #print ("alfa {}".format(alfa))


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
"antena1": 130,
"antena2": 70,
"antena3": 180,
"antena4": 60,
"antena5": 183,
}

#arreglo de costos
costos={
"antena1": 600,
"antena2": 701,
"antena3": 1000,
"antena4": 200,
"antena5": 1000
}

heuristica_antena(G, "CABRERA")

nx.draw(G, pos=cab)
plt.show()
#funcion(181,[38, 123 , 181] , radios, costos)

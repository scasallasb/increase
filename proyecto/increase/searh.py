import networkx as nx
import math as m
import matplotlib.pyplot as plt

def nextGeneration(N , pasado= None ):
      #listar nodos primera generacion
      listNeih=[]
      for  i in N:
            Neigh= H[i]
            neigh= [i for i in Neigh.keys() if not i =='root']
            if not neigh == [] :
                  for i in neigh:
                        if pasado == None:
                              listNeih.append(i)
                        else :
                              if not i in pasado:
                                    listNeih.append(i)
      return listNeih

def heuristica(node1, node2):
      return(G.node[node2]['diferencia']+ distancia(node1,node2))

def distancia(node1, node2):
    return ( m.sqrt((G.node[node1]['valor'][0] - G.node[node2]['valor'][0])**2   + (G.node[node1]['valor'][1] - G.node[node2]['valor'][1])**2 )  )

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
      ,'e':[6, 8]
      ,'f':[3 ,6]
      ,'g':[7,4]
      ,'h':[11,1.5]
      ,'i':[22,2.5]
      ,'j':[25,6.5]
      ,'k':[24,9]
      ,'l':[20,9]
      ,'m':[20,5.5]
               }
nx.set_node_attributes(G,valor,'valor')
N = ['a' , 'b', 'c', 'd']
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




path= []
for i in  N:
    for j in T_N:
            answer=nx.astar_path(G,i,j,heuristica)
            cont = 0
            for k in range(1,len(answer)):
                  if  answer[k] in  N :
                        cont += 1
            if cont ==   0:
                  path.append(answer)

bestList = []
#escoger la rutas que den mejor beneficio
for j in T_N:
      aux  = 99999
      cont = 0
      for i in path:
            if i[len(i)-1] == j :
                  for k in range (1,len(i)):
                        cont += G.node[i[k]]['diferencia']
                  if cont < aux:
                        aux= cont
                        best =  i
                  cont =0
      bestList.append(best)
      best= 0


#convierte todas las rutas en tuplas de pares de nodos
lista=[]
for i  in bestList:
      for j  in range(0,len(i)-1):
            tupla =(i[j],i[j+1])
            lista.append(tupla)


#agregar nodo raiz
G.add_node('root', valor = [0, 0])
for i in N:
      tupla=('root', i)
      G.add_edge('root', i)
      lista.append(tupla)

#agregar atributo c
c = 0.005


#convertir lista a nodos
H= nx.Graph(lista)


###etiquetar nodos

#atributos de distance r : distancia al nodo raiz
NPV= {}
lista = []
pasado = N
GenR=  nextGeneration(N)
for i in GenR:
      NPV[i]= G.node[i]['diferencia'] /(1 + c)
print (GenR)
bandera=0
cont = 1
while bandera==0:
      cont += 1
      nextGen = nextGeneration(GenR, pasado= pasado)
      pasado = GenR
      GenR=nextGen
      print ("esta generacion {}".format(nextGen))
      for j in nextGen:
            NPV[j]= G.node[j]['diferencia'] /(1 + c)**cont
      if nextGen == []:
            bandera=1
print (NPV)
nx.set_node_attributes(G,NPV,'NPV')



pathsD=[]
    for i in diferen:
    if i != 'root':
        path = nx.dijkstra_path(G, 'root', i )
        print (path)


nextG = nextGeneration(N)
print (nextG)

nextG1=nextGeneration(nextG, pasado= N)

print (nextG1)

nextG2=nextGeneration(nextG1, pasado= nextG)
print (nextG2)

nextG3=nextGeneration(nextG2, pasado= nextG1)
print (nextG3)


#graficas
plt.subplot(211)
nx.draw_networkx(G , valor, nodelist = N,      node_color = 'r')
nx.draw_networkx(G , valor, nodelist = T_N,    node_color = 'g')
nx.draw_networkx(G , valor, nodelist = ['root'],    node_color = 'b')
plt.subplot(212)
nx.draw_networkx(H , valor)
plt.show()

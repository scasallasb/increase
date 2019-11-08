import networkx as nx 
import math as m
import matplotlib.pyplot as plt


import dkjistra as dkj





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

def searchIncrease(G):
      #agregar nodo raiz 
      G.add_node('root', valor = [0, 0])
      lista=[]
      for i in N:
            tupla=('root', i)
            lista.append(tupla)
      G.add_edges_from(lista)



      listPath=[]
      #aplicar el algoritmo Dkjistra desde el nodo raiz a cada n de G
      R=nx.Graph()

      for i  in diferencia.keys():
            path = dkj.dijkstra_path(G, "root", i, weight='diferencia')
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
      c= 0.05
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
      ,'f':[6 ,7] 
      ,'g':[7,3] 
      ,'h':[11,1.5]
      ,'i':[22,2.5]
      ,'j':[25,6.5]
      ,'k':[24,9]
      ,'l':[20,9]
      ,'m':[20,5.5]         
               }
nx.set_node_attributes(G,valor,'valor')
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


R, lista= searchIncrease(G)
plt.subplot(211)
nx.draw_networkx(G, valor)
plt.subplot(212)
nx.draw_networkx(R,valor)
plt.show()



import networkx as nx
import matplotlib.pyplot as plt

import math as m 

def heuristica(node1, node2):
    return(G.node[node1]['costo'] - G.node[node1]['calor'])  

def distancia(node1, node2):
    print ( m.sqrt((G.node[node1]['valor'][0] - G.node[node2]['valor'][0])**2   + (G.node[node1]['valor'][1] - G.node[node2]['valor'][1])**2 )  )
    #return ()

edgeList=   [('1','2'),
            ('2','3'),
            ('3','4'),
            ('4','5'),
            ('3','5'),
            ('1','6'),
            ('6','2'),
            ('6','4'),]
G=nx.Graph(edgeList)

valor={'1':[1, 2]
      ,'2':[1, 3]
      ,'3':[1, 4]
      ,'4':[3, 8]
      ,'5':[1, 6]    
      ,'6':[2 ,2]          
               }
key=list(valor.keys())
G.add_nodes_from(valor.keys())

nx.set_node_attributes(G,valor,'valor')

costo={'1':6
      ,'2':6
      ,'3':6
      ,'4':6
      ,'5':6
      ,'6':6              
               }
nx.set_node_attributes(G,costo,'costo')


calor={'1':1
      ,'2':6
      ,'3':6
      ,'4':4
      ,'5':5
      ,'6':6                 
               }
nx.set_node_attributes(G,calor,'calor')

print ("costo : {}".format(costo))
print ("calor : {}".format( calor))


values = []
for i  in costo.keys():
      values.append(costo[i] - calor[i]) 
      
print(values)
nx.draw_networkx(G , valor)

answer=nx.astar_path(G,'1','5',heuristica)
print (answer)

plt.show()
#funciones python
import networkx as nx
#funciones propias
import Funciones as fn
import TC_ALGO as tc
import START_TC_ALGO as sta
"""
def testEconomy():
    assert()

def comparacionNaiveHeursitic():
    assert()
"""
def funciona():
    #crear un grafo
    j=nx.Graph()

    #crear diccionarios con obstaculos
    er= {(1,2): 12,(2,3):13,(2,4):12,(3,4):16,(4,6):23,(6,7):21,(5,7):13,(5,8):2,(7,8):12,(9,8):4,(9,10):16,(11,9):2}

    for i in er.keys():
        r=list(i)
        j.add_edge(r[0],r[1],weight=er[i])
    assert(tc.TC_ALGO(j))


if __name__== "__main__":
    funciona()
    

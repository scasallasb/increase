import TC_ALGO as tc
import tc_algoMil as tcm
import networkx as nx
if __name__ == "__main__":
    K,A,B,hmax,hmin=1,2.0,10,30,15
    #crear un grafo aleatorio
    #j=nx.erdos_renyi_graph(10,1)
    tc.preparTC(K,A,B,hmax,hmin)
    #crear un grafo
    j=nx.Graph()
    #crear diccionarios con obstaculos
    er= {(1,2): 12,(2,3):13,(2,4):12,(3,4):16,(4,6):23}
    #,(6,7):21,(5,7):13,(5,8):2,(7,8):12,(9,8):4,(9,10):16,(11,9):2}

    for i in er.keys():
        r=list(i)
        j.add_edge(r[0],r[1],weight=er[i])

    #dibujar y graficar
    #nx.draw(j)
    #plt.show()

    #TC_ALGO
    tc.TC_ALGO(j)
    COSTO=[0.75,0.65,1,30,20]
    cC,cT, InG,coverh,T = tc.algo(j,COSTO)
    
    

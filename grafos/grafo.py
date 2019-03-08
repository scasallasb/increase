
import numpy as np 


#nodos=int(input('cuantos nodos tiene el grafo:'))
nodos=6

#init graph
n=[1,2,3,4,5,6]
v=[4,2,1,5,1,8,10,5,8,2,6,10,2]
G= ([1,2],[1,3],[2,3],[2,4],[3,2],[3,4],[3,5],[4,2],[4,3],[4,5], [4,6],[5,3],[5,6])

test=[0,0]
m= np.zeros((nodos, nodos))
MG=np.zeros((nodos, nodos))



#inicializar matriz de respuesta 
Gr=[]
for i in range(nodos):
    Gr.append([0]*nodos)
vertice = -1
cont=0
iteracion=[]




aux_arr= []

for i in range (0,nodos):
    for j in range (0,nodos):
        if ([i+1,j+1] in G ):
            vertice+= 1
            #m[j][i]=1
            m[j][i]= v[vertice]

            
            aux_arr.append(v[vertice])
            iteracion.append([cont+v[vertice],vertice+1,vertice+1])
            Gr[j][i]=[cont+v[vertice],i,i+1]
            

        else:
            m[j][i]= 999

#el primero tiene que ser cero 
m[0][0]=0

        
print(m)


"""algoritmo Djkistra """

compara =np.zeros([nodos,1])

definitivos= np.zeros([nodos,1])
pociciones= np.zeros([nodos,1])

cont =0
posicion=0
definitivo=0
for i in range (0, 2):
    for j in range (0, nodos):
        

        m[:,i]=m[:,int(posicion+definitivo)]
        m[posicion][i]=definitivo
        
        
        
        compara[j]=m[j][posicion]
        if (compara [j]==0):
            compara[j]= 99
        
        print compara
        
        definitivo=min(compara)
        
        

        """
        n=np.where(compara==definitivo)
        print(n)
        """
        


    
    for k in range(len(compara)):
        if (compara[k]==definitivo):
            posicion=k

        #cont=0     

            
    #definitivos[i]=definitivo

#probar traspasar todas una columna

#m[:,1]=m[:,2]
print(m)
#print(n[0])
#print (definitivos)
#print (pociciones)
#print(Gr)

    






import numpy as np
import math as m
import scipy as sc
import matplotlib.pyplot as plt
import networkx as nx


def algo(G1, COST0,met=False,**kwds):
    G=nx.Graph()
    K,A,B,hmax,hmin=COST0[0],COST0[1],COST0[2],COST0[3],COST0[4]
    if met == True:
        G=nx.Graph()
        j=nx.erdos_renyi_graph(G1,1)
        for i in j.edges():
            r=list(i)
            e=np.random.random_integers(0,150)
            G.add_edge(r[0],r[1],weight=e)
        print ('edges, nodes','=',nx.number_of_edges(G),nx.number_of_nodes(G))
    else:
        G=G1;
    print ('ENTRAN_GRA(e,n)=',len(G.edges()),len(G.nodes()))
    InG,G,no_in=Grafo_inicial(G,hmax)
    print ('no_in =',no_in)
    """nx.draw(InG)
    plt.show()

    no_in = [1,8]
    for i in no_in:
        try:
          print i,InG.neighbors(i)
        except nx.exception.NetworkXError:
            pass"""
    #print G.neighbors(31)

    COVERh=nx.Graph()
    COVERh.add_nodes_from(G)
    COMPh=nx.number_connected_components(COVERh)

    inf=m.factorial(10)
    u=nx.get_edge_attributes(G,'weight')
    print ('edges, nodes','=',nx.number_of_edges(G),nx.number_of_nodes(G))
    def c(h):
         if h <= 5:
            costo=K*h*0.1
         elif h <= hmin and h > 5:
            costo=K
         elif h<(hmax) and h > hmin:
            costo=(A*h)+B
         else:
            costo=inf
         return costo
    def c_1(ci):
         if ci > (c(hmin)):
             l=np.ceil((ci-B)/A)
         elif ci>(c(5)) and ci <=(c(hmin)):
             l=hmin
         else:
             l=ci/(K*0.1)
         return l

    def beta(n1,n2,d):
         try:
             aux=(2.0*(u[(n1,n2)]))
         except (IndexError, KeyError):
             aux=(2.0*(u[(n2,n1)]))
         HI=h[n1]+h[n2]+d
         if HI<aux:
             B =aux-HI
         else:
             B=0
         return B

    def nbrfun(n,d):
         p=[]
         r=set()
         for i in range(0,nx.number_connected_components(COVERh)):
             subgraph=(list(nx.connected_component_subgraphs(COVERh)))
             p.append(subgraph[i])
             for o in p[i].nodes():
                 if o==n:
                     r=set(G.neighbors(n)) - set(p[i].neighbors(n))

         r=list(r)
         L=[]
         l=[]
         for i in range(0,len(r)):
             beTa=beta(n,r[i],d)
             G.add_node(r[i],hinc=beTa)
             G.add_node(r[i],cinc=(c(beTa + h[r[i]])- c(h[r[i]])))
             l.append((r[i],(c(beTa+ h[r[i]])-c(h[r[i]]))))
         l=dict(l)

         va=l.values()
         vk=list(l.keys())
         Li=[]
         va = list(va)
         while len(va)>0:
             mi=np.min(va)
             #retirar valor minimo
             d=va.index(mi)
             L.append(vk[d])
             vk.remove(vk[d])
             va.remove(va[d])
         va=[]
         for i in range(0,nx.number_connected_components(COVERh)):
             ri=list(set(L) & set(p[i].nodes()))
             u=inf
             for j in range(0,len(ri)):
                 if L.index(ri[j])< u:
                     try:
                         L.remove(L[u])
                         break
                     except (IndexError):
                         pass
                     u = L.index(ri[j])
         return r, L

    def START_TC_ALGO( h, n, dirac):
         G.add_node(n,hinc=(dirac))
         G.add_node(n,cinc=c(h[n]+dirac)-c(h[n]))
         nbr, L= nbrfun(n,dirac)
         rbest, kbest=inf,0
         for k in range(1,len(L)+1):
             sum=0
             for i in range(0,k):
                 sum= (G.node[L[i]]['cinc'])+sum
             rtemp= ((G.node[n]['cinc']) + sum)/(k)
             if rtemp <  rbest:
                 kbest,rbest=k,rtemp
         L=L[:kbest]
         ri=list(set(G.nodes()) - set(L))
         for i in ri:
             if i==n:
                pass
             else:
                G. add_node(i,hinc=0)
         incr= nx.get_node_attributes(G,'hinc')
         return rbest,incr, L

    for n in G.nodes():
         G.add_node(n,hi=0)
    for n in InG.nodes():
         InG.add_node(n,hi=0)

    while COMPh > 1:
         rbest=inf
         for n in G.nodes():
             h=nx.get_node_attributes(G,'hi')
             chn=c(h[n])
             i,e=1,(c_1(chn+ 1))
             H=[h[n],hmax]
             while e < hmax:
                 H.append(e)
                 e= c_1(chn + (i))
                 i=i+1
             for i in range(0, len(H)):
                 a=(H[i]-h[n])
                 if a<0:a=0
                 rtmp,incrtmp, mayl=START_TC_ALGO(h,n,a)
                 if (rtmp < rbest):
                     nodo,rbest,incrbest, mayL=n,rtmp,incrtmp, mayl
         #print incrbest,nodo,mayL,rbest
         for i in incrbest.keys():
             for j in range (0,len(mayL)):
                 if (incrbest[i] >= 0) and (i==mayL[j]):
                     COVERh.add_edge(nodo,i)
         for i in G.nodes():
             G.add_node(i,hi=h[i]+incrbest[i])
         COMPh=nx.number_connected_components(COVERh)
    costo =0
    for n in G.nodes():
        costo=costo+(c(G.node[n]['hi']))
    T=nx.minimum_spanning_tree(G)
    u1 =nx.get_edge_attributes(T,'weight')
    for n  in T.nodes():
        T.node[n]['hi']=0
    for n in T.edges():
        r=list(n)
        aux=T.node[r[0]]['hi']+T.node[r[1]]['hi']
        aux1=(2* u1[n])
        if aux< aux1:
            T.node[r[0]]['hi']=T.node[r[0]]['hi']+((aux1-aux)/2.0)
            T.node[r[1]]['hi']=T.node[r[1]]['hi']+((aux1-aux)/2.0)
    costo1 =0
    for n in T.nodes():
        costo1=costo1+(c(T.node[n]['hi']))
    InGr=nx.Graph()
    InGr.add_nodes_from(InG.nodes())
    InGr.add_edges_from(COVERh.edges())
    uw =nx.get_edge_attributes(COVERh,'weigth')
    nw =nx.get_node_attributes(G,'hi')
    u1 =nx.get_edge_attributes(T,'weight')
    nx.set_node_attributes(InGr,nw,'hi')
    print ('COVERh','=',nx.number_of_edges(COVERh),nx.number_of_nodes(COVERh))
    print ('T','=',nx.number_of_edges(T),nx.number_of_nodes(T))
    print ('COVERh','=',(nx.get_node_attributes(G,'hi')))
    print ('T','=',(nx.get_node_attributes(T,'hi')))
    print ('COVERh ed=',COVERh.edges())
    print ('T ed=',T.edges())
    return costo,costo1, InG,InGr, T

def Grafo_inicial(G, hmax):
    InG1=nx.Graph()
    InG=nx.Graph()
    no_in=[]
    InG.add_nodes_from(G.nodes())
    u=nx.get_edge_attributes(G,'weight')
    for i in G.edges():
        if u[i]<hmax:
            InG.add_edge(i[0],i[1],weight=u[i])
            InG1.add_edge(i[0],i[1],weight=u[i])
    for i in G.nodes():
        if nx.degree(InG,i)==0:
            no_in.append(i)
    y= nx.number_connected_components(InG1)
    print('Components=',y)
    s1,s=0,0
    if (y)>1:
        aux=list(nx.connected_component_subgraphs(InG1))

        for gr in range(y):

            gr1=aux[gr]
            aux3= list(gr1.nodes())
            s1=len(aux3)
            if s<s1:
                s=s1
                aux1=gr
            else:
                for n in aux[gr].nodes():
                    if n not in no_in:
                        no_in.append(n)
        InG1=aux[aux1]
    return InG,InG1,no_in
"""
costo=[0.65,0.5,1,90,20]
#K,A,B,hmax,hmin
algo(10,costo,met=True)#"""

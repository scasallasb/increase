import networkx as nx
import numpy as np
import scipy as sc
import matplotlib.pyplot as plt
import tc_algo  as tc
import bd2py as bd
import  Hgt as h
import repetidor as rp

def la_lon(Fil=None, Arco=None):
    if Fil is None:
        if Arco:
            la=[]
            lon=[]
            for i in Arco.values():
                la.append(i[1])
                lon.append(i[0])
            coo=[np.mean(la),np.mean(lon)]
    else:
        lon,la=la_lon(Fil=Fil,Arco=Arco)
        coo=[np.mean(la.values()), np.mean(lon.values())]
    return coo

def ext_map(cocen=None,Arco=None, met=False, Fil=None, s=None, **kwds):
    if met==True:
        coo=la_lon(Fil=Fil,Arco=Arco)
        if s is None:
            s=h.vercu(coo,Arco)
    else:
        coo=[cocen[1],cocen[0]]
        if s is None:
            s=10
    au, DiM = h.manipular_mapas(coo,s)
    return au, DiM

def edge_gen(n):
    n=list(n)
    res=[]
    for i in range (0,len(n)):
        for j in range(i+1,len(n)-1):
            res.append((n[i],n[j]))
            
    return res

def ins_rep(DeCo, map, DiM, tam=None, No=None):
    import repetidor as rp
    MaIr={}
    map1=np.ones((len(map),len(map)))
    for i in DeCo.keys():
        PGi=[DeCo[i][1],DeCo[i][0]]
        if tam is None:
            r,p=rp.crcir(PGi,10,DiM,map)
        else:
            r,p=rp.crcir(PGi,tam,DiM,map)
        map1=rp.cirpix(p,map,DiM,Cond=True, map1=map1)
        map1,ar=rp.perfil2(map,DiM,r,PGi,map1,10)
        MaIr[i]=ar
    return MaIr, map1
def map_inter(map, DiM, No='pre', r=True, G=None, p1=None, p2=None):
    if G is not None:
         po=nx.get_node_attributes(G,'pos')
         print (po)
         nx.draw_networkx_nodes(G,po,node_size=80,node_color='g'
                         ,nodelist=p2)
         nx.draw_networkx_nodes(G,po,node_size=250,node_color='r',width=2.0
                         ,nodelist=p1)
         h.draw_networkx_labels1(G,po,font_size=15,font_weight='bold',font_color='w'
                        ,nodelist=p1)
    plt.imshow(map, interpolation='bilinear', extent=DiM, alpha=1.0)
    plt.show()
    if r==True:
        plt.show()
    else:
        try:
            plt.savefig('/home/mrios/Documentos/img2/'+No+"1_rep.png")
        except TypeError:
            plt.savefig('/home/mrios/Documentos/img2/'+str(No)+"1_rep.png")
    plt.clf()
    plt.close()
def conone(map, j):
    aux1=0
    co=0
    for k in j:
        aux=map[k[0], k[1]]
        if aux>aux1:
            aux1=aux
            co=[k[0],k[1]]
    return co
    
def Conv_Rep(Rep, DiM, map):
    PxRep={}
    CoRep={}
    iter=0
    for i in Rep.keys():
        aux1={}
        aux3={}
        for j in Rep[i]:
            aux2=conone(map,j)
            iter=iter+1
            sit='rep'+str(iter)
            aux1[sit]=aux2
            aux3[sit]=(h.px2co(DiM,{1:aux2},map)[1])
        PxRep[i]=aux1
        CoRep[i]=aux3
    return PxRep,CoRep
def color(i):
    color =(10*i) + 20
    return color

def Inter_search(MaIr,DiM, map, map1):
    aux=MaIr.keys()
    Rep={}
    for i in range(len(aux)):
        for j in range(1+i,len(aux)):
            co=color(1)
            aux0=rp.Inter(MaIr[aux[i]],MaIr[aux[j]], co, map1)
            iter=0
            if aux0:
                iter+=1
                try:
                    Rep[iter].append(aux0)
                except KeyError:
                    Rep[iter]=[]                    
                    Rep[iter].append(aux0)
                for k in range(j+1,len(aux)):
                    co=color(iter+1)
                    aux0=rp.Inter(aux0,MaIr[aux[k]], co, map1)
                    if aux0:
                        iter+=1
                        try:
                            Rep[iter].append(aux0)
                        except KeyError:
                            Rep[iter]=[]
                            Rep[iter].append(aux0)
    PxRep,CoRep=Conv_Rep(Rep,DiM,map)
    return Rep, CoRep, map1

def dibujar_grafo_unido(G=None, cab=None,Rep=None
                        ,map=None, DiM=None,nols=None,
                        no_lab=None,title=None, rt=False,s=None,**kwds):
    po=0
    key=list(cab.keys())
    if cab is None:
        pass
    else:
        if len(cab)==1:
            pos= bd.georefxc(key[0])
        else:
            pos= bd.georefxc()
    if G is None:
        G= nx.Graph()
        G.add_nodes_from(cab.keys())
        nx.set_node_attributes(G,'pos',cab)
        attr={}
        for i in pos.keys():
            G.add_nodes_from(pos[i].keys())
            nx.set_node_attributes(G,'pos',pos[i])
            aux=edge_gen(pos[i].keys())
            G.add_edges_from(aux)
            attr[i]=(aux)
    po=nx.get_node_attributes(G,'pos')
    G1nodels=[]
    if map is None:
        map=[]
        map, DiM = ext_map(Arco=po,met=True,s=s)
    if Rep is not None:
        h.show_map(map,DiM,G,Pos=po,nodels=cab.keys()
                ,G1nodels=nols,Repls=Rep,no_lab=no_lab, p=True
                ,title=title, rt=rt)
    else:
        h.show_map(map,DiM,G,Pos=po,nodels=cab.keys()
                    ,G1nodels=nols,no_lab=no_lab, p=True
                    ,title=title, rt=rt)
    return map, DiM
def w_eg(G):
    po=nx.get_node_attributes(G,'pos')
    au, DiM =ext_map(Arco=po, met=True)
    we=[]
    for i in G.edges():
        r=list(i)
        per,o= h.perfil(au,[po[i[0]],po[i[1]]],DiM)
        aux=np.round(np.max(per[3]))  
        we.append((i,aux))   
    we=dict(we)
    return we
def grafo_unido(Cab=None,Rep=None,we=False,co=True,**kwds):
    G= nx.Graph()    
    PO=[]
    Gax=nx.Graph() 
    if Cab is not None:
        G.add_nodes_from(Cab.keys())
        nx.set_node_attributes(G,Cab,'pos')
        aux=edge_gen(G.nodes())
        G.add_edges_from(aux) 
        for i in Cab.keys():
            Gax=nx.Graph()
            if Rep is not None:
                re=Rep[i]
                pre=pos_rep(re)
                Gax.add_nodes_from(pre.keys())
                G.add_nodes_from(pre.keys())
                nx.set_node_attributes(G,pre,'pos')
            pos= bd.georefxc(Fil=[i])
            for t in pos[i].keys():
                PO.append(t)
            Gax.add_nodes_from(pos[i].keys())
            nx.set_node_attributes(Gax,pos[i],'pos')
            G.add_nodes_from(pos[i].keys())
            nx.set_node_attributes(G,pos[i],'pos')
            ed=edge_gen(Gax.nodes())
            Gax.add_edges_from(ed)            
            G.add_edges_from(Gax.edges())
    if we==True:
        w={}
        w=w_eg(G)
        nx.set_edge_attributes(G,w,'weight')
    return G, PO
def pos_rep(Rep, Repcon=None):
    prep={}
    if Repcon is None:
        for i in Rep:
            for j in Rep[i].keys():
                prep[j]=Rep[i][j]
    else:
        for i in RepCon:
             for j in Rep[i].keys():
                prep[j]=Rep[i][j]
    return prep

def ejec_rep(Cab,G=None):
    
    for i in Cab.keys():
        rep={}
        G1=nx.Graph()
        map=[]
        pos= bd.georefxc(Fil=[i])
        G1, pos1=grafo_unido({i:Cab[i]})
        print (i)
        #pos ={'7':{'rep199': [-74.497104, 4.610978], 'rep200': [-74.555972, 4.578489]
         #       ,'rep19': [-74.4903, 4.5924],'rep2': (-74.508625, 4.603122)}}
        Arcoo=pos.values()[0]
        map,DiM=ext_map(Arco=Arcoo,met=True)
        MaIr, map1=ins_rep(pos.values()[0],map,DiM, tam=7)
        Rep,Corep, map1=Inter_search(MaIr,DiM,map, map1)
        #map1[97,131]=120
        G=nx.Graph()
        map_inter(map1,DiM, No=i, r=False,G=G1, p1=[i],p2=pos1)
        try: 
            rep[i]=Corep
        except KeyError:
            rep[i]={}
            rep[i]=Corep
        print (Corep)
        print ('-'*120)
    
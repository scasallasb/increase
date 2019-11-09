import numpy as np
import scipy as sc
import matplotlib.pyplot as plt



import rep_ejec as Re
import tc_algo  as tc
import bd2py as bd
import  Hgt as h
import networkx as nx
import dic_rep as dr


import increase as inc

def usar_algo(G,Cab, rep1=False,max=False,num_rep=None
                    , icu=False, no_lab=None, label =False,**kwds):
    sG={}
    GT=nx.Graph()
    GC=nx.Graph()
    Gi=nx.Graph()
    lsRe=[]
    Po1=[]
    Ps={}
    Sp={}
    for i in Cab.keys():
        cab={i:Cab[i]}
        sG[i]= nx.Graph()
        print (i)
        if rep1 == True:
            rep=dr.dict_rep([i], max=max
                            ,num_rep=num_rep, icu=icu)
            print('Repetidor =',rep)
            lsrep=Re.pos_rep(rep)
            lsrep=Re.pos_rep(lsrep)
            for k in lsrep:
                lsRe.append(k)
        else:
            lsrep=None
            rep=None
            lsRe=None


        sG[i], pos1=Re.grafo_unido(cab,we=True,Rep=rep)



        for k in pos1:
            Po1.append(k)
        """
        pos= bd.georefxc(Fil=[i])
        pos=pos[i]
        pos[i]=cab[i]
        if no_lab is not None:
            no_lab=pos
        """

        u1=nx.get_node_attributes(sG[i],'pos')
        ps= bd.georefxc(Fil=[i],label=True)
        sp=dict((n,n) for n in u1.keys())

        print (nx.get_edge_attributes(sG[i],'weight'))

        map,DiM=Re.dibujar_grafo_unido(G=sG[i], cab=cab, nols=pos1
                    ,rt=True, title=i, Rep=lsrep,no_lab=sp)
        COSTO=[0.75,0.65,1,30,20]
        for k in ps.keys():
            Sp[k]=sp[k]
        for k in ps.keys():
            Ps[k]=ps[k]

        cC,cT, InG,coverh,T = tc.algo(G,COSTO)

        u=nx.get_node_attributes(sG[i],'pos')
        GT.add_nodes_from(sG[i].nodes())
        nx.set_node_attributes(GT,u,'pos')
        GT.add_edges_from(sG[i].edges())
        GC.add_nodes_from(coverh.nodes())
        GC.add_edges_from(coverh.edges())
        nx.set_node_attributes(GC,u,'pos')
        Gi.add_nodes_from(InG.nodes())
        Gi.add_edges_from(InG.edges())
        nx.set_node_attributes(Gi,u,'pos')
        print ('cC=',cC,'cT=', cT)
        print ('*'*200)

    map,DiM=Re.dibujar_grafo_unido(G=GT, cab=Cab, nols=Po1)
    map,DiM=Re.dibujar_grafo_unido(G=GC, cab=Cab, nols=Po1)
    map,DiM=Re.dibujar_grafo_unido(G=Gi, cab=Cab, nols=Po1) 
    return GT

def main():
    G=nx.Graph()
    cab={u'SILVANIA':[-74.388056,4.403333]
            ,u'ARBELAEZ':[-74.415556,4.272222]
            ,u'PANDI':[-74.487778,4.191111]
            ,u'PASCA' :[-74.300833, 4.3075]
            ,u'SAN BERNARDO':[-74.422222,4.178889]
            ,u'VENECIA':[-74.4775,4.088611]
            ,u'CABRERA':[-74.485833,3.978056]
            ,u'GRANADA':[-74.351389,4.518611]
            ,u'FUSAGASUGA':[-74.364444,4.337222]}
    
    
    nx.set_node_attributes(G,cab, 'pos')

    calor={u'SILVANIA':10
                ,u'TIBACUY':10
                ,u'ARBELAEZ':10
                ,u'PANDI':10
                ,u'PASCA' :10
                ,u'SAN BERNARDO':10
                ,u'VENECIA':10
                ,u'CABRERA':10
                ,u'GRANADA':10
                ,u'FUSAGASUGA':10}

    nx.set_node_attributes(G,calor,'calor')
    costo={u'SILVANIA':10
                ,u'TIBACUY':11
                ,u'ARBELAEZ':10
                ,u'PANDI':10
                ,u'PASCA' :10
                ,u'SAN BERNARDO':11
                ,u'VENECIA':10
                ,u'CABRERA':10
                ,u'GRANADA':10
                ,u'FUSAGASUGA':10}

    nx.set_node_attributes(G,costo,'costo')
    
    calor =nx.get_node_attributes(G, 'calor')
    costo =nx.get_node_attributes(G, 'costo')
    """

    diferencia = {
        u'SILVANIA': G.node['SILVANIA']['costo']  - G.node['SILVANIA']['calor'],
        u'TIBACUY': G.node['TIBACUY']['costo']         - G.node['TIBACUY']['calor'] ,
        u'ARBELAEZ': G.node['ARBELAEZ' ]['costo']       - G.node['ARBELAEZ' ]['calor'] ,
        u'PANDI': G.node['PANDI' ]['costo']          - G.node['PANDI' ]['calor']  ,
            u'PASCA' :G.node['PASCA'  ]['costo']         - G.node['PASCA'  ]['calor'] ,
            u'SAN BERNARDO': G.node['SAN BERNARDO']['costo']    - G.node['SAN BERNARDO']['calor'],
            u'VENECIA':G.node['VENECIA'  ]['costo']       - G.node['VENECIA' ]['calor'] ,
            u'CABRERA':G.node['CABRERA'  ]['costo']       - G.node['CABRERA'  ]['calor'],
            u'GRANADA':G.node['GRANADA'  ]['costo']       - G.node['GRANADA'  ]['calor'],
            u'FUSAGASUGA':G.node['FUSAGASUGA' ]['costo']     - G.node['FUSAGASUGA' ]['calor']

        }
    
    nx.set_node_attributes(G,diferencia,'diferencia')
    """
    
    ## searchIncrease
    listSource=[ 'VENECIA']
    listTarget=['PASCA', 'GRANADA']
   
    #answer= inc.targetIncrease(G,listSource,listTarget)
    #print(answer)

    ## searchIncrease
    N = ['FUSAGASUGA' , "CABRERA"]
    T_N=['SILVANIA','ARBELAEZ','TIBACUY','PANDI','PASCA','GRANADA']

    c= 0.05
    #R, lista= inc.searchIncrease(G, N, T_N,c)

    #tc_algo
    #usar_algo(cab, rep1=False)
    
main()

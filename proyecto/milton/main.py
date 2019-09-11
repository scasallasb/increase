import rep_ejec as Re
import numpy as np
import scipy as sc
import matplotlib.pyplot as plt
import tc_algo  as tc
import bd2py as bd
import  Hgt as h
import networkx as nx
import dic_rep as dr

def usar_algo(Cab, rep1=False,max=False,num_rep=None
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
        pos= bd.georefxc(Fil=[i])
        pos=pos[i]
        pos[i]=cab[i]
        if no_lab is not None:
            no_lab=pos

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
        cC,cT, InG,coverh,T = tc.algo(sG[i],COSTO)
        h.show_map(map,DiM,InG,Pos=u1,nodels=[i],Repls=lsrep
            ,G1nodels=pos1,no_lab=ps, p=True
            ,title='InG'+i, rt=True)
        h.show_map(map,DiM,InG,Pos=u1,nodels=[i],Repls=lsrep
            ,G1nodels=pos1,no_lab=sp, p=True
            ,title='InG'+i+'NL', rt=True)
        h.show_map(map,DiM,coverh,Pos=u1,nodels=[i]
            ,G1nodels=pos1,no_lab=ps, p=True,Repls=lsrep
            ,title='cover'+i, rt=True)
        h.show_map(map,DiM,coverh,Pos=u1,nodels=[i]
            ,G1nodels=pos1,no_lab=sp,Repls=lsrep
            ,title='cover'+i+'NL', rt=True)
        plt.show()
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
                    #,rt=True, title='Sumapaz', Rep=lsRe)
    map,DiM=Re.dibujar_grafo_unido(G=GT, cab=Cab, nols=Po1)
                    #,rt=True, title='Sumapazl', Rep=lsRe, no_lab=Ps)
    map,DiM=Re.dibujar_grafo_unido(G=GC, cab=Cab, nols=Po1)
                    #,rt=True, title='Sumapazco', Rep=lsRe)
    map,DiM=Re.dibujar_grafo_unido(G=GC, cab=Cab, nols=Po1)
                    #,rt=True, title='Sumapazcol', Rep=lsRe, no_lab=Ps)
    map,DiM=Re.dibujar_grafo_unido(G=Gi, cab=Cab, nols=Po1)
                    #,rt=True, title='Sumapazi', Rep=lsRe)
    map,DiM=Re.dibujar_grafo_unido(G=Gi, cab=Cab, nols=Po1)
                    #,rt=True, title='Sumapazil', Rep=lsRe, no_lab=Ps)

def main():

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

    #cab={u'CABRERA':[-74.485833,3.978056]}

    """mapa_repetidora
    Re.ejec_rep(cab)
    #"""

    """tcalgo -repetidoras
    usar_algo(cab,num_rep=1,rep1=True)
    # """

    #"""tcalgo
    usar_algo(cab,rep1=False)
    # """

    """ dibujar un solo municipio

    G=nx.Graph()
    G, pos1=Re.grafo_unido(cab)
    Re.dibujar_grafo_unido(G=G, cab=cab, nols=pos1)
    # """

main()

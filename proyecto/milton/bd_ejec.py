import numpy as np
import sqlite3 as sq
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import networkx as nx
import tc_algo as tc

def pru_desem(nmin,nmax,taz,nvec):
    database = sq.connect("midb.db")
    cu = database.cursor()
    try:
        cu.execute("CREATE TABLE Tab_nombre (iter INTEGER PRIMARY KEY, tabla TEXT)")
        database.commit()
    except sq.OperationalError:
        pass
    cu.execute('SELECT * FROM Tab_nombre')
    resultado = dict(cu.fetchall())
    try:
        lid=max(resultado.keys())
        s='Ejecucion'+str(lid+1)
    except ValueError:
        s='Ejecucion1'    
    cu.execute("INSERT INTO Tab_nombre ( tabla) VALUES ('"+s+"' )")
    cu.execute("CREATE TABLE "+s+" (Num_Nodos INTEGER, media float, DeS float)")
    #nmin,nmax,taz,nvec= 3,7,3,2
    med, des=tc.datos(nmin,nmax,taz,nvec,s)
    for i in med.keys():
        cu.execute("INSERT INTO "+s+" ( Num_Nodos, Media, DeS) VALUES ("+str(i)+", "
            +str(med[i])+", "+str(des[i])+")")
    database.commit()
    cu.close()
    database.close()
    
def datos(nmin, nmax, taz, nvec, sis):
    data=[]
    Tda=[]
    Apda=[]
    for i in range(nmin,nmax,taz):
        d=[]
        T=[]
        Ap=[]
        for j in range(nvec):
            a,a1,CO,T=tc.algo(i)
            d.append((a1-a)/a)
            T.append(a1)
            Ap.append(a)
        data.append((i,d))
        Tda.append((i,T))
        Apda.append((i,Ap))
    data=dict(data)
    Tda=dict(Tda)
    Apda=dict(Apda)
    des=[]
    med=[]
    for i in data.keys():
        des.append((i,np.std(data[i])))
        med.append((i,np.mean(data[i])))

    des=dict(des)
    med=dict(med)
    x=med.keys()
    y=med.values()
    error1=des.values()
    
    plt.errorbar(x, y, yerr=error1,linestyle="None", fmt='-o')
    plt.xticks(np.arange(min(med.keys())-1,max(med.keys())+2, 1.0))
    plt.title('Algoritmo Aproximado vs Heuristica Simple')
    plt.xlabel(u'Numero de Nodos')
    plt.ylabel(u'Media R_simple')
    plt.grid()
    plt.savefig(sis+".png")
    return med,des
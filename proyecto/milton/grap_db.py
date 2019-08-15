import numpy as np
import sqlite3 as sq
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import networkx as nx
import tc_algo as tc
def graph_db(save=False, show=False):
    database = sq.connect("midb.db")
    cu = database.cursor()

    cu.execute('SELECT * FROM Ejecucion1')
    med0=cu.fetchall()
    database.commit()
    cu.close()
    database.close()
    med=[]
    des=[]
    for i in range(0,len(med0)):
        med.append((med0[i][0], med0[i][1]))
        des.append((med0[i][0], med0[i][2]))
    med.sort()
    des.sort()
    med =dict(med)
    des=dict(des)
    print des
    x=med.keys()
    y=med.values()
    error1=des.values()

    plt.errorbar(x, y, yerr=error1,linestyle="None", fmt='-o')
    plt.axis([9,51,0,3.0])
    plt.xticks(np.arange(min(med.keys()),max(med.keys())+1, 5))
    plt.title('Algoritmo Aproximado vs Heuristica Simple')
    plt.xlabel(u'Numero de Nodos $n$')
    plt.ylabel(r'Media $R_{simple}$')
    plt.grid()
    if save==True:
        plt.savefig(sis+".png")
    if show==True:
        plt.show()

import urllib.request as urllib2
import urllib
import zipfile
from pylab import *
import numpy as np
import matplotlib.cm as cm
import struct
import networkx  as nx

def px2co(DiM, Pos,aa):
    """
     Devuelve el valor de una posicion geografica alosindices de una matriz
     en dos dimensiones.
     aa es lamatriz geografica recortada HGT.
     DiM son los limites goograficos de la imagen o matriz de alturas HGT.
     Pos es una un diccionario donde se evian varias llaves
     representadas por una lista [lon,la] en pixeles
    """
    e=aa.shape

    pos=[]
    for i in Pos.keys():
        aux=list(Pos[i])
        lon=round(DiM[0]+ ((abs(DiM[0]-DiM[1])/e[1])*aux[1]),6)
        la=round(DiM[3]-((abs(DiM[2]-DiM[3])/e[0])*aux[0]),6)
        pos.append((i,(lon,la)))
    coo=dict(pos)
    return coo

def co2px(DiM, Pos,aa):
    """
     Devuelve el valor de una posicion carteciana en una matriz a una posicion
     geografica.
     aa es lamatriz geografica recortada HGT.
     DiM son los limites goograficos de la imagen o matriz de alturas HGT.
     Pos es una un diccionario donde se evian varias llaves
     representadas por una lista [lon,la] en coordenadas
    """
    pos=[]
    for i in Pos.keys():
        aux=list(Pos[i])
        pos.append((i,(int(abs((aux[0]-DiM[0])*1200)),int(abs((aux[1]-DiM[3])*1200)))))
    pos=dict(pos)
    return pos

def descargar_mapas(strig):
    try:
        open(r"HGT_storage/"+strig+".HGT","rb")
    except IOError:
        req=urllib2.Request('http://rmw.recordist.com/srtm3/'+strig+'.hgt.zip')
        to=urllib2.urlopen(req)
        lc_file = open("HGT_storage/"+strig+".hgt.zip", "wb")
        lc_file.write(to.read())
        lc_file.close()
        so = zipfile.ZipFile( "HGT_storage/"+strig+".hgt.zip" ,  'r')
        for name in so.namelist():
            a =so.extract(name, "HGT_storage/")
        so.close()
def matriz_mapas(strig):
    import matplotlib.pyplot as plt
    filename=(r"HGT_storage/"+strig+".HGT")
    fi=open(filename,"rb")
    contents=fi.read()
    fi.close()
    z=struct.unpack(">1442401H", contents)
    zzz = np.zeros((1201,1201))
    for r in range(0,1201):
        for c in range(0,1201):
            va=z[(1201*r)+c]
            if (va==65535 or va<0 ):
                va=0.0
            zzz[c][r]=float(va)
    aaa=np.array(zzz)
    return aaa
def show_map(aaa,Dim,G1,p=True,Pos=None,
                        G1nodels=None,
                        nodels=None,
                        edgels=None,
                        line=None,
                        Repls=None,
                        no_lab=None,
                        rt=False,
                        title=False,
                        **kwds):
    import networkx as nx
    G=nx.Graph()
    G=G1
    x, y = np.gradient(aaa)
    slope = np.pi/2. - np.arctan(np.sqrt(x*x + y*y))
    aspect = np.arctan2(-x, y)
    altitude = np.pi / 6.
    azimuth = np.pi /2.
    zz = np.sin(altitude) * np.sin(slope)\
        + np.cos(altitude) * np.cos(slope)\
        * np.cos((azimuth - np.pi/2.) - aspect)
    grid(False)
    if p==True:
        if Repls is not None:
            pass
            nx.draw_networkx_nodes(G,Pos,node_size=80,node_color='g'
                              ,nodels=Repls)
        nx.draw_networkx_nodes(G,Pos,node_size=80,node_color='b'
                         ,nodelist=G1nodels)
        nx.draw_networkx_nodes(G,Pos,node_size=250,node_color='r',width=2.0
                         ,nodelist=nodels)
        if no_lab is not None:
            draw_networkx_labels1(G,Pos,labels=no_lab,font_size=5,font_color='w'
                 ,nodelist=G1nodels,font_weight='bold')
        draw_networkx_labels1(G,Pos,font_size=14,font_weight='bold',font_color='k'
                 ,nodelist=nodels)
        nx.draw_networkx_edges(G,Pos,width=0.5)
    else:
        nx.draw_networkx(G,Pos,node_size=250,node_color='w')
    plt.imshow(zz, interpolation='bilinear',extent=Dim,cmap='gist_earth', alpha=1.0)
    s=18
    plt.ylabel(r"$Latitud$", size=s)
    plt.xlabel(r"$Longitud$", size=s)
    if rt ==False:
        plt.show()
    else:
        plt.savefig('img3/'+title+'.png')
    plt.clf()
    plt.close()
def cadena(PGi,xom):
    if PGi[0]<0.0:
        La="S"
        if PGi[0] > -9:
            aux= int(np.abs(PGi[0]))+1
            la="0"+ str(aux)
        else:
            aux= int(np.abs(PGi[0]))+1
            la=str(aux)
    else:
        La="N"
        if PGi[0] < 10:
            aux= int(np.abs(PGi[0]))
            la="0"+ str(aux)
        else:
            aux= int(np.abs(PGi[0]))
            la=str(aux)
    if PGi[1]<0:
        Lo="W"
        if PGi[0] > -99:
            aux= int(np.abs(PGi[1]))+1
            lo="0"+ str(aux)
        else:
            aux=int(np.abs(PGi[1]))+1
            lo=str(aux)
    else:
        Lo="E"
        if PGi[1] < 100:
            aux=int(np.abs(PGi[1]))
            lo="0"+ str(aux)
        else:
            aux=int(np.abs(PGi[1]))
            lo=str(aux)
    if xom ==0:
        cadena=La+la+Lo+lo
    if xom== 1:
        cadena=[int(la),(int(lo),La+la+Lo+lo)]
    return cadena
def cal_dis(PGi):
    pgi=PGi[0]
    pgf=PGi[1]
    lai=(pgi[0]*3.1416)/180.0
    loi=(pgi[1]*3.1416)/180.0
    laf=(pgf[0]*3.1416)/180.0
    lof=(pgf[1]*3.1416)/180.0
    dla=laf-lai
    dlo=lof-loi
    Dis= 6378.137 * np.arccos( np.cos(lai) * np.cos(laf) * np.cos(lof - loi) + np.sin(lai) * np.sin(laf))
    return Dis
def fresnel(dis, f):
    fr=[]
    d=dis[len(dis)-1]
    for i in dis:
        fr.append((17.3*(np.sqrt((i*(d-i))/(f*(i+(d-i)))))))
    return np.array(fr)

def max2cen(per, d, **atr):
    pass

def max_alt(per):
    al=np.array(per[1])
    dis=np.array(per[0])
    d=len(al)-1
    dydx=(al[d]-al[0])/(dis[d]-dis[0])
    fr=fresnel(dis, 5000)
    lv=(dis*dydx)+al[0]
    lv0=list(al-lv+fr)
    dp=dis[lv0.index(max(lv0))]
    #max2cen(per,[dp,lv0])
    #plt.plot(dis,al,dis,lv)
    #plt.show()
    #print lv0
    #return [dp,max(lv0)]
    return [dis,al,lv,lv0]

def perfil(aaa, coo, DiM,met=False,**kwds):
    pot=0
    p={0:coo[0],1:coo[1]}
    p1={0:[coo[0][1], coo[0][0]],1:[coo[1][1], coo[1][0]]}
    d=cal_dis(p1)
    pix=co2px(DiM, p,aaa)
    if pix[1][0]==pix[0][0]and pix[1][1]==pix[0][1]:
        do=do=[0,0,0,[0,0,0]]
    else:
        dx=pix[0][0]-pix[1][0]
        dy=pix[0][1]-pix[1][1]
        if np.abs(dx)>=np.abs(dy):
            if pix[1][0]<pix[0][0]:
                p1=pix[1]
                p2=pix[0]
                pot=1
            else:
                p1=pix[0]
                p2=pix[1]
                pot=0
            dydx=(p2[1]-p1[1])*1.0/(p2[0]-p1[0])
            b=p1[1]-dydx*p1[0]
            bx=p1[0]
            dom=np.abs(p2[0]-p1[0])
            aux=1
        else:
            if pix[1][1]<pix[0][1]:
                p1=pix[1]
                p2=pix[0]
                pot=1
            else:
                p1=pix[0]
                p2=pix[1]
                pot=0
            dydx=(p2[0]-p1[0])*1.0/(p2[1]-p1[1])
            b=p1[0]-dydx*p1[1]
            bx=p1[1]
            dom=np.abs(p2[1]-p1[1])
            aux=0
        y=[]
        x=[]
        pr=[]
        x0,y0=0,0
        for i in range(0,dom+1):
            y0=int(round((dydx*(bx+i)))+b)
            x.append(x0)
            if aux==1:
                r=aaa[y0][bx+i]
                pr.append((x0,[y0,bx+i]))
            else:
                r=aaa[bx+i][y0]
                pr.append((x0,[bx+i,y0]))
            y.append(r)
            x0=(x0+(d/dom))
        per=[x,y]
        do=max_alt(per)
    if met==True:
        do=[do,pr]
    return do,pot

def manipular_mapas(PG, AnKM):
    PoIm=[]
    if PG[0]<=0:
        KmP=cal_dis(([PG[0]-1,PG[1]],[PG[0]-1,PG[1]+1]))/1200.0
    else:
        KmP=cal_dis(([PG[0]+1,PG[1]],[PG[0]+1,PG[1]+1]))/1200.0
    Nps=int(np.round(AnKM/(2*KmP)))
    PoIm.append(1201-np.round(np.abs(PG[0]-int(PG[0]))*1200))
    PoIm.append(1201-np.round(np.abs(PG[1]-int(PG[1]))*1200))
    Pu=[PoIm[0]+Nps,PoIm[1]+Nps,PoIm[0]-Nps, PoIm[1]-Nps]
    pu=dict([(Pu[0],(Pu[1],Pu[3])),(Pu[2], (Pu[1], Pu[3]))])
    coo=[]
    aux1=[]
    for i in pu.keys():
        for j in range(0,2):
            if i <0:
                if pu[i][j] <0:
                    aux1.append(np.ceil((np.abs(i))/1200))
                    aux1.append(np.ceil(np.abs(pu[i][j])/1200))
                    aux =int(max (aux1))
                    for u in range(0,aux+1):
                        for t in range(0,(aux+1)):
                            coo.append((PG[0]+u,PG[1]-t))
                elif pu[i][j]>1200:
                    aux1.append(np.ceil(np.abs(i)/1200))
                    aux1.append(np.ceil((np.abs(pu[i][j])-(1200-PoIm[1]))/1200))
                    aux =int(max (aux1))
                    for u in range(0,aux+1):
                        for t in range(0,(aux+1)):
                            coo.append((PG[0]+u,PG[1]+t))
                else:
                    coo.append((PG[0]+1,PG[1]))
            elif i>1200:
                if pu[i][j]< 0:
                    aux1.append(np.ceil((np.abs(i)-(1200-PoIm[0]))/1200))
                    aux1.append( np.ceil((np.abs(pu[i][j]))/1200))
                    aux =int(max (aux1))
                    for u in range(0,aux+1):
                        for t in range(0,(aux+1)):
                            coo.append((PG[0]-u,PG[1]-t))
                elif pu[i][j]>1200:
                    aux1.append(np.ceil((np.abs(i)-(1200-PoIm[0]))/1200))
                    aux1.append(np.ceil((np.abs(pu[i][j])-(1200-PoIm[1]))/1200))
                    aux =int(max (aux1))
                    for u in range(0,aux+1):
                        for t in range(0,(aux+1)):
                            coo.append((PG[0]-u,PG[1]+t))
                else:
                    coo.append((PG[0]-1,PG[1]))
            elif pu[i][j]<0:
                coo.append((PG[0],PG[1]-1))
            elif pu[i][j]>1200:
                coo.append((PG[0],PG[1]+1))
            else:
                coo.append((PG[0],PG[1]))
    co=[cadena(coo[0],1)]
    co1={}
    co1[co[0][0]]=dict([co[0][1]])
    k=[]
    for  i in range(0,len(coo)):
        aux=cadena(coo[i],1)
        k=aux
        for  j in range(0,len(co)):
            if aux  == co[j]:
               k=['no']
        if k==aux:
            aux2=[]
            co.append(aux)
            for j in range (0,len (co)):
                if co[j][0]==aux[0]:
                    aux2.append(co[j][1])
            d=dict(aux2)
            co1[aux[0]]=d
    aux, aux3, aux2, aux1=0,0,0,0
    for i in co1.keys():
        aux1=0
        for j in co1[i].keys():

            aux=matriz_mapas(co1[i][j])
            try:
                aux1=np.concatenate((aux,aux1), axis=0)
            except  (IndexError, KeyError,ValueError):
                aux1=aux
        try:
            aux2=np.concatenate((aux1,aux2), axis=1)
        except  (IndexError, KeyError,ValueError):
            aux2=aux1
    p=[0,0]
    for i in range(0,2):
        if Pu[i+2] <0:
            p[i]=int((np.ceil(np.abs(Pu[i+2]/1200))*1200)+PoIm[i])
        else:
            p[i]=int(np.abs(PoIm[i]))

    #aux2[p[1]-20:p[1]+20,p[0]-20:p[0]+20]=-.8
    au=aux2[p[1]-Nps:p[1]+Nps,p[0]-Nps:p[0]+Nps]
    DiM=[PG[1]-(Nps/1200.0),PG[1]+(Nps/1200.0),PG[0]-(Nps/1200.0),PG[0]+(Nps/1200.0)]
    #show_map(au.T,DiM,1,pos)
    return au.T, DiM


def vercu(PG, Pos):
    TKm=5
    PoIm=[]
    if PG[0]<=0:
        KmP=cal_dis(([PG[0]-1,PG[1]],[PG[0]-1,PG[1]+1]))/1200.0
    else:
        KmP=cal_dis(([PG[0]+1,PG[1]],[PG[0]+1,PG[1]+1]))/1200.0
    Nps=int(np.round(TKm/(2*KmP)))
    PoIm.append(1201-np.round(np.abs(PG[0]-int(PG[0]))*1200))
    PoIm.append(1201-np.round(np.abs(PG[1]-int(PG[1]))*1200))
    Pu=[PoIm[0]+Nps,PoIm[1]+Nps,PoIm[0]-Nps, PoIm[1]-Nps]
    DiM=[PG[1]-(Nps/1200.0),PG[1]+(Nps/1200.0),PG[0]-(Nps/1200.0),PG[0]+(Nps/1200.0)]
    s=TKm
    s1=0
    for i in Pos.keys():
        aux=list(Pos[i])
        if aux [1]< DiM [3] and aux[1]> DiM[2]:
            if aux [0]<DiM [0]:
                s1=TKm + 2*ceil(cal_dis([[aux[0],aux[1]],[DiM[0],DiM[3]]]))
            if aux [0]>DiM [1]:
                s1=TKm + 2*ceil(cal_dis(([aux[0],aux[1]],[DiM[1],DiM[3]])))
        elif aux [0]> DiM [0] and aux[0] <DiM[1]:
            if aux [1]< DiM [2]:
                s1=TKm + 2*ceil(cal_dis([[aux[0],aux[1]],[DiM[1],DiM[2]]]))
            if aux [1]>DiM [3]:
                s1=TKm + 2*ceil(cal_dis(([aux[0],aux[1]],[DiM[1],DiM[3]])))
        else:
            if aux [0]< DiM [0] and aux[1]< DiM[2]:
                s1=TKm + 2*ceil(cal_dis(([aux[0],aux[1]],[DiM[0],DiM[2]])))
            elif aux [0]< DiM [0] and aux[1]> DiM[3]:
                s1=TKm + 2*ceil(cal_dis(([aux[0],aux[1]],[DiM[0],DiM[3]])))
            elif aux [0]> DiM [1] and aux[1]< DiM[2]:
                s1=TKm + 2*ceil(cal_dis(([aux[0],aux[1]],[DiM[1],DiM[2]])))
            elif aux [0]> DiM [1] and aux[1]> DiM[3]:
                s1=TKm + 2*ceil(cal_dis(([aux[0],aux[1]],[DiM[1],DiM[3]])))
        if s1>s:
            s=s1
    return s*2

def draw_networkx_labels1(G, pos,
                         labels=None,
                         font_size=None,
                         font_color='k',
                         font_family='sans-serif',
                         font_weight='normal',
                         alpha=1.0,
                         ax=None,
                         nodelist=None,
                         **kwds):
    """Draw node labels on the graph G.

    Parameters
    ----------
    G : graph
       A networkx graph

    pos : dictionary, optional
       A dictionary with nodes as keys and positions as values.
       If not specified a spring layout positioning will be computed.
       See networkx.layout for functions that compute node positions.

    font_size : int
       Font size for text labels (default=12)

    font_color : string
       Font color string (default='k' black)

    font_family : string
       Font family (default='sans-serif')

    font_weight : string
       Font weight (default='normal')

    alpha : float
       The text transparency (default=1.0)

    ax : Matplotlib Axes object, optional
       Draw the graph in the specified Matplotlib axes.


    Examples
    --------
    >>> G=nx.dodecahedral_graph()
    >>> labels=nx.draw_networkx_labels(G,pos=nx.spring_layout(G))

    Also see the NetworkX drawing examples at
    http://networkx.lanl.gov/gallery.html


    See Also
    --------
    draw()
    draw_networkx()
    draw_networkx_nodes()
    draw_networkx_edges()
    draw_networkx_edge_labels()
    """
    try:
        import matplotlib.pylab as pylab
        import matplotlib.cbook as cb
    except ImportError:
        raise ImportError("Matplotlib required for draw()")
    except RuntimeError:
        print("Matplotlib unable to open display")
        raise

    if font_size is None:
        font_size=12
    else:
        font_size=font_size

    if ax is None:
        ax=pylab.gca()

    if labels is None:
        if nodelist is None:
            labels=dict( (n,n) for n in G.nodes())
        else:
            labels=dict( (n,n) for n in nodelist)
    # set optional alignment
    horizontalalignment=kwds.get('horizontalalignment','center')
    verticalalignment=kwds.get('verticalalignment','center')

    text_items={}  # there is no text collection so we'll fake one
    for n, label in labels.items():
        (x,y)=pos[n]
        #if not cb.is_string_like(label):
            #label=str(label) # this will cause "1" and 1 to be labeled the same
        t=ax.text(x, y,
                  label,
                  size=font_size,
                  color=font_color,
                  family=font_family,
                  weight=font_weight,
                  horizontalalignment=horizontalalignment,
                  verticalalignment=verticalalignment,
                  transform = ax.transData,
                  clip_on=True,
                  )
        text_items[n]=t
    return text_items

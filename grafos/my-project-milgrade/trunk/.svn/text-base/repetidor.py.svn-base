import Hgt as h
import numpy as np
import matplotlib.pyplot as plt
import networkx  as nx

def drange(start, stop, step):
    r = [start]
    d=start
    while d < stop:
        d= d+step
        r.append(d)
    return r
    
def distan(PGi,Km,DiM):
    dis= h.cal_dis([[DiM[0],DiM[2]],[DiM[1],DiM[2]]])
    rel=abs(DiM[0]-DiM[1])*Km*1200/dis
    rel1=abs(DiM[0]-DiM[1])*Km/dis
    return dis , rel,rel1
def crcir(PGi,Km,DiM,aa):
    di,n,n1=distan(PGi,Km,DiM)
    g=np.ceil(((np.ceil(n)+1))*10)
    t=drange(0.0, 2*np.pi,(2*np.pi/g))
    cc=[]
    ccp=[]
    aux1=0
    red=0.999999
    red1=1.000001
    DiM=[DiM[0]*red,DiM[1]*red1,DiM[2]*red1,DiM[3]*red]
    for i in t:
        la,lon=PGi[0]+(n1*np.sin(i)),PGi[1]+(n1*np.cos(i))
        if la< DiM[2] or la> DiM[3]:
            if la< DiM[2]:
                aux=DiM[2]
            else:
                aux=DiM[3]
            if lon<DiM[0]:
                aux1=(aux,DiM[0])
            elif lon>DiM[1]:
                aux1=(aux,DiM[1])
            else:
                aux1=(aux,lon)
        elif lon< DiM[0] or lon> DiM[1]:
            if lon< DiM[0]:
                aux=DiM[0]
            else:
                aux=DiM[1]
            if la<DiM[2]:
                aux1=(DiM[2],aux)
            elif la>DiM[3]:
                aux1=(DiM[3],aux)
            else:
                aux1=(la, aux)
        else:
            aux1=(la,lon)
        cc.append(aux1)
        ccp. append(h.co2px(DiM,{0:[aux1[1],aux1[0]]},aa)[0])
    return cc,ccp
def cirpix(ccp, aa, DiM, Cond=False, map1=None, **kwds):
    ncc=[]
    if Cond==False:
        aa1=np.ones((len(aa),len(aa)))
    else:
        aa1=map1  
    cc=[]
    for i in ccp:
        if i[0]> len(aa)-1 or i[0]<0 :
            if i[0]< 0:
                aux=0
            else:
                aux=len(aa)-1
            if i[1]< 0 :
                aux1=(aux,0)
            elif i[1]> len(aa)-1 :
                aux1=(aux,len(aa)-1)
            else:
                aux1=(aux,i[1])
        elif i[1]> len(aa)-1 or i[1]<0 :
            if i[1]< 0:
                aux=0
            else:
                aux=len(aa)-1
            if i[0]< 0 :
                aux1=(0,aux)
            elif i[0]> len(aa)-1 :
                aux1=(len(aa)-1,aux)
            else:
                aux1=(i[0],aux)
        else:
            aux1=(i[0],i[1])
        #cc.append(h.px2co(DiM,{0:[aux1[0],aux1[1]]},aa)[0])
        aa1[aux1[1]][aux1[0]]=150
    return aa1
def irpoint(per,o,aa1,AreaIr, color):
    d=per[0][0]
    al=per[0][3]
    ld=len(d)-1
    er=dict(per[1])
    if o ==1:
        aux=ld
    else:
        aux=0
    ip=abs(0+aux)
    j=0
    for i in  range(0, ld):
        iter=abs(aux-i)
        e=np.arctan2(al[iter],d[iter])
        if e>=j:
            j=e
            AreaIr.append(er[d[iter]])
            row=int(er[d[iter]][0])
            col=int(er[d[iter]][1])
            if aa1[row][col]==150:
                pass
            else:
                aa1[row][col]=color
            
def perfil2(aa,DiM, cc, PGi,aa1, color):
    """
    se envian parametros PG como la posicion central como una lista de dos items
    PGi=(lat,lon)
    """
    AreaIr=[]
    for i in cc:
        coo=[[PGi[1],PGi[0]],[i[1],i[0]]]
        per,o=h.perfil(aa,coo,DiM, met=True)
        irpoint(per,o,aa1,AreaIr, color)
    return aa1, AreaIr
def Inter(a,b, co ,map):
    y={}
    r=[]
    for i in a:
        for j in b:
            if i == j:
                if map[j[0],j[1]] == 150:
                    pass
                elif map[j[0],j[1]]<co:
                    map[j[0],j[1]]=co
                y[(j[0],j[1])]=0;
    for  i in y.keys():
        r.append([i[0], i[1]])
    return r


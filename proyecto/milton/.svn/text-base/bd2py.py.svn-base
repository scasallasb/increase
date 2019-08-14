def georefxc(Fil=None, label=False,**kwds):
    import xlrd as xl
    b=xl.open_workbook("inesu.xls")
    sh=b.sheet_by_index(1)
    co=[]
    co2={}
    if Fil is not None:
        for i in Fil:
            for rx in range(sh.nrows):
                if i==sh.cell_value(rowx=rx,colx=0):  
                    co.append((rx,sh.cell_value(rowx=rx,colx=2)
                            ))
                    try:
                        co2[sh.cell_value(rowx=rx,colx=0)][rx]=[sh.cell_value(rowx=rx,colx=7) 
                            ,sh.cell_value(rowx=rx,colx=6)]
                    except KeyError:
                        co2[sh.cell_value(rowx=rx,colx=0)]={rx:[sh.cell_value(rowx=rx,colx=7)
                            ,sh.cell_value(rowx=rx,colx=6)]}
    else:
        for rx in range(sh.nrows):  
            co.append((rx,sh.cell_value(rowx=rx,colx=2)))
            try:
                co2[sh.cell_value(rowx=rx,colx=0)][rx]=[sh.cell_value(rowx=rx,colx=7)
                    ,sh.cell_value(rowx=rx,colx=6)]
            except KeyError:
                co2[sh.cell_value(rowx=rx,colx=0)]={rx:[sh.cell_value(rowx=rx,colx=7)
                    ,sh.cell_value(rowx=rx,colx=6)]}
    if label== False:
        return co2
    else:
        return dict(co)
    
def la_lon(Fil=None,**kwds):
    import xlrd as xl
    b=xl.open_workbook("inesu.xls")
    sh=b.sheet_by_index(1)
    co={}
    co1={}
    coco={}
    t=0
    if Fil is not None:
        for rx in range(sh.nrows):
            if Fil==sh.cell_value(rowx=rx,colx=0):
                co[t]=sh.cell_value(rowx=rx,colx=7)
                co1[t]=sh.cell_value(rowx=rx,colx=6)
                coco[t]=(sh.cell_value(rowx=rx,colx=7),sh.cell_value(rowx=rx,colx=6))
                t=t+1
    else: 
        for rx in range(sh.nrows):  
            co[rx]=sh.cell_value(rowx=rx,colx=7)
            co1[rx]=sh.cell_value(rowx=rx,colx=6)
            coco[rx]=(sh.cell_value(rowx=rx,colx=7),sh.cell_value(rowx=rx,colx=6))
    return co,co1


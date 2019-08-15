from __future__ import division
import urllib2
import urllib
import zipfile
from pylab import *
import networkx as nx
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import matplotlib.image as mg
import struct

def down(strig):
    try:
        print open(r"/home/mrios/Documentos/HGT_storage/"+strig+".HGT","rb")
    except IOError:
        req=urllib2.Request('http://rmw.recordist.com/srtm3/'+strig+'.hgt.zip')
        to=urllib2.urlopen(req)
        lc_file = open("/home/mrios/Documentos/HGT_storage/"+strig+".hgt.zip", "wb")
        lc_file.write(to.read())
        lc_file.close()
def down1(rios):
    s= "-74.52378273010254,4.435755478979805,-74.4279956817627,4.487440116858266"
    req=urllib2.Request("http://render.openstreetmap.org/cgi-bin/export?bbox=%s&scale=34502&format=png"%s)
    to=urllib2.urlopen(req)
  
    lc_file = open("/home/mrios/Documentos/OSM_storage/%s.png"%rios, "wb")
    lc_file.write(to.read())
    lc_file.close()

rios ='miltonten'
down1(rios)

'''
so = zipfile.ZipFile("/home/mrios/Documentos/HGT_storage/"+strig+".hgt.zip" ,  'r')
for name in so.namelist():
    print name
    a =so.extract(name, "/home/mrios/Documentos/HGT_storage/")
so.close()'''
aaa=mg.imread(r"/home/mrios/Documentos/OSM_storage/%s.png"%rios)

'''x, y = np.gradient(aaa)
slope = np.pi/2. - np.arctan(np.sqrt(x*x + y*y))
aspect = np.arctan2(-x, y)
altitude = np.pi / 6.
azimuth = np.pi /2.
zz = np.sin(altitude) * np.sin(slope)\
    + np.cos(altitude) * np.cos(slope)\
    * np.cos((azimuth - np.pi/2.) - aspect)
G=nx.complete_graph(3)
#pos={1:(0,1200), 0 :(0,0), 2:(1200,1200), 3:(1200,0), 4:(600,600)}
pos={0:(-74.1,4.33),1:(-74.234,3.99),2:(-74.38756,4.5)}
ext=[-74.74083333333333, -74.01916666666666, 3.9691666666666667, 4.690833333333334]
nx.draw_networkx(G,pos)'''
#imshow(zz*3600, interpolation='bilinear',cmap='gist_earth', alpha=1.0)

#plt.imshow(aaa, interpolation='bilinear', alpha=1.0)
aa=aaa[1:200,1:200]
print len(aa), len(aa.T)
'''s=18
plt.ylabel(r"$Latitud$", size=s)
plt.xlabel(r"$Longitud$", size=s)'''

#plt.show()"""
#!/usr/bin/env python
"""
Layer images above one another using alpha blending
"""

from pylab import *

def func3(x,y):
    return (1- x/2 + x**5 + y**3)*exp(-x**2-y**2)

# make these smaller to increase the resolution
dx, dy = 0.05, 0.05

x = arange(-3.0, 3.0, dx)
y = arange(-3.0, 3.0, dy)
X,Y = meshgrid(x, y)
x=len(aa)
y=len(aa)

# when layering multiple images, the images need to have the same
# extent.  This does not mean they need to have the same shape, but
# they both need to render to the same coordinate system determined by
# xmin, xmax, ymin, ymax.  Note if you use different interpolations
# for the images their apparent extent could be different due to
# interpolation edge effects


xmin, xmax, ymin, ymax = amin(x), amax(x), amin(y), amax(y)
extent = xmin, xmax, ymin, ymax
fig = plt.figure(frameon=False)

Z1 = array(([0,1]*4 + [1,0]*4)*4); Z1.shape = 8,8  # chessboard
im1 = imshow(Z1, cmap=cm.gray, interpolation='nearest')
 #            extent=extent)
hold(True)

Z2 = func3(X, Y)

im2 = imshow(aaa, alpha=0.9, interpolation='bilinear')
#xis([xmin, xmax, ymin, ymax])

show()


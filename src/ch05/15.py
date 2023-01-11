import pylab
import numpy as np
from random import *
pi=np.pi
n=1000
ts=np.linspace(0,12*pi,n)
xs=np.sin(ts)*(np.exp(np.cos(ts))-2*np.cos(4*ts)-np.sin(ts/12)**5)
ys=np.cos(ts)*(np.exp(np.cos(ts))-2*np.cos(4*ts)-np.sin(ts/12)**5)


map=[[0x8,0x8,0x7f,0x49,0x7f,0x8,0x8],[0x8,0x8,0x3e,0x2a,0x7f,0x14,0x63]]
R,C=7,7
ds=5
#m=int(input("> "))
m = 1
ds=20
pylab.axis("off")
for r in range(R):
    for L in range(len(map)):
        for c in range(C-1,-1,-1):
            if (map[L][r]>>c)%2:
                a=2*pi*random()
                sina=np.sin(a)
                cosa=np.cos(a)
                ra=(1/m)*(0.8+0.2*random())
                for i in range(m):
                    for j in range(m):
            
                        dx=(C-1-c)*ds+i*(ds/m)+L*(C+1)*ds
                        dy=(R-1-r)*ds+j*(ds/m)
                        
                        xs2=(cosa*xs-sina*ys)*ra+dx
                        ys2=(sina*xs+cosa*ys)*ra+dy        
                        cs=[random()for k in range(3)]
                        pylab.fill(xs2,ys2,color=cs)
pylab.show()

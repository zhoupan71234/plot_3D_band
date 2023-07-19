#!/usr/bin/env /home/zhoupan/software/python2.7.3/epd_free-7.3-2-rh5-x86_64/bin/python2.7



from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import re
from matplotlib import cm
##
fig = plt.figure()
ax = Axes3D(fig)
##X = np.arange(-4, 4, 0.25)
##Y = np.arange(-4, 4, 0.25)
##X, Y = np.meshgrid(X, Y)
##R = np.sqrt(X**2 + Y**2)
##Z = np.sin(R)
##
##ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')
##
##plt.show()

bandfile = open('eig.dat','r')
numpoint = 100
X = np.linspace(0, 1, numpoint)
Y = np.linspace(0, 1, numpoint)

X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

lines = bandfile.readlines()
testnumk = -1
for i in range(np.shape(X)[0]):
    for j in range(np.shape(Y)[0]):
        testnumk = testnumk +1
        tmpArr = re.split('\s+',lines[testnumk].strip())
        tmpx = int(tmpArr[0])
        tmpy = int(tmpArr[1])
        Z[tmpx,tmpy] = float(tmpArr[2])
        

ax.plot_surface(X, Y, Z.T, rstride=1, cstride=1, color=plt.cm.Accent(4), alpha=1.0,linewidth=0,antialiased=False)
ax.grid(False)
#plt.imshow(Z,cmap='winter_r')
#ax.plot(linex,liney,linez)
ax.view_init(90, 0)
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.axis('off')



plt.show()
bandfile.close()

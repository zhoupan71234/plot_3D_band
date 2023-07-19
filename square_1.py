#!/usr/bin/env /home/zhoupan/software/python2.7/epd_free-7.3-2-rh5-x86_64/bin/python2.7

import sys

from pythtb import * # import TB model class
import numpy as np
import matplotlib.pyplot as plt
# define lattice vectors
lat=[[1.0,0.0],[0.0,1.0]]
# define coordinates of orbitals
orb=[[0.0,0.0]]

t=1.0
# make two dimensional tight-binding checkerboard model
my_model=tb_model(2,2,lat, orb)

my_model.set_hop(t, 0, 0, [0, 1])
my_model.set_hop(t, 0, 0, [1, 0])
# lat= [[1.0,0.0,0.0],[0.0,1.0,0.0],[0.0,0.0,1.0]]

# latv = np.dot(lat[0],np.cross(lat[1],lat[2]))


# b1=2*np.pi*np.cross(lat[1],lat[2])/latv
# b2=2*np.pi*np.cross(lat[2],lat[0])/latv
# b3=2*np.pi*np.cross(lat[0],lat[1])/latv
# rlat = [b1,b2,b3]
# rev_rlat = np.linalg.inv(rlat)

# xx = [0.5,0.0,0.5]
# center_real = np.dot(xx,rlat)
# print center_real
#sys.exit()
#print rlat
#sys.exit()


ceterpoint = [0.5,0.5]
detakx = 0.5
detaky = 0.5
detakz = 0.0
start_pointx = ceterpoint[0]-detakx
end_pointx   = ceterpoint[0]+detakx
start_pointy = ceterpoint[1]-detaky
end_pointy   = ceterpoint[1]+detaky
# start_pointz = ceterpoint[2]-detakz
# end_pointz   = ceterpoint[2]+detakz
numpoint=100

X = np.linspace(start_pointx, end_pointx, numpoint)
Y = np.linspace(start_pointy, end_pointy, numpoint)
#Z = np.linspace(start_pointz, end_pointz, numpoint)

file = open('eig.dat','w')


#eig = np.zeros((numpoint,numpoint))
for kx in range(numpoint):
    for ky in range(numpoint):
        kpttmp = [X[kx],Y[ky]]
        eigtmp = my_model.solve_one(kpttmp)
        file.write(str(kx) + ' ' + str(ky) + ' ' + str(eigtmp[0])+'\n')
        #eig[kx][ky] = eigtmp
#print(X[0])
#print(X[-1])
        
file.close()


# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
#import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
onedrive = os.environ.get("OneDrive").replace('\\','/')
path = onedrive + '/Documents/mit_analytics/py/enviro/OceanFlow'

#import math 

mask = np.genfromtxt(path + '/mask.csv', delimiter=',').T
map_grid_shape = mask.shape

min_time=1
max_time=100
#Store the u,v flow components in a dictionary
dCarFlow = {}
for t in np.arange(min_time,max_time+1):
    # we transpose these files so: ui[X,Y] will return colX, rowY
    u = np.genfromtxt(path + '/' + str(t) + 'u.csv', delimiter=',').T
    v = np.genfromtxt(path + '/' + str(t) + 'v.csv', delimiter=',').T    
    dCarFlow[t] = (u,v)

land_x = []
land_y = []
coast_x = []
coast_y = []
for i in range(map_grid_shape[0]):
    for j in range(map_grid_shape[1]):
        if mask[i,j] == 0:
            land_x.append(i*3)
            land_y.append((map_grid_shape[1] - j)*3)
            nbr = 0
            for x in np.arange(-1,2):
                for y in np.arange(-1,2):
                   if i+x >= 0 and i+x <= map_grid_shape[0] and j+y >= 0 and j+y <= map_grid_shape[1] and (i != 0 or j != 0):
                       nbr += mask[i+x,j+y]
            if nbr > 0 and nbr < 8:
                coast_x.append(i*3)
                coast_y.append((map_grid_shape[1] - j)*3)

X, Y = np.meshgrid(np.arange(0, 3*map_grid_shape[0], 3), np.arange(0, 3*map_grid_shape[1], 3))

def plot_stream(t, X, Y, ax):
    U = np.empty(map_grid_shape)
    V = np.empty(map_grid_shape)
    for i in range(map_grid_shape[0]):
        for j in range(map_grid_shape[1]):
            U[i,j] = dCarFlow[t+1][0][i,j]
            V[i,j] = dCarFlow[t+1][1][i,j]
    return ax.streamplot(X, Y, U.T, V.T, density=[0.5, 1])            

path = onedrive + '/Documents/mit_analytics/py/enviro/imgs'

for T in np.arange(min_time,max_time+1):

    fig = plt.figure(figsize=(16,15))              
    plt.scatter(land_x, land_y, s=1, linewidths=0, c='khaki', alpha=0.1)
    plt.scatter(coast_x, coast_y, s=1, linewidths=0, c='navy', alpha=0.2)
    
    ax = plt.gca()
    ps = plot_stream(T-1,X,Y,ax)
    
    plt.text(0,1500,'t=' + str((T-1)*3))
    ax.set_aspect('equal', 'box')
    
    for loc, spine in ax.spines.items():
            spine.set_color('none')
    
    plt.savefig(path + '/stream_t' + str(T) + '.png')
    plt.close()

import cv2
import numpy as np
import glob

img_array = []
for filename in glob.glob(path + '/*.png'):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)

out = cv2.VideoWriter(onedrive + '/Documents/mit_analytics/py/enviro/project.avi',cv2.VideoWriter_fourcc(*'DIVX'), 6, size)
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()


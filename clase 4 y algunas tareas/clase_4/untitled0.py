# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 09:16:43 2023

@author: JavierMunho
"""

import numpy as  np
import matplotlib.pyplot as plt


def distancia_p(x_vect,y_vect,p):
    res = 0
    if (len(x_vect) == len(y_vect)):
        dist_coord = x_vect.copy() - y_vect.copy()
        dist_a_la_p = 0
        for i in dist_coord:
            dist_a_la_p = dist_a_la_p + i**p
        res = dist_a_la_p ** (1/p)
    return res

def punto_a_r_en_dist_p(y_1,p):
    return (1-y_1**p)**(1/p)


x = np.linspace(-1, 1,200)
y = np.linspace(-1, 1,200)


plt.plot()
plt.xlim(-2,2)
plt.ylim(-2,2)

bola = []
p = 3
for i in range(len(x)):
    for j in range(len(x)):
        punto = np.array([x[i],y[j]])
        r = distancia_p(np.array([0,0]), punto, p)
        if (r < 1.02) and (r > 0.98):
            bola.append(punto)
bola = np.array(bola).T
plt.plot(bola[0],bola[1],"bo")
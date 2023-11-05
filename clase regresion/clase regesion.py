# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 09:25:36 2023

@author: JavierMunho
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv(".\clase regresion\datos_roundup.csv", sep= " ")
x,y = np.array(data["RU"].array),np.array(data["ID"].array)
x_prom = x.mean()
y_prom = y.mean()


Num = 0
Den = 0
for i in range(len(x)):
    Num = Num + (x[i] - x_prom)*(y[i] - y_prom)
    Den =  Den + ((x[i] - x_prom) ** 2)

B_1 = Num / Den

B_0 = y_prom - B_1*x_prom

lineal= lambda x,a,b : a*x + b

plt.plot(x,y,".")
plt.plot(x,x*B_1 + B_0)

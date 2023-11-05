# -*- coding: utf-8 -*-
"""
Materia     : Laboratorio de datos - FCEyN - UBA
Clase       : Clase Regresion Lineal
Detalle     : Modelo KNN
Autores     : Manuela Cerdeiro y Pablo Turjanski
Modificacion: 2023-10-21
"""

# Importamos bibliotecas
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsRegressor
import matplotlib.pyplot as plt
import seaborn as sns

#%%
####################################################################
########  DEFINICION DE FUNCIONES AUXILIARES
####################################################################

# Dibuja una recta. Toma como parametros pendiente e intercept
def plotRectaRegresion(slope, intercept):
    """Plot a line from slope and intercept"""
    axes = plt.gca()
    x_vals = np.array(axes.get_xlim())
    y_vals = intercept + slope * x_vals
    plt.plot(x_vals, y_vals, color="red")

#%%
####################################################################
########  MAIN
####################################################################
# Cargamos el archivo 
carpeta = '~/Downloads/'
data_train = pd.read_csv(carpeta+"datos_roundup.txt", sep=" ", encoding='utf-8')
#%%

# ----------------------------------
# ----------------------------------
#       Modelo KNN
# ----------------------------------
# ----------------------------------
#  X = RU (variable predictora) [Dosis de Roundup]
#  Y = ID (variable a predecir) [Damage Index]
########################
## Generacion del modelo
########################
# Declaramos las variables

# Declaramos el tipo de modelo

# Entrenamos el modelo

#####################################
## Evaluacion del modelo contra TRAIN
#####################################
# Calculamos el R2. Recordar que 1 es en el caso de una prediccion perfecta


#####################################
## Prediccion
#####################################
# Cargamos el archivo (no posee valores para ID)
carpeta = '~/Downloads/'
data_a_predecir = pd.read_csv(carpeta+"datos_a_predecir.txt", sep=" ", encoding='utf-8')

# Realizamos la prediccion de ID utilizando el modelo y
# la asignamos a la columna ID


# Graficamos una dispersion de puntos de ID en funcion de la Dosis de RU
# Graficamos tanto los puntos de entrenamiento del modelo como los predichos


# Graficamos la recta que habiamos obtenido en el modelo RLS la clase pasada




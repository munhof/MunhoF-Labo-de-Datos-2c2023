# -*- coding: utf-8 -*-
"""
Materia     : Laboratorio de datos - FCEyN - UBA
Clase       : Clase Regresion Lineal
Detalle     : Modelo de Regresion Lineal Simple
Autores     : Maria Soledad Fernandez y Pablo Turjanski
Modificacion: 2023-10-13
"""

# Importamos bibliotecas
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import seaborn as sns
from inline_sql import sql, sql_val

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
carpeta = '.\clase regresion'
data_train = pd.read_csv(".\clase regresion\datos_libreta_15221.txt", sep=" ", encoding='utf-8')


# ----------------------------------
# ----------------------------------
#       Modelo Lineal Simple (rls)
# ----------------------------------
# ----------------------------------
#  X = RU (variable predictora) [Dosis de Roundup]
#  Y = ID (variable a predecir) [Damage Index]
########################
## Generacion del modelo
########################
# Declaramos las variables

X = data_train[["RU"]]
Y = data_train[["ID"]]

# Declaramos el tipo de modelo

rls = linear_model.LinearRegression()

# Entrenamos el modelo

rls.fit(X,Y)

# Observamos los valores obtenidos (pendiente e intercept)
print("Coeficientes")
print("------------")
print("intercept :",rls.intercept_[0])
print("pendiente :",rls.coef_[0][0])
print("R2 :", rls.score(X,Y))

###############################################
## Visualizacion del modelo vs valores de TRAIN
###############################################
# Graficamos una dispersion de puntos de ID en funcion de la Dosis de RU
ax = sns.scatterplot(data = data_train, x = "RU", y = "ID", s = 40, color = "black")
ax.set_xlabel("Dosis de RU (ug/huevo)")
ax.set_ylabel("Indice de Daño")
plotRectaRegresion(rls.coef_[0][0], rls.intercept_[0])

#####################################
## Prediccion
#####################################
# Cargamos el archivo (no posee valores para ID)
data_a_predecir = pd.read_csv(".\clase regresion\datos_a_predecir.txt", sep=" ", encoding='utf-8')

# Realizamos la prediccion de ID utilizando el modelo y
# la asignamos a la columna ID
data_a_predecir[["ID"]] = rls.predict(data_a_predecir[["RU"]])

# Graficamos una dispersion de puntos de ID en funcion de la Dosis de RU
# Graficamos tanto los puntos de entrenamiento del modelo como los predichos

ax = sns.scatterplot(data = data_train, x = "RU", y = "ID", 
                     s = 40, color = "black",
                     label = "Data train")
ax = sns.scatterplot(data = data_a_predecir, x = "RU", y = "ID", 
                     s = 60, color = "olive",  marker = "v",
                     label = "Data a predecir")

ax.set_xlabel("Dosis de RU (ug/huevo)")
ax.set_ylabel("Indice de Daño")
plotRectaRegresion(rls.coef_[0][0], rls.intercept_[0])


#####################################
## Evaluacion del modelo contra TRAIN
#####################################
#  R2

x,y = np.array(data_train["RU"].array),np.array(data_train["ID"].array)
x_prom = x.mean()
y_prom = y.mean()
y_prect = rls.coef_[0][0]*x + rls.intercept_[0]

total = 0
explicada = 0
for i in range(len(x)):
    total = total + (y[i] - y_prom) ** 2
    explicada =  explicada + ((y_prect[i] - y_prom) ** 2)
    
R2 = explicada/total

x,y = np.array(data_train["RU"].array),np.array(data_train["ID"].array)
x_prom = x.mean()
y_prom = y.mean()
y_prect = rls.coef_[0][0]*x + rls.intercept_[0]

total = 0
explicada = 0
for i in range(len(x)):
    total = total + (y[i] - y_prom) ** 2
    explicada =  explicada + ((y_prect[i] - y_prom) ** 2)
    
R2 = explicada/total





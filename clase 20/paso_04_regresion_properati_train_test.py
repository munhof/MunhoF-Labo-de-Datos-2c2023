# -*- coding: utf-8 -*-
"""
Materia     : Laboratorio de datos - FCEyN - UBA
Clase       : Clase Regresion Lineal
Detalle     : Modelos de Regresion Lineal
                - Cargamos los datos de test y train de properati
                - Proponemos distintos modelos y los evaluamos
Autores     : Manuela Cerdeiro y Pablo Turjanski
Modificacion: 2023-10-13
"""

# Importamos bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures

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
    plt.plot(x_vals, y_vals, '--', color="darkgreen")

#%%
####################################################################
########  MAIN
####################################################################

# Cargamos el archivo ya limpio
carpeta = ''
data_train = pd.read_csv(carpeta+'data_alq_caba_train.csv', index_col = 'id', encoding='utf-8')
data_test  = pd.read_csv(carpeta+'data_alq_caba_test.csv' , index_col = 'id', encoding='utf-8')


#%%
# ----------------------------------
# ----------------------------------
#       Modelo Lineal Simple 1
# ----------------------------------
# ----------------------------------
# Primer propuesta: Modelo Lineal Simple (rls) tomando a:
#  X1 = surface_total (variable predictora)
#  Y  = price         (variable a predecir)
########################
## Generacion del modelo
########################
# Declaramos las variables
X1 = data_train[["surface_total"]]
Y  = data_train[["price"]]  
# Declaramos el tipo de modelo
rls = linear_model.LinearRegression()
# Entrenamos el modelo
rls.fit(X1,Y)
# Observamos los valores obtenidos (pendiente e intercept)
print("Coefficients")
print("------------")
print("   intercept: ", rls.intercept_[0])
print("   pendiente: ", rls.coef_[0])


#####################################
## Evaluacion del modelo contra TRAIN
#####################################
#  R2
# Calculamos el R2. Recordar que 1 es en el caso de una prediccion perfecta
# ... Para calcular R2 usamos los residuos de predecir los datos 

print("R^2 (train): %.2f" %rls.score(X1,Y))
# Otra manera de calcular R2, es con la funcion score


# MSE (mean squared error, o en castellano error cuadratico medio)
y_pred = rls.predict(X1)
print("MSE (train): %.2f" % mean_squared_error(Y, y_pred))

#####################################
## Evaluacion del modelo contra TRAIN
#####################################
#  R2
# Calculamos el R2. Recordar que 1 es en el caso de una prediccion perfecta
# ... Para calcular R2 usamos los residuos de predecir los datos 
Y_pred1 = rls.predict(X1)
print("R^2 (train): %.2f" % r2_score(Y, Y_pred1))
# Otra manera de calcular R2, es con la funcion score
rls.score(X1, Y)

# MSE (mean squared error, o en castellano error cuadratico medio)
print("MSE (train): %.2f" % mean_squared_error(Y, Y_pred1))


####################################
## Evaluacion del modelo contra TEST
####################################
# Declaramos las variables a partir de los datos de test
X1_test = data_test[['surface_total']] # doble corchete es importante
Y_test  = data_test[['price']]

#  R2
# Calculamos el R2. Recordar que 1 es en el caso de una prediccion perfecta
# ... Para calcular R2 usamos los residuos de predecir los datos 
Y_pred1_test = rls.predict(X1_test)
print("R^2 (test ): %.2f" % r2_score(Y_test, Y_pred1_test))
# Otra manera de calcular R2, es con la funcion score
rls.score(X1_test, Y_test)

# MSE (mean squared error, o en castellano error cuadratico medio)
print("MSE (test ): %.2f" % mean_squared_error(Y_test, Y_pred1_test))



###############################################
## Visualizacion del modelo vs valores de TRAIN
###############################################
# Graficamos una dispersion de puntos de precio en funcion de la superficie total
ax = sns.scatterplot(data=data_train, x="surface_total", y="price", s = 5, alpha = 0.7)
ax.set_xlabel("Superficie total (m2)",fontsize=12)
ax.set_ylabel("Precio de Alquiler (AR$)",fontsize=12)
plotRectaRegresion(rls.coef_[0][0], rls.intercept_[0])
plt.title('Scatterplot de datos de entrenamiento\njunto con la recta el ajuste')

##############################################
## Visualizacion del modelo vs valores de TEST
##############################################
# Graficamos una dispersion de puntos de precio en funcion de la superficie total
ax = sns.scatterplot(data=data_test, x="surface_total", y="price", s = 5, alpha = 0.7)
ax.set_xlabel("Superficie total (m2)",fontsize=12)
ax.set_ylabel("Precio de Alquiler (AR$)",fontsize=12)
plotRectaRegresion(rls.coef_[0][0], rls.intercept_[0])
plt.title('Scatterplot de datos de entrenamiento\njunto con la recta el ajuste')

# Eliminamos las variables auxiliares que ya no utilizamos
del rls
del X1, Y, Y_pred1
del X1_test, Y_test, Y_pred1_test
del ax



#%%
# ----------------------------------
# ----------------------------------
#       Modelo Lineal Simple 2
# ----------------------------------
# ----------------------------------
# Segunda propuesta: Modelo Lineal Simple (rls) tomando a:
#  X1 = surface_covered (variable predictora)
#  Y  = price           (variable a predecir)
########################
## Generacion del modelo
########################
# Declaramos las variables
X1 = data_train[['surface_covered']] # doble corchete es importante
Y = data_train[['price']]

# Declaramos el tipo de modelo
rls = linear_model.LinearRegression()
# Entrenamos el modelo
rls.fit(X1, Y)

# Observamos los valores obtenidos (pendiente e intercept)
print("Coefficients")
print("------------")
print("   intercept: ", rls.intercept_[0])
print("   pendiente: ", rls.coef_[0][0])


######################################
## Evaluacion del modelo contrar TRAIN
######################################
#  R2
# Calculamos el R2. Recordar que 1 es en el caso de una prediccion perfecta
# ... Para calcular R2 usamos los residuos de predecir los datos de test
Y_pred1 = rls.predict(X1)
print("R^2 (train): %.2f" % r2_score(Y, Y_pred1))
# Otra manera de calcular R2, es con la funcion score
rls.score(X1, Y)

# MSE (mean squared error, o en castellano error cuadratico medio)
print("MSE (train): %.2f" % mean_squared_error(Y, Y_pred1))

####################################
## Evaluacion del modelo contra TEST
####################################
# Declaramos las variables a partir de los datos de test
X1_test = data_test[['surface_covered']] # doble corchete es importante
Y_test  = data_test[['price']]

#  R2
# Calculamos el R2. Recordar que 1 es en el caso de una prediccion perfecta
# ... Para calcular R2 usamos los residuos de predecir los datos 
Y_pred1_test = rls.predict(X1_test)
print("R^2 (test ): %.2f" % r2_score(Y_test, Y_pred1_test))
# Otra manera de calcular R2, es con la funcion score
rls.score(X1_test, Y_test)

# MSE (mean squared error, o en castellano error cuadratico medio)
print("MSE (test ): %.2f" % mean_squared_error(Y_test, Y_pred1_test))

###############################################
## Visualizacion del modelo vs valores de TRAIN
###############################################
# Graficamos una dispersion de puntos de precio en funcion de la superficie total
ax = sns.scatterplot(data=data_train, x="surface_covered", y="price", s = 5, alpha = 0.7)
ax.set_xlabel("Superficie cubierta (m2)",fontsize=12)
ax.set_ylabel("Precio de Alquiler (AR$)",fontsize=12)
plotRectaRegresion(rls.coef_[0][0], rls.intercept_[0])
plt.title('Scatterplot de datos de entrenamiento\njunto con la recta el ajuste')

##############################################
## Visualizacion del modelo vs valores de TEST
##############################################
# Graficamos una dispersion de puntos de precio en funcion de la superficie total
ax = sns.scatterplot(data=data_test, x="surface_covered", y="price", s = 5, alpha = 0.7)
ax.set_xlabel("Superficie cubierta (m2)",fontsize=12)
ax.set_ylabel("Precio de Alquiler (AR$)",fontsize=12)
plotRectaRegresion(rls.coef_[0][0], rls.intercept_[0])
plt.title('Scatterplot de datos de entrenamiento\njunto con la recta el ajuste')

# Eliminamos las variables auxiliares que ya no utilizamos
del rls
del X1, Y, Y_pred1
del X1_test, Y_test, Y_pred1_test
del ax


#%%
# ----------------------------------
# ----------------------------------
#       Modelo Multilineal 1
# ----------------------------------
# ----------------------------------
# Tercera propuesta: Modelo Multilineal tomando a:
#  X1 = surface_covered    (variable predictora 1)
#  X2 = surface_notCovered (variable predictora 2)
#  Y  = price           (variable a predecir)
########################
## Generacion del modelo
########################
# Declaramos las variables
data_train['surface_not_covered'] = data_train['surface_total']-data_train['surface_covered']
# Un chequeo que se podria realizar es si surface_not_covered>=0 en todos los casos
Xs = data_train[['surface_covered', 'surface_not_covered']] # doble corchete es importante
Y  = data_train[['price']]

# Declaramos el tipo de modelo
rls = linear_model.LinearRegression()
# Entrenamos el modelo
rls.fit(Xs, Y)

# Observamos los valores obtenidos (pendiente e intercept)
print("Coefficients")
print("------------")
print("   intercept: ", rls.intercept_[0])
print("   pendiente: ", rls.coef_[0])


#####################################
## Evaluacion del modelo contra TRAIN
#####################################
#  R2
# Calculamos el R2. Recordar que 1 es en el caso de una prediccion perfecta
# ... Para calcular R2 usamos los residuos de predecir los datos de test
Y_pred1 = rls.predict(Xs)
print("R^2 (train): %.2f" % r2_score(Y, Y_pred1))
# Otra manera de calcular R2, es con la funcion score
rls.score(Xs, Y)

# MSE (mean squared error, o en castellano error cuadratico medio)
print("MSE (train): %.2f" % mean_squared_error(Y, Y_pred1))

####################################
## Evaluacion del modelo contra TEST
####################################
# Declaramos las variables
data_test['surface_not_covered'] = data_test['surface_total']-data_test['surface_covered']
# Un chequeo que se podria realizar es si surface_not_covered>=0 en todos los casos
Xs_test = data_test[['surface_covered', 'surface_not_covered']] # doble corchete es importante
Y_test  = data_test[['price']]

#  R2
# Calculamos el R2. Recordar que 1 es en el caso de una prediccion perfecta
# ... Para calcular R2 usamos los residuos de predecir los datos 
Y_pred1_test = rls.predict(Xs_test)
print("R^2 (test ): %.2f" % r2_score(Y_test, Y_pred1_test))
# Otra manera de calcular R2, es con la funcion score
rls.score(Xs_test, Y_test)

# MSE (mean squared error, o en castellano error cuadratico medio)
print("MSE (test ): %.2f" % mean_squared_error(Y_test, Y_pred1_test))



#######################################################
## Visualizacion del modelo vs valores de entrenamiento
#######################################################
# Este tipo de modelos ya es mas dificil de visualizar

# Eliminamos las variables auxiliares que ya no utilizamos
del rls
del Xs, Y, Y_pred1
del Xs_test, Y_test, Y_pred1_test

#%% 
# ----------------------------------
# ----------------------------------
#       Modelo Multilineal 2
# ----------------------------------
# ----------------------------------
# Cuarta propuesta: Modelo Multilineal tomando a:
#  X1 = surface_covered    (variable predictora 1)
#  X2 = lat                (variable predictora 2)
#  X3 = lon                (variable predictora 2)
#  Y  = price           (variable a predecir)
########################
## Generacion del modelo
########################
# Antes de utilizar lat y lon veamos si tienen valores null
# Comenzamos con lat ...
print("Cantidad de valores null en columna lat en data_train: ",data_train['lat'].isna().sum())
# Generamos un nuevo dataframe de datos para este modelo tal que no 
# contenga na en lat
data_train_l = data_train[~data_train['lat'].isna()]
# Ahora verificamos en data_train_l si quedan registros con null en lon
print("Cantidad de valores null en columna lon en data_train_l: ",data_train_l['lon'].isna().sum())
# data_l ya no tiene null ni en lat ni en lon
# Declaramos las variables
Xs = data_train_l[['surface_covered', 'lat', 'lon']] # doble corchete es importante
Y  = data_train_l[['price']]

# Declaramos el tipo de modelo
rls = linear_model.LinearRegression()
# Entrenamos el modelo
rls.fit(Xs, Y)

# Observamos los valores obtenidos (pendiente e intercept)
print("Coefficients")
print("------------")
print("   intercept: ", rls.intercept_[0])
print("   pendiente: ", rls.coef_[0])


####################################
## Evaluacion del modelo contra TRAIN
#####################################  R2
# Calculamos el R2. Recordar que 1 es en el caso de una prediccion perfecta
# ... Para calcular R2 usamos los residuos de predecir los datos de test
Y_pred1 = rls.predict(Xs)
print("R^2 (train): %.2f" % r2_score(Y, Y_pred1))
# Otra manera de calcular R2, es con la funcion score
rls.score(Xs, Y)

# MSE (mean squared error, o en castellano error cuadratico medio)
print("MSE (train): %.2f" % mean_squared_error(Y, Y_pred1))

####################################
## Evaluacion del modelo contra TEST
####################################
# Declaramos las variables
# Antes de utilizar lat y lon veamos si tienen valores null
# Comenzamos con lat ...
print("Cantidad de valores null en columna lat en data_train: ",data_test['lat'].isna().sum())
# Generamos un nuevo dataframe de datos tal que no 
# contenga na en lat
data_test_l = data_test[~data_test['lat'].isna()]
# Ahora verificamos en data_test_l si quedan registros con null en lon
print("Cantidad de valores null en columna lon en data_train_l: ",data_test_l['lon'].isna().sum())
# data_l ya no tiene null ni en lat ni en lon
# Declaramos las variables
Xs_test = data_test_l[['surface_covered', 'lat', 'lon']] # doble corchete es importante
Y_test  = data_test_l[['price']]

#  R2
# Calculamos el R2. Recordar que 1 es en el caso de una prediccion perfecta
# ... Para calcular R2 usamos los residuos de predecir los datos 
Y_pred1_test = rls.predict(Xs_test)
print("R^2 (test ): %.2f" % r2_score(Y_test, Y_pred1_test))
# Otra manera de calcular R2, es con la funcion score
rls.score(Xs_test, Y_test)

# MSE (mean squared error, o en castellano error cuadratico medio)
print("MSE (test ): %.2f" % mean_squared_error(Y_test, Y_pred1_test))



#######################################################
## Visualizacion del modelo vs valores de entrenamiento
#######################################################
# Este tipo de modelos ya es mas dificil de visualizar


# Eliminamos las variables auxiliares que ya no utilizamos
del rls
del Xs, Y, Y_pred1
del Xs_test, Y_test, Y_pred1_test


#%% 
# ----------------------------------
# ----------------------------------
#       Modelo Polinomial 1
# ----------------------------------
# ----------------------------------
# Quinta propuesta: Modelo Polinomial tomando a:
#  X1    = surface_covered  (variable predictora)
#  Y     = price            (variable a predecir)
#  grado = 30
########################
## Generacion del modelo
########################
# Declaramos las variables
X1    = data_train[['surface_covered']] # doble corchete es importante
Y     = data_train[['price']]
grado = 30

# Generamos las variables polinomicas (Xp = [X^0,X^1,...,X^30])
pol = PolynomialFeatures(grado)
Xp  = pol.fit_transform(X1)
# Declaramos el tipo de modelo
rls = linear_model.LinearRegression()
# Entrenamos el modelo
rls.fit(Xp, Y)

# Observamos los valores obtenidos (pendiente e intercept)
print("Coefficients")
print("------------")
print("   intercept : ", rls.intercept_[0])
print("   pendientes: ", rls.coef_[0])

#####################################
## Evaluacion del modelo contra TRAIN
#####################################
#  R2
# Calculamos el R2. Recordar que 1 es en el caso de una prediccion perfecta
# ... Para calcular R2 usamos los residuos de predecir los datos de test
Y_pred1 = rls.predict(Xp)
print("R^2 (train): %.2f" % r2_score(Y, Y_pred1))
# Otra manera de calcular R2, es con la funcion score
rls.score(Xp, Y)

# MSE (mean squared error, o en castellano error cuadratico medio)
print("MSE (train): %.2f" % mean_squared_error(Y, Y_pred1))

####################################
## Evaluacion del modelo contra TEST
####################################
X1_test    = data_test[['surface_covered']] # doble corchete es importante
Y_test     = data_test[['price']]

# Generamos las variables polinomicas (Xp = [X^0,X^1,...,X^30])
Xp_test   = pol.fit_transform(X1_test)

#  R2
# Calculamos el R2. Recordar que 1 es en el caso de una prediccion perfecta
# ... Para calcular R2 usamos los residuos de predecir los datos 
Y_pred1_test = rls.predict(Xp_test)
print("R^2 (test ): %.2f" % r2_score(Y_test, Y_pred1_test))
# Otra manera de calcular R2, es con la funcion score
rls.score(Xp_test, Y_test)

# MSE (mean squared error, o en castellano error cuadratico medio)
print("MSE (test ): %.2f" % mean_squared_error(Y_test, Y_pred1_test))


# Eliminamos las variables auxiliares que ya no utilizamos
del rls
del X1, Y, Xp, Y_pred1
del X1_test, Y_test, Xp_test, Y_pred1_test
del grado, pol

































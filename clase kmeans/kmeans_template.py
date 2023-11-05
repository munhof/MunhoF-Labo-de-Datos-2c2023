# -*- coding: utf-8 -*-
"""
Materia     : Laboratorio de datos - FCEyN - UBA
Clase       : Clase Aprendizaje No Supervisado
Detalle     : Modelos KMeans
Autores     : Manuela Cerdeiro y Pablo Turjanski
Modificacion: 2023-10-31
"""

# Importamos bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans


#%%
####################################################################
########  MAIN
####################################################################
# Cargamos el archivo 
carpeta = './'
data_train = pd.read_csv(carpeta+'datos_clase_clustering.csv', index_col = 0, encoding='utf-8')

#%%
# Analizamos el precio de venta (U$S) por m2 de superficie cubierta. Para ello 
# generamos la variable ppm (precio por m2 de superficie cubierta)
data_train['ppm'] = data_train['price']/data_train['surface_covered']


#%%
# ------------------------------------------
# ------------------------------------------
#       Exploracion de Datos - Propuesta 1
# ------------------------------------------
# ------------------------------------------
# Queremos ver como es la relacion entre el precio de venta por m2 de 
# superficie cubierta (U$S) y la superficie cubierta (m2)


# Para ello visualizamos el precio de venta por m2 de superficie cubierta (U$S)
# en funcion de la superficie cubierta (m2)
ax = sns.scatterplot(data=data_train, x='surface_covered', y= 'ppm') 
ax.set_xlabel("Superficie cubierta (m2)")
ax.set_ylabel("Precio de venta por m2 de sup. cubierta (U$S)")

# Eliminamos las variables que ya no utilizamos
del ax

#%%
# ----------------------------------
# ----------------------------------
#       Modelo KMeans - Propuesta 1
# ----------------------------------
# ----------------------------------
#  X1 = surface_covered (variable predictora) [Superficie cubierta (m2)]
#  X2 = ppm             (variable predictora) [Precio por m2 de superficie cubierta (U$S)]
#  k  = Cantidad de grupos
########################
## Generacion del modelo
########################
# Declaramos las variables
Xs = data_train[["surface_covered","ppm"]]
k = 3
# Declaramos el tipo de modelo
kmeansps = KMeans(n_clusters = k, random_state = 0)

# Entrenamos el modelo
kmeansps.fit(Xs)

# Asignamos las etiquetas predichas a cada fila de nuestro dataset
data_train["cluster"] = kmeansps.labels_
centros = kmeansps.cluster_centers_

# Visualizamos los 3 clusters generados en funcion de su 
# superficie cubierta (m2) y el precio por m2 de la superficie cubierta (U$S)
ax = sns.scatterplot(data=data_train, x='surface_covered', y= 'ppm', 
                     hue = "cluster", palette = "viridis") 
sns.scatterplot(centros)
ax.set_xlabel("Superficie cubierta (m2)")
ax.set_ylabel("Precio de venta por m2 de sup. cubierta (U$S)")

# Eliminamos las variables que ya no utilizamos

del Xs,k,ax,kmeansps
plt.close()
#%%
# ------------------------------------------
# ------------------------------------------
#       Exploracion de Datos - Propuesta 2
# ------------------------------------------
# ------------------------------------------
# Queremos ver como es la relacion entre el precio TOTAL de venta (U$S) 
# y la superficie cubierta (m2)

# Para ello visualizamos el precio total de venta (U$S)
# en funcion de la superficie cubierta (m2)
ax = sns.scatterplot(data=data_train, x='surface_covered', y= 'price', palette = 'viridis') 
ax.set_xlabel("Superficie cubierta (m2)")
ax.set_ylabel("Precio total de venta (U$S)")

# Eliminamos las variables que ya no utilizamos
del ax


#%%
# ----------------------------------
# ----------------------------------
#       Modelo KMeans - Propuesta 2
# ----------------------------------
# ----------------------------------
#  X1 = surface_covered (variable predictora) [Superficie cubierta (m2)]
#  X2 = precio          (variable predictora) [Precio total de venta (U$S)]
#  k  = Cantidad de grupos
########################
## Generacion del modelo
########################
# Declaramos las variables

Xs = data_train[["surface_covered","price"]]
k = 3
# Declaramos el tipo de modelo
kmeansps = KMeans(n_clusters = k, random_state = 0)

# Entrenamos el modelo
kmeansps.fit(Xs)

# Asignamos las etiquetas predichas a cada fila de nuestro dataset
data_train["cluster"] = kmeansps.labels_
centros = kmeansps.cluster_centers_

# Visualizamos los 3 clusters generados en funcion de su 
# superficie cubierta (m2) y el precio por m2 de la superficie cubierta (U$S)
ax = sns.scatterplot(data=data_train, x='surface_covered', y= 'price', 
                     hue = "cluster", palette = "viridis") 
#sns.scatterplot(centros, label = "centroide")
ax.set_xlabel("Superficie cubierta (m2)")
ax.set_ylabel("Precio (U$d)")

# Eliminamos las variables que ya no utilizamos

del Xs,k,ax,kmeansps

#%%
# ------------------------------------------------------
# ------------------------------------------------------
#       Volvemos a la Exploracion de Datos - Propuesta 1
# ------------------------------------------------------
# ------------------------------------------------------
# Queremos ver como es la relacion entre el precio de venta por m2 de 
# superficie cubierta (U$S) y la superficie cubierta (m2). 


# Para ello visualizamos el precio de venta por m2 de superficie cubierta (U$S)
# en funcion de la superficie cubierta (m2)
ax = sns.scatterplot(data=data_train, x='surface_covered', y= 'ppm') 
ax.set_xlabel("Superficie cubierta (m2)")
ax.set_ylabel("Precio de venta por m2 de sup. cubierta (U$S)")

# Eliminamos las variables que ya no utilizamos
del ax

#%%
# ---------------------------------------------------------------
# ---------------------------------------------------------------
#       Modelo KMeans - Probamos rango de valores k - Propuesta 1
# ---------------------------------------------------------------
# ---------------------------------------------------------------
#  X1     = surface_covered (variable predictora) [Superficie cubierta (m2)]
#  X2     = ppm             (variable predictora) [Precio por m2 (U$S)]
#  k_vals = Rango de valores para k
########################
## Generacion del modelo
########################
# Declaramos las variables
k_vals = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
Xs = data_train[["surface_covered","ppm"]]
WCSS = []
# En wcss vamos a almacenar el Within-Cluster Sum of Square
# para cada uno de los k utilizados
fig1, axs = plt.subplots(nrows = 2, ncols = 7)

# Realizamos el modelado, visualiazcion y evaluacion para cada k
for k,ax in zip(k_vals,axs.flat):
    print('k: ', k)
    ### Modelamos 
    # Declaramos el tipo de modelo
    kmeansps = KMeans(n_clusters = k, random_state = 0)
    # Entrenamos el modelo
    kmeansps.fit(Xs)
    # Asignamos las etiquetas predichas a cada fila de nuestro dataset
    data_train["cluster"] = kmeansps.labels_

    ### Visualizamos
    # Visualizamos los k clusters generados en funcion de su 
    # superficie cubierta (m2) y el precio por m2 de la superficie cubierta (U$S)
    sns.scatterplot(data=data_train, x='surface_covered', y= 'ppm', 
                     hue = "cluster", palette = "viridis", ax = ax) 
    #sns.scatterplot(centros, label = "centroide")
    ax.set_xlabel("Superficie cubierta (m2)")
    ax.set_ylabel("Precio (U$d)")
    
    
    ### Evaluamos
    # Almacenamos el Within-Cluster Sum of Square del modelo para el k utilizado
    WCSS.append(kmeansps.inertia_)

plt.show()
# Visualizamos el wcss en funcion de la cantidad de grupos (k) para el modelo 
# y los datos utilizados (superficie cubierta y ppm)
fig2, axs = plt.subplots(nrows = 1, ncols = 1)
axs.plot(k_vals,WCSS,"--",label = "WCSS", )
plt.legend()
axs.set_xlabel("cantidad de clusters")
axs.set_ylabel("WCSS")
plt.grid()
plt.show()
# Eliminamos las variables que ya no utilizamos


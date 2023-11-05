#!/usr/bin/env python
# coding: utf-8

# # Evaluación de Modelos
# 
# **Objetivo:** dada los datos de una canción (una fila en nuestro dataset) poder predecir si esta en Folklore o Evermore o es de otro álbum.
# 
# **Datos:** dataset con distintas variables de las canciones de Taylor Swift.

# In[1]:


import pandas as pd 
import numpy as np
import seaborn as sns
import utils
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score

# #### Cargamos el dataset -- la función load_dataset limpia un poco los datos

# In[2]:


df_taylor = utils.load_dataset_taylor(".")
df_taylor.head()


# ### Separemos los labels y eliminamos el nombre de la canción

# In[ ]:


X = df_taylor.drop(columns = ['track_name', 'is_folklore_or_evermore'])
y = df_taylor['is_folklore_or_evermore']


# In[4]:
sns.pairplot(df_taylor.drop(columns=["track_name","mode","time_signature"]), hue="is_folklore_or_evermore")
#variables que separan
variable1 = df_taylor.drop(columns=["track_name","mode","time_signature"]).columns.array[7]
variable2 = df_taylor.drop(columns=["track_name","mode","time_signature"]).columns.array[4]

df_filtrado = df_taylor[["loudness","acousticness","instrumentalness","is_folklore_or_evermore"]]
sns.pairplot(df_filtrado, hue="is_folklore_or_evermore")

sns.scatterplot(data=df_filtrado,x= "loudness", y = "acousticness", hue="is_folklore_or_evermore")
#separo datos
X_train, X_test, y_train, y_test = train_test_split(X[["loudness","acousticness","instrumentalness"]], y
                                                    , test_size=0.1, stratify = y)
# Complete aqui con su clasificador de preferencia!
nbrs = KNeighborsClassifier(n_neighbors=2)
nbrs.fit(X_train,y_train)
nbrs.score(X_test,y_test)
vector = cross_val_score(nbrs, X[["loudness","acousticness","instrumentalness"]], y, cv=5)
vector.mean()
vector.std()

X_train, X_test, y_train, y_test = train_test_split(X, y
                                                    , test_size=0.1, stratify = y)
# Complete aqui con su clasificador de preferencia!
nbrs = KNeighborsClassifier(n_neighbors=5)
nbrs.fit(X_train,y_train)
nbrs.score(X_test,y_test)
cross_val_score(nbrs, X, y, cv=5)
vector = cross_val_score(nbrs,X, y, cv=5)
vector.mean()
vector.std()

#%% ahora con kfold 

kf = KFold(n_splits=5,shuffle = True)
kf.get_n_splits(X)

kf.split(X[["loudness","acousticness"]])
    




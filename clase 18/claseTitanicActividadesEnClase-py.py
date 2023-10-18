#!/usr/bin/env python
# coding: utf-8

# ## Podemos predecir quienes sobrevivieron en el Titanic? 
# 
# Tenemos un dataset muy famoso con datos de los pasajeros del titanic. El mismo está disponible en: 
# 
# https://www.kaggle.com/c/titanic/data 

# In[1]:


import utilsTitanic as utils
from IPython.display import display
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# ### Cargamos los datos

# In[2]:


df_titanic, X, y = utils.cargar_datos('titanic_training.csv') # X tiene todas las columnas del dataframe menos la que queremos predecir,
                                        # Y tiene la columna que indica si sobrevivieron
df_titanic.head()


# ### Exploren estos datos!! Ideas: histogramas, pairplots, etc 

# In[3]:


##Exploren 


# ## Competencia: Armen sus Reglas !!

# In[3]:


def clasificador_naive_instance(x):
    ## Completen con sus reglas por ej
    if x.Pclass == 1 :
        return True
    else:
        return False


# In[4]:


def clasificador_naive(X):
    y_predict = []
    for x in X.itertuples(index=False): 
        y_predict.append(clasificador_naive_instance(x))
    return y_predict


# In[5]:


def score(y, y_pred):
    print("Le pego a " + str(np.sum(y==y_pred)) + " de " + str(len(y)))


# #### Usemos nuestro clasificador sobre los datos 

# In[6]:


y_predict = clasificador_naive(X)
score(y_predict, y)


# In[9]:


X_comp = utils.cargar_datos_competencia("titanic_competencia.csv")
y_pred_comp = clasificador_naive(X_comp)
y_pred_comp


# ## Ahora armemos un clasificador usando árboles de decisión

# In[7]:


# Algo de procesamiento de los datos
X = utils.encode_sex_column(X)


# ## Decision Tree
# Para saber más: <https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html>

# In[9]:


# planta tu árbol aquí


# #### Generamos el gráfico de nuestro árbol
# Para saber más <https://scikit-learn.org/stable/modules/generated/sklearn.tree.export_graphviz.html#sklearn.tree.export_graphviz>

# In[10]:


# plot arbol


# ### ¿Cuál es el mejor corte? 

# In[8]:


utils.plot_hist_sex_survived(df_titanic)


# In[9]:


utils.plot_hist_age_survived(df_titanic)


# ## ¿Todos los árboles son iguales?
# 
# veamos dos ejemplos

# In[13]:


## Armar un árbol de altura 2


# In[14]:


## Armar un arbol con altura indefinida


# ## Veamos la performance de estos árboles sobre un conjunto de test

# In[10]:


#Cargamos los datos de tests
X_test, y_test = utils.cargar_datos_test('test_titanic.csv')


# In[ ]:


# Veamos el score del arbol de altura 2 sobre los datos de entrenamiento y los datos de tests


# In[ ]:


# Veamos el score del arbol de altura inf sobre los datos de entrenamiento y los datos de tests


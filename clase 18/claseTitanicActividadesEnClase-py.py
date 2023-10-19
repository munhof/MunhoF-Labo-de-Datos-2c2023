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
data_surv = df_titanic[df_titanic["Survived"] == 1]
data_nosurv = df_titanic[df_titanic["Survived"] == 0]
df_titanic.hist()


data_surv.describe()
data_surv[data_surv["Sex"] == "male"]["Sex"].value_counts()
data_nosurv[data_nosurv["Sex"] == "male"]["Sex"].value_counts()
data_surv[data_surv["Sex"] == "female"]["Sex"].value_counts()
data_nosurv[data_nosurv["Sex"] == "female"]["Sex"].value_counts()

data_male = df_titanic[df_titanic["Sex"] == "male"]
data_male.hist()
plt.scatter(x = data_male["Age"], y = data_male["Survived"])
plt.plot()
data_male[data_male["Survived"] == 1]["Age"].hist()
plt.show()
plt.plot()
data_male[data_male["Survived"] == 0]["Age"].hist()
plt.show()

data_age = data_male[(data_male["Age"] >= 20)]
data_age = data_age[data_age["Age"] <= 70]
data_age[data_age["Survived"] == 1].hist()
data_age[data_age["Survived"] == 0].hist(color = "red")

data_pclass = data_age[data_age["Pclass"] != 1]
data_pclass[data_pclass["Survived"] == 1].hist()
data_pclass[data_pclass["Survived"] == 0].hist(color = "red")

# ## Competencia: Armen sus Reglas !!

# In[3]:


def clasificador_naive_instance(x):
    ## Completen con sus reglas por ej
    regla_sexo = lambda x : x == "female"
    regla_edad = lambda x : x < 19 or x > 70
    regla_clase = lambda x : x == 1
    if regla_clase(x.Pclass):
        return True
    elif regla_edad(x.Age):
        return True
    elif regla_sexo(x.Sex):
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
from sklearn.tree import DecisionTreeClassifier,plot_tree,export_graphviz
arbol = DecisionTreeClassifier(criterion="entropy",max_depth= 3)
arbol.fit(X, y) #Entrenamiento
prediction = arbol.predict(X) #Generamos las predicciones
plot_tree(arbol)

# #### Generamos el gráfico de nuestro árbol
# Para saber más <https://scikit-learn.org/stable/modules/generated/sklearn.tree.export_graphviz.html#sklearn.tree.export_graphviz>

# In[10]:


# plot arbol
import graphviz
dot_data = export_graphviz(arbol, out_file=None, feature_names= X.columns, 
                           class_names= ["Not Survived", "Survived"],
                           filled=True, rounded=True, special_characters=True)

graph = graphviz.Source(dot_data) #Armamos el grafo
graph.render("titanic", format= "png") #Guardar la imágen


# ### ¿Cuál es el mejor corte? 

#%%
import graphviz # doctest: +NO_EXE
dot = graphviz.Digraph(comment='The Round Table')
dot  #doctest: +ELLIPSIS
dot.node('A', 'King Arthur')  # doctest: +NO_EXE
dot.node('B', 'Sir Bedevere the Wise')
dot.node('L', 'Sir Lancelot the Brave')

dot.edges(['AB', 'AL'])
dot.edge('B', 'L', constraint='false')


print(dot.source)  # doctest: +NORMALIZE_WHITESPACE +NO_EXE

doctest_mark_exe()

dot.render('doctest-output/round-table.gv').replace('\\', '/') 
'doctest-output/round-table.gv.pdf'

doctest_mark_exe()

dot.render('doctest-output/round-table.gv', view=True)  # doctest: +SKIP
'doctest-output/round-table.gv.pdf'

# In[8]:


utils.plot_hist_sex_survived(df_titanic)


# In[9]:


utils.plot_hist_age_survived(df_titanic)


# ## ¿Todos los árboles son iguales?
# 
# veamos dos ejemplos

# In[13]:


## Armar un árbol de altura 2
from sklearn.tree import DecisionTreeClassifier,plot_tree,export_graphviz
arbol2 = DecisionTreeClassifier(criterion="entropy",max_depth= 2)
arbol2.fit(X, y) #Entrenamiento
prediction = arbol2.predict(X) #Generamos las predicciones
plot_tree(arbol2)



# In[14]:


## Armar un arbol con altura indefinida

from sklearn.tree import DecisionTreeClassifier,plot_tree,export_graphviz
arbol = DecisionTreeClassifier(criterion="entropy")
arbol.fit(X, y) #Entrenamiento
prediction = arbol.predict(X) #Generamos las predicciones
plot_tree(arbol)

# ## Veamos la performance de estos árboles sobre un conjunto de test

#%%
from sklearn.tree import DecisionTreeClassifier,plot_tree,export_graphviz
arbol3 = DecisionTreeClassifier(criterion="entropy")
arbol3.fit(X, y) #Entrenamiento
prediction = arbol3.predict(X) #Generamos las predicciones
plot_tree(arbol3)

# In[10]:


#Cargamos los datos de tests
X_test, y_test = utils.cargar_datos_test('test_titanic.csv')


# In[ ]:


# Veamos el score del arbol de altura 2 sobre los datos de entrenamiento y los datos de tests
score(arbol2.predict(X),y)
score(arbol2.predict(X_test),y_test)

# In[ ]:


# Veamos el score del arbol de altura inf sobre los datos de entrenamiento y los datos de tests
score(arbol.predict(X),y)
score(arbol.predict(X_test),y_test)

#%%
score(arbol3.predict(X),y)
score(arbol3.predict(X_test),y_test)

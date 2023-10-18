#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 10:22:30 2023

Labo de Datos 2023, 1C

@author: Mariano
"""

import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

df = pd.read_csv('iris.csv')

df.columns

df.head(5)

#aca vemos un set de datos donde hay tres especies de plantas del mismo
#genero, con datos numericos de partes de las flores, y a que especie
#pertenecen...

#seran importantes, o mas importantes unos que otros? o
#alguna relacion entre ellos? para el fin de clasificar las especies?

#bueno, primero vale la pena ver de que van esos datos?
#medidas caracteristicas de cada especie? datos de la distribucion de
#dicha variable? bueno! vamos viendo!

#por ejemplo, cual sera la media del largo del petalo de iris Setosa?

df['petal.width'].plot.kde()

setosa = df[(df['variety']=='Setosa')]

setosa['petal.length'].mean()

#y la mediana??

setosa['petal.length'].median()

#y el percentil 50?  que les parece??

setosa['petal.length'].quantile(0.5)

setosa['petal.length'].quantile([0.25 , 0.5 , 0.75])
#parece que va creciendo la var, veamos otros cuantiles

setosa['petal.length'].quantile(
    [0.25 , 0.35 , 0.5 , 0.75, 0.8, 0.85 , 0.9 , 0.95 , 0.99])

#otra forma de verlo era con...

df.describe()#sirve esto a mi objetivo??

#mejor probar...

df[df['variety'] == 'Setosa'].describe()

#sera que tiene distribucion normal?, 'verifiquemoslo' con un graf
# de densidad...

setosa['petal.length'].plot(kind = 'kde').set(title='Distribucion longitud petalo de iris setosa',xlabel='Longitud Petalo')

plt.show()

plt.close()
#pareciera que si...

#ahora bien... podriamos agregar algunos de estos valores obtenidos
#de las medidas de resumen en el grafico de densidad por kernel?

#a ver si nos dan alguna pista, o intucion estadistica??  miremoslo!!



##para agregar una linea vertical en algun valor arbitrario
#usar plt.axvline
df.plot(kind = 'kde')

#####################################3
setosa['petal.length'].plot(kind = 'kde')

plt.axvline(setosa['petal.length'].mean(), color = 'orange')#la media
#naranja

plt.axvline(setosa['petal.length'].median() , color = 'red')#mediana
#roja

plt.axvline(setosa['petal.length'].quantile(0.5) , color = 'blue' , linestyle = '--')
#cuantil 50, en azul
plt.axvline(setosa['petal.length'].quantile(0.25) , color = 'green')
#cuartil 25 en verde 
plt.axvline(setosa['petal.length'].quantile(0.75) , color = 'violet')
#cuartil 75 en violeta
plt.axvline(setosa['petal.length'].mean()+setosa['petal.length'].std(), color='black' , linestyle='-.')

plt.axvline(setosa['petal.length'].mean()-setosa['petal.length'].std(), color='black' , linestyle='-.')

plt.show()

plt.close()
#--------------------------------------------------------------------
setosa['petal.width'].plot(kind = 'kde')

plt.axvline(setosa['petal.width'].mean(), color = 'orange')#la media
#naranja

plt.axvline(setosa['petal.width'].median() , color = 'red')#mediana
#roja

plt.axvline(setosa['petal.width'].quantile(0.5) , color = 'blue' , linestyle = '--')
#cuantil 50, en azul
plt.axvline(setosa['petal.width'].quantile(0.25) , color = 'green')
#cuartil 25 en verde 
plt.axvline(setosa['petal.width'].quantile(0.75) , color = 'violet')
#cuartil 75 en violeta
plt.axvline(setosa['petal.width'].mean()+setosa['petal.width'].std(), color='black' , linestyle='-.')

plt.axvline(setosa['petal.width'].mean()-setosa['petal.width'].std(), color='black' , linestyle='-.')

plt.show()

plt.close()
#-------------------------------------------------------------------

setosa['sepal.length'].plot(kind = 'kde')

plt.axvline(setosa['sepal.length'].mean(), color = 'orange')#la media
#naranja

plt.axvline(setosa['sepal.length'].median() , color = 'red')#mediana
#roja

plt.axvline(setosa['sepal.length'].quantile(0.5) , color = 'blue' , linestyle = '--')
#cuantil 50, en azul
plt.axvline(setosa['sepal.length'].quantile(0.25) , color = 'green')
#cuartil 25 en verde 
plt.axvline(setosa['sepal.length'].quantile(0.75) , color = 'violet')
#cuartil 75 en violeta
plt.axvline(setosa['sepal.length'].mean()+setosa['sepal.length'].std(), color='black' , linestyle='-.')

plt.axvline(setosa['sepal.length'].mean()-setosa['sepal.length'].std(), color='black' , linestyle='-.')

plt.show()

plt.close()
#--------------------------------------------------------------------
setosa['sepal.width'].plot(kind = 'kde')

plt.axvline(setosa['sepal.width'].mean(), color = 'orange')#la media
#naranja

plt.axvline(setosa['sepal.width'].median() , color = 'red')#mediana
#roja

plt.axvline(setosa['sepal.width'].quantile(0.5) , color = 'blue' , linestyle = '--')
#cuantil 50, en azul
plt.axvline(setosa['sepal.width'].quantile(0.25) , color = 'green')
#cuartil 25 en verde 
plt.axvline(setosa['sepal.width'].quantile(0.75) , color = 'violet')
#cuartil 75 en violeta
plt.axvline(setosa['sepal.width'].mean()+setosa['sepal.width'].std(), color='black' , linestyle='-.')

plt.axvline(setosa['sepal.width'].mean()-setosa['sepal.width'].std(), color='black' , linestyle='-.')

plt.show()

plt.close()
#---------------------------------------------------------------------
setosa.hist( )

#--------------------------------------------------------------------

#veamos que pinta tienen esas variables...

sns.boxplot(data = df).set(title='Boxplot iris')

plt.show()

plt.close()

#podriamos querer valernos de nuestro ingenio, y de los boxplots,
#para ir viendo si la dispercion se algunos datos se debe a alguna
#especie en particular...

sns.boxplot(data = df[df['variety'] == 'Setosa']).set(title='Boxplot iris Setosa')

plt.show()

plt.close()

sns.boxplot(data = df[df['variety'] == 'Versicolor']).set(title='Boxplot iris Versicolor')

plt.show()

plt.close()

sns.boxplot(data = df[df['variety'] == 'Virginica']).set(title='Boxplot iris Virginica')

plt.show()

plt.close()


#otra cosa que podriamos preguntarnos es la relacion entre el
#largo y ancho del petalo... pero coloreado por especie

df.plot.box()


sns.scatterplot(data = df , x = 'petal.width' , y = 'petal.length' , hue = 'variety').set(title='Relacion ancho_largo petalo')

plt.show()

plt.close()
#pasara algo parecido con los sepalos???

sns.scatterplot(data = df , x = 'sepal.width' , y = 'sepal.length' , hue = 'variety').set(title='Relacion ancho_largo sepalo')

plt.show()

plt.close()

#probemos una regresion de todas las especies juntas, a ver..

sns.lmplot(data = df , x = 'petal.width' , y = 'petal.length').set(title='Regrecion ancho_largo petalo')

plt.show()

plt.close()

sns.lmplot(data = df , x = 'petal.width' , y = 'petal.length' , hue = 'variety').set(title='Regrecion ancho_largo petalo')

plt.show()

plt.close()


#antes podriamos ver un  pairplot

sns.pairplot(data = df , hue = 'variety')#cual es la trampa en este pairplot?

plt.show()

plt.close()


#aja!!!!  trampa!!!

#estamos viendo todas las var juntas, con todas las sp juntas...

#eso es un problema no??

#veamos alguno por sp mejor, no???

sns.pairplot(data = df[df['variety'] == 'Setosa'])#cual es la trampa en este pairplot?

plt.show()

plt.close()

#ahora parece tener m'as sentido, no??

#y si combinaramos variables? tal vez generando variables nuevas
#a partir de relaciones netre otras veamos algo mas util para separar..

df['length_ratio'] = df['petal.length']/df['sepal.length']

df['width_ratio'] = df['petal.width']/df['sepal.width']

df['length_sup'] = df['petal.length']*df['sepal.length']

df['width_sup'] = df['petal.width']*df['sepal.width']

#probemos si usando estas relaciones mejora en algo...

sns.scatterplot(data = df , x = 'width_ratio' , y = 'length_ratio' , hue = 'variety').set(title='Regrecion RatioAncho_RatioLargo petalo')

plt.show()

plt.close()


sns.scatterplot(data = df , x = 'width_sup' , y = 'length_sup' , hue = 'variety').set(title='Regrecion supAncho_supLargo petalo')

plt.show()

plt.close()


#violin plot para el dataset con las otras dos variables agregadas

sns.violinplot(data = df)

plt.show()

plt.close()

#aparentemente los ratios, le quitaron variablidad??


###setosa
sns.violinplot(data = df[df['variety']=='Setosa'])

plt.show()

plt.close()

#virginica
sns.violinplot(data = df[df['variety']=='Virginica'])

plt.show()

plt.close()

#versicolor
sns.violinplot(data = df[df['variety']=='Versicolor'])

plt.show()

plt.close()

sns.pairplot(data = df , hue = 'variety')#cual es la trampa en este pairplot?

plt.show()

plt.close()

#se podria recapitular con el PCA, para ver si este metodo
#logra diferenciar las especies de todos modos...
#tal vez, incluyendo, unas u otras variables cambie??
#seria, solo las originales, y si inlcuyo los ratios?

#para los pca, armemos sin, y con ratios

#from sklearn.decomposition import PCA

#X_iris = df.loc[: , ['sepal.length', 'sepal.width', 'petal.length', 'petal.width']]

#pca_iris = PCA(n_components = 2)

#matriz_iris = pca_iris.fit_transform(X_iris.T)

#pd.DataFrame(matriz_iris).plot.scatter(x = 0 , y = 1).set(title = 'PCA variables iris' , xlabel = 'Componentes principal 1' , ylabel = 'Componente principal 2')

#plt.show()

#plt.close()

#####CON TODOS LOS FEATURES AGREGADOS

#X_todos = df.loc[: , ['sepal.length', 'sepal.width', 'petal.length', 'petal.width' , 'length_ratio', 'width_ratio']]

#pca_todos = PCA(n_components = 2)

#matriz_todos = pca_todos.fit_transform(X_todos.T)

#pd.DataFrame(matriz_todos).plot.scatter(x = 0 , y = 1).set(title ='PCA +ratios' , xlabel = 'Componentes principal 1' , ylabel = 'Componente principal 2')

#plt.show()

#plt.close()

#donde esta la trampita???

#si colapsaban con los ratios, por que no diferencia bien??

#donde esta el perro??

#####CON TODOS LOS FEATURES AGREGADOS

#X_ratios = df.loc[: , ['length_ratio', 'width_ratio']]

#pca_ratios = PCA(n_components = 2)

#matriz_ratios = pca_ratios.fit_transform(X_ratios.T)

#pd.DataFrame(matriz_ratios).plot.scatter(x = 0 , y = 1).set(title ='PCA ratios' , xlabel = 'Componentes principal 1' , ylabel = 'Componente principal 2')

#plt.show()

#plt.close()
#se ve que colaps'o demasiado, perdimos mucha variabilidad...
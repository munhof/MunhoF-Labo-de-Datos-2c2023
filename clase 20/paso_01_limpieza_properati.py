# -*- coding: utf-8 -*-
"""
Materia     : Laboratorio de datos - FCEyN - UBA
Clase       : Clase Regresion Lineal
Detalle     : Limpieza y Exploracion de Datos
                - Cargamos datos de properati
                - Seleccionamos campos y registros 
                  (correspondientes a alquiler, AR$, CABA, barrios con mas datos)
                - Guardamos el dataframe ya filtrado
Autores     : Manuela Cerdeiro y Pablo Turjanski
Modificacion: 2023-10-13
"""

# Importamos bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from inline_sql import sql, sql_val

#%%
# Cargamos el archivo original
data_prop_orig = pd.read_csv('ar_properties.csv', index_col = 'id')

#%%
# Exploramos contenido

# Nombres de columnas
data_prop_orig.columns

#
#[ 'ad_type', 'start_date', 'end_date', 'created_on', 'lat', 'lon',
#       'l1', 'l2', 'l3', 'l4', 'l5', 'l6', 'rooms', 'bedrooms', 'bathrooms',
#       'surface_total', 'surface_covered', 'price', 'currency', 'price_period',
#       'title', 'property_type', 'operation_type']

# Medidas resumen de cada columna
data_prop_orig.describe()

# Contenido de las primeras filas
data_prop_orig.head()

# Nos fijamos en cada columnas que cantidad de valores distintos de null hay
data_prop_orig.info() # acá veo MUCHOS nan


# Explorando el dataframe nos parece que la columna 'ad_type' tiene
# siempre el mismo valor para todas sus filas. Lo verificamos.
data_prop_orig['ad_type'].value_counts() 
# Confirmado. Todas sus filas poseen la cadena 'Propiedad'


#%%
# Seleccion de columnas
# Nos vamos a quedar solo con algunas columnas
#   - 'start_date'
#   - 'lat'
#   - 'lon'
#   - 'l1'
#   - 'l2'
#   - 'l3'
#   - 'surface_total'
#   - 'surface_covered'
#   - 'price'
#   - 'currency'
#   - 'title'
#   - 'property_type'
#   - 'operation_type'


cols_sel = ['start_date', 'lat', 'lon',
       'l1', 'l2', 'l3', 'surface_total', 'surface_covered', 'price', 'currency', 'title', 'property_type', 'operation_type']
data_prop = data_prop_orig[cols_sel]

# Medidas resumen de cada columna
data_prop.describe()

# Contenido de las primeras filas
data_prop.head()

# Eliminamos las variables auxiliares que ya no utilizamos
del cols_sel
#%%
# Exploramos que valores posee l1 (localizacion nivel 1)
data_prop['l1'].value_counts()
# Argentina         374977
# Uruguay            13575
# Estados Unidos       305
# Brasil                34

# Nos quedamos solo con las filas correspondientes a Argentina
data_prop_ar = data_prop[ data_prop['l1'] == 'Argentina']

# Eliminamos las variables auxiliares que ya no utilizamos
del data_prop

#%%
# Exploramos que valores posee l2 (localizacion nivel 2)
data_prop_ar['l2'].value_counts()
# Capital Federal                 124327
# Bs.As. G.B.A. Zona Norte         72088
# Santa Fe                         36199
# Buenos Aires Costa Atlántica     30649
# ...

# Nos quedamos solo con las filas correspondientes a Capital Federal
data_prop_caba = data_prop_ar[data_prop_ar['l2'] == 'Capital Federal']

# Eliminamos las variables auxiliares que ya no utilizamos
del data_prop_ar
#%%
# Exploramos que valores posee l3 (localizacion nivel 3)
data_prop_caba['l3'].value_counts()
# Palermo                  18907
# Belgrano                  9626
# Recoleta                  8263
# Villa Crespo              7485
# Almagro                   7296
# Caballito                 6956
# ...

# En principio dejamos todos los barrios

#%%
# Exploramos que valores posee en las columnas:
# - 'currency'
# - 'operation_type'

data_prop_caba['currency'].value_counts()
# USD    81601
# ARS    36646

data_prop_caba['operation_type'].value_counts()
# Venta                80871
# Alquiler             32248
# Alquiler temporal    11208

# Nos quedamos solo con las filas correspondientes a 'ARS' AND 'Alquiler'
filtro_pesos =data_prop_caba['currency'] == 'ARS'
filtro_alq = data_prop_caba['operation_type'] == 'Alquiler'
data_alq_caba = data_prop_caba[filtro_pesos & filtro_alq]

# Eliminamos las variables auxiliares que ya no utilizamos
del data_prop_caba
del filtro_pesos 
del filtro_alq

#%%
# Exploramos que valores posee en 'property_type'
data_alq_caba['property_type'].value_counts()
# Departamento       17752
# Local comercial     4022
# Oficina             2929
# PH                  1138
# Casa                 483
# Otro                 429
# Depósito             331
# Cochera              252
# Lote                  80

# En principio dejamos todos los tipos de propiedades


#%%
# Nombres de columnas
data_alq_caba.columns
# ['start_date', 'lat', 'lon', 'l1', 'l2', 'l3', 'surface_total',
#  'surface_covered', 'price', 'currency', 'title', 'property_type',
#  'operation_type']

# Nos vamos a quedar con menos columnas
cols_subsel = ['start_date', 'lat', 'lon', 'l3', 'surface_total', 'surface_covered', 'price', 'title', 'property_type', 'operation_type']
data_alq_caba = data_alq_caba[cols_subsel]

# Eliminamos las variables auxiliares que ya no utilizamos
del cols_subsel

#%%
# Medidas resumen de cada columna
data_alq_caba.describe()

# Nos fijamos en cada columnas que cantidad de valores distintos de null hay
data_alq_caba.info()
# surface_total = 25.033
# surface_covered = 24.787
# total 27.416  
#%%    
# Descartamos a aquellos registros que poseen nulls en 'surface_total' y 'surface_covered'
data_alq_caba = data_alq_caba.dropna(subset=['surface_total', 'surface_covered'])

# Nos fijamos en cada columnas que cantidad de valores distintos de null hay
data_alq_caba.info()
#surface_total = 23.686
#surface_covered = 23.686
#total 23.686  


#%%
# Graficamos boxplot en base a los precios de alquiler
colName = 'price'
plt.boxplot(data_alq_caba[colName])
plt.xticks([1], [colName])
plt.ylabel('AR$')

# Medidas resumen de la columna
data_alq_caba[colName].describe()

# Construimos un filtro (aun no lo aplicamos)
price_filter_mayor = data_alq_caba[colName].quantile(0.90)
price_filter_menor = data_alq_caba[colName].quantile(0.05)

price_filter = (    (data_alq_caba[colName] <= price_filter_mayor) 
                  & (data_alq_caba[colName] >= price_filter_menor) 
               )

# Eliminamos las variables auxiliares que ya no utilizamos
del colName
del price_filter_menor, price_filter_mayor

#%%
# Graficamos boxplot en base a la superficie total
colName = 'surface_total'
plt.boxplot(data_alq_caba[colName])
plt.xticks([1], [colName])
plt.ylabel('m2')

# Medidas resumen de la columna
data_alq_caba[colName].describe()

# Construimos un filtro (aun no lo aplicamos)
surface_total_filter_mayor = data_alq_caba[colName].quantile(0.90)
surface_total_filter_menor = data_alq_caba[colName].quantile(0.05)
surface_total_filter = (    
            (data_alq_caba[colName] <= surface_total_filter_mayor) 
          & (data_alq_caba[colName] >= surface_total_filter_menor) 
                       )

# Eliminamos las variables auxiliares que ya no utilizamos
del colName
del surface_total_filter_menor, surface_total_filter_mayor

#%%
# Graficamos boxplot en base a la superficie total
colName = 'surface_covered'
plt.boxplot(data_alq_caba[colName])
plt.xticks([1], [colName])
plt.ylabel('m2')

# Medidas resumen de la columna
data_alq_caba[colName].describe()

# Construimos un filtro (aun no lo aplicamos)
surface_covered_filter_mayor = data_alq_caba[colName].quantile(0.90)
surface_covered_filter_menor = data_alq_caba[colName].quantile(0.05)
surface_covered_filter = (    
            (data_alq_caba[colName] <= surface_covered_filter_mayor) 
          & (data_alq_caba[colName] >= surface_covered_filter_menor) 
                       )

# Eliminamos las variables auxiliares que ya no utilizamos
del colName
del surface_covered_filter_menor, surface_covered_filter_mayor

#%%
# Aplicamos los 3 filtros que eliminan "outliers" (notacion -> so = Sin Outliers)
# Es decir, un Y de los tres filtros: price, total_surface y covered_surface
data_alq_caba_so = data_alq_caba[price_filter & surface_total_filter & surface_covered_filter]

# Eliminamos las variables auxiliares que ya no utilizamos
del data_alq_caba
del price_filter, surface_total_filter, surface_covered_filter

#%%
# Graficamos boxplot en base a los precios de alquiler
colName = 'price'
plt.boxplot(data_alq_caba_so[colName])
plt.xticks([1], [colName])
plt.ylabel('AR$')
plt.title('Precio de Alquiler en CABA (en pesos)')

# Eliminamos las variables auxiliares que ya no utilizamos
del colName

#%%
# Graficamos boxplot en base a la superficie total
colName = 'surface_total'
plt.boxplot(data_alq_caba_so[colName])
plt.xticks([1], [colName])
plt.ylabel('m2')
plt.title('Superficie Total de Alquiler en CABA (en m²)')

# Eliminamos las variables auxiliares que ya no utilizamos
del colName

#%%
# Graficamos boxplot en base a la superficie cubierta
colName = 'surface_covered'
plt.boxplot(data_alq_caba_so[colName])
plt.xticks([1], [colName])
plt.ylabel('m2')
plt.title('Superficie Cubierta de Alquiler en CABA (en m²)')

# Eliminamos las variables auxiliares que ya no utilizamos
del colName


#%%
# Graficamos boxplot en base a los precios de alquiler por barrio
# ... ordenamos por mediana de precio de cada barrio
my_order = sql^""" SELECT l3, MEDIAN(price) AS medianaPrecio
                   FROM data_alq_caba_so
                   GROUP BY l3
                   ORDER BY medianaPrecio DESC, l3 ASC"""
ax = sns.boxplot(data=data_alq_caba_so,x='price', y = 'l3', order=my_order['l3'])
ax.set_xlabel("Precio de Alquiler (AR$)",fontsize=12)
ax.set_ylabel("Barrios (l3)",fontsize=10)
ax.tick_params(labelsize=6)


# Eliminamos las variables auxiliares que ya no utilizamos
del my_order, ax



#%%
# Nos interesa quedarnos con los barrios que mas propiedades disponibles tienen
# Veamos cuales son ...
print(data_alq_caba_so['l3'].value_counts())
# Palermo                 2854
# Belgrano                1860
# Recoleta                1210
# Caballito               1119
# Barrio Norte             964
# Almagro                  838
# Villa Crespo             824
# Villa Urquiza            785
# Nuñez                    657
# Flores                   482
# Balvanera                448
# Retiro                   394
# San Nicolás              387
# Centro / Microcentro     376
# ...

# Nos quedamos solo con los registros correspondientes a los primeros 10
# (hasta Flores incluido)
barrios_selec = list(dict(data_alq_caba_so['l3'].value_counts()).keys())[:10]
data_selec = data_alq_caba_so[data_alq_caba_so['l3'].isin(barrios_selec)]

# Eliminamos las variables auxiliares que ya no utilizamos
del barrios_selec, data_alq_caba_so

#%%
# Graficamos boxplot en base a los precios de alquiler por barrio
# ... ordenamos por mediana de precio de cada barrio
my_order = sql^""" SELECT l3, MEDIAN(price) AS medianaPrecio
                   FROM data_selec
                   GROUP BY l3
                   ORDER BY medianaPrecio DESC, l3 ASC"""
ax = sns.boxplot(data=data_selec,x='price', y = 'l3', order=my_order['l3'])
ax.set_xlabel("Precio de Alquiler (AR$)",fontsize=12)
ax.set_ylabel("Barrios (l3)",fontsize=10)
ax.tick_params(labelsize=10)

# Eliminamos las variables auxiliares que ya no utilizamos
del my_order, ax


#%%
# Graficamos una dispersion de puntos de precio en funcion de la superficie total
ax = sns.scatterplot(data=data_selec, x="surface_covered", y="price")
ax.set_xlabel("Superficie total (m2)",fontsize=12)
ax.set_ylabel("Precio de Alquiler (AR$)",fontsize=12)
# Observacion: Se superponen muchos puntos y no se entiende muy bien el grafico

# Eliminamos las variables auxiliares que ya no utilizamos
del ax
#%%
# Graficamos una dispersion de puntos de precio en funcion de la superficie total,
# pero esta vez tratamos de solucionar la superposicion de multiples puntos
fig, ax = plt.subplots(figsize=(6, 6))
sns.scatterplot(
    data=data_selec,
    x="surface_total",
    y="price",
    color="k",
    ax=ax,
)

sns.kdeplot(
    data=data_selec,
    x="surface_total",
    y="price",
    levels=5,
    fill=True,
    alpha=0.6,
    cut=2,
    ax=ax,
)

ax.set_xlabel("Superficie total (m2)",fontsize=12)
ax.set_ylabel("Precio de Alquiler (AR$)",fontsize=12)

# Eliminamos las variables auxiliares que ya no utilizamos
del fig, ax


#%%
# Queremos verificar que sean todos de fechas iniciales mas o menos cercanas y 
# que se distribuyan parejos en el tiempo. Para ello, primero vamos a definir 
# el formato de fecha (anio-mes-dia)
data_selec['start_date'] = pd.to_datetime(data_selec['start_date'],format='%Y-%m-%d')


#%%
# Graficamos una dispersion de puntos de precio en funcion de la fecha inicial
ax = sns.scatterplot(data=data_selec, x="start_date", y="price")
ax.set_xlabel("Fecha inicial",fontsize=12)
ax.set_ylabel("Precio de Alquiler (AR$)",fontsize=12)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
# Observacion: Se superponen muchos puntos y no se entiende muy bien el grafico

# Eliminamos las variables auxiliares que ya no utilizamos
del ax


#%%
# Graficamos una dispersion de puntos de precio en funcion de la fecha inicial,
# pero esta vez tratamos de solucionar la superposicion de multiples puntos
fig, ax = plt.subplots(figsize=(6, 6))
sns.scatterplot(
    data=data_selec,
    x="start_date",
    y="price",
    color="k",
    ax=ax,
)

sns.kdeplot(
    data=data_selec,
    x="start_date",
    y="price",
    levels=5,
    fill=True,
    alpha=0.6,
    cut=2,
    ax=ax,
)

ax.set_xlabel("Fecha inicial",fontsize=12)
ax.set_ylabel("Precio de Alquiler (AR$)",fontsize=12)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)

# Eliminamos las variables auxiliares que ya no utilizamos
del fig, ax

#%%
# Generamos el dataframe y lo grabamos en disco
# Utilizamos como standard el encoding utf-8
data_selec.to_csv('data_selec.csv', encoding='utf-8')

# -*- coding: utf-8 -*-
"""
Materia     : Laboratorio de datos - FCEyN - UBA
Clase       : Clase Regresion Lineal
Detalle     : Division en test y train
                - Cargamos los datos de properati previamente procesados (para 
                  mejorar la calidad de datos)
                - utilizamos rutina para dividir en test(20%) y train(80&)
                - Guardamos ambos dataframes
Autores     : Manuela Cerdeiro y Pablo Turjanski
Modificacion: 2023-10-13
"""

# Importamos bibliotecas
import pandas as pd
from sklearn.model_selection import train_test_split

#%%
# Cargamos el archivo ya limpio
data_selec = pd.read_csv('data_selec.csv', index_col = 'id', encoding='utf-8')

#%%
# Dividimos en test(20%) y train(80%)
train, test = train_test_split(data_selec, test_size=0.2)

#%%
# Guardamos ambos dataframes
train.to_csv('data_alq_caba_train.csv')
test.to_csv('data_alq_caba_test.csv')


# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 09:19:46 2023

@author: JavierMunho
"""

import pandas as pd
import os

file = "prices.csv"

df = pd.read_csv(file,header = 0)

empresas = pd.unique(df.symbol)

higers_prices = []
lowers_prices = []

#for i in empresas:
#    df_empresa = df[df["symbol"] == i ]
#    higers_prices.append(max(df_empresa["high"]))
#    lowers_prices.append(max(df_empresa["low"]))
    
empresa = empresas[159]
df_empresa_2 = df[df["symbol"] == empresa].reset_index()
media = (df_empresa_2.high + df_empresa_2.low)/2
df_empresa_2["media"] = media
rachas_subida_primera = [] #fomato dia inicio, cantidad de dias
rachas_subida_segunda = 0
rachas_bajada_primera = []
rachas_bajada_segunda = 0

for i in range(0,len(df_empresa_2)-1): 
    if df_empresa_2["media"][i] <= df_empresa_2["media"][i+1]:
        rachas_subida_segunda = rachas_subida_segunda + 1
    else : 
        rachas_subida_primera.append((rachas_bajada_segunda,df_empresa_2["date"][i-rachas_subida_segunda]))
        rachas_subida_segunda = 0
    if df_empresa_2["media"][i] >= df_empresa_2["media"][i+1]:
        rachas_bajada_segunda = rachas_bajada_segunda + 1
    else : 
        rachas_bajada_primera.append((rachas_bajada_segunda,df_empresa_2["date"][i-rachas_bajada_segunda]))
        rachas_bajada_segunda = 0

print(max(rachas_bajada_primera))
print(max(rachas_subida_primera))

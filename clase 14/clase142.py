# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 11:24:08 2023

@author: JavierMunho
"""

import pandas as pd
import matplotlib.pyplot as plt

pinguinos = pd.read_csv("penguins_size.csv")

pinguinos.describe()

fig, axs = plt.subplots(2, 2)
axs[0,0].hist(pinguinos["body_mass_g"],bins="sturges")
axs[0,1].hist(pinguinos["culmen_length_mm"],bins="sturges")
axs[1,0].hist(pinguinos["culmen_depth_mm"],bins="sturges")
axs[1,1].hist(pinguinos["flipper_length_mm"],bins="sturges")
plt.show()
plt.close()

sexos =  pd.unique(pinguinos.sex)
especie =  pd.unique(pinguinos.species)

filtro_male = pinguinos["sex"] == sexos[0]
filtro_especie = pinguinos["species"] == especie[0]

pinguinos_male = pinguinos[filtro_male]
pringuinos_male_adelie = pinguinos_male[filtro_especie]

pringuinos_male_adelie.describe()



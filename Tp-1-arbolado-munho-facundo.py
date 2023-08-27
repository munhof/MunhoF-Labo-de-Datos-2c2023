# -*- coding: utf-8 -*-
"""
Materia: Laboratorio de Datos
TÃ­tulo del trabajo: TP Arbolado
Autores: Richard Pavez
Descripcion general del contenido:
Fecha de creacion: 23/8/2023
Fecha de ultima modificacion: 
"""
import csv

archivo_arbolado = "arbolado-en-espacios-verdes.csv"


#Ejercicio 1
def leer_parque(nombre_archivo:str, parque:str) -> dict:
    with open(nombre_archivo, "rt",encoding="utf8") as f:
        filas = csv.reader(f)
        encabezado:list = next(filas)
        info_arboles_por_parque:list = []
        for linea in filas:
            if linea[encabezado.index("espacio_ve")] == parque:
                info_arboles_por_parque.append(dict(zip(encabezado,linea)))
        return info_arboles_por_parque

cant_arboles_gral_paz = len(leer_parque(archivo_arbolado,"GENERAL PAZ"))
print(f"cantidad de arboles en parque gral Paz: {cant_arboles_gral_paz}")

#Ejercicio 2
def especies(lista_arboles):
    especies: list = []
    for i in lista_arboles:
        especies.append(i["nombre_com"])
    especies:list = list(set(especies))
    return especies

print(especies(leer_parque(archivo_arbolado,"GENERAL PAZ")))

#Ejercicio 3
def contar_ejemplares(lista_arboles):
    especies_en_parque = especies(lista_arboles)
    cant_ejemplares = {}
    for especie in especies_en_parque:
        cant_arboles = 0
        for i in lista_arboles:
            if i["nombre_com"] == especie:
                cant_arboles += 1
        cant_ejemplares[especie] = cant_arboles
    return cant_ejemplares

general_paz = leer_parque(archivo_arbolado,"GENERAL PAZ")
ejemplares_general = contar_ejemplares(general_paz)

jacarandas_gral_paz = ejemplares_general["Jacarandá"]
print(f"Cantidad ejemplares jacarandá en parque Gral Paz: { jacarandas_gral_paz }")


#Ejercicio 4
def obtener_alturas(lista_arboles, especie):
    alturas = []
    for i in lista_arboles:
        if i["nombre_com"] == especie:
            alturas.append(float(i.get("altura_tot")))
    return alturas

alturas_jacaranda_gral_paz = obtener_alturas(general_paz, "Jacarandá")

print(f"Altura maxima Jacaranda Parque Gral Paz: {max(alturas_jacaranda_gral_paz)}")
print(f"Altura promedio Jacaranda Parque Gral Paz: {sum(alturas_jacaranda_gral_paz)/len(alturas_jacaranda_gral_paz)}")

#Ejercicio 5
def obtener_inclinacion(lista_arboles, especie):
    inclinacion = []
    for i in lista_arboles:
        if i["nombre_com"] == especie:
            inclinacion.append(float(i.get("inclinacio")))
    return inclinacion

#Ejercicio 6
def especimen_mas_inclinado(lista_arboles):
    especies_del_parque = especies(lista_arboles)
    mayor_inclinacion = 0
    mas_inclinados = ""
    for i in especies_del_parque:
        inclinaciones = obtener_inclinacion(lista_arboles, i)
        max_inclinacion = max(inclinaciones)
        if max_inclinacion > mayor_inclinacion:
            mayor_inclinacion = max_inclinacion
            mas_inclinados = i
    return [mas_inclinados,mayor_inclinacion]

parque_centenario = leer_parque(archivo_arbolado,"CENTENARIO")
mas_inclinado_centenario_esp, mayor_inclinacion_centenario = especimen_mas_inclinado(parque_centenario)
print(f"El especimen mas inclinado en parque Centario es {mas_inclinado_centenario_esp} y esta a {mayor_inclinacion_centenario}")

#Ejercicio 7
def especie_promedio_mas_inclinada(lista_arboles):
    especies_del_parque = especies(lista_arboles)
    mayor_promedio_inclinacion = 0
    mas_inclinados_promedio = ""
    for i in especies_del_parque:
        inclinaciones = obtener_inclinacion(lista_arboles, i)
        max_inclinacion_promedio = sum(inclinaciones)/len(inclinaciones)
        if max_inclinacion_promedio > mayor_promedio_inclinacion:
            mayor_promedio_inclinacion = max_inclinacion_promedio
            mas_inclinados_promedio = i
    return [mas_inclinados_promedio,mayor_promedio_inclinacion]

mas_inclinado_prom_centenario_esp, mayor_inclinacion_prom_centenario = especie_promedio_mas_inclinada(parque_centenario)
print(f"La especie mas inclinado en promedio en el parque Centario es {mas_inclinado_prom_centenario_esp} y estan en promedio a {mayor_inclinacion_prom_centenario}")


"""
Funciones auxialiares para obtener informacion de nombres de los parques

def leer_archivo(nombre_archivo:str) -> dict:
    with open(nombre_archivo, "rt",encoding="utf8") as f:
        filas = csv.reader(f)
        encabezado:list = next(filas)
        info_arboles:list = []
        for linea in filas:
            info_arboles.append(dict(zip(encabezado,linea)))
        return info_arboles
    
def parques(diccionario):
    parque: list = []
    for i in diccionario:
        parque.append(i["espacio_ve"])
    parque:list = list(set(parque))
    return parque
"""








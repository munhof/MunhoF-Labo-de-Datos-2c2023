# -*- coding: utf-8 -*-
"""
Materia: Laboratorio de datos - FCEyN - UBA
Clase  : Clase SQL. Script clase.
Autor  : Pablo Turjanski
Fecha  : 2023-03-07
"""

# Importamos bibliotecas
import pandas as pd
from inline_sql import sql, sql_val

def main():

    print()
    print("# =============================================================================")
    print("# Creamos/Importamos los datasets que vamos a utilizar en este programa")
    print("# =============================================================================")
    #carpeta = "C;\Users\JavierMunho\Documents\MunhoF-Labo-de-Datos-2c2023\Guia SQL\"
    
    # Ejercicios AR-PROJECT, SELECT, RENAME
    empleado       = get_empleado()
    # Ejercicios AR-UNION, INTERSECTION, MINUS
    alumnosBD      = get_alumnosBD()
    alumnosTLeng   = get_alumnosTLeng()
    # Ejercicios AR-CROSSJOIN
    persona        = get_persona_ejemploCrossJoin()
    nacionalidades = get_nacionalidades()
    # Ejercicios ¿Mismos Nombres?
    se_inscribe_en=get_se_inscribe_en_ejemploMismosNombres()
    materia       =get_materia_ejemploMismosNombres()
    # Ejercicio JOIN múltiples tablas
    vuelo      = pd.read_csv("vuelo.csv")    
    aeropuerto = pd.read_csv("aeropuerto.csv")    
    pasajero   = pd.read_csv("pasajero.csv")    
    reserva    = pd.read_csv("reserva.csv")    
    # Ejercicio JOIN tuplas espúreas
    empleadoRol= pd.read_csv("empleadoRol.csv")    
    rolProyecto= pd.read_csv("rolProyecto.csv")    
    # Ejercicios funciones de agregación, LIKE, Elección, Subqueries y variables de Python
    examen     = pd.read_csv("examen.csv")
    # Ejercicios de manejo de valores NULL
    examen03 = pd.read_csv("examen03.csv")
    
    
    print()
    print("# =============================================================================")
    print("# Ejemplo inicial")
    print("# =============================================================================")
    
    print(empleado)
    alumnosBD      = get_alumnosBD()
    alumnosTLeng   = get_alumnosTLeng()
    consultaSQL = """
                   SELECT DISTINCT DNI, Salario
                   FROM empleado;
                  """
    vuelo      = pd.read_csv("vuelo.csv")    
    aeropuerto = pd.read_csv("aeropuerto.csv")    
    pasajero   = pd.read_csv("pasajero.csv")    
    reserva    = pd.read_csv("reserva.csv")    


    dataframeResultado = sql^ consultaSQL
    
    print(dataframeResultado)


    print()
    print("# =============================================================================")
    print("# Ejercicios AR-PROJECT <-> SELECT")
    print("# =============================================================================")
    
    consigna    = "a.- Listar DNI y Salario de empleados "
    consultaSQL = """
                   SELECT DISTINCT DNI, Salario
                   FROM empleado;
                  """
    imprimirEjercicio(consigna, [empleado], consultaSQL, sql^consultaSQL)    
    
    # -----------
    consigna    = "b.- Listar Sexo de empleados "
    consultaSQL = """
                   SELECT DISTINCT Sexo
                   FROM empleado
                  """
    imprimirEjercicio(consigna, [empleado], consultaSQL, sql^consultaSQL)    

    # -----------
    consigna    = "c.- Listar Sexo de empleados (sin DISTINCT)"
    consultaSQL = """
                   SELECT Sexo
                   FROM empleado
                  """
    imprimirEjercicio(consigna, [empleado], consultaSQL, sql^consultaSQL)    

    print()
    print("# =============================================================================")
    print("# Ejercicios AR-SELECT <-> WHERE")
    print("# =============================================================================")
    
    consigna    = "a.- Listar de EMPLEADO sólo aquellos cuyo sexo es femenino"
    consultaSQL = """
                   SELECT DISTINCT DNI, Nombre, Sexo, Salario
                   FROM empleado
                   WHERE Sexo = 'F'
                  """
    imprimirEjercicio(consigna, [empleado], consultaSQL, sql^consultaSQL)    

    # -----------
    consigna    = "b.- Listar de EMPLEADO aquellos cuyo sexo es femenino y su salario es mayor a $15.000"
    consultaSQL = """
                    SELECT DISTINCT *
                    FROM empleado
                    WHERE Sexo = 'F' AND Salario > 15000; 
                  """
    imprimirEjercicio(consigna, [empleado], consultaSQL, sql^consultaSQL)    
    
    print()
    print("# =============================================================================")
    print("# Ejercicios AR-RENAME <-> AS")
    print("# =============================================================================")
    
    consigna    = """a.- Listar DNI y Salario de EMPLEADO, y renombrarlos como id e Ingreso"""
    consultaSQL = """
                   SELECT DISTINCT DNI AS ID, Salario AS Ingreso
                   FROM empleado
                  """
    
    imprimirEjercicio(consigna, [empleado], consultaSQL, sql^consultaSQL)    
 
    
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
     # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
     # #                                                                     # #
    # #    INICIO -->           EJERCICIO Nro. 01                             # #
     # #                                                                     # # 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
     # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # nuevos datos del dataframe persona para los ejercicios de AR-INNER y LEFT OU
    # IMPORTANTE: Recordar que se utilizaran los datos de vuelo, aeropuerto, pasajero y reserva

    print()
    print("# =============================================================================")
    print("# EJERCICIOS PARA REALIZAR DE MANERA INDIVUDUAL --> EJERCICIO Nro. 01")
    print("# =============================================================================")

    
    consigna    = "Ejercicio 01.1.- Retornar Codigo y Nombre de los aeropuertos de Londres"
    consultaSQL = """
                   SELECT DISTINCT Codigo, Nombre
                   FROM aeropuerto
                   WHERE Ciudad = 'Londres';
                  """
    imprimirEjercicio(consigna, [vuelo, aeropuerto, pasajero, reserva], consultaSQL, sql^consultaSQL)    

    # -----------
    consigna    = "Ejercicio 01.2.- ¿Qué retorna \n     SELECT DISTINCT Ciudad AS City \n     FROM aeropuerto \n     WHERE Codigo='ORY' OR Codigo='CDG'; ?"
    consultaSQL = """
                   SELECT DISTINCT Ciudad AS City
                   FROM aeropuerto
                   WHERE Codigo='ORY' OR Codigo='CDG';
                  """
    imprimirEjercicio(consigna, [vuelo, aeropuerto, pasajero, reserva], consultaSQL, sql^consultaSQL)    

    # -----------
    consigna    = "Ejercicio 01.3.- Obtener los números de vuelo que van desde CDG hacia LHR"
    consultaSQL = """
                   SELECT DISTINCT Numero
                   From vuelo
                   WHERE Origen = 'CDG' AND Destino = 'LHR'
                  """
    imprimirEjercicio(consigna, [vuelo, aeropuerto, pasajero, reserva], consultaSQL, sql^consultaSQL)    

    # -----------
    consigna    = "Ejercicio 01.4.- Obtener los números de vuelo que van desde CDG hacia LHR o viceversa"
    consultaSQL = """
                   SELECT DISTINCT Numero
                   FROM vuelo
                   WHERE (Origen = 'CDG' AND Destino = 'LHR') OR (Origen = 'LHR' AND Destino = 'CDG');               
                  """
    imprimirEjercicio(consigna, [vuelo, aeropuerto, pasajero, reserva], consultaSQL, sql^consultaSQL)    

    # -----------
    consigna    = "Ejercicio 01.5.- Devolver las fechas de reservas cuyos precios son mayores a $200"
    consultaSQL = """
                   SELECT DISTINCT Fecha
                   From reserva
                   WHERE Precio > 200
                  """
    imprimirEjercicio(consigna, [vuelo, aeropuerto, pasajero, reserva], consultaSQL, sql^consultaSQL)    

    
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
     # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
     # #                                                                     # #
    # #    FIN -->              EJERCICIO Nro. 01                             # #
     # #                                                                     # # 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
     # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    
    
    print()
    print("# =============================================================================")
    print("# Ejercicios AR-UNION, INTERSECT, MINUS <-> UNION, INTERSECTION, EXCEPT")
    print("# =============================================================================")

    consigna    = """a1.- Listar a los alumnos que cursan BDs o TLENG"""
    
    consultaSQL = """
                   SELECT DISTINCT *
                   FROM alumnosBD
                   UNION
                   SELECT DISTINCT *
                   FROM alumnosTLeng
                  """

    imprimirEjercicio(consigna, [alumnosBD, alumnosTLeng], consultaSQL, sql^consultaSQL)    


    # -----------
    consigna    = """a2.- Listar a los alumnos que cursan BDs o TLENG (usando UNION ALL)"""
    
    consultaSQL = """
                   SELECT DISTINCT *
                   FROM alumnosBD
                   UNION ALL
                   SELECT DISTINCT *
                   FROM alumnosTLeng
                  """

    imprimirEjercicio(consigna, [alumnosBD, alumnosTLeng], consultaSQL, sql^consultaSQL)    


    # -----------
    consigna    = """b.- Listar a los alumnos que cursan simultáneamente BDs y TLENG"""
    
    consultaSQL = """
                   SELECT DISTINCT *
                   FROM alumnosBD
                   INTERSECT
                   SELECT DISTINCT *
                   FROM alumnosTLeng
                  """

    imprimirEjercicio(consigna, [alumnosBD, alumnosTLeng], consultaSQL, sql^consultaSQL)    

    
    # -----------
    consigna    = """c.- Listar a los alumnos que cursan BDs y no cursan TLENG """
    
    consultaSQL = """
                   SELECT DISTINCT *
                   FROM alumnosBD
                   EXCEPT
                   SELECT DISTINCT *
                   FROM alumnosTLeng
                  """

    imprimirEjercicio(consigna, [alumnosBD, alumnosTLeng], consultaSQL, sql^consultaSQL)    


    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
     # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
     # #                                                                     # #
    # #    INICIO -->           EJERCICIO Nro. 02                             # #
     # #                                                                     # # 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
     # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    
    # IMPORTANTE: Recordar que se utilizaran los datos de vuelo, aeropuerto, pasajero y reserva

    print()
    print("# =============================================================================")
    print("# EJERCICIOS PARA REALIZAR DE MANERA INDIVUDUAL --> EJERCICIO Nro. 02")
    print("# =============================================================================")

    
    consigna    = "Ejercicio 02.1.- Devolver los números de vuelo que tienen reservas generadas (utilizar intersección)"
    consultaSQL = """
                   SELECT DISTINCT Numero 
                   FROM vuelo
                   INTERSECT
                   SELECT DISTINCT NroVuelo
                   FROM reserva
                  """
    imprimirEjercicio(consigna, [vuelo, aeropuerto, pasajero, reserva], consultaSQL, sql^consultaSQL)    

    # -----------
    consigna    = "Ejercicio 02.2.- Devolver los números de vuelo que aún no tienen reservas"
    consultaSQL = """
                   SELECT Numero 
                   FROM vuelo
                   EXCEPT
                   SELECT NroVuelo
                   FROM reserva
                  """
    imprimirEjercicio(consigna, [vuelo, aeropuerto, pasajero, reserva], consultaSQL, sql^consultaSQL)    

    # -----------
    consigna    = "Ejercicio 02.3.- Retornar los códigos de aeropuerto de los que parten o arriban los vuelos"
    consultaSQL = """
                   SELECT destino as codigo
                   FROM vuelo
                   UNION
                   SELECT origen
                   FROM vuelo
                  """
    imprimirEjercicio(consigna, [vuelo, aeropuerto, pasajero, reserva], consultaSQL, sql^consultaSQL)    



    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
     # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
     # #                                                                     # #
    # #    FIN -->              EJERCICIO Nro. 02                             # #
     # #                                                                     # # 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
     # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

   
    
    print("# =============================================================================")
    print("# Ejercicios AR-... JOIN <-> ... JOIN")
    print("# =============================================================================")

    consigna    = """a1.- Listar el producto cartesiano entre las tablas persona y nacionalidades"""
    
    consultaSQL = """
                   SELECT DISTINCT *
                   FROM persona
                   CROSS JOIN 
                   nacionalidades;
                  """

    imprimirEjercicio(consigna, [persona, nacionalidades], consultaSQL, sql^consultaSQL)


    # -----------
    consigna    = """a2.- Listar el producto cartesiano entre las tablas persona y nacionalidades (sin usar CROSS JOIN)"""
    
    consultaSQL = """
                   SELECT DISTINCT *
                   FROM persona, nacionalidades
                  """

    imprimirEjercicio(consigna, [persona, nacionalidades], consultaSQL, sql^consultaSQL)


    # ---------------------------------------------------------------------------------------------- 
    # Carga los nuevos datos del dataframe persona para los ejercicios de AR-INNER y LEFT OUTER JOIN
    # ----------------------------------------------------------------------------------------------
    persona        = get_persona_ejemplosJoin()
    # ----------------------------------------------------------------------------------------------
    
    
    consigna    = """b1.- Vincular las tablas persona y nacionalidades a través de un INNER JOIN"""
    
    consultaSQL = """
                   SELECT *
                   FROM persona
                   INNER JOIN nacionalidades
                   ON Nacionalidad = IDN
                  """

    imprimirEjercicio(consigna, [persona, nacionalidades], consultaSQL, sql^consultaSQL)


    # -----------
    consigna    = """b2.- Vincular las tablas persona y nacionalidades (sin usar INNER JOIN)"""
    
    consultaSQL = """
                    SELECT DISTINCT *
                    FROM persona,nacionalidades
                    WHERE Nacionalidad = IDN
                  """

    imprimirEjercicio(consigna, [persona, nacionalidades], consultaSQL, sql^consultaSQL)


    # -----------
    consigna    = """c.- Vincular las tablas persona y nacionalidades a través de un LEFT OUTER JOIN"""
    
    consultaSQL = """
                   SELECT *
                   FROM persona
                   LEFT OUTER JOIN nacionalidades
                   ON Nacionalidad = IDN
                  """

    imprimirEjercicio(consigna, [persona, nacionalidades], consultaSQL, sql^consultaSQL)
    

    print("# =============================================================================")
    print("# Ejercicios SQL - ¿Mismos Nombres?")
    print("# =============================================================================")

    consigna    = """a.- Vincular las tablas Se_inscribe_en y Materia. Mostrar sólo LU y Nombre de materia"""
    
    consultaSQL = """
                   SELECT LU, Nombre
                   FROM se_inscribe_en
                   INNER JOIN materia
                   ON se_inscribe_en.Codigo_materia = materia.Codigo_materia 
                  """

    imprimirEjercicio(consigna, [se_inscribe_en, materia], consultaSQL, sql^consultaSQL)
    
    
    
    
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
     # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
     # #                                                                     # #
    # #    INICIO -->           EJERCICIO Nro. 03                             # #
     # #                                                                     # # 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
     # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    
    # IMPORTANTE: Recordar que se utilizaran los datos de vuelo, aeropuerto, pasajero y reserva

    print()
    print("# =============================================================================")
    print("# EJERCICIOS PARA REALIZAR DE MANERA INDIVUDUAL --> EJERCICIO Nro. 03")
    print("# =============================================================================")
    
    consigna    = "Ejercicio 03.1.- Devolver el nombre de la ciudad de partida del vuelo número 165"

    consultaSQL = """
                    SELECT Ciudad
                    FROM aeropuerto
                    INNER JOIN vuelo
                    ON Origen = Codigo
                    Where Numero = 165
                  """

    imprimirEjercicio(consigna, [vuelo, aeropuerto, pasajero, reserva], consultaSQL, sql^consultaSQL)    

    # -----------
    consigna    = "Ejercicio 03.2.- Retornar el nombre de las personas que realizaron reservas a un valor menor a $200"

    consultaSQL = """
                    SELECT Nombre
                    FROM pasajero
                    LEFT OUTER JOIN reserva
                    ON pasajero.DNI = reserva.DNI
                    Where Precio < 200
                  """

    imprimirEjercicio(consigna, [vuelo, aeropuerto, pasajero, reserva], consultaSQL, sql^consultaSQL)    

    # -----------
    consigna    = "Ejercicio 03.3.- Obtener Nombre, Fecha y Destino del Viaje de todos los pasajeros que vuelan desde Madrid"

    consulta_union_pasajero_reserva = """
                                        SELECT *
                                        From pasajero
                                        LEFT OUTER  JOIN reserva
                                        ON pasajero.DNI = reserva.DNI
                                        """

    pasajero_j_reserva = sql^consulta_union_pasajero_reserva
    
    consulta_union_pasajero_j_reserva_j_vuelo = """
                                                SELECT *
                                                FROM pasajero_j_reserva
                                                LEFT OUTER JOIN vuelo
                                                ON NroVuelo = Numero
                                                WHERE Origen = 'MAD'
                                                """
    pasajero_j_reserva_j_vuelo = sql^consulta_union_pasajero_j_reserva_j_vuelo

    
    consultaSQL = """
                    SELECT Nombre, Fecha, Destino
                    From pasajero_j_reserva_j_vuelo
                  """
    imprimirEjercicio(consigna, [vuelo, aeropuerto, pasajero, reserva], consultaSQL, sql^consultaSQL)    


    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
     # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
     # #                                                                     # #
    # #    FIN -->              EJERCICIO Nro. 03                             # #
     # #                                                                     # # 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
     # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    
    
    print("# =============================================================================")
    print("# Ejercicios SQL - Join de varias tablas en simultáneo")
    print("los nuevos datos del dataframe persona para los ejercicios de AR-INNER y LEFT OUT")
    print("# =============================================================================")

    consigna    = """a.- Vincular las tablas Reserva, Pasajero y Vuelo. Mostrar sólo Fecha de reserva, hora de salida del vuelo y nombre de pasajero."""
    
    consultaSQL = """
                   SELECT DISTINCT r.Fecha, v.Salida, p.Nombre
                   FROM reserva AS r, pasajero AS p, vuelo AS v
                   WHERE r.DNI=p.DNI AND r.NroVuelo=v.Numero;
                  """

    imprimirEjercicio(consigna, [reserva, pasajero, vuelo], consultaSQL, sql^consultaSQL)

    
    print("# =============================================================================")
    print("# Ejercicios SQL - Tuplas espúreas")
    print("# =============================================================================")

    consigna    = """a.- Vincular (JOIN)  EmpleadoRol y RolProyecto para obtener la tabla original EmpleadoRolProyecto"""
    
    consultaSQL ="""
                    SELECT e.empleado, e.rol, r.proyecto
                    FROM empleadoRol as e
                    INNER JOIN rolProyecto as r
                    ON e.rol = r.rol
                """

    imprimirEjercicio(consigna, [empleadoRol, rolProyecto], consultaSQL, sql^consultaSQL)

#para evitar esto recordar usar una superclave para unir
    

    print("# =============================================================================")
    print("# Ejercicios SQL - Funciones de agregación")
    print("# =============================================================================")

    consigna    = """a.- Usando sólo SELECT contar cuántos exámenes fueron rendidos (en total)"""
    
    consultaSQL = """
                    SELECT count(*) as cantidad_de_examen
                    FROM examen
                  """

    imprimirEjercicio(consigna, [examen], consultaSQL, sql^consultaSQL)


    # -----------
    consigna    = """b1.- Usando sólo SELECT contar cuántos exámenes fueron rendidos en cada Instancia"""
    
    consultaSQL = """
                    SELECT Instancia, count(*) as cantidad_de_examen
                    FROM examen
                    GROUP BY Instancia;
                  """

    imprimirEjercicio(consigna, [examen], consultaSQL, sql^consultaSQL)


    # -----------
    consigna    = """b2.- Usando sólo SELECT contar cuántos exámenes fueron rendidos en cada Instancia (ordenado por instancia)"""
    
    consultaSQL = """
                    SELECT Instancia, count(*) as cantidad_de_examen
                    FROM examen
                    GROUP BY Instancia
                    ORDER BY Instancia ASC
                  """

    imprimirEjercicio(consigna, [examen], consultaSQL, sql^consultaSQL)


    # -----------
    consigna    = """b3.- Ídem ejercicio anterior, pero mostrar sólo las instancias a las que asistieron menos de 4 Estudiantes"""
    
    consultaSQL = """
                    SELECT Instancia, count(*) as Asistieron
                    FROM examen
                    GROUP BY Instancia
                    HAVING Asistieron < 4
                    ORDER BY Instancia ASC
                  """

    imprimirEjercicio(consigna, [examen], consultaSQL, sql^consultaSQL)


    # -----------
    consigna    = """c.- Mostrar el promedio de edad de los estudiantes en cada instancia de examen"""
    
    consultaSQL = """
                    SELECT Instancia, AVG(EDAD) as PromedioEdad
                    FROM examen
                    GROUP BY Instancia
                    ORDER BY Instancia ASC
                  """

    imprimirEjercicio(consigna, [examen], consultaSQL, sql^consultaSQL)


    print("# =============================================================================")
    print("# Ejercicios SQL - LIKE")
    print("# =============================================================================")

    consigna    = """a1.- Mostrar cuál fue el promedio de notas en cada instancia de examen, sólo para instancias de parcial."""
    
    consultaSQL = """
                    SELECT Instancia, 
                            AVG(Nota) as PromedioNotas
                    FROM examen
                    GROUP BY Instancia
                    HAVING (Instancia = 'Parcial-01') OR (Instancia = 'Parcial-02')
                  """

    imprimirEjercicio(consigna, [examen], consultaSQL, sql^consultaSQL)


    # -----------
    consigna    = """a2.- Mostrar cuál fue el promedio de notas en cada instancia de examen, sólo para instancias de parcial. Esta vez usando LIKE."""
    
    consultaSQL = """
                    SELECT Instancia, 
                            AVG(Nota) as PromedioNotas
                    FROM examen
                    GROUP BY Instancia
                    HAVING Instancia LIKE 'Parcial%'
                  """

    imprimirEjercicio(consigna, [examen], consultaSQL, sql^consultaSQL)


    print("# =============================================================================")
    print("# Ejercicios SQL - Eligiendo")
    print("# =============================================================================")

    consigna    = """a1.- Listar a cada alumno que rindió el Parcial-01 y decir si aprobó o no (se aprueba con nota >=4)."""
    
    consultaSQL = """
                    SELECT Nombre, 
                           Nota,
                           CASE WHEN Nota >=4
                               THEN 'Aprobo'
                               ELSE 'No Aprobo'
                           END AS Estado
                    FROM examen
                    WHERE Instancia='Parcial-01'
                  """

    imprimirEjercicio(consigna, [examen], consultaSQL, sql^consultaSQL)


    # -----------
    consigna    = """a2.- Modificar la consulta anterior para que informe cuántos estudiantes aprobaron/reprobaron en cada instancia."""
    
    
    consultaSQL = """
                    SELECT Instancia,
                           CASE WHEN Nota >=4
                               THEN 'Aprobo'
                               ELSE 'No Aprobo'
                           END AS Estado,
                           COUNT(*) AS Cantidad
                    FROM examen
                    GROUP BY Instancia, Estado
                  """

    imprimirEjercicio(consigna, [examen], consultaSQL, sql^consultaSQL)


    print("# =============================================================================")
    print("# Ejercicios SQL - Subqueries")
    print("# =============================================================================")

    consigna    = """a.- Listar los alumnos que en cada instancia obtuvieron una nota mayor al promedio de dicha instancia"""
    
    
    consultaSQL_obtener_promedio = """
                    SELECT Instancia, 
                            AVG(Nota) as PromedioNotas
                    FROM examen
                    GROUP BY Instancia
                    ORDER BY Instancia
                  """
    tabla_promedio = sql^consultaSQL_obtener_promedio
    
    
    consultaSQL_add_promedio = """
                                SELECT *
                                FROM examen as e
                                INNER JOIN tabla_promedio as p
                                ON e.Instancia = p.Instancia
                                ORDER BY p.Instancia
                               """
    
    examen_con_promedio = sql^consultaSQL_add_promedio
    
    consultaSQL = """
                    SELECT
                           Nombre,
                           Instancia,
                           Nota
                    FROM examen_con_promedio
                    WHERE Nota >= PromedioNotas
                    ORDER BY Instancia
                  """


    imprimirEjercicio(consigna, [examen,consultaSQL_obtener_promedio,consultaSQL_add_promedio], consultaSQL, sql^consultaSQL)
    # -----------
    consigna    = """b.1- Listar los alumnos que en cada instancia obtuvieron una nota mayor al promedio de dicha instancia con subquery"""
    
    
    consultaSQL = """
                    SELECT
                           e1.Nombre,
                           e1.Instancia,
                           e1.Nota
                    FROM examen as e1
                    WHERE Nota >(
                        SELECT AVG(Nota)
                        FROM examen as e2
                        WHERE e2.Instancia = e1.Instancia
                    )
                    ORDER BY Instancia ASC, Nota DESC
                  """

    imprimirEjercicio(consigna, [examen], consultaSQL, sql^consultaSQL)


    # -----------
    consigna    = """b.- Listar los alumnos que en cada instancia obtuvieron la mayor nota de dicha instancia"""
    
    consultaSQL_obtener_maximo = """
                    SELECT Instancia, 
                            MAX(Nota) as MaxNotas
                    FROM examen
                    GROUP BY Instancia
                    ORDER BY Instancia
                  """
    tabla_maximo = sql^consultaSQL_obtener_maximo
    
    
    consultaSQL_add_maximo= """
                                SELECT *
                                FROM examen as e
                                INNER JOIN tabla_maximo as m
                                ON e.Instancia = m.Instancia
                                ORDER BY m.Instancia
                               """
    
    examen_con_maximo = sql^consultaSQL_add_maximo
    
    consultaSQL = """
                    SELECT
                           Nombre,
                           Instancia,
                           Nota
                    FROM examen_con_maximo
                    WHERE Nota == MaxNotas
                    ORDER BY Instancia
                  """

    imprimirEjercicio(consigna, [examen], consultaSQL, sql^consultaSQL)

# -----------
    consigna    = """b.1- Listar los alumnos que en cada instancia obtuvieron la mayor nota de dicha instancia con subquery"""
    
    
    consultaSQL = """
                    SELECT
                           e1.Nombre,
                           e1.Instancia,
                           e1.Nota
                    FROM examen as e1
                    WHERE Nota == ALL(
                        SELECT MAX(Nota)
                        FROM examen as e2
                        WHERE e2.Instancia = e1.Instancia
                    )
                    ORDER BY Instancia ASC, Nota DESC
                  """

    imprimirEjercicio(consigna, [examen], consultaSQL, sql^consultaSQL)


    # -----------
    consigna    = """c.- Listar el nombre, instancia y nota sólo de los estudiantes que no rindieron ningún Recuperatorio"""
    
    consultaSQL = """
                    SELECT 
                           e1.Nombre,
                           e1.Instancia,
                           e1.Nota
                    FROM examen as e1
                    WHERE NOT EXISTS(
                        SELECT *
                        FROM examen as e2          
                        WHERE e2.Nombre = e1.Nombre AND 
                              e2.Instancia LIKE 'Recuperatorio%'
                        
                    )
                    ORDER BY Nombre ASC, Instancia ASC
                  """

    imprimirEjercicio(consigna, [examen], consultaSQL, sql^consultaSQL)


    print("# =============================================================================")
    print("# Ejercicios SQL - Integrando variables de Python")
    print("# =============================================================================")

    consigna    = """a.- Mostrar Nombre, Instancia y Nota de los alumnos cuya Nota supera el umbral indicado en la variable de Python umbralNota"""
    
    umbralNota = 7
    
    consultaSQL = f"""
                    SELECT
                           e1.Nombre,
                           e1.Instancia,
                           e1.Nota
                    FROM examen as e1
                    WHERE Nota >= $umbralNota
                    ORDER BY Instancia ASC, Nota DESC
                  """

    imprimirEjercicio(consigna, [examen], consultaSQL, sql^consultaSQL)


    print("# =============================================================================")
    print("# Ejercicios SQL - Manejo de NULLs")
    print("# =============================================================================")

    consigna    = """a.- Listar todas las tuplas de Examen03 cuyas Notas son menores a 9"""
    
    umbralNota = 9
    
    consultaSQL = """
                    SELECT *
                    FROM examen03 as e1
                    WHERE Nota <= 9
                    ORDER BY Instancia ASC, Nota DESC
                  """

    imprimirEjercicio(consigna, [examen03], consultaSQL, sql^consultaSQL)

    # -----------
    consigna    = """b.- Listar todas las tuplas de Examen03 cuyas Notas son mayores o iguales a 9"""
    
    consultaSQL = """
                    SELECT *
                    FROM examen03 as e1
                    WHERE Nota >= $umbralNota
                    ORDER BY Instancia ASC, Nota DESC
                  """


    imprimirEjercicio(consigna, [examen03], consultaSQL, sql^consultaSQL)


    # -----------
    consigna    = """c.- Listar el UNION de todas las tuplas de Examen03 cuyas Notas son menores a 9 y las que son mayores o iguales a 9"""
    
    consultaSQL_menores = """
                    SELECT *
                    FROM examen03 as e1
                    WHERE Nota <= $umbralNota
                    ORDER BY Instancia ASC, Nota DESC
                  """
    
    consultaSQL_mayores = """
                    SELECT *
                    FROM examen03 as e1
                    WHERE Nota >= $umbralNota
                    ORDER BY Instancia ASC, Nota DESC
                  """
                  
    tabla_menores = sql^consultaSQL_menores
    
    tabla_mayores = sql^consultaSQL_mayores
    
    consultaSQL = """
                  SELECT *
                  FROM tabla_menores
                  UNION
                  SELECT *
                  FROM tabla_mayores
                  """

    imprimirEjercicio(consigna, [examen03], consultaSQL, sql^consultaSQL)


    # -----------
    consigna    = """d1.- Obtener el promedio de notas"""
    
    consultaSQL =   """
                    SELECT Instancia,
                            AVG(Nota) as PromedioNotas
                    FROM examen03
                    GROUP BY Instancia
                    ORDER BY Instancia
                    """

    imprimirEjercicio(consigna, [examen03], consultaSQL, sql^consultaSQL)

                           
    # -----------
    consigna    = """d2.- Obtener el promedio de notas (tomando a NULL==0)"""
    
    consultaSQL = """
                    SELECT Instancia,
                           AVG(CASE WHEN Nota IS NULL THEN 0 ELSE Nota END) as PromedioNotas
                    FROM examen03
                    GROUP BY Instancia
                    ORDER BY Instancia

                  """


    imprimirEjercicio(consigna, [examen03], consultaSQL, sql^consultaSQL)

    print("# =============================================================================")
    print("# Ejercicios SQL - Desafío")
    print("# =============================================================================")

    consigna    = """a.- Mostrar para cada estudiante las siguientes columnas con sus datos: Nombre, Sexo, Edad, Nota-Parcial-01, Nota-Parcial-02, Recuperatorio-01 y , Recuperatorio-02"""
    
    # ... Paso 1: Obtenemos los datos de los estudiantes
    consultaSQL = """
                    SELECT DISTINCT Nombre, Sexo, Edad
                    FROM examen
                  """

    datosEstudiantes = sql^ consultaSQL
    
    
    #... Paso aux: tomo la tabla de la instancia Parcial-01
    consultaSQL = """
                    SELECT Nombre, Nota
                    FROM examen
                    WHERE Instancia  = 'Parcial-01'
                  """

    datosParcial01 = sql^ consultaSQL
    
    
    # ... Paso 2: Agregamos las notas del Parcial-01
    consultaSQL = """
                    SELECT d.Nombre, d.Sexo, d.Edad, e.Nota as Parcial_01
                    FROM datosEstudiantes as d
                    LEFT OUTER JOIN datosParcial01 as e
                    ON d.Nombre = e.Nombre
                  """

    datosHastaParcial01 = sql^ consultaSQL
    
    #... Paso aux: tomo la tabla de la instancia Parcial-02
    consultaSQL = """
                    SELECT Nombre, Nota
                    FROM examen
                    WHERE Instancia  = 'Parcial-02'
                  """

    datosParcial02 = sql^ consultaSQL

    # ... Paso 3: Agregamos las notas del Parcial-02
    consultaSQL = """
                    SELECT d.Nombre, d.Sexo, d.Edad, d.Parcial_01, e.Nota as Parcial_02
                    FROM datosHastaParcial01 as d
                    LEFT OUTER JOIN datosParcial02 as e
                    ON d.Nombre = e.Nombre
                  """
    
    datosHastaParcial02 = sql^ consultaSQL
    
        #... Paso aux: tomo la tabla de la instancia Recuperatorio-01
    consultaSQL = """
                    SELECT Nombre, Nota
                    FROM examen
                    WHERE Instancia  = 'Recuperatorio-01'
                  """

    datosRecupeatorio1 = sql^ consultaSQL

    # ... Paso 3: Agregamos las notas del Recuperatorio-01
    consultaSQL = """
                    SELECT d.Nombre, d.Sexo, d.Edad, d.Parcial_01, d.Parcial_02,
                        e.Nota as Recupeatorio_01
                    FROM datosHastaParcial02 as d
                    LEFT OUTER JOIN datosRecupeatorio1 as e
                    ON d.Nombre = e.Nombre
                  """
    
    datosHastaRecupeatorio01 = sql^ consultaSQL
    
    #... Paso aux: tomo la tabla de la instancia Recuperatorio-02
    
    consultaSQL = """
                    SELECT Nombre, Nota
                    FROM examen
                    WHERE Instancia  = 'Recuperatorio-02'
                  """

    datosRecupeatorio2 = sql^ consultaSQL

    # ... Paso 3: Agregamos las notas del Recuperatorio-02
    consultaSQL = """
                    SELECT d.Nombre, d.Sexo, d.Edad, d.Parcial_01, d.Parcial_02,
                        d.Recupeatorio_01, e.Nota as Recuperatorio_02
                    FROM datosHastaRecupeatorio01 as d
                    LEFT OUTER JOIN datosRecupeatorio2 as e
                    ON d.Nombre = e.Nombre
                    ORDER BY Parcial_01 DESC,Parcial_02 DESC,Recupeatorio_01 DESC
                  """
    
    datosHastaRecupeatorio02 = sql^ consultaSQL


    desafio_01 = datosHastaRecupeatorio02

    imprimirEjercicio(consigna, [examen], consultaSQL, sql^consultaSQL)


    # -----------
    consigna    = """b.- Agregar al ejercicio anterior la columna Estado, que informa si el alumno aprobó la cursada (APROBÓ/NO APROBÓ). Se aprueba con 4."""
    
    consultaSQL = """SELECT Nombre, Sexo, Edad, Parcial_01, Parcial_02,
                    Recupeatorio_01 as Recuperatorio_01, Recuperatorio_02,
                    CASE WHEN (Recuperatorio_01 >=4 OR Parcial_01 >=4 ) AND (Recuperatorio_02 >=4 OR Parcial_02 >=4 )
                        THEN 'Aprobo'
                        ELSE 'No Aprobo'
                    END AS Estado
                    FROM desafio_01
                    ORDER BY Parcial_01 DESC,Parcial_02 DESC,Recuperatorio_02 DESC
                  """

    desafio_02 = sql^ consultaSQL
    
    imprimirEjercicio(consigna, [examen], consultaSQL, sql^consultaSQL)

    # -----------
    consigna    = """c.- Generar la tabla Examen a partir de la tabla obtenida en el desafío anterior."""
    
    consultaSQL = """
                    SELECT Nombre, Sexo, Edad, 'Parcial-01' AS Instancia, Parcial_01 AS Nota
                    FROM desafio_02
                    WHERE Parcial_01 IS NOT NULL
                UNION 
                    SELECT Nombre, Sexo, Edad, 'Parcial-02' AS Instancia, Parcial_02 AS Nota
                    FROM desafio_02
                    WHERE Parcial_02 IS NOT NULL
                UNION 
                    SELECT Nombre, Sexo, Edad, 'Recuperatorio-01' AS Instancia, Recuperatorio_01 AS Nota
                    FROM desafio_02
                    WHERE Recuperatorio_01 IS NOT NULL
                UNION 
                    SELECT Nombre, Sexo, Edad, 'Recuperatorio-02' AS Instancia, Recuperatorio_02 AS Nota
                    FROM desafio_02
                    WHERE Recuperatorio_02 IS NOT NULL
                ORDER BY Instancia
                  """

    desafio_03 = sql^ consultaSQL
    
    imprimirEjercicio(consigna, [examen], consultaSQL, sql^consultaSQL)

    print("# =============================================================================")
    print("# Ejercicios SQL - Reemplazos")
    print("# =============================================================================")

    consigna    = """a.- Consigna: En la descripción de los roles de los empleados reemplazar las ñ por ni"""
    
    consultaSQL = """
                    SELECT empleado,
                           REPLACE(rol, 'ñ', 'ni') as rol
                    FROM empleadoRol
                  """

    imprimirEjercicio(consigna, [empleadoRol], consultaSQL, sql^consultaSQL)

    print("# =============================================================================")
    print("# Ejercicios SQL - Mayúsculas/Minúsculas")
    print("# =============================================================================")

    consigna    = """a.- Consigna: Transformar todos los caracteres de las descripciones de los roles a mayúscula"""
    
    consultaSQL = """
                    SELECT empleado,
                           UPPER(rol) as rol
                    FROM empleadoRol
                  """

    imprimirEjercicio(consigna, [empleadoRol], consultaSQL, sql^consultaSQL)

    # -----------
    consigna    = """b.- Consigna: Transformar todos los caracteres de las descripciones de los roles a minúscula"""
    
    consultaSQL = """
                    SELECT empleado,
                           LOWER(rol) as rol
                    FROM empleadoRol
                  """

    imprimirEjercicio(consigna, [empleadoRol], consultaSQL, sql^consultaSQL)

    # -----------


# =============================================================================
# FUNCIONES PARA LA GENERACIÓN DE DATAFRAMES 
# =============================================================================
def get_empleado():
    # Genera el dataframe "empleado" que contiene las siguientes columnas 
    # (en el orden mencionado):
        # 1. DNI
        # 2. Nombre
        # 3. Sexo
        # 4. Salaro
        
    # ... Creamos el dataframe vacío (sólo con los nombres de sus columnas)
    empleado = pd.DataFrame(columns = ['DNI', 'Nombre', 'Sexo', 'Salario'])
    # ... Agregamos cada una de las filas al dataFrame
    empleado = pd.concat([empleado,pd.DataFrame([
        {'DNI' : 20222333, 'Nombre' : 'Diego' , 'Sexo' : 'M', 'Salario' : 20000.0},
        {'DNI' : 33456234, 'Nombre' : 'Laura' , 'Sexo' : 'F', 'Salario' : 25000.0},
        {'DNI' : 45432345, 'Nombre' : 'Marina', 'Sexo' : 'F', 'Salario' : 10000.0}
                                                ])
                        ])
    return empleado


def get_alumnosBD():
    # Genera el dataframe "alumnosBD" que contiene las siguientes columnas 
    # (en el orden mencionado):
        # 1. ID
        # 2. Nombre
        
    # ... Creamos el dataframe vacío (sólo con los nombres de sus columnas)
    alumnosBD = pd.DataFrame(columns = ['ID', 'Nombre'])
    # ... Agregamos cada una de las filas al dataFrame
    alumnosBD = pd.concat([alumnosBD,pd.DataFrame([
        {'ID' : 1, 'Nombre' : 'Diego' },
        {'ID' : 2, 'Nombre' : 'Laura' },
        {'ID' : 3, 'Nombre' : 'Marina'}
                                                    ])
                        ])
    return alumnosBD


def get_alumnosTLeng():
    # Genera el dataframe alumnosTLeng que contiene las siguientes columnas 
    # (en el orden mencionado):
        # 1. ID
        # 2. Nombre
        
    # ... Creamos el dataframe vacío (sólo con los nombres de sus columnas)
    alumnosTLeng = pd.DataFrame(columns = ['ID', 'Nombre'])
    # ... Agregamos cada una de las filas al dataFrame
    alumnosTLeng = pd.concat([alumnosTLeng,pd.DataFrame([
        {'ID' : 2, 'Nombre' : 'Laura'    },
        {'ID' : 4, 'Nombre' : 'Alejandro'}
                                                        ])
                        ])
    return alumnosTLeng


def get_persona_ejemploCrossJoin():
    # Genera el dataframe "persona" que contiene las siguientes columnas 
    # (en el orden mencionado):
        # 1. Nombre
        # 2. Nacionalidad
        
    # ... Creamos el dataframe vacío (sólo con los nombres de sus columnas)
    persona = pd.DataFrame(columns = ['Nombre', 'Nacionalidad'])
    # ... Agregamos cada una de las filas al dataFrame
    persona = pd.concat([persona,pd.DataFrame([
        {'Nombre' : 'Diego'   , 'Nacionalidad' : 'AR'    },
        {'Nombre' : 'Laura'   , 'Nacionalidad' : 'BR'    },
        {'Nombre' : 'Marina'  , 'Nacionalidad' : 'AR'    }
                                              ])
                        ])
    return persona


def get_persona_ejemplosJoin():
    # Genera el dataframe "persona" que contiene las siguientes columnas 
    # (en el orden mencionado):
        # 1. Nombre
        # 2. Nacionalidad
        
    # ... Creamos el dataframe vacío (sólo con los nombres de sus columnas)
    persona = pd.DataFrame(columns = ['Nombre', 'Nacionalidad'])
    # ... Agregamos cada una de las filas al dataFrame
    persona = pd.concat([persona,pd.DataFrame([
        {'Nombre' : 'Diego'   , 'Nacionalidad' : 'BR'    },
        {'Nombre' : 'Laura'   , 'Nacionalidad' : None    },
        {'Nombre' : 'Marina'  , 'Nacionalidad' : 'AR'    },
        {'Nombre' : 'Santiago', 'Nacionalidad' : 'UY'    }
                                              ])
                        ])
    return persona


def get_se_inscribe_en_ejemploMismosNombres():
    # Genera el dataframe "se_inscribe_en" que contiene las siguientes columnas 
    # (en el orden mencionado):
        # 1. LU
        # 2. Codigo_materia
        
    # ... Creamos el dataframe vacío (sólo con los nombres de sus columnas)
    se_inscribe_en = pd.DataFrame(columns = ['LU','Codigo_materia'])
    # ... Agregamos cada una de las filas al dataFrame
    se_inscribe_en = pd.concat([se_inscribe_en,pd.DataFrame([
        {'LU':'123/09','Codigo_materia': 1},
        {'LU':' 22/10','Codigo_materia': 1},
        {'LU':' 22/10','Codigo_materia': 2},
        {'LU':'344/09','Codigo_materia': 1}
                                              ])
                        ])
    return se_inscribe_en

def get_materia_ejemploMismosNombres():
    # Genera el dataframe "materia" que contiene las siguientes columnas 
    # (en el orden mencionado):
        # 1. Codigo_materia
        # 2. Nombre
        
    # ... Creamos el dataframe vacío (sólo con los nombres de sus columnas)
    materia = pd.DataFrame(columns = ['Codigo_materia','Nombre'])
    # ... Agregamos cada una de las filas al dataFrame
    materia = pd.concat([materia,pd.DataFrame([
        {'Codigo_materia': 1, 'Nombre':'Laboratorio de Datos'   },
        {'Codigo_materia': 2, 'Nombre':'Análisis II'   },
        {'Codigo_materia': 3, 'Nombre':'Probabilidad'   }
                                              ])
                        ])
    return materia


def get_nacionalidades():
    # Genera el dataframe "nacionalidades" que contiene las siguientes columnas 
    # (en el orden mencionado):
        # 1. IDN (Id Nacionalidad)
        # 2. Detalle
    
    # ... Creamos el dataframe vacío (sólo con los nombres de sus columnas)
    nacionalidades = pd.DataFrame(columns = ['IDN', 'Detalle'])
    # ... Agregamos cada una de las filas al dataFrame
    nacionalidades = pd.concat([nacionalidades,pd.DataFrame([
        {'IDN' : 'AR', 'Detalle' : 'Agentina'},
        {'IDN' : 'BR', 'Detalle' : 'Brasilera'},
        {'IDN' : 'CH', 'Detalle' : 'Chilena'}
                                                          ])
                        ])
    return nacionalidades

# =============================================================================
# DEFINICION DE FUNCIÓN DE IMPRESIÓN EN PANTALLA
# =============================================================================
# Imprime en pantalla en un formato ordenado:
    # 1. Consigna
    # 2. Cada dataframe de la lista de dataframes de entrada
    # 3. Query
    # 4. Dataframe de salida
def imprimirEjercicio(consigna, listaDeDataframesDeEntrada, consultaSQL, dataframeResultadoDeConsultaSQL):
    
    print("# -----------------------------------------------------------------------------")
    print("# Consigna: ", consigna)
    print("# -----------------------------------------------------------------------------")
    print()
    for i in range(len(listaDeDataframesDeEntrada)):
        print("# Entrada 0",i,sep='')
        print("# -----------")
        print(listaDeDataframesDeEntrada[i])
        print()
    print("# SQL:")
    print("# ----")
    print(consultaSQL)
    print()
    print("# Salida:")
    print("# -------")
    print(dataframeResultadoDeConsultaSQL)
    print()
    print("# -----------------------------------------------------------------------------")
    print("# -----------------------------------------------------------------------------")
    print()
    print()


# =============================================================================
# EJECUCIÓN MAIN
# =============================================================================

if __name__ == "__main__":
    main()
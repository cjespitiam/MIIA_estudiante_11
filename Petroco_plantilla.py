# -*- coding: utf-8 -*-
"""
Petroco - MIIA4102
Profesor: Andrés L. Medaglia (amedagli@uniandes.edu.co)
Instructor: Alfaima Solano
Asistente: Santiago Bobadilla
Created:  Aug. 31, 2021
Modified: Aug. 27, 2021
@author: amedagli
"""

# Importa las funciones de PuLP 
import pulp as lp

#------------------
#    Conjuntos 
#------------------
# Conjunto de pozos
Pozos = ['DELE B-1', 
         'EL MORRO-1', 
         'FLORENA A-5', 
         'FLORENA C-6', 
         'FLORENA N-2', 
         'FLORENA N-4 ST',
         'FLORENA-T8',
         'PAUTO J-6',
         'PAUTO M4',
         'PAUTO M-5',
         'PAUTO SUR B-1',
         'PAUTO SUR C-2',
         'PAUTO-1',
         'VOLCANERA A-1',
         'VOLCANERA C-2']

# Conjunto de tiempos - [2022,2029] 
Tiempos = range(2020,2030) #no incluye 2030

# Conjunto con todas las duplas (pozo,tiempo)
Pozo_x_Tiempo = [(pozo, tiempo) for pozo in Pozos for tiempo in Tiempos] 

#------------------
#    Parámetros 
#------------------
dataPozos = {# pozo: prod.minima, prod.moda, prod.máxima, operarios, generadores
             'DELE B-1':       [1,3,4,3,3],
             'EL MORRO-1':     [3,4,6,2,3],
             'FLORENA A-5':    [3,6,7,4,2],
             'FLORENA C-6':    [1,3,6,4,3],
             'FLORENA N-2':    [4,6,10,3,2],
             'FLORENA N-4 ST': [1,4,6,4,3],
             'FLORENA-T8':     [2,4,8,2,2],
             'PAUTO J-6':      [2,3,5,3,2],
             'PAUTO M4':       [3,5,7,3,3],
             'PAUTO M-5':      [1,4,8,4,2],
             'PAUTO SUR B-1':  [4,5,7,2,4],
             'PAUTO SUR C-2':  [4,6,8,3,3],
             'PAUTO-1':        [3,5,8,3,2],
             'VOLCANERA A-1':  [4,5,9,2,3],
             'VOLCANERA C-2':  [2,5,7,2,2]}

meta ={ # tiempo: meta (miles de barriles por día)
        2020:	3,
        2021:	4,
        2022:	5,
        2023:	4,
        2024:	5,
        2025:	3,
        2026:	5,
        2027:	4,
        2028:	4,
        2029:	6}

dataPozoTiempo ={ # (pozo, tiempo):   costo utilidad   
                ('DELE B-1',2020)       :[13,14],
                ('EL MORRO-1',2020)     :[21,81],
                ('FLORENA A-5',2020)    :[8,81],
                ('FLORENA C-6',2020)    :[7,93],
                ('FLORENA N-2',2020)    :[3,26],
                ('FLORENA N-4 ST',2020) :[23,77],
                ('FLORENA-T8',2020)     :[6,88],
                ('PAUTO J-6',2020)      :[2,13],
                ('PAUTO M4',2020)       :[9,57],
                ('PAUTO M-5',2020)      :[12,34],
                ('PAUTO SUR B-1',2020)  :[2,10],
                ('PAUTO SUR C-2',2020)  :[21,20],
                ('PAUTO-1',2020)        :[12,43],
                ('VOLCANERA A-1',2020)  :[16,51],
                ('VOLCANERA C-2',2020)  :[22,44],
                ('DELE B-1',2021)       :[25,55],
                ('EL MORRO-1',2021)     :[9,54],
                ('FLORENA A-5',2021)    :[15,70],
                ('FLORENA C-6',2021)    :[14,40],
                ('FLORENA N-2',2021)    :[23,65],
                ('FLORENA N-4 ST',2021) :[5,55],
                ('FLORENA-T8',2021)     :[10,24],
                ('PAUTO J-6',2021)      :[23,92],
                ('PAUTO M4',2021)       :[10,58],
                ('PAUTO M-5',2021)      :[3,26],
                ('PAUTO SUR B-1',2021)  :[16,72],
                ('PAUTO SUR C-2',2021)  :[11,39],
                ('PAUTO-1',2021)        :[2,57],
                ('VOLCANERA A-1',2021)  :[15,51],
                ('VOLCANERA C-2',2021)  :[8,45],
                ('DELE B-1',2022)       :[17,74],
                ('EL MORRO-1',2022)     :[22,23],
                ('FLORENA A-5',2022)    :[12,44],
                ('FLORENA C-6',2022)    :[11,31],
                ('FLORENA N-2',2022)    :[7,53],
                ('FLORENA N-4 ST',2022) :[12,71],
                ('FLORENA-T8',2022)     :[12,80],
                ('PAUTO J-6',2022)      :[17,22],
                ('PAUTO M4',2022)       :[14,59],
                ('PAUTO M-5',2022)      :[15,34],
                ('PAUTO SUR B-1',2022)  :[24,88],
                ('PAUTO SUR C-2',2022)  :[25,61],
                ('PAUTO-1',2022)        :[8,46],
                ('VOLCANERA A-1',2022)  :[14,33],
                ('VOLCANERA C-2',2022)  :[17,15],
                ('DELE B-1',2023)       :[19,75],
                ('EL MORRO-1',2023)     :[6,70],
                ('FLORENA A-5',2023)    :[23,18],
                ('FLORENA C-6',2023)    :[16,36],
                ('FLORENA N-2',2023)    :[14,44],
                ('FLORENA N-4 ST',2023) :[18,34],
                ('FLORENA-T8',2023)     :[6,22],
                ('PAUTO J-6',2023)      :[20,30],
                ('PAUTO M4',2023)       :[5,93],
                ('PAUTO M-5',2023)      :[7,68],
                ('PAUTO SUR B-1',2023)  :[25,12],
                ('PAUTO SUR C-2',2023)  :[13,75],
                ('PAUTO-1',2023)        :[12,56],
                ('VOLCANERA A-1',2023)  :[10,16],
                ('VOLCANERA C-2',2023)  :[6,11],
                ('DELE B-1',2024)       :[7,54],
                ('EL MORRO-1',2024)     :[8,58],
                ('FLORENA A-5',2024)    :[22,15],
                ('FLORENA C-6',2024)    :[17,29],
                ('FLORENA N-2',2024)    :[20,95],
                ('FLORENA N-4 ST',2024) :[17,32],
                ('FLORENA-T8',2024)     :[10,91],
                ('PAUTO J-6',2024)      :[6,29],
                ('PAUTO M4',2024)       :[6,72],
                ('PAUTO M-5',2024)      :[25,91],
                ('PAUTO SUR B-1',2024)  :[21,95],
                ('PAUTO SUR C-2',2024)  :[15,63],
                ('PAUTO-1',2024)        :[17,64],
                ('VOLCANERA A-1',2024)  :[12,54],
                ('VOLCANERA C-2',2024)  :[17,19],
                ('DELE B-1',2025)       :[10,84],
                ('EL MORRO-1',2025)     :[13,48],
                ('FLORENA A-5',2025)    :[9,10],
                ('FLORENA C-6',2025)    :[25,32],
                ('FLORENA N-2',2025)    :[17,92],
                ('FLORENA N-4 ST',2025) :[25,21],
                ('FLORENA-T8',2025)     :[5,62],
                ('PAUTO J-6',2025)      :[23,28],
                ('PAUTO M4',2025)       :[22,87],
                ('PAUTO M-5',2025)      :[7,97],
                ('PAUTO SUR B-1',2025)  :[25,88],
                ('PAUTO SUR C-2',2025)  :[19,88],
                ('PAUTO-1',2025)        :[4,66],
                ('VOLCANERA A-1',2025)  :[6,32],
                ('VOLCANERA C-2',2025)  :[5,2],
                ('DELE B-1',2026)       :[12,94],
                ('EL MORRO-1',2026)     :[3,45],
                ('FLORENA A-5',2026)    :[19,15],
                ('FLORENA C-6',2026)    :[4,40],
                ('FLORENA N-2',2026)    :[6,103],
                ('FLORENA N-4 ST',2026) :[21,9],
                ('FLORENA-T8',2026)     :[13,63],
                ('PAUTO J-6',2026)      :[8,25],
                ('PAUTO M4',2026)       :[15,94],
                ('PAUTO M-5',2026)      :[8,113],
                ('PAUTO SUR B-1',2026)  :[10,99],
                ('PAUTO SUR C-2',2026)  :[12,100],
                ('PAUTO-1',2026)        :[3,70],
                ('VOLCANERA A-1',2026)  :[12,29],
                ('VOLCANERA C-2',2026)  :[7,13],
                ('DELE B-1',2027)       :[23,104],
                ('EL MORRO-1',2027)     :[13,42],
                ('FLORENA A-5',2027)    :[16,21],
                ('FLORENA C-6',2027)    :[7,48],
                ('FLORENA N-2',2027)    :[4,94],
                ('FLORENA N-4 ST',2027) :[11,5],
                ('FLORENA-T8',2027)     :[20,63],
                ('PAUTO J-6',2027)      :[15,22],
                ('PAUTO M4',2027)       :[22,100],
                ('PAUTO M-5',2027)      :[21,129],
                ('PAUTO SUR B-1',2027)  :[19,110],
                ('PAUTO SUR C-2',2027)  :[14,113],
                ('PAUTO-1',2027)        :[15,74],
                ('VOLCANERA A-1',2027)  :[8,27],
                ('VOLCANERA C-2',2027)  :[19,20],
                ('DELE B-1',2028)       :[8,114],
                ('EL MORRO-1',2028)     :[23,39],
                ('FLORENA A-5',2028)    :[2,25],
                ('FLORENA C-6',2028)    :[23,56],
                ('FLORENA N-2',2028)    :[23,87],
                ('FLORENA N-4 ST',2028) :[20,10],
                ('FLORENA-T8',2028)     :[11,63],
                ('PAUTO J-6',2028)      :[20,19],
                ('PAUTO M4',2028)       :[8,107],
                ('PAUTO M-5',2028)      :[15,144],
                ('PAUTO SUR B-1',2028)  :[12,121],
                ('PAUTO SUR C-2',2028)  :[6,120],
                ('PAUTO-1',2028)        :[2,78],
                ('VOLCANERA A-1',2028)  :[5,33],
                ('VOLCANERA C-2',2028)  :[25,24],
                ('DELE B-1',2029)       :[14,124],
                ('EL MORRO-1',2029)     :[19,36],
                ('FLORENA A-5',2029)    :[22,32],
                ('FLORENA C-6',2029)    :[13,50],
                ('FLORENA N-2',2029)    :[20,80],
                ('FLORENA N-4 ST',2029) :[16,8],
                ('FLORENA-T8',2029)     :[9,64],
                ('PAUTO J-6',2029)      :[7,16],
                ('PAUTO M4',2029)       :[15,113],
                ('PAUTO M-5',2029)      :[10,160],
                ('PAUTO SUR B-1',2029)  :[5,132],
                ('PAUTO SUR C-2',2029)  :[2,115],
                ('PAUTO-1',2029)        :[16,82],
                ('VOLCANERA A-1',2029)  :[25,40],
                ('VOLCANERA C-2',2029)  :[18,32]
}


# Parámetros no indexados
presupuesto = 100 # Presupuesto máximo
maxProyectos = 12  # Máximo número de proyectos a realizar - restricción ambiental
maxOperarios = 4   # Máximo número de operarios por año
maxGeneradores = 4 # Máximo número de generadores por año

# Partir diccionarios por facilidad de modelamiento
# Parámetros indexados en pozos
(prodMin, prodModa, prodMax, operarios, generadores) = lp.splitDict(dataPozos)
# Parámetros indexados en (pozo,tiempo)
(costo, utilidad) = lp.splitDict(dataPozoTiempo)


#-------------------------------------
# Creación del objeto problema en PuLP
#-------------------------------------

# Crea el problema para cargarlo con la instancia    
problema = lp.LpProblem("Petroco", lp.LpMaximize)

#-----------------------------
#    Variables de Decisión
#-----------------------------

# Creación de variables x_it : pozo i se explora en tiempo t
#TO-DO-------------------------------------------
x = lp.LpVariable.dicts(           #Nombre
                                   #Conjunto
                                   #Límite inferior
                                   #Límite superior
                                 ) #Tipo de variable
#TO-DO--------------------------------------------

#-----------------------------
#    Función objetivo
#-----------------------------

# Crea la expresión de minimización de costos
problema += lp.lpSum([utilidad[(i,t)]*x[(i,t)] for (i,t) in Pozo_x_Tiempo]),\
           "Utilidad total"

#-----------------------------
#    Restricciones
#-----------------------------

# La inversión total no puede superar el presupuesto.
#TO-DO------------------------------------------------------

# Un proyecto se hace máximo una vez dentro del horizonte de planeación.
#TO-DO------------------------------------------------------

# Las metas de producción deben ser cumplidas.
for t in Tiempos:
    problema += \
    lp.lpSum([(prodMin[i]+prodModa[i]+prodMax[i])/3 * x[i,t] for i in Pozos])\
             >= meta[t],\
    "Compromiso - año %s"%t

# No se puede superar la cantidad de operarios disponibles en cada año.
for t in Tiempos:
    problema += \
    lp.lpSum([ operarios[i] * x[i,t] for i in Pozos]) <= maxOperarios,\
    "Límite operarios - año %s"%t

# No se puede superar la cantidad de generadores disponibles en cada año.
for t in Tiempos:
    problema += \
    lp.lpSum([ generadores[i] * x[i,t] for i in Pozos]) <= maxGeneradores,\
    "Límite generadores - año %s"%t

# No se debe exceder la cantidad de pozos perforados impuesta por el gobierno.
problema += lp.lpSum([x[i,t] for i,t in Pozo_x_Tiempo]) <= maxProyectos,\
            "Máximo de proyectos - ambiental"


#-----------------------------
#    Imprimir formato LP
#-----------------------------

# Escribe el problema en un archivo con formato LP 
problema.writeLP("Petroco.lp")

#-----------------------------
#    Invocar el optimizador
#-----------------------------
# Optimizar el modelo con CBC (default de PuLP)
problema.solve()
#problema.solve(GUROBI())

#-----------------------------
#    Imprimir resultados
#-----------------------------

# Imprimir estado final del optimizador
print("Estado (optimizador):",lp.LpStatus[problema.status],end='\n')

# Valor óptimo del portafolio de Petroco    
print("\nPetroco - Utilidad total = $", lp.value(problema.objective))

# Inversión   
print("\nPetroco - Inversión total = $",sum(costo[i,t]*x[i,t].value() \
                                        for i,t in Pozo_x_Tiempo),end='\n\n')

# Imprimir variables de programación de los proyectos
for v in problema.variables():
    if v.varValue > 0:
        print(v.name, "=", v.varValue)
        
# Imprimir producción cada año
print('\nProducción\tOperarios\tGeneradores')
for t in Tiempos:
    print(t,round(sum((prodMin[i]+prodModa[i]+prodMax[i])/3*x[i,t].value()\
                            for i in Pozos),1),\
                sum(operarios[i]*x[i,t].value() for i in Pozos),\
                sum(generadores[i]*x[i,t].value() for i in Pozos),sep='\t')

# Imprimir año de cada pozo 
print('\nAño')
for i in Pozos: 
    print(i,end='\t')
    for t in Tiempos:
        if(x[i,t].value()>0):
            print(t,end='')
    print()
    
    
    

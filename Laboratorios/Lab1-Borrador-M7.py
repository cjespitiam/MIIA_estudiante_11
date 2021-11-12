#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 08:21:19 2021

@author: cjespitiam
"""

# código

def cargar(ruta):
    
    nombre =[]
    
    with ruta as archivo:
        
        lista = [linea.rstrip() for linea in archivo]
        nombre=lista
    
    return lista 

edad_base = open("/Users/cjespitiam/Documents/MIIA/1_Herramientas_Computacionales_para_Analisis_de_Datos/HCAD/Lab 1/Archivos/edad.txt", "r")
genero_base = open("/Users/cjespitiam/Documents/MIIA/1_Herramientas_Computacionales_para_Analisis_de_Datos/HCAD/Lab 1/Archivos/genero.txt", "r")
estado_civil_base = open("/Users/cjespitiam/Documents/MIIA/1_Herramientas_Computacionales_para_Analisis_de_Datos/HCAD/Lab 1/Archivos/estado_civil.txt", "r")
escolaridad_base = open("/Users/cjespitiam/Documents/MIIA/1_Herramientas_Computacionales_para_Analisis_de_Datos/HCAD/Lab 1/Archivos/escolaridad.txt", "r")
estrato_base = open("/Users/cjespitiam/Documents/MIIA/1_Herramientas_Computacionales_para_Analisis_de_Datos/HCAD/Lab 1/Archivos/estrato.txt", "r")
region_base = open("/Users/cjespitiam/Documents/MIIA/1_Herramientas_Computacionales_para_Analisis_de_Datos/HCAD/Lab 1/Archivos/region.txt", "r")
promedio_base = open("/Users/cjespitiam/Documents/MIIA/1_Herramientas_Computacionales_para_Analisis_de_Datos/HCAD/Lab 1/Archivos/promedio.txt", "r")



edad=cargar(edad_base)
genero=cargar(genero_base)
estado_civil=cargar(estado_civil_base)
escolaridad=cargar(escolaridad_base)
estrato=cargar(estrato_base)
region=cargar(region_base)
promedio=cargar(promedio_base)

# código

# importación de paquetes necesarios

import numpy as np

from scipy import stats 

import matplotlib.pyplot as plt


# función que calcula la mediana de una lista de datos numéricos

edad = list(map(int, edad))

estrato = list(map(int, estrato))

mediana_edad = np.median(edad,0)

mediana_estrato = np.median(estrato,0)



# función que calcula la desviación de una lista de datos numéricos

desviacion_edad = np.std(edad,0)

desviacion_estrato = np.std(estrato,0)

# respuesta en texto (solo leeremos los primeros 300 caracteres de la respuesta)

pregunta_negocio = '¿Cual de los dos grupos es el mas adecuado para distribuir las becas disponibles de la universidad?'

pregunta_analytics = '¿Que metodologia es la mas apta, la mas eficiente y la mas equilibrada para asignar las becas de la universidad?'




#Codigo

becas = input("¿Cuantas becas hay disponibles? :")

becas=int(becas)

edad_min = input("¿Cual es la edad minima? :")

edad_min=int(edad_min)

edad_max = input("¿Cual es la edad maxima? :")

edad_max=int(edad_max)

indicador = input("Escoja un numero para el estudio (1.Genero 2.Estrato 3.Region) :") #1.Genero 2.Estrato 3.Region

indicador = int(indicador)

proporcion=input("¿Cual es el porcentaje deseado por grupo? (Escriba el numero sin el simbolo de porcentaje(%) :")

proporcion=float(proporcion)/100

#Datos como matriz

i=0
id_datos=[]

while i<500:
    id_datos.append(i)
    i=i+1

matrix_aux = [id_datos,edad,genero,estado_civil,escolaridad,estrato,region,promedio] 

matriz_datos = np.array(matrix_aux)

# Filtro Edad

i=0
categoria_vector=[]

while i < 500:
    if int(matriz_datos[1,i]) >= edad_min and int(matriz_datos[1,i]) <= edad_max:
        categoria_vector.append(matriz_datos[:,i])
        i=i+1
    else:
        i=i+1
        
matriz_datos = np.array(categoria_vector) 

# Calculo la proporcion por estrato que debe llevar cada categoria   



if indicador == 1:
    categoria_array = np.array(matriz_datos[:,2])
    var = 2
elif indicador == 2:
    categoria_array = np.array(matriz_datos[:,5])     
    var = 5
elif indicador == 3:
    categoria_array = np.array(matriz_datos[:,6])   
    var = 6
else:
    print("Numero de Categoria invalido")       
 

(categoria_unicos, count_categoria) = np.unique(categoria_array, return_counts=True)

prop_categoria = []

for i in count_categoria:
    prop_categoria.append(np.floor(i*proporcion))


#Se crea matriz por categoria

i=0
n=1

    
for k in categoria_unicos:
    globals()['llave_%s' % n] = []
    
    while i < len(categoria_array):
        if matriz_datos[i,var] == k:
            globals()['llave_%s' % n].append(matriz_datos[i,:])
            i=i+1
        else:
            i=i+1
    globals()['matriz_%s' % n] = np.array(globals()['llave_%s' % n])  
    globals()['matriz_%s' % n] = globals()['matriz_%s' % n][globals()['matriz_%s' % n][:,7].argsort()]      
    n=n+1
    i=0          
    

#Calculo de ganadores
    

ganadores_becas=[]

p=1
for k in categoria_unicos:
    
    globals()['j_%s' % p] = -1
    p=p+1

while len(ganadores_becas)<becas:
    
    n=1
    m=0

    
    for k in categoria_unicos:
        
        globals()['conteo_%s' % n] = 0
    
        while globals()['conteo_%s' % n] < prop_categoria[m] and len(ganadores_becas)<becas:
            if globals()['conteo_%s' % n] < len(globals()['matriz_%s' % n]):
                ganadores_becas.append(globals()['matriz_%s' % n][globals()['j_%s' % n],:])
                globals()['conteo_%s' % n]=globals()['conteo_%s' % n]+1
                globals()['j_%s' % n]=globals()['j_%s' % n]-1
            else:
                globals()['conteo_%s' % n]=globals()['conteo_%s' % n]+1
                globals()['j_%s' % n]=globals()['j_%s' % n]-1
        
        globals()['conteo_%s' % n] = 0
        n=n+1
        m=m+1        
    

matriz_ganadores_3 = np.array(ganadores_becas) 

edad_3 =[]
estrato_3 =[]
region_3 = []
promedio_3 =[]

for i in matriz_ganadores_3:
    edad_3.append(int(i[1]))
    
for i in matriz_ganadores_3:
    estrato_3.append(int(i[5]))

for i in matriz_ganadores_3:
    region_3.append(i[6])

for i in matriz_ganadores_3:
    promedio_3.append(float(i[7]))
    
    
intervalos = range(min(edad_3), max(edad_3) )

plt.hist(x=edad_3, bins=intervalos, color='#F2AB6D', rwidth=1.85)
plt.title('Histograma de edades')
plt.xlabel('Edades')
plt.ylabel('Frecuencia')
plt.xticks(intervalos)

plt.show()        


plt.scatter(edad_3,promedio_3)
plt.title('Dispersion de edad Vs Promedio Grupo 1')

plt.show()

plt.scatter(promedio_3,estrato_3)
plt.title('Dispersion de estratos Vs Promedio Grupo 1')

plt.show()

plt.hist(x=region_3, color='#F2AB6D', rwidth=1.85)
plt.title('Histograma de Regiones')
plt.xlabel('Regiones')
plt.ylabel('Frecuencia')

plt.show()






    
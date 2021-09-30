#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 16:35:02 2021

@author: cjespitiam
"""

def cargar(ruta):
    
    nombre =[]
    
    with ruta as archivo:
        
        lista = [linea.rstrip() for linea in archivo]
        nombre=lista
    
    return nombre 

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

import matplotlib.pyplot as plt


# función que calcula la mediana de una lista de datos numéricos

edad = list(map(int, edad))

estrato = list(map(int, estrato))

mediana_edad = np.median(edad,0)

mediana_estrato = np.median(estrato,0)

print("Mediana de Edad:",mediana_edad)

print("Mediana de Estrato:",mediana_estrato)


# función que calcula la desviación de una lista de datos numéricos

desviacion_edad = np.std(edad,0)

desviacion_estrato = np.std(estrato,0)

print("Desviación de Edad:",desviacion_edad)

print("Desviación de Estrato:",desviacion_estrato)

# código
 
becas = 40 #input("Cuantas becas hay disponibles: ")

becas = int(becas)   


#Datos como matriz

i=0
j=0
id_datos=[]
llave=[]

while i<500:
    id_datos.append(i)
    i=i+1
    
while j<500:
    llave.append(region[j]+'-'+genero[j])
    j=j+1    
    
    
llave_array = np.array(llave)   

(llave_unicos, count_llave) = np.unique(llave_array, return_counts=True)    

matrix_aux = [id_datos,edad,genero,estado_civil,escolaridad,estrato,region,promedio,llave] 

matriz_datos = np.array(matrix_aux)

#Matriz por estrato

i=0
n=1


for k in llave_unicos:
    globals()['llave_%s' % n] = []
    
    while i < 500:
        if matriz_datos[8,i] == k:
            globals()['llave_%s' % n].append(matriz_datos[:,i])
            i=i+1
        else:
            i=i+1
    globals()['matriz_%s' % n] = np.array(globals()['llave_%s' % n])  
    globals()['matriz_%s' % n] = globals()['matriz_%s' % n][globals()['matriz_%s' % n][:,7].argsort()]      
    n=n+1
    i=0         
    

    


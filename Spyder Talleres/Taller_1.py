#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 18:35:28 2021

@author: cjespitiam
"""

########## CASO 1

# No modifiques esta celda

lista_meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

cuarto_trimestre = [lista_meses[-3],lista_meses[-2],lista_meses[-1]]

lista_ventas = [20,21,22,20,21,27]

# No modifiques esta celda

mes_a_actualizar = 4
ventas_mes_a_actualizar = 18

# YOUR CODE HERE
lista_ventas[mes_a_actualizar-1] = ventas_mes_a_actualizar

# No modifiques esta celda

n = 3

lista_ventas.sort(reverse=True)

bucle=range(n)

mejores_ventas = []

for i in bucle:
    mejores_ventas.append(lista_ventas[i])
    print(mejores_ventas)  

######## CASO 2 

nombres = ["Sara", "Juan", "Alberto", "Ana", "Enrique", "Lola"]

nombres.sort()

largo = len(nombres)

import math

bucle_1 = range(math.ceil(largo/2))
bucle_2 = range(math.floor(largo/2))
i_inverso = -1

primera_mitad = []
segunda_mitad = []

for i in bucle_1:
    primera_mitad.append(nombres[i])

for i in bucle_2:
    segunda_mitad.append(nombres[i_inverso])
    i_inverso = i_inverso -1

segunda_mitad.sort()

######## CASO 3

lista_abecedario = ["a", "b", "c", ["d", "e", ["f", "g"]]]

lista_abc = [lista_abecedario[0],lista_abecedario[1],lista_abecedario[2]]

lista_de = [lista_abecedario[3][0],lista_abecedario[3][1]]

lista_fgh = [lista_abecedario[3][2][0],lista_abecedario[3][2][1],"h"]

lista_a_j = lista_abc + lista_de + lista_fgh + ["i","j"]


######## CASO 4


tupla_primos =  (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)

a_buscar = 73

indice = tupla_primos.index(a_buscar)

lim_inferior = 3
lim_superior = 53

tupla_secuencia = tupla_primos[tupla_primos.index(lim_inferior):tupla_primos.index(lim_superior)+2:2]

######## CASO 4

pedidos_semana_1 = (3,2)
pedidos_semana_2 = (2,4)
pedidos_semana_3 = (1,1)

tupla_pedidos = (pedidos_semana_1,pedidos_semana_2,pedidos_semana_3)

s = 2

total_pedidos_semana_s = sum(tupla_pedidos[s-1])

######## CASO 5

dicc_meses = {"Enero":31,
              "Febrero":28,
              "Marzo": 31,
              "Abril": 30,
              "Mayo":31,
              "Julio":31,
              "Agosto":31,
              "Septiembre":30,
              "Noviembre":30}

dicc_meses["Junio"]=30
dicc_meses["Octubre"]=31
dicc_meses["Diciembre"]=31

###### CASO 6

import numpy as np

matriz_0 = np.array([[0,1,0,1,1],[0,0,0,0,1],[1,0,0,1,0],[1,0,1,0,1]])

var = matriz_0[0,0]

matriz={}

i=0
j=0

while i <= 3:
    j=0
    while j <= 4:
        if matriz_0[i,j] == 1:
            matriz[(i+1,j+1)]= 1
            j=j+1
        else:
            j=j+1
    i=i+1
    
h = 5
t = 2

prediccion_familia = matriz.get((t,h),0) 

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

bucle_1 = range()
bucle_2 = range()

base_1 = 

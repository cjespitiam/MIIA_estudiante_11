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

print("Mediana de Edad:",mediana_edad)

print("Mediana de Estrato:",mediana_estrato)


# función que calcula la desviación de una lista de datos numéricos

desviacion_edad = np.std(edad,0)

desviacion_estrato = np.std(estrato,0)

print("Desviación de Edad:",desviacion_edad)

print("Desviación de Estrato:",desviacion_estrato)

# respuesta en texto (solo leeremos los primeros 300 caracteres de la respuesta)

pregunta_negocio = '¿Cual de los dos grupos es el mas adecuado para distribuir las becas disponibles de la universidad?'

pregunta_analytics = '¿Que metodologia es la mas apta, la mas eficiente y la mas equilibrada para asignar las becas de la universidad?'

# código

import numpy as np
 
becas = input("Cuantas becas hay disponibles: ")

becas = int(becas)   
    
# Calculo la proporcion por estrato que debe llevar cada categoria    
       
estrato_array = np.array(estrato)   

(estratos_unicos, count_estrato) = np.unique(estrato_array, return_counts=True)

prop_estrato = []

for i in count_estrato:
    prop_estrato.append(np.floor(i*0.02))
    
    
#Datos como matriz

i=0
id_datos=[]

while i<500:
    id_datos.append(i)
    i=i+1

matrix_aux = [id_datos,edad,genero,estado_civil,escolaridad,estrato,region,promedio] 

matriz_datos = np.array(matrix_aux)
    
#Matriz por estrato

i=0
estrato_1_vector=[]

while i < 500:
    if matriz_datos[5,i] == "1":
        estrato_1_vector.append(matriz_datos[:,i])
        i=i+1
    else:
        i=i+1
        
estrato_1_matriz = np.array(estrato_1_vector)  



i=0
estrato_2_vector=[]

while i < 500:
    if matriz_datos[5,i] == "2":
        estrato_2_vector.append(matriz_datos[:,i])
        i=i+1
    else:
        i=i+1
        
estrato_2_matriz = np.array(estrato_2_vector)  



i=0
estrato_3_vector=[]

while i < 500:
    if matriz_datos[5,i] == "3":
        estrato_3_vector.append(matriz_datos[:,i])
        i=i+1
    else:
        i=i+1
        
estrato_3_matriz = np.array(estrato_3_vector)  



i=0
estrato_4_vector=[]

while i < 500:
    if matriz_datos[5,i] == "4":
        estrato_4_vector.append(matriz_datos[:,i])
        i=i+1
    else:
        i=i+1
        
estrato_4_matriz = np.array(estrato_4_vector)  



i=0
estrato_5_vector=[]

while i < 500:
    if matriz_datos[5,i] == "5":
        estrato_5_vector.append(matriz_datos[:,i])
        i=i+1
    else:
        i=i+1
        
estrato_5_matriz = np.array(estrato_5_vector)        
        
    
# Odenar las Matrices de estratos por promedios

Id_columna = 7

estrato_1_matriz_ord = estrato_1_matriz[estrato_1_matriz[:,Id_columna].argsort()]

estrato_2_matriz_ord = estrato_2_matriz[estrato_2_matriz[:,Id_columna].argsort()]

estrato_3_matriz_ord = estrato_3_matriz[estrato_3_matriz[:,Id_columna].argsort()]

estrato_4_matriz_ord = estrato_4_matriz[estrato_4_matriz[:,Id_columna].argsort()]

estrato_5_matriz_ord = estrato_5_matriz[estrato_5_matriz[:,Id_columna].argsort()]


asignadas=0
conteo_E1 = 0
conteo_E2 = 0
conteo_E3 = 0
conteo_E4 = 0
conteo_E5 = 0
ganadores_becas=[]
j_1=-1
j_2=-1
j_3=-1
j_4=-1
j_5=-1


while asignadas < becas:
    if conteo_E1 < prop_estrato[0] : #and estrato_1_matriz_ord[j_1,0] not in ganadores_becas[:,0]:
        ganadores_becas.append(estrato_1_matriz_ord[j_1,:])
        asignadas=asignadas+1
        conteo_E1=conteo_E1+1
        j_1=j_1-1
    elif conteo_E2 < prop_estrato[1] : # and estrato_2_matriz_ord[j_2,0] not in ganadores_becas[:,0]:    
        ganadores_becas.append(estrato_2_matriz_ord[j_2,:])
        asignadas=asignadas+1
        conteo_E2=conteo_E2+1    
        j_2=j_2-1
    elif conteo_E3 < prop_estrato[2] : # and estrato_3_matriz_ord[j_3,0] not in ganadores_becas[:,0]:    
        ganadores_becas.append(estrato_3_matriz_ord[j_3,:])
        asignadas=asignadas+1
        conteo_E3=conteo_E3+1     
        j_3=j_3-1
    elif conteo_E4 < prop_estrato[3] : # and estrato_4_matriz_ord[j_4,0] not in ganadores_becas[:,0]:    
        ganadores_becas.append(estrato_4_matriz_ord[j_4,:])
        asignadas=asignadas+1
        conteo_E4=conteo_E4+1   
        j_4=j_4-1
    elif conteo_E5 < prop_estrato[4] : # and estrato_5_matriz_ord[j_5,0] not in ganadores_becas[:,0]:    
        ganadores_becas.append(estrato_5_matriz_ord[j_5,:])
        asignadas=asignadas+1
        conteo_E5=conteo_E5+1
        j_5=j_5-1
    else:
        conteo_E1 = 0
        conteo_E2 = 0
        conteo_E3 = 0
        conteo_E4 = 0
        conteo_E5 = 0   
        
matriz_ganadores_1 = np.array(ganadores_becas)

# código 

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
    
prop = int(np.floor(becas/len(llave_unicos)))    



n=1
ganadores_becas=[]


for k in llave_unicos:
    
    globals()['conteo_%s' % n] = 0
    globals()['j_%s' % n] = -1

    while globals()['conteo_%s' % n] < prop:
        if globals()['conteo_%s' % n] < len(globals()['matriz_%s' % n]):
            ganadores_becas.append(globals()['matriz_%s' % n][globals()['j_%s' % n],:])
            globals()['conteo_%s' % n]=globals()['conteo_%s' % n]+1
            globals()['j_%s' % n]=globals()['j_%s' % n]-1
        else:
            globals()['conteo_%s' % n]=globals()['conteo_%s' % n]+1
            globals()['j_%s' % n]=globals()['j_%s' % n]-1
        
    n=n+1    
    
matriz_ganadores_2 = np.array(ganadores_becas) 

edad_1 =[]
edad_2 =[]
estrato_1 =[]
estrato_2 =[]
region_1 = []
region_2 = []
promedio_1=[]
promedio_2=[]

for i in matriz_ganadores_1:
    edad_1.append(int(i[1]))

for i in matriz_ganadores_2:
    edad_2.append(int(i[1]))
    
for i in matriz_ganadores_1:
    estrato_1.append(int(i[5]))

for i in matriz_ganadores_2:
    estrato_2.append(int(i[5]))

for i in matriz_ganadores_1:
    region_1.append(i[6])

for i in matriz_ganadores_2:
    region_2.append(i[6])

for i in matriz_ganadores_1:
    promedio_1.append(float(i[7]))

for i in matriz_ganadores_2:
    promedio_2.append(float(i[7]))  
    
intervalos = range(min(edad_1), max(edad_1) )

plt.hist(x=edad_1, bins=intervalos, color='#F2AB6D', rwidth=1.85)
plt.title('Histograma de edades Grupo 1')
plt.xlabel('Edades')
plt.ylabel('Frecuencia')
plt.xticks(intervalos)

plt.show()    

intervalos = range(min(edad_2), max(edad_2) )

plt.hist(x=edad_2, bins=intervalos, color='#F2AB6D', rwidth=1.85)
plt.title('Histograma de edades Grupo 2')
plt.xlabel('Edades')
plt.ylabel('Frecuencia')
plt.xticks(intervalos)

plt.show()    

plt.scatter(edad_1,promedio_1)
plt.title('Dispersion de edad Vs Promedio Grupo 1')

plt.show()

plt.scatter(edad_2,promedio_2)
plt.title('Dispersion de edad Vs Promedio Grupo 2')

plt.show()

plt.scatter(promedio_1,estrato_1)
plt.title('Dispersion de estratos Vs Promedio Grupo 1')

plt.show()

plt.scatter(promedio_2,estrato_2)
plt.title('Dispersion de estratos Vs Promedio Grupo 2')

plt.show()


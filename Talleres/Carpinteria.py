#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 13:01:07 2021

@author: cjespitiam
"""

import numpy as np
import pandas as pd

def importar_e_indexar():
    
    base = pd.read_stata("Archivos/pooled_data_public.dta")
    base = base.set_index("id")
    
    return base




def indice_sencillo_a_multiple():
    
    data = importar_e_indexar()
    
    data.reset_index(drop=False, inplace = True)
    
    data["index"] = data.index
    
    index = pd.MultiIndex.from_arrays([data["index"],data["country_code"]])
    
    data = pd.DataFrame(data = data, index = index)
    
    data_drop = data.drop(["index", "country_code","id"],axis=1)
    
    return data_drop

data2 = indice_sencillo_a_multiple()


## AUTO-CALIFICADOR

# Base variables
import inspect

nombre_columnas = ['country_name', 'weight', 'weight_pop', 'pop', 'recordeddate', 'genero', 'edad', 'educ', 'estcivil', 'nrhogar', 'nrhogar_antes', 'hayninhos', 'ninos_5', 'nrninhos', 'matriculados', 'esc_publica', 'grado', 'haymayores', 'diasmercado', 'lugarmercado', 'comprotodo', 'nocompra_pan', 'nocompra_vegetal', 'nocompra_carne', 'nocompra_envasados', 'nocompra_bebidas', 'nocompra_limpieza', 'nocompra_medicinas', 'nocompra_otro', 'nrnegocios', 'esperarfila', 'subaprecios', 'hambre', 'menos_saludable', 'vivienda', 'probvivienda', 'probvivienda_prox', 'ayuda_alquiler', 'sufialimento', 'sufirecursos', 'gasto_emergencia', 'monto_gasto', 'pre_cash', 'new_cash', 'coima', 'tiene_banco', 'tiene_tarjdebito', 'tiene_segsaludpub', 'tiene_segsaludpriv', 'recibeprestamos', 'darprestamos', 'remesas_enero', 'remesas_origen', 'remesas_persona', 'recibio_remesas', 'lm_perdioempleo', 'lm_cerronegocio_gob', 'lm_cerronegocio_dem', 'lm_asistmedica', 'lm_perdioingrarriendo', 'lm_dejoasistencia', 'lm_freq', 'recibio_ayudaemp', 'compromiso_futurotrabajo', 'empleo_formal', 'actividad_empleado', 'actividad_negocio', 'actividad_estudio', 'trabajocasa', 'diastrabajo', 'horastrabajo', 'sector', 'redujo_ingreso', 'ingreso_jan2020', 'ingreso_apr2020', 'retorno_ingreso', 'sintoma_ninguno', 'sintoma_garganta', 'sintoma_gripe', 'sintoma_sarpullido', 'sintoma_fiebre', 'sintoma_tos', 'conoce_sintomas', 'infectados_sinsintomas', 'sinsintomas_contagiar', 'visito_trabajo', 'visito_hospital', 'visito_mercado', 'visito_banco', 'visito_amigos', 'visito_familiares', 'visito_ejercitar', 'visito_iglesia', 'comotransmite', 'sabe_comotransmite', 'distsoc', 'recom_trabajo', 'recom_hospital', 'recom_mercado', 'recom_banco', 'recom_amigos', 'recom_familiares', 'recom_ejercicio', 'recom_iglesia', 'haceds_hogar', 'haceds_vecinos', 'haceds_jovenes', 'haceds_mayores', 'haceds_otropais', 'haceds_emplmercados', 'medios_noti_redessociales', 'medios_noti_chat', 'medios_noti_periodicos', 'medios_noti_tv', 'medios_noti_radio', 'medios_covid_redessociales', 'medios_covid_chat', 'medios_covid_periodicos', 'medios_covid_tv', 'medios_covid_radio', 'nps_medio_redessoc', 'nps_medio_sms', 'nps_medio_periodico', 'nps_medio_tv', 'nps_medio_radio', 'nps_medio_website', 'nps_medio_otro']
tipo_columnas = ['dtype[object_]', 'dtype[float32]', 'dtype[float32]', 'dtype[float64]', 'dtype[object_]', 'CategoricalDtype', 'dtype[int16]', 'CategoricalDtype', 'CategoricalDtype', 'dtype[int8]', 'dtype[int8]', 'CategoricalDtype', 'CategoricalDtype', 'dtype[float64]', 'dtype[float64]', 'CategoricalDtype', 'dtype[float64]', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'dtype[float32]', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'dtype[float64]', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'dtype[float64]', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'dtype[int8]', 'dtype[int8]', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'dtype[float32]', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'dtype[object_]', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype', 'CategoricalDtype']

# Caso 1: no existe la función.
try:
    source = inspect.getsource(indice_sencillo_a_multiple)
    assert type(indice_sencillo_a_multiple) == type(lambda:None)
except:
    raise NotImplementedError("No existe una función llamada indice_sencillo_a_multiple.",)
    
# Caso 2: la función es interrumpida por errores durante su ejecución.
try:
    resultado = indice_sencillo_a_multiple()
except:
    raise RuntimeError("Tu función produce un error al ejecutarse.")

# Caso 3: no retorna un DataFrame
assert type(resultado) == pd.DataFrame, f"Tu función debe retornar un valor de tipo {pd.DataFrame.__name__}."

# Caso 4: no ejecuta la función importar_e_indexar
assert source.find("importar_e_indexar()") >= 0, "Tu código no hace referencia a la función importar_e_indexar. Asegurate de ejecutarla en tu función."

# Caso 5: retorna el dataframe con la columna 'id'
assert "id" not in resultado.columns, "Tu función retorna un DataFrame que incluye la columna 'id'. Esta columna debes haberla convertido en el index sencillo del DataFrame."

# Caso 6: retorna el dataframe con la columna 'country_code'
assert "country_code" not in resultado.columns, "Tu función retorna un DataFrame que incluye la columna 'country_code'. Esta columna debes haberla unido al index del DataFrame para formar un índice múltiple."

# Caso 7: retorna un dataframe con cantidad de columnas errada
assert resultado.shape[1] == 127, "Tu función retorna un DataFrame con cantidad de columnas errada."

# Caso 8: devuelve un dataframe cuyas columnas tienen nombre distinto de lo esperado
assert [*resultado.columns] == nombre_columnas, "Tu función retorna un DataFrame con columnas cuyos nombres no coinciden con los de los datos del archivo."

# Caso 9: devuelve un dataframe cuyas columnas tienen tipo distinto de lo esperado
assert [i.__class__.__name__ for i in resultado.dtypes] == tipo_columnas, "Tu función retorna un DataFrame con columnas cuyos tipos no coinciden con los de los datos del archivo."

# Caso 10: devuelve un dataframe con cantidad de filas errada
assert resultado.shape[0] == 230509, "Tu función retorna un DataFrame con cantidad de filas errada."

# Caso 11: devuelve un dataframe con indice no multiple
assert type(resultado.index) == pd.MultiIndex, "Tu función retorna un DataFrame con índice no múltiple."

# Caso 12: devuelve un dataframe con primer nivel de indice multiple del mismo tipo que por defecto ('int64')
assert resultado.index.get_level_values(0).dtype.name != 'int64', "Tu función retorna un DataFrame con índice múltiple cuyo primer nivel es del mismo tipo que el que se crea por defecto en pandas. Asegurate de estar asignando la columna 'id' al índice."

# Caso 13: devuelve un dataframe con primer nivel de indice multiple de tipo errado
assert resultado.index.get_level_values(0).dtype.name == 'float64', "Tu función retorna un DataFrame con índice múltiple cuyo primer nivel es de tipo distinto del esperado. Asegurate de estar usando la columna 'id' sin editarla."

# Caso 14: devuelve un dataframe con segundo nivel de indice multiple de tipo errado
assert resultado.index.get_level_values(1).dtype.name == 'category', "Tu función retorna un DataFrame con índice múltiple cuyo segundo nivel es de tipo distinto del esperado. Asegurate de estar usando la columna 'country_code' sin editarla."

# Caso 15: el multiíndice no tiene el nombre de la columna 'id' y 'country_code'
assert [*resultado.index.names] == ['id', 'country_code'], "Tu función retorna un DataFrame con índice de nombres distintos de las columna 'id' y 'country_code'."

# Caso 16: primera o última posicion del índice distintas de lo esperado
assert resultado.index[0] == (1000060.0, 'Bahamas'), "Tu función retorna un DataFrame que es errado por lo menos en la primera posición de su índice"
assert resultado.index[len(resultado.index) - 1] == (17003990.0, 'Uruguay'), "Tu función retorna un DataFrame que es errado por lo menos en la última posición de su índice"


# Mensaje de felicitaciones
print("Felicidades, realizaste este ejercicio correctamente.")
    

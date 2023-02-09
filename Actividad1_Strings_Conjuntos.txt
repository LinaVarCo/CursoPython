'''
Punto 1: Strings
Se tiene el siguiente objeto

variable = 'appname=pythonbancolombia.corp'

a. Se requiere crear una variable que almacene el valor de appname, pythonbancolombia y corp: utilizando slice
b. Se requiere identificar el índice de '=', '.' y '/'
'''
# Variable de inicio
var = 'appname=pythonbancolombia.corp'

# Punto 1.a
var_a = [var[:7], var[8:25], var[26:30]]
print('''-----------------------------------------------------------------------------------
 Solución punto 1.a: crear una variable que almacene el valor de appname, pythonbancolombia y corp''', 
'\n',var_a, '\n')

# Punto 1.b
var_b = [var.find('='), var.find('.'), var.find('/')]
print('''-----------------------------------------------------------------------------------
 Solución punto 1.b: Identificar el índice de "=", "." y "/"''','\n', var_b, 
'\n', 'Nota: La solución implementada devuelve "-1" para los caracteres no localizados', '\n')

'''
Punto 2: Conjuntos

Se tiene el siguiente objeto

elementos = '1 2 3 4 5 6 7 8 8 8 8 8'

A partir del anterior string, construir una lista con los números únicos
'''


# Variable de inicio
elementos = '1 2 3 4 5 6 7 8 8 8 8 8'
elementos_limpios = elementos.replace(" ", "")
var_set = set(elementos_limpios)
var_list = list(var_set)
var_list.sort()
#print(var_set)
print('''-----------------------------------------------------------------------------------
 Solución punto 2: Construir una lista con los números únicos del string entregado''', '\n', var_list)

'''
Punto 3: Del siguiente string, se debe crear una lista con todos los carácteres (sin distinguir mayusculas y minúsculas) ordenados alfabeticamente.

texto = """

Hola, El dia de hoy es 7 de FEBRERO del 2023. Estamos realizaNDO un

rePAso de lo que podemoS haCEr en PythoN.
'''

# Variable de inicio
texto = """

Hola, El dia de hoy es 7 de FEBRERO del 2023. Estamos realizaNDO un

rePAso de lo que podemoS haCEr en PythoN."""

minusculas = texto.lower()
string_limpio1 = minusculas.strip()
string_limpio2 = minusculas.replace(" ", "")
minusculas_set = set(string_limpio2)
minusculas_list = list(minusculas_set)
minusculas_list.sort()
print('''-----------------------------------------------------------------------------------
 Solución punto 3: crear una lista con todos los carácteres del string dado 
 (sin distinguir mayusculas y minúsculas) ordenados alfabeticamente''', '\n', minusculas_list)
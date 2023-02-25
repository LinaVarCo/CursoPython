# Ejercicios

# 1. Convertir el siguiente objeto en un json e imprimirlo utilizando una
# identacion de 2 espacios:

carros = [{
    'referencia': 'Rav4',
    'marca': 'Toyota',
    'cilindraje': '2500 cc',
    'modelo': 2020,
    'precio': 32000,
    'nuevo': False
    },
    {
    'referencia': 'Niro',
    'marca': 'KIA',
    'cilindraje': '1600 cc',
    'precio': 15000,
    'nuevo': True
    }]

import json as js
import jsonlines as jsl
from pprint import pprint as pp

carros_json = js.dumps(carros, indent=2)
print('\n', '----------Ejercicio 1.----------', '\n')
print(carros_json)



# 2. A partir del archivo 20_ejercicio.json obtener responder las siguientes
data = []
with jsl.open('D:/livargas/Cursos/Python Intermedio/CursoPython/20_ejercicio.json') as file:
    for linea in file:
        data.append(linea)
# preguntas:
# a. Cuál es el nombre de la persona que mayor balance tiene?
mayor_balance = 0
for elemento in data:
    valor_balance = float(elemento.get('balance').replace('$','').replace(',','')) 
    if valor_balance > mayor_balance:
        mayor_balance = valor_balance
        nombre = elemento.get('name')
print('\n', '----------Ejercicio 2.a.----------', '\n')
print(f'El nombre de la persona con mayor  balance es {nombre}')

# b. Cuántos hombres y mujeres hay en el archivo?
conteo_hombres = 0
conteo_mujeres = 0
conteo_otro_gender = 0
for elemento in data:
    conteo_hombres += (1 if elemento.get('gender') == 'male' else 0)
    conteo_mujeres += (1 if elemento.get('gender') == 'female' else 0)
    conteo_otro_gender += (1 if (elemento.get('gender') != 'male' and elemento.get('gender') != 'female') else 0)
print('\n', '----------Ejercicio 2.b.----------', '\n')
print(f'''En el archivo hay:
{conteo_hombres} hombres
{conteo_mujeres} mujeres
y {conteo_otro_gender} personas de otros géneros''')


# c. El usuario Elsie Lowery se encuentra activo?
print('\n', '----------Ejercicio 2.c.----------', '\n')
for elemento in data:
    if elemento.get('name') == 'Elsie Lowery' and elemento.get('isActive'):
        print('El usuario está activo')
    elif elemento.get('name') == 'Elsie Lowery' and not elemento.get('isActive'):
        print('El usuario está inactivo')

# d. Cuál es la frecuencia de repetición de las frutas
frutas = {}
for elemento in data:
    fruta = elemento.get('favoriteFruit')
    frutas[fruta] = frutas.get(fruta, 0) + 1
print('\n', '----------Ejercicio 2.d.----------', '\n')
pp(frutas)

# e. Cuál es el promedio de edad de los usuarios
suma_edades = 0
conteo_usuarios = 0
for elemento in data:
    suma_edades += elemento.get('age')
    conteo_usuarios += 1
print('\n', '----------Ejercicio 2.e.----------', '\n')
print(f'el promedio de edad de los usuarios es {suma_edades/conteo_usuarios}')    

# 3. Almacenar la información del archivo anterior en un archivo nuevo donde
# solo se almacenen las siguientes llaves, tener en cuenta que debe ser un
# archivo json estándar:
# idx, isActive, name, email.
print('\n', '----------Ejercicio 3.----------', '\n')
print('Ver archivo creado en la ruta indicada, no olvide especificar la ruta donde desea crearlo')
nuevo_diccionario = {}
nueva_lista = []
for elemento in data:
    lista_claves = elemento.keys()
    for clave in lista_claves:
        if clave == 'idx' or clave == 'isActive' or clave == 'name' or clave == 'email':
            nuevo_diccionario[clave] = elemento.get(f'{clave}')
    nueva_lista.append(nuevo_diccionario)
#pp(len(nueva_lista))
#pp(nueva_lista)
with open('D:/livargas/Cursos/Python Intermedio/CursoPython/nuevo_archivo.json', 'w') as f:
    js.dump(nueva_lista, f)



"""
Ejercicio 1.

Por medio de la libreria random, podemos crear valores numéricos aleatorios, 
haciendo uso de la siguiente sintaxis:

    random.randint(1, 10)

El comando anterior generará un único valor entre 1 y 10 incluídos cada que lo 
ejecutamos.

Haciendo uso de la librería random, escribir el código necesario para:
 a. Almacene en las variables num1, num2 y num3 tres valores generados aleatoriamente
    entre el 10 y el 30.

 b. Si num1 es mayor que num2 sumado con num3, se debe imprimir el valor de num1
    en caso contrario se deberá imprimir num2

 c. Si num3 es multiplo de num2, imprimir "el num3 contiene XX veces el num2"
    en caso contrario imprimir "no son multiplos"
"""

# Ejercicio 1.
# -- Ejercicio 1. Punto a
# import random as rm
from random import randint as rm
print('-------------------------------------------Ejercicio 1.-------------------------------------------')
num1 = rm(10, 30)
num2 = rm(10, 30)
num3 = rm(10, 30)
print('a = ', num1, ' b = ', num2, ' c =', num3)

# -- Ejercicio 1. punto b
print('num1 = ', num1) if num1 > (num2 + num3) else print('num2 = ', num2)

# -- Ejercicio 1. punto c
print(f'el {num3} contiene {num3//num2} veces el {num2}') if (num3 % num2 == 0) else print(f'El número {num3} y el número {num2} no son multiplos')


"""
Ejercicio 2.
Haciendo uso de la librerñia random, escribir el código necesario para:
 a. Generar una lista de 10 elementos con números aleatorios entre 5 y 15 y
    almacenarla en una variable llamada list1

 b. Generar un número aleatorio entre el 5 y el 15 y almacenarlo en una 
    variable llamada num1 

 c. Si num1 se encuentra en la list1 se debe imprimir "contenido" en caso 
    contrario se debe imprimir "no contenido"
"""

# Ejercicio 2.
# -- Ejercicio 2. punto a
print('-------------------------------------------Ejercicio 2.-------------------------------------------')
list1 = [rm(5, 15) for i in range(10)]
print('list1 = ', list1)

# -- Ejercicio 2. punto b
num1 = rm(5, 15)
print('num1 = ', num1)

# -- Ejercicio 2. punto b
print(f'número {num1} contenido') if num1 in list1 else print(f'número {num1} no contenido')
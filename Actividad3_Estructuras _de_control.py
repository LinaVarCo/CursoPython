"""
Ejercicio 1.

Escribir un programa que permita identificar cuándo un número es negativo,
cero o positivo, haciendo uso de random.randint(-20, 20)
"""

# Soulución Ejercicio 1.
from random import randint as rm

var = rm(-20, 20)

print('------------------------------Ejercicio 1.------------------------------', '\n')
if var < 0:
    print(f'El valor {var} es Negativo')
elif var == 0:
    print(f'El valor es Cero')
else:
    print(f'El valor {var} es Positivo')

"""
Ejercicio 2.

Escribir un programa que almacene en las variables num1, num2 y num3 tres
valores generados aleatoriamente haciendo uso de random.randint(1, 30). Sí el
num2 está entre num1 y num3 imprimir 'el num2 está entre num1 y num3' en caso
contrario imprimir 'el num2 está por fuera del rango.
"""

# Solución Ejercicio 2

num1 = rm(1, 30)
num2 = rm(1, 30)
num3 = rm(num1, 30)

print('\n', '------------------------------Ejercicio 2.------------------------------', '\n')
print(f'Los valores generados son {num1}, {num2} y {num3}')

if num2 >= num1  and num2 <= num3:
    print(f'El número {num2} está entre {num1} y {num3}')
else:
    print(f'el {num2} está por fuera del rango')



"""
Ejercicio 3.

Escribir un programa que permita realizar una clasificación de la siguiente
cadena de acuerdo a las siguientes reglas:
a. Cada uno de los caracteres en digitos o letras
b. Cada una de las palabras en digitos o letras
c. Cada uno de los caracteres en vocales o consonantes

cadena = 'este es el numero 10 y este es el numero 20'
"""
cadena = 'este es el numero 10 y este es el numero 20'
#cadena = cadena.replace(" ", ',')
cadena_b = cadena.split()

print('\n', '------------------------------Ejercicio 3.------------------------------', '\n')

#a.
print('-----3.a-----')
for i in cadena:
    if i.isdigit():
        print(f'El caracter {i} es dígito')
    elif i.isalpha():
        print(f'El caracter {i} es letra')
    else:
        print(f'El caracter {i} no es Alfanumérico')

#b.
print('-----3.b-----', '\n')
for i in cadena_b:
    if i.isdigit():
        print(f'La palabra "{i}" esta formada por dígitos')
    elif i.isalpha():
        print(f'La palabra "{i}" esta formada por letras')
    

#c.
print('-----3.c-----', '\n')

for i in cadena:
    if i in ('a', 'e', 'i', 'o', 'u'):
        print(f'{i} es una vocal')
    elif i.isalpha():
        print(f'{i} es una consonante')
    else:
       print(f'{i} no es una letra')

"""
Ejercicio 4.

Escribir un programa que imprima la siguiente lista en el orden inverso haciendo
uso de un ciclo 

lista = [1, 1, 2, 3, 5, 8, 13, 21]
"""

# Solución Ejercicio 4.
lista = [1, 1, 2, 3, 5, 8, 13, 21]
new_lista = []
for i in range(len(lista) -1, -1, -1):
    new_lista.append(lista[i])

print('\n', '------------------------------Ejercicio 4.------------------------------', '\n')
print(f'la lista {lista} a la inversa es: {new_lista}')

"""
Ejercicio 5.

Dada la siguiente lista:
numeros = [1, 2, 3, 4, 5, 6, 7, 100, 110, 21, 33, 32, 2, 4]

Escribir un programa que permita clasificar cada uno de los elementos en pares
e impares (dos nuevas listas)
"""

# Solución Ejercicio 5.
numeros = [1, 2, 3, 4, 5, 6, 7, 100, 110, 21, 33, 32, 2, 4]
pares = []
impares = []

for i in numeros:
    if i % 2 == 0:
        pares.append(i)  
    else:
        impares.append(i) 

print('\n', '------------------------------Ejercicio 5.------------------------------', '\n')
print(f'En la siguiente lista {numeros}', '\n')
print(f'Los numeros pares son {pares} y los numeros impares son {impares}')

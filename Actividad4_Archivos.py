# Crear un script en python que permita responder cada uno de los siguientes
# puntos a partir del archivo ejercicio.txt
# 1. Cuál es la cantidad de veces que aparece cada una de las palabras en el
#    texto. Esto debe quedar almacenado en un diccionario
# 2. Cuál es la frecuencia de cada una de las palabras que contienen 2 letras.
#    Esto debe quedar almacenado en un diccionario
# 3. Cuál es la linea qué más palabras contiene? Imprimir dicha linea y la
#    cantidad de palabras
# 4. Cuál es la linea qué más palabras de 3 letras contiene? Imprimir dicha
#    linea y la cantidad de palabras
# 5. Cree un archivo nuevo donde se almacene cada una de las líneas del archivo
#    original eliminando cada una de las palabras con 4 o letras menos. El
#    archivo destino se llamará ejercicio_mod.txt

# Nota: No olvidar remover caracteres especiales para el conteo de las palabras
# y estandarizar las palabras

import re
from pprint import pprint
with open('D:\livargas\Cursos\Python Intermedio\ejercicio.txt') as var:

    contenido = var.read()
    #print(contenido_lineas)
    conteo_palabras = {}
    contenido = re.sub(r'[^a-zA-Z0-9]', ' ', contenido)
    contenido = contenido.lower().split()
    palabras = set(contenido)
    #print(palabras)
    
    # -----------------------------------------Ejercicio 1.-----------------------------
    for palabra in palabras:
        conteo_palabras[palabra] = contenido.count(palabra)
    #print('\n', '------------------------------Ejercicio 1.------------------------------', '\n')
    #pprint(conteo_palabras)

    # -----------------------------------------Ejercicio 2.-----------------------------
    par_letras = {}
    for palabra_2 in palabras:
        if len(palabra_2) == 2:
            repeticiones = contenido.count(palabra_2)
            par_letras[palabra_2] = repeticiones
    print('\n', '------------------------------Ejercicio 2.------------------------------', '\n')
    pprint(par_letras)
    
    
with open('D:\livargas\Cursos\Python Intermedio\ejercicio.txt') as var2:
    
    contenido_lineas = var2.readlines()
    #pprint(contenido_lineas)
    max_punto_3 = 0
    lista = []
    lista_punto_3 = []
    max_punto_4 = 0
    lista_punto_4 = []
    lista_punto_5 = []
    for fila in contenido_lineas:
        fila = fila.replace('\n', ' ')
        fila = fila.lower()
        fila = re.sub(r'[^a-zA-Z0-9]', ' ', fila)
        lista = fila
        lista_palabras = lista.split()
        # -----------------------------------------Ejercicio 3.-----------------------------
        conteo_punto_3 = len(lista_palabras)
        if conteo_punto_3 > max_punto_3:
            max_punto_3 = conteo_punto_3
            lista_punto_3 = lista
        # -----------------------------------------Ejercicio 4.-----------------------------
        conteo_punto_4 = 0
        for palabra in lista_palabras:
            if len(palabra) == 3:
                conteo_punto_4 += 1
            if conteo_punto_4 > max_punto_4:
                max_punto_4 = conteo_punto_4
                lista_punto_4 = lista
    
    print('\n', '------------------------------Ejercicio 3.------------------------------', '\n')
    print(f'La linea qué más palabras contiene es "{lista_punto_3}" y contiene {max_punto_3} palabras')
    print('\n', '------------------------------Ejercicio 4.------------------------------', '\n')
    print(f'la linea qué más palabras de 3 letras contiene es "{lista_punto_4}" y contiene {max_punto_4} palabras')
    
        # -----------------------------------------Ejercicio 5.-----------------------------
    '''
        var3 = open('D:\livargas\Cursos\Python Intermedio\ejercicio_mod.txt', 'a')
        for palabra_5 in lista_palabras:
            if len(palabra_5) <= 4:
                continue
            lista_punto_5.append(palabra_5)
            lista_punto_5.append(' ')
    var3.writelines(lista_punto_5)
    var3.close()
    #print('\n', '------------------------------Ejercicio 5.------------------------------', '\n')
    #print(lista_punto_5)
    '''



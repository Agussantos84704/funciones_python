
# CODE:35
# IMPORTANTE: NO borrar los comentarios

'''
Alumno:
- Generar una nueva funcion que se llame "contar",
que cuente la cantidad de veces que un número (pasado
por parámetro a la función) se repite en la lista
(también pasada por parámetro)
- Primer parámetro --> la lista de números
- Segundo parámetro --> el número a buscar y contar

Para saber cuantas veces se repiten el elemento pasado
en la lista pueden usar el método nativo de list "count"
'''

# --------------------------------
# Aquí copiar la función "lista_aleatoria"
# ya elaborada en el ejercicio anterior

import random

num_list = []

def lista_aleatoria(inicio, fin, cantidad):
    print ("Funcion Listado Aleatorio")
    for i in range(cantidad):
        numero = random.randint(inicio, fin) 
        num_list.append(numero)
    

    return num_list

    

# --------------------------------

# --------------------------------
# Aquí dentro definir la función contar

def contar (lista, numero_a_contar):
    cantidad = lista.count(numero_a_contar)

    return cantidad

# --------------------------------

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # Alumno: Utilizar la función "lista_aleatoria"
    # para que genere una lista de 5 números que esten comprendidos
    # entre los números 1 al 6 inclusive
    inicio = 1
    fin = 6
    cantidad = 5

    lista_numeros = lista_aleatoria(inicio, fin, cantidad)

    # Imprimir en pantalla "lista_numeros" que tendrá
    # los valores retornado por la función "lista_aleatoria":

    

    print(lista_numeros)

    # Luego quiero averiguar cuantas veces se repite el numero 3
    # en la lista aleatoria creada
    cantidad_tres = contar(lista_numeros, 3)

    print(f'La cantidad de veces que encontramos el numero 3 es: {cantidad_tres} veces')

    print("terminamos")

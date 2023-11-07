
# CODE:29
# IMPORTANTE: NO borrar los comentarios

# Alumno importate --> la función imprimir_mayor
# ya está creada y se invoca en el bloque principal del bloque
# Su misión es completar lo que esa función hace, el código
# que deben desarrollar debe ir dentro de la función
# como se detalla:

def imprimir_mayor(numero_1, numero_2):
    print("Funcion imprimir mayor")
    # Alumno:
    # En esta función debe determinar cual de los dos
    # números ingresados por parámetro es mayor
    if numero_1 > numero_2:
        mayor = numero_1
    elif numero_2 == numero_1:
        mayor = f'{numero_1} y {numero_2} son iguales'
    else:
        mayor = numero_2
    print(f'el numero más grande es {mayor}')
    # Crear una variable llamada mayor en donde
    # almacenará el número mayor ingresado
    # Si ambos números son iguales, almacenar
    # cualquier de los datos en la variable mayor

    # Imprimir en pantalla la variable mayor


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    imprimir_mayor(2, 10)

    print("terminamos")


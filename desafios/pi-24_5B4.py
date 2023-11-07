
# CODE:32
# IMPORTANTE: NO borrar los comentarios

# --------------------------------
# Alumno:
# Aquí dentro definir la función que solicitará
# el nombre de tres invitados

def generar_invitados():
    lista_invitados = []
    
    for _ in range(3):
        nombre = input('Ingrese el nombre completo del invitado: ')
        lista_invitados.append(nombre)

    return lista_invitados
    
# --------------------------------


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # Alumno: Crear la función "generar_invitados"
    # fuera del bloque condicional principal (ver arriba los comentarios)
    
    # Esta función no recibe parámetros

    # Dentro de esa función el sistema deberá solicitar
    # al usuario por consola que ingrese tres nombres de 
    # tres invitados.
    # IMPORTANTE: Utilizar un "input" por cada invitado
    # que se solicite ingresar

    # Los tres nombres ingresados se deberán guardar en
    # una lista

    # La función generar_invitados deberá retornar
    # la lista de invitados generados, el valor de retorno
    # se debe almacenar en una variable llamada "lista_invitados"

    # NOTA: Recomendamos utilizar bucles para no repetir código
    # y solicitar los 3 invitiados, uno en cada iteración del bucle

    # Luego de crear la función invocarla en este lugar:

    Invitados = generar_invitados()

    # Imprimir en pantalla "lista_invitados":
    print(f'La lista habría quedado de la siguiente manera: {Invitados}')

    print("terminamos")

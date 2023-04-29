def listarProductos(lista: list[str]) -> None:
    print("+---------------------------+ Opciones de listado +---------------------------+")
    print("| 1-. Según su cantidad (ascendente - quicksort)                              |") 
    print("| 2-. Según su peso (descendente - mergesort)                                 |")
    print("| 3-. Según su fecha de creación (ascendente/descendente - shellsort)         |")
    print("| 4-. Segun su cantidad (ascendente - heapsort)                               |")
    print("| 5-. Segun sus dimensiones y antigüedad (ascendente/descendente - algoritmo) |")
    print("| 6-. Salir                                                                   |")
    print("+-----------------------------------------------------------------------------+")
    # Captura de la opcion de listado
    try:
        opcion = int(input("-> Opcion deseada: "))
        error = opcion not in range(1, 7)
        print("-> Ha ingresado un numero fuera de rango\n" if error else "")
    except:
        error = True
        print("-> No se ha ingresado un numero, seleccione una opcion valida\n")

    # Seleccionamos la opcion
    if not error:
        if opcion == 1:
            quicksort(lista)
        elif opcion == 2:
            mergesort(lista)
        elif opcion == 3:
            shellsort(lista)
        elif opcion == 4:
            heapsort(lista)
        elif opcion == 5: 
            algoritmo(lista)
        else:
            pass
            

"""Funciones de listado de productos segun las indicaciones"""
def quicksort(productos):
    # Ordenar ascendentemente los productos segun la cantidad
    print(productos)

def mergesort(productos):
    # Ordernar descendentemente segun su peso en un rango de fecha de actualizacion introducido por el usuario
    print(productos)

def shellsort(productos):
    # De forma ascendente o descendente 
    print("+---+ Opciones de listado +---+")
    print("| 1-. Ascendente              |")
    print("| 2-. Descendente             |")
    print("+-----------------------------+")
    print(productos)

def heapsort(productos):
    # Ascendentemente sgun su cantidad
    print(productos)

def algoritmo(productos):
    # Ascendente o descendente segun sus dimensiones y antiguedad en un rango de fecha
    print("+---+ Opciones de listado +---+")
    print("| 1-. Ascendente              |")
    print("| 2-. Descendente             |")
    print("+-----------------------------+")
    print(productos)
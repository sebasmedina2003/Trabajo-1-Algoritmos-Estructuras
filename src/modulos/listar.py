def listarProductos(lista: list[str]) -> None:
    # Mostrar un submenu para elegir la opcion del reporte al listar 
    print("+---------------------------+ Opciones de listado +---------------------------+")
    # Listar los productos de forma ascendente segun la cantidad- quicksort
    print("| 1-. Según su cantidad (ascendente - quicksort)                              |") 
    # De forma descendente según su peso en un rango de fecha de actualizacion introducido por el usuario - mergesort
    print("| 2-. Según su peso (descendente - mergesort)                                 |")
    # De forma ascendente o descendente - shellsort -> Agregar submenú para determinar el orden
    print("| 3-. Según su fecha de creación (ascendente/descendente - shellsort)         |")
    # De forma ascendente segun su cantidad - heapsort
    print("| 4-. Segun su cantidad (ascendente - heapsort)                               |")
    # de forma ascendente o descendente segun sus dimensiones y antiguedad en un rango de fecha - cualquier algoritmo
    print("| 5-. Segun sus dimensiones y antigüedad (ascendente/descendente - algoritmo) |")
    print("+-----------------------------------------------------------------------------+")

# Crear las funciones de listado segun el tipo y el algoritmo de ordenamiento
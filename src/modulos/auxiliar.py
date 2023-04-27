def lecturaDatos() -> list:
    """
    Funcion para la lectura de los datos para la creacion y actualizacion de un producto
    """
    # Leemos los datos de consola
    nombre = input("Ingrese el nombre del producto: ")
    descripcion = input("Ingrese una descripcion corta del producto: ")
    categoria = input("Ingrese la categoria del producto: ")

    while True:
        try:
            precio = float(input("Ingrese el precio del producto: "))
            break
        except:
            print("Ingrese un precion valido\n")

    imagen = input("Ingrese el path de la imagen: ")
    sku = input("Ingrese el SKU del producto: ")

    while True:
        try:
            cantidad = float(
                input("Ingrese la cantidad de articulos disponibles: "))
            break
        except:
            print("Ingrese una cantidad valdia\n")

    while True:
        try:
            peso = float(input("Ingrese el peso del producto: "))
            break
        except:
            print("Ingrese un peso valido\n")

    while True:
        dimensiones = input(
            "Ingrese las dimensionenes de su producto, formato anchoXalto: ")
        if len(dimensiones.split("X")) == 2:
            break

    return [nombre, descripcion, categoria, precio, imagen, sku, cantidad, peso, dimensiones]


def shellSort(array, n):
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j-interval] > temp:
                array[j] = array[j - interval]
                j -= interval
            array[j] = temp
        interval //= 2


array = [1, 10, 5]
shellSort(array, 3)
print(array)

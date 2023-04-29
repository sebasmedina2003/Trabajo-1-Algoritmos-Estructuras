# Funcion para la captura de los atributos de un producto
def lecturaDatos() -> list:
    # Leemos los datos de consola
    nombre = input("Ingrese el nombre del producto: ")  # Nombre del producto
    # Descripcion del producto
    descripcion = input("Ingrese una descripcion corta del producto: ")
    # Categoria del producto
    categoria = input("Ingrese la categoria del producto: ")
    # Precio del producto
    while True:
        try:
            precio = float(input("Ingrese el precio del producto: "))
            break
        except:
            print("Ingrese un precion valido\n")

    # Direccion de imagen del producto
    imagen = input("Ingrese el path de la imagen: ")

    while True:
        sku = input("Ingrese el SKU del producto: ")  # SKU del producto
        aux = sku.split("-")
        if len(aux) == 3:
            break

    # Cantidad de articulos disponibles
    while True:
        try:
            cantidad = float(
                input("Ingrese la cantidad de articulos disponibles: "))
            break
        except:
            print("Ingrese una cantidad valdia\n")
    # Peso del producto
    while True:
        try:
            peso = float(input("Ingrese el peso del producto: "))
            break
        except:
            print("Ingrese un peso valido\n")
    # Dimensiones del producto
    while True:
        dimensiones = input(
            "Ingrese las dimensionenes de su producto (anchoXalto): ")
        if "x" in dimensiones and len(dimensiones.split("x")) == 2:
            break
        elif "X" in dimensiones and len(dimensiones.split("X")) == 2:
            break

    # Leemos la fecha de creacion del producto
    while True:
        fecha = input(
            "Ingrese fecha de creacion del producto, formado dia-mes-año: ")
        aux = fecha.split("-")
        error = False
        if len(aux) == 3:
            for valores in aux:
                if not error:
                    try:
                        int(valores)
                    except:
                        print("No ha ingresado numeros en los campos")
                        error = True
            if not error:
                break

    # Retornar el producto en un vector, indicando como ultimo parametro "sin modificacion"
    return [nombre, descripcion, categoria, precio, imagen, sku, cantidad, peso, dimensiones, fecha, "Sin modificacion"]

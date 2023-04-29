# Funcion para la captura de los atributos de un producto
def lecturaDatos() -> list:
    formato = {
        "Nombre": "",
        "Descripcion": "",
        "Categoria": "",
        "Precio": 0,
        "Imagen": "",
        "SKU": "",
        "Cantidad": 0,
        "Peso": 0,
        "Dimensiones": "",
        "Fecha Creacion": "",
        "Fecha Modificacion": "Sin modificaciones"
    }
    # Leemos los datos de consola
    formato["Nombre"] = input(
        "Ingrese el nombre del producto: ")  # Nombre del producto
    # Descripcion del producto
    formato["Descripcion"] = input(
        "Ingrese una descripcion corta del producto: ")
    # Categoria del producto
    formato["Categoria"] = input("Ingrese la categoria del producto: ")
    # Precio del producto
    while True:
        try:
            formato["Precio"] = float(
                input("Ingrese el precio del producto: "))
            break
        except:
            print("Ingrese un precion valido\n")

    # Direccion de imagen del producto
    formato["Imagen"] = input("Ingrese el path de la imagen: ")

    while True:
        formato["SKU"] = input(
            "Ingrese el SKU del producto: ")  # SKU del producto
        aux = formato["SKU"].split("-")
        if len(aux) == 3:
            break
        print("-> Formato incorrecto - (XXX-XXX-XXX o XXXX-XXXX-XXXX)")

    # Cantidad de articulos disponibles
    while True:
        try:
            formato["Cantidad"] = float(
                input("Ingrese la cantidad de articulos disponibles: "))
            break
        except:
            print("Ingrese una cantidad valdia\n")
    # Peso del producto
    while True:
        try:
            formato["Peso"] = float(input("Ingrese el peso del producto: "))
            break
        except:
            print("Ingrese un peso valido\n")
    # Dimensiones del producto
    while True:
        formato["Dimensiones"] = input(
            "Ingrese las dimensionenes de su producto (anchoXalto): ")
        if "x" in formato["Dimensiones"] and len(formato["Dimensiones"].split("x")) == 2:
            break
        elif "X" in formato["Dimensiones"] and len(formato["Dimensiones"].split("X")) == 2:
            break

    # Retornar el diccionario, indicando como ultimo parametro "sin modificacion"
    return formato

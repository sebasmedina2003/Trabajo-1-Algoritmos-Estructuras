# Funcion para la captura de los atributos de un producto
def lecturaDatos() -> dict:
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
    while True : # Nombre del producto - Validacion cantidad de caracteres
        formato["Nombre"] = input(">>> Ingrese el nombre del producto: ")  
        if len(formato["Nombre"]) > 19:
            print(">>> Cantidad de caracteres excedida...")
        elif len(formato["Nombre"]) <=19 and formato["Nombre"]!="":
            break
        else:
            print(">>> Ingrese el nombre del producto...")
    
    while True: # Descripcion del producto - Validacion cantidad de caracteres
        formato["Descripcion"] = input(">>> Ingrese una descripcion corta del producto: ")
        if len(formato["Descripcion"]) > 23:
            print(">>> Cantidad de caracteres excedida...")
        elif len(formato["Descripcion"]) <= 23 and formato["Descripcion"]!="":
            break
        else:
            print(">>> Ingrese la descripcion del producto...")

    while True: # Categoria del producto - Validacion cantidad de caracteres
        formato["Categoria"] = input(">>> Ingrese la categoria del producto: ")
        if len(formato["Categoria"]) > 15:
            print(">>> Cantidad de caracteres excedida...")
        elif len(formato["Categoria"]) <= 15 and formato["Categoria"]!="":
            break
        else:
            print(">>> Ingrese la descripcion del producto...")
    """ Validaciones restantes"""
    # Precio del producto
    while True:
        try:
            formato["Precio"] = float(input(">>> Ingrese el precio del producto: "))
            break
        except:
            print("-> Ingrese un precion valido\n")

    # Direccion de imagen del producto
    formato["Imagen"] = input(">>> Ingrese el path de la imagen: ")
    
    # SKU del producto
    while True:
        formato["SKU"] = input(">>> Ingrese el SKU del producto: ")  
        aux = formato["SKU"].split("-")
        if len(aux) == 3:
            if len(aux[0]) == 3 and len(aux[1])==3 and len(aux[2])==3:
                break
            elif len(aux[0]) == 4 and len(aux[1])==4 and len(aux[2])==4:
                break
            else:
                print("-> Formato incorrecto - (XXX-XXX-XXX o XXXX-XXXX-XXXX)")
        else:
            print("-> Formato incorrecto - (XXX-XXX-XXX o XXXX-XXXX-XXXX)")


    # Cantidad de articulos disponibles
    while True:
        try:
            formato["Cantidad"] = float(input(">>> Ingrese la cantidad de articulos disponibles: "))
            break
        except:
            print("-> Ingrese una cantidad valdia\n")
    
    # Peso del producto
    while True:
        try:
            formato["Peso"] = float(input(">>> Ingrese el peso del producto (gramos/gr): "))
            break
        except:
            print("-> Ingrese un peso valido\n")
    
    # Dimensiones del producto
    permitido = ["0","1","2","3","4","5","6","7","8","9", "x", "X"]
    while True:
        formato["Dimensiones"] = input(">>> Ingrese las dimensionenes de su producto (anchoXalto): ")
        if "x" in formato["Dimensiones"] or "X" in formato["Dimensiones"]:
            if len(formato["Dimensiones"].split("x")) == 2 or len(formato["Dimensiones"].split("X")) == 2:
                error = False
                for i in list(formato["Dimensiones"]):
                    if i not in permitido:
                        error = True
                if not error:
                    break
                else:
                    print("-> Informacion incorrecta... ")
            else:
                print("-> Formato de dimensiones incorrecto (anchoXalto)...")
    return formato
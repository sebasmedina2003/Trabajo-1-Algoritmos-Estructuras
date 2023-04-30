import modulos.auxiliar as auxiliar
import datetime


def creacionProducto() -> None:
    """
    Se llama a la funcion de lectura de datos para la creacion de un producto
    """
    print("Ingrese los siguientes datos para la creacion de su producto\n")
    producto = auxiliar.lecturaDatos()

    # Leemos la fecha de creacion del producto
    while True:
        fecha = input(
            ">>> Ingrese fecha de creacion del producto, formado dia-mes-año: ")
        # Validacion de la fecha
        try:
            fecha_str = datetime.datetime.strptime(fecha, '%d-%m-%Y')
            break
        except:
            print("-> Formato de fecha incorrecto (dd-mm-yyyy)...")
    producto["Fecha Creacion"] = fecha
    return producto


def cargaDatos(lista: list[dict]) -> list[dict]:
    archivo = open("src/archivos/registros.csv", "r")
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
    for lineas in archivo:
        aux = lineas.split(",")
        print("Agregando " + aux[0])
        formato["Nombre"] = aux[0]
        formato["Descripcion"] = aux[1]
        formato["Categoria"] = aux[2]
        formato["Precio"] = aux[3]
        formato["Imagen"] = aux[4]
        formato["SKU"] = aux[5]
        formato["Cantidad"] = aux[6]
        formato["Peso"] = aux[7]
        formato["Dimensiones"] = aux[8]
        formato["Fecha Creacion"] = aux[9]
        formato["Fecha Modificacion"] = aux[10].replace("\n", "")
        lista.append(formato)

    print("\n---------------Carga de archivo de prueba terminada---------------\n")
    return lista

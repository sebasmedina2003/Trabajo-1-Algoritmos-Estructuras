import modulos.auxiliar as auxiliar
from datetime import datetime
import time


def creacionProducto() -> None:
    """
    Se llama a la funcion de lectura de datos para la creacion de un producto
    """
    print("Ingrese los siguientes datos para la creacion de su producto\n")
    producto = auxiliar.lecturaDatos()

    fecha = datetime.now()
    dia = "0"+str(fecha.day) if len(str(fecha.day)) == 1 else str(fecha.day)
    mes = "0"+str(fecha.month) if len(str(fecha.month)
                                      ) == 1 else str(fecha.month)
    año = str(fecha.year)
    producto["Fecha Creacion"] = dia + "-" + mes + "-" + año
    producto["Fecha Modificacion"] = producto["Fecha Creacion"]
    return producto


def cargaDatos(lista: list[dict]) -> list[dict]:
    archivo = open("archivos/registros.csv", "r")
    print(">>> Cargando datos de prueba...")
    for lineas in archivo:
        time.sleep(0.5)
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
            "Fecha Modificacion": ""
        }
        aux = lineas.split(",")
        print("-> Agregando " + aux[0]+"...")
        formato["Nombre"] = aux[0]
        formato["Descripcion"] = aux[1]
        formato["Categoria"] = aux[2]
        formato["Precio"] = float(aux[3])
        formato["Imagen"] = aux[4]
        formato["SKU"] = aux[5]
        formato["Cantidad"] = int(aux[6])
        formato["Peso"] = float(aux[7])
        formato["Dimensiones"] = aux[8]
        formato["Fecha Creacion"] = aux[9]
        formato["Fecha Modificacion"] = aux[10].replace("\n", "")
        lista.append(formato)
    print("\n+-----------------+ Datos almacenados exitosamente +-----------------+\n")
    return lista

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
        fecha = input(">>> Ingrese fecha de creacion del producto, formado dia-mes-año: ")
        # Validacion de la fecha 
        try:
            fecha_str = datetime.datetime.strptime(fecha, '%d-%m-%Y')
            break
        except:
            print("-> Formato de fecha incorrecto (dd-mm-yyyy)...")
    producto["Fecha Creacion"] = fecha
    return producto

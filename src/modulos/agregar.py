
import modulos.auxiliar as auxiliar


def creacionProducto() -> None:
    """
    Se llama a la funcion de lectura de datos para la creacion de un producto
    """
    print("Ingrese los siguientes datos para la creacion de su producto\n")
    # Se movieron todas las capturas del producto en el modulo auxiliar
    producto = auxiliar.lecturaDatos()

    # Leemos la fecha de creacion del producto
    while True:
        producto["Fecha Creacion"] = input(
            "Ingrese fecha de creacion del producto, formado dia-mes-año: ")
        aux = producto["Fecha Creacion"].split("-")
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

    return producto

import modulos.auxiliar as auxiliar

def creacionProducto() -> None:
    """
    Se llama a la funcion de lectura de datos para la creacion de un producto
    """
    print("Ingrese los siguientes datos para la creacion de su producto\n")
    producto = auxiliar.lecturaDatos() # Se movieron todas las capturas del producto en el modulo auxiliar
    return producto
    
import modulos.actualizar as actualizar
import modulos.agregar as agregar
import modulos.consultar as consultar
import modulos.listar as listar


def menu() -> None:
    """
    Funcion que muestra el menu principal, consta del bucle principal y la seleccion de opciones
    """
    listaProductos = []
    datosCargados = False
    while True:
        error = False
        print("Menu de opciones, seleccione un numero")
        print("1-.Creacion de productos")
        print("2-.Modificar un producto")
        print("3-.Consultar")
        print("4-.Listar Productos")
        print("5-.Cargar Datos de Prueba")
        print("6-.Salir del programa")

        # Verificamos si la opcion es un numero y esta entre el rango de opciones
        try:
            opcion = int(input("Ingreso del numero -> "))
            error = False if opcion in range(1, 7) else True
            print("Ha ingresado un numero fuera de rango\n" if error else "")
        except:
            error = True
            print("No se ha ingresado un numero, seleccione una opcion valida\n")

        # Seleccionamos la opcion
        if not error:
            if opcion == 1:
                listaProductos.append(agregar.creacionProducto())
                print("Producto creado Exitosamente\n")
            elif opcion == 2:
                pass
            elif opcion == 3:
                pass
            elif opcion == 4:
                listar.listarProductos(listaProductos)
            elif opcion == 5:
                if not datosCargados:
                    pass
                else:
                    print("Ya se han cargado los datos del csv")
            elif opcion == 6:
                print("Saliendo del programa")
                break


if __name__ == "__main__":
    menu()

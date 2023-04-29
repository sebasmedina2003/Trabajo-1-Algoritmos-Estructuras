import modulos.actualizar as actualizar
import modulos.agregar as agregar
import modulos.consultar as consultar
import modulos.listar as listar


def menu() -> None:
    # Funcion que muestra el menu principal, consta del bucle principal y la seleccion de opciones
    listaProductos = []
    datosCargados = False
    while True:
        error = False
        print("+--------------------------------+ Menu de opciones +--------------------------------+")
        print("| 1-.Crear | 2-.Modificar | 3-.Consultar | 4-.Listar | 5-.Datos de Prueba | 6-.Salir |")
        print("+------------------------------------------------------------------------------------+")

        # Verificamos si la opcion es un numero y esta entre el rango de opciones
        try:
            opcion = int(input("\nOpción deseada -> "))
            error = not opcion in range(1, 7)
            print("-> Ha ingresado un numero fuera de rango\n" if error else "")
        except:
            error = True
            print("-> No se ha ingresado un numero, seleccione una opcion valida\n")

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
            else:
                print("-> Saliendo del programa...")
                break


if __name__ == "__main__":
    menu()

import modulos.actualizar as actualizar
import modulos.agregar as agregar
import modulos.listar as listar

#Prueba 
def menu() -> None:
    # Funcion que muestra el menu principal, consta del bucle principal y la seleccion de opciones
    listaProductos = []
    datosCargados = False
    while True:
        error = False
        print("+-------------------------+ Menu de opciones +------------------------+")
        print("| 1-.Crear | 2-.Modificar | 3-.Listar | 4-.Datos de Prueba | 5-.Salir |")
        print("+---------------------------------------------------------------------+")

        # Verificamos si la opcion es un numero y esta entre el rango de opciones
        try:
            opcion = int(input("\nOpción deseada -> "))
            error = not opcion in range(1, 6)
            print("-> Ha ingresado un numero fuera de rango\n" if error else "")
        except:
            error = True
            print("-> No se ha ingresado un numero, seleccione una opcion valida\n")

        # Seleccionamos la opcion
        if not error:
            if opcion == 1:  # Crear producto
                producto = agregar.creacionProducto()
                listaProductos.append(producto)
                print("\n+-----+ Producto creado Exitosamente +-----+")
                print(" Nombre: " + producto["Nombre"])
                print(" Descripcion: " + producto["Descripcion"])
                print(" Categoria: " + producto["Categoria"])
                print(" Precio: " + str(producto["Precio"]))
                print(" Imagen: " + str(producto["Imagen"]))
                print(" SKU: " + producto["SKU"])
                print(" Cantidad: " + str(producto["Cantidad"]))
                print(" Peso: " + str(producto["Peso"]))
                print(" Dimensiones: " + producto["Dimensiones"])
                print(" Fecha Creacion: " + producto["Fecha Creacion"])
                print(" Fecha Modificacion: " + producto["Fecha Modificacion"])
                print("+------------------------------------------+\n")

            elif opcion == 2:  # Modificar Producto
                if len(listaProductos) != 0:
                    actualizar.actualizar(listaProductos)
                else:
                    print("-> No existen productos registrados...\n")

            elif opcion == 3:  # Listar productos
                if len(listaProductos) != 0:
                    listar.listarProductos(listaProductos)
                else:
                    print("-> No existen productos registrados...\n")

            elif opcion == 4:  # Cargar datos de prueba
                if not datosCargados:
                    datosCargados = True
                    listaProductos = agregar.cargaDatos(listaProductos)
                else:
                    print("-> Ya se han cargado los datos del CSV...\n")

            elif opcion == 5:  # Salir del programa
                print("-> Saliendo del programa...")
                break


if __name__ == "__main__":
    menu()

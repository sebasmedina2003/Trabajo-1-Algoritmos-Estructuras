from decouple import config
from pandas import DataFrame, read_csv

def lecturaDatos() -> list:
    """
    Funcion para la lectura de los datos para la creacion y actualizacion de un producto
    """
    #Leemos los datos de consola
    nombre = input("Ingrese el nombre del producto: ")
    descripcion = input("Ingrese una descripcion corta del producto: ")
    categoria = input("Ingrese la categoria del producto: ")

    while True:
        try:
            precio = float(input("Ingrese el precio del producto: "))
            break
        except:
            print("Ingrese un precion valido\n")
        
    imagen = input("Ingrese el path de la imagen: ")
    sku = input("Ingrese el SKU del producto: ")

    while True:
        try:
            cantidad = float(input("Ingrese la cantidad de articulos disponibles: "))
            break
        except:
            print("Ingrese una cantidad valdia\n")
    
    while True:
        try:
            peso = float(input("Ingrese el peso del producto: "))
            break
        except:
            print("Ingrese un peso valido\n")
    
    while True:
        dimensiones = input("Ingrese las dimensionenes de su producto, formato anchoXalto: ")
        if len(dimensiones.split("X")) == 2:
            break
    
    return [nombre, descripcion, categoria, precio, imagen, sku, cantidad, peso, dimensiones]
        

def creacionProducto() -> None:
    """
    Se llama a la funcion de lectura de datos para la creacion de un producto
    """
    print("Ingrese los siguientes datos para la creacion de su producto\n")
    producto = lecturaDatos()

    #Leemos la fecha de creacion del producto
    while True:
        fecha = input("Ingrese fecha de creacion del producto, formado dia-mes-año: ")
        aux = fecha.split("-")
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

    fechaModificacion = "Sin modificacion"
    producto.append(fecha)
    producto.append(fechaModificacion)

    text=""
    for valores in producto:
        text += f"{valores},"
    text = text[0:len(text)-1]
    text +="\n"
    archivo = open(config("NAME_CSV"),"w",newline="")
    archivo.write(text)
    archivo.close()

        
def menu() -> None:
    """
    Funcion que muestra el menu principal, consta del bucle principal y la seleccion de opciones
    """
    while True:
        error = False
        print("Menu de opciones, seleccione un numero")
        print("1-.Creacion de productos")
        print("2-.Modificar un producto")
        print("3-.Consultar")
        print("4-.Listar Productos")
        print("5-.Salir del programa")

        #Verificamos si la opcion es un numero y esta entre el rango de opciones
        try:
            opcion=int(input("Ingreso del numero -> "))
            error = False if opcion in range(1,6) else True
            print("Ha ingresado un numero fuera de rango\n" if error else "")
        except:
            error=True
            print("No se ha ingresado un numero, seleccione una opcion valida\n")
        
        #Seleccionamos la opcion
        if not error:
            if opcion == 1:
                creacionProducto()
            elif opcion == 2:
                pass
            elif opcion == 3:
                pass
            elif opcion == 4:
                pass
            elif opcion == 5:
                print("Saliendo del programa")
                break

if __name__ == "__main__":
    
    menu()

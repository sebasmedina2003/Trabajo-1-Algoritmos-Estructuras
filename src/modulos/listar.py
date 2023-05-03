from datetime import datetime
import time
def listarProductos(lista: list[str]) -> None:
    lista_aux = []
    cantidad = []
    pesos = []
    fechas_creacion = []
    fechas_modificacion = []
    dimensiones = []
    lista_ordenada = [] # Vector con la lista ordenada para imprimir
    for i in range (0, len(lista)):
        cantidad.append(lista[i]["Cantidad"])
        fechas_creacion.append(datetime.strptime(lista[i]["Fecha Creacion"], '%d-%m-%Y').date())
        fechas_modificacion.append(datetime.strptime(lista[i]["Fecha Modificacion"], '%d-%m-%Y').date())

    print("+---------------------------+ Opciones de listado +---------------------------+")
    print("| 1-. Según su cantidad (ascendente - quicksort)                              |") 
    print("| 2-. Según su peso (descendente - mergesort)                                 |")
    print("| 3-. Según su fecha de creación (ascendente/descendente - shellsort)         |")
    print("| 4-. Segun su cantidad (ascendente - heapsort)                               |")
    print("| 5-. Segun sus dimensiones y antigüedad (ascendente/descendente - algoritmo) |")
    print("| 6-. Salir                                                                   |")
    print("+-----------------------------------------------------------------------------+")
    # Captura de la opcion de listado
    try:
        opcion = int(input("-> Opcion deseada: "))
        error = opcion not in range(1, 7)
        print("-> Ha ingresado un numero fuera de rango\n" if error else "")
    except:
        error = True
        print("-> No se ha ingresado un numero, seleccione una opcion valida\n")

    # Seleccionamos la opcion
    if not error:
        if opcion == 1:
            cantidad = quicksort(cantidad)
            for i in range(len(cantidad)):
                for j in range(len(lista)):
                    if cantidad[i] == lista[j]["Cantidad"]:
                        #print(str(i) + " " + str(lista[j]))
                        lista_ordenada.append(lista[j])
                        break
            mostrarProductos(lista_ordenada)# Imprimir productos ordenados - salida formateada
        elif opcion == 2:
            lista_aux.clear()
            while True:
                fecha_desde = input(">>> Fecha desde (dia-mes-año): ")
                fecha_hasta = input(">>> Fecha hasta (dia-mes-año): ")
                print()
                try:
                    fecha_desde = datetime.strptime(fecha_desde, '%d-%m-%Y').date()
                    fecha_hasta = datetime.strptime(fecha_hasta, '%d-%m-%Y').date()
                    if (fecha_hasta < fecha_desde):
                        print(int("a"))
                    break
                except:
                    print("-> Formato de fecha incorrecto (dd-mm-yyyy)...")

            fechas_rango = list(fechas_modificacion)
            for i in range (len(fechas_modificacion)):
                if (fecha_hasta < fechas_modificacion[i] or fecha_desde > fechas_modificacion[i]):
                    fechas_rango.remove(fechas_modificacion[i])
            
            for i in range(len(fechas_rango)):
                for j in range(len(lista) ):
                    if fechas_rango[i] == datetime.strptime(lista[j]["Fecha Modificacion"], '%d-%m-%Y').date():
                        pesos.append(lista[j]["Peso"])
                        lista_aux.append(lista[j])
                        break
            
            pesos = mergesort(pesos)
            reps = []
            for i in range(len(pesos) ):
                for j in range(len(lista_aux)):
                    if pesos[i] == lista_aux[j]["Peso"] and lista_aux[j]["Nombre"] not in reps:
                        #print(str(i) + " " + str(lista_aux[j]))
                        lista_ordenada.append(lista_aux[j])
                        reps.append(lista_aux[j]["Nombre"])
                        break
            mostrarProductos(lista_ordenada)# Imprimir productos ordenados - salida formateada
        elif opcion == 3:
            print("+---+ Opciones de listado +---+")
            print("| 1-. Ascendente              |")
            print("| 2-. Descendente             |")
            print("+-----------------------------+")    
            try:
                opcion = int(input("-> Opcion deseada: "))
                error = opcion not in range(1, 3)
                print("-> Ha ingresado un numero fuera de rango\n" if error else "")
            except:
                error = True
                print("-> No se ha ingresado un numero, seleccione una opcion valida\n")
            if not error:
                if opcion == 1:           
                    fechas_creacion = shellsort(fechas_creacion, 1)
                elif opcion == 2:
                    fechas_creacion = shellsort(fechas_creacion, 0)
                for i in range(len(fechas_creacion) ):
                    for j in range(len(lista) ):
                        if fechas_creacion[i] == datetime.strptime(lista[j]["Fecha Creacion"], '%d-%m-%Y').date():
                            #print(str(i) + " " + str(lista[j]))
                            lista_ordenada.append(lista[j]) # Almacenar en un vector los productos ordenados
                            break
            mostrarProductos(lista_ordenada)# Imprimir productos ordenados - salida formateada
        elif opcion == 4:
            cantidad = heapsort(cantidad)
            for i in range(len(cantidad) ):
                for j in range(len(lista) ):
                    if cantidad[i] == lista[j]["Cantidad"]:
                        #print(str(i) + " " + str(lista[j]))
                        lista_ordenada.append(lista[j])
                        break
            mostrarProductos(lista_ordenada)# Imprimir productos ordenados - salida formateada 
        elif opcion == 5: 
            lista_aux.clear()
            while True:
                fecha_desde = input(">>> Fecha desde (dia-mes-año): ")
                fecha_hasta = input(">>> Fecha hasta (dia-mes-año): ")
                try:
                    fecha_desde = datetime.strptime(fecha_desde, '%d-%m-%Y').date()
                    fecha_hasta = datetime.strptime(fecha_hasta, '%d-%m-%Y').date()
                    if (fecha_hasta < fecha_desde):
                        print(int("a"))
                    break
                except:
                    print("-> Formato de fecha incorrecto (dd-mm-yyyy)...")
            fechas_rango = list(fechas_creacion)
            for i in range (len(fechas_creacion)):
                if (fecha_hasta < fechas_creacion[i] or fecha_desde > fechas_creacion[i]):
                    fechas_rango.remove(fechas_creacion[i])

            '''Arreglo y condicionales'''
            print("+---+ Opciones de listado +---+")
            print("| 1-. Dimensiones             |")
            print("| 2-. Antigüedad              |")
            print("+-----------------------------+")
            try:
                opcion = int(input("-> Opcion deseada: "))
                error = opcion not in range(1, 3)
                print("-> Ha ingresado un numero fuera de rango\n" if error else "")
            except:
                error = True
                print("-> No se ha ingresado un numero, seleccione una opcion valida\n")
            if not error:
                print("+---+ Opciones de listado +---+")
                print("| 1-. Ascendente              |")
                print("| 2-. Descendente             |")
                print("+-----------------------------+")
                if opcion == 1: #Dimensiones
                    try:
                        opcion = int(input("-> Opcion deseada: "))
                        error = opcion not in range(1, 3)
                        print("-> Ha ingresado un numero fuera de rango\n" if error else "")
                    except:
                        error = True
                        print("-> No se ha ingresado un numero, seleccione una opcion valida\n")
                    if not error:

                        for i in range(len(fechas_rango) ):
                            for j in range(len(lista) ):
                                if fechas_rango[i] == datetime.strptime(lista[j]["Fecha Creacion"], '%d-%m-%Y').date():
                                    dim = lista[j]["Dimensiones"].split("x")
                                    dimensiones.append(int(dim[0]) * int(dim[1]))
                                    lista_aux.append(lista[j])

                        if opcion == 1: #Ascendente 1
                            dimensiones = quicksort(dimensiones)
                        elif opcion == 2: #Descendente 0
                            dimensiones = mergesort(dimensiones)       
                        reps = []
                        for i in range(len(dimensiones)):
                            for j in range(len(lista_aux) ):
                                dim = lista_aux[j]["Dimensiones"].split("x")
                                if dimensiones[i] == (int(dim[0]) * int(dim[1])) and lista_aux[j]["Nombre"] not in reps:
                                    #print(str(i) + " " + str(lista_aux[j]))
                                    lista_ordenada.append(lista_aux[j]) # Almacenar los productos en orden en un vector
                                    reps.append(lista_aux[j]["Nombre"])
                                    break              
                    mostrarProductos(lista_ordenada)# Mostrar los productos ordenados - salida formateada

                elif opcion == 2: #Antiguedad
                    try:
                        opcion = int(input("-> Opcion deseada: "))
                        error = opcion not in range(1, 3)
                        print("-> Ha ingresado un numero fuera de rango\n" if error else "")
                    except:
                        error = True
                        print("-> No se ha ingresado un numero, seleccione una opcion valida\n")
                    if not error:
                        fechas_creacion.clear()
                        if opcion == 1:           
                            fechas_creacion = shellsort(fechas_rango, 1)
                        elif opcion == 2:
                            fechas_creacion = shellsort(fechas_rango, 0)
                        for i in range(len(fechas_creacion) ):
                            for j in range(len(lista) ):
                                if fechas_creacion[i] ==  datetime.strptime(lista[j]["Fecha Creacion"], '%d-%m-%Y').date():
                                    #print(str(i) + " " + str(lista[j]))
                                    lista_ordenada.append(lista[j]) # Almacenar los productos ordenados en una lista
                                    break
                    mostrarProductos(lista_ordenada) # Mostrar los productos ordenados - salida formateada
        else:
            pass
            

"""Funciones de listado de productos segun las indicaciones"""
def quicksort(cantidad):
    if len(cantidad) <= 1:
        return cantidad
    else:
        pivote = cantidad[0]
        lista_izq = []
        lista_der = []
        for i in range(1, len(cantidad)):
            if cantidad[i] < pivote:
                lista_izq.append(cantidad[i])
            else:
                lista_der.append(cantidad[i])
        return quicksort(lista_izq) + [pivote] + quicksort(lista_der)

def mergesort(pesos):
    if len(pesos) > 1:
        mitad = len(pesos) // 2
        mitad_izq = pesos[:mitad]
        mitad_der = pesos[mitad:]
        mergesort(mitad_izq)
        mergesort(mitad_der)
        i = j = k = 0
        while i < len(mitad_izq) and j < len(mitad_der):
            if mitad_izq[i] > mitad_der[j]:
                pesos[k] = mitad_izq[i]
                i += 1
            else:
                pesos[k] = mitad_der[j]
                j += 1
            k += 1
        while i < len(mitad_izq):
            pesos[k] = mitad_izq[i]
            i += 1
            k += 1
        while j < len(mitad_der):
            pesos[k] = mitad_der[j]
            j += 1
            k += 1
    return pesos

def shellsort(fechas, orden):
    n = len(fechas)
    intervalo = n // 2
    while intervalo > 0:
        for i in range(intervalo, n):
            temp = fechas[i]
            j = i
            while j >= intervalo and ((orden == 1 and fechas[j - intervalo] > temp) or (orden == 0 and fechas[j - intervalo] < temp)):
                fechas[j] = fechas[j - intervalo]
                j -= intervalo

            fechas[j] = temp
        intervalo //= 2
    return fechas

def heapify(cantidad, n, i):
    largest = i
    izq = 2 * i + 1
    der = 2 * i + 2

    if ((izq < n) and (cantidad[largest] < cantidad[izq])):
        largest = izq

    if ((der < n) and (cantidad[largest] < cantidad[der])):
        largest = der

    if (largest != i):
        cantidad[i], cantidad[largest] = cantidad[largest], cantidad[i]
        heapify(cantidad, n, largest)

def heapsort(cantidad):
    n = len(cantidad)
    for i in range((n // 2 - 1), -1, -1):
        heapify(cantidad, n, i)

    for i in range((n - 1), 0, -1):
        cantidad[i], cantidad[0] = cantidad[0], cantidad[i]
        heapify(cantidad, i, 0)
    return cantidad

""" Modulo extra para la salida formateada de los productos """
def mostrarProductos(productos):
    print("+" + "-"*174 + "+")
    print("| I |       Nombre        |      Descripcion      |   Categoria   | Precio |       Imagen       |      SKU      | Cantidad |  Peso  | Dimension | Creacion |   Modificacion    | ")
    print("+" + "-"*174 + "+")
    for producto in range(len(productos)):
        time.sleep(0.5)
        print("|{:3}|{:<21}|{:<23}|{:<15}|${:<7}|{:<20}|{:<15}|{:<10}|{:<8}|{:<11}|{:<10}|{:<18} |".format(producto, productos[producto]["Nombre"], productos[producto]["Descripcion"], productos[producto]["Categoria"], str(productos[producto]["Precio"]), productos[producto]["Imagen"], productos[producto]["SKU"], str(productos[producto]["Cantidad"]), str(productos[producto]["Peso"]), productos[producto]["Dimensiones"], productos[producto]["Fecha Creacion"], productos[producto]["Fecha Modificacion"]))
        print("+" + "-"*174 + "+")
    print("\n")
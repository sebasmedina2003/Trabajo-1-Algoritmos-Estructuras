from datetime import datetime

def listarProductos(lista: list[str]) -> None:
    cantidad = []
    pesos = []
    fechas_creacion = []
    fechas_modificacion = []
    dimensiones = []
    for i in range (0, len(lista)):
        cantidad.append(lista[i]["Cantidad"])
        fecha_temp = lista[i]["Fecha Creacion"].split("-")
        fechas_temp = datetime(int(fecha_temp[2]), int(fecha_temp[1]), int(fecha_temp[0])).date()
        fechas_creacion.append(fechas_temp)
        if lista[i]["Fecha Modificacion"] == "Sin Modificaciones":
            fechas_modificacion.append(datetime.strptime(lista[i]["Fecha Creacion"], '%d-%m-%Y').date())
        else: 
            fechas_modificacion.append(datetime.strptime(lista[i]["Fecha Modificacion"], '%d-%m-%Y').date())
        dim = lista[i]["Dimensiones"].split("x")
        dimensiones.append(int(dim[0]) * int(dim[1]))
    
    print()
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
                        print(str(i) + " " + str(lista[j]))
                        break
            
        elif opcion == 2:

            while True:
                fecha_desde = input(">>> Fecha desde (dia-mes-año): ")
                fecha_hasta = input(">>> Fecha hasta (dia-mes-año): ")
                try:
                    fecha_desde = datetime.strptime(fecha_desde, '%d-%m-%Y').date()
                    fecha_hasta = datetime.strptime(fecha_hasta, '%d-%m-%Y').date()
                    break;
                except:
                    print("-> Formato de fecha incorrecto (dd-mm-yyyy)...")

            fechas_rango = list(fechas_modificacion)
            for i in range (len(fechas_modificacion)):
                fecha_prod = fechas_modificacion[i]
                if (fecha_hasta.year < fecha_prod.year):
                    fechas_rango.remove(fecha_prod)
                elif (fecha_hasta.year == fecha_prod.year):
                    if (fecha_hasta.month < fecha_prod.month):
                        fechas_rango.remove(fecha_prod)
                    elif (fecha_hasta.month == fecha_prod.month) :
                        if (fecha_hasta.day < fecha_prod.day):
                            fechas_rango.remove(fecha_prod)
                if (fecha_desde.year > fecha_prod.year):
                    fechas_rango.remove(fecha_prod)
                elif (fecha_desde.year == fecha_prod.year):
                    if (fecha_desde.month > fecha_prod.month):
                        fechas_rango.remove(fecha_prod)
                    elif (fecha_desde.month == fecha_prod.month) :
                        if (fecha_desde.day > fecha_prod.day):
                            fechas_rango.remove(fecha_prod)
            for i in range(len(fechas_rango) ):
                for j in range(len(lista) ):
                    fecha_c_temp = lista[j]["Fecha Creacion"].split("-")
                    fecha_m_temp = lista[j]["Fecha Creacion"].split("-")
                    if lista[j]["Fecha Modificacion"] == "Sin Modificaciones":
                        if fechas_rango[i] == datetime(int(fecha_c_temp[2]), int(fecha_c_temp[1]), int(fecha_c_temp[0])).date():
                            pesos.append(lista[j]["Peso"])
                    else:
                        if fechas_rango == datetime(int(fecha_m_temp[2]), int(fecha_m_temp[1]), int(fecha_m_temp[0])).date():
                            pesos.append(lista[j]["Peso"])
            
            pesos = mergesort(pesos) # fechas_modi
            for i in range(len(pesos) ):
                for j in range(len(lista) ):
                    if pesos[i] == lista[j]["Peso"]:
                        print(str(i) + " " + str(lista[j]))
                        break

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
                    fechas_creacion = shellsort(fechas_creacion, 0)
                    for i in range(len(fechas_creacion) ):
                        for j in range(len(lista) ):
                            fecha_temp = lista[j]["Fecha Creacion"].split("-")
                            if fechas_creacion[i] ==  datetime(int(fecha_temp[2]), int(fecha_temp[1]), int(fecha_temp[0])).date():
                                print(str(i) + " " + str(lista[j]))
                                break
                elif opcion == 2:
                    fechas_creacion = shellsort(fechas_creacion, 1)
                    for i in range(len(fechas_creacion) ):
                        for j in range(len(lista) ):
                            fecha_temp = lista[j]["Fecha Creacion"].split("-")
                            if fechas_creacion[i] ==  datetime(int(fecha_temp[2]), int(fecha_temp[1]), int(fecha_temp[0])).date():
                                print(str(i) + " " + str(lista[j]))
                                break
        
        elif opcion == 4:
            cantidad = heapsort(cantidad)
            for i in range(len(cantidad) ):
                for j in range(len(lista) ):
                    if cantidad[i] == lista[j]["Cantidad"]:
                        print(str(i) + " " + str(lista[j]))
                        break
        
        elif opcion == 5: 
            
            while True:
                fecha_desde = input(">>> Fecha desde (dia-mes-año): ")
                fecha_hasta = input(">>> Fecha hasta (dia-mes-año): ")
                try:
                    fecha_desde = datetime.strptime(fecha_desde, '%d-%m-%Y').date()
                    fecha_hasta = datetime.strptime(fecha_hasta, '%d-%m-%Y').date()
                    break;
                except:
                    print("-> Formato de fecha incorrecto (dd-mm-yyyy)...")
            fechas_rango = []
            fechas_rango = list(fechas_creacion)
            for i in range (len(fechas_creacion)):
                fecha_prod = fechas_creacion[i]
                if (fecha_hasta.year < fecha_prod.year):
                    fechas_rango.remove(fecha_prod)
                elif (fecha_hasta.year == fecha_prod.year):
                    if (fecha_hasta.month < fecha_prod.month):
                        fechas_rango.remove(fecha_prod)
                    elif (fecha_hasta.month == fecha_prod.month) :
                        if (fecha_hasta.day < fecha_prod.day):
                            fechas_rango.remove(fecha_prod)
                if (fecha_desde.year > fecha_prod.year):
                    fechas_rango.remove(fecha_prod)
                elif (fecha_desde.year == fecha_prod.year):
                    if (fecha_desde.month > fecha_prod.month):
                        fechas_rango.remove(fecha_prod)
                    elif (fecha_desde.month == fecha_prod.month) :
                        if (fecha_desde.day > fecha_prod.day):
                            fechas_rango.remove(fecha_prod)


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
                if opcion == 1:
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
                            dimensiones = shellsort(dimensiones, 0)
                            for i in range(len(dimensiones) ):
                                for j in range(len(lista) ):
                                    dim = lista[j]["Dimensiones"].split("x")
                                    if dimensiones[i] == (int(dim[0]) * int(dim[1])):
                                        print(str(i) + " " + str(lista[j]))
                                        break
                        elif opcion == 2:
                            dimensiones = shellsort(dimensiones, 1)        
                            for i in range(len(dimensiones) ):
                                for j in range(len(lista) ):
                                    dim = lista[j]["Dimensiones"].split("x")
                                    if dimensiones[i] == (int(dim[0]) * int(dim[1])):
                                        print(str(i) + " " + str(lista[j]))   
                                        break     
                elif opcion == 2:
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
                            fechas_creacion = shellsort(fechas_creacion, 0)
                            for i in range(len(fechas_creacion) ):
                                for j in range(len(lista) ):
                                    fecha_temp = lista[j]["Fecha Creacion"].split("-")
                                    if fechas_creacion[i] ==  datetime(int(fecha_temp[2]), int(fecha_temp[1]), int(fecha_temp[0])).date():
                                        print(str(i) + " " + str(lista[j]))
                                        break
                        elif opcion == 2:
                            fechas_creacion = shellsort(fechas_creacion, 1)
                            for i in range(len(fechas_creacion) ):
                                for j in range(len(lista) ):
                                    fecha_temp = lista[j]["Fecha Creacion"].split("-")
                                    if fechas_creacion[i] ==  datetime(int(fecha_temp[2]), int(fecha_temp[1]), int(fecha_temp[0])).date():
                                        print(str(i) + " " + str(lista[j]))
                                        break
        
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

def shellsort(fechas, orden=0):
    n = len(fechas)
    intervalo = n // 2
    while intervalo > 0:
        for i in range(intervalo, n):
            temp = fechas[i]
            j = i
            if orden == 0:
                while j >= intervalo and fechas[j-intervalo] > temp:
                    fechas[j] = fechas[j-intervalo]
                    j -= intervalo
            else:
                while j >= intervalo and fechas[j-intervalo] < temp:
                    fechas[j] = fechas[j-intervalo]
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

def algoritmo(productos):
    # Ascendente o descendente segun sus dimensiones y antiguedad en un rango de fecha
    print("+---+ Opciones de listado +---+")
    print("| 1-. Ascendente              |")
    print("| 2-. Descendente             |")
    print("+-----------------------------+")
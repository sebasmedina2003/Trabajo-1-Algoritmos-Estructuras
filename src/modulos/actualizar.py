import time, datetime 
def actualizar(productos):
    # Indicar cual es el producto a modificar
    print(">>> Productos registrados...")
    print("+" + "-"*171 + "+")
    print("|I|       Nombre        |      Descripcion      |   Categoria   | Precio |       Imagen       |      SKU      | Cantidad |  Peso  | Dimension | Creacion |   Modificacion   | ")
    print("+" + "-"*171 + "+")
    for producto in range(len(productos)):
        time.sleep(0.5)
        print("|{:1}|{:<21}|{:<23}|{:<15}|${:<7}|{:<20}|{:<15}|{:<10}|{:<8}|{:<11}|{:<10}|{:<18}|".format(producto, productos[producto]["Nombre"], productos[producto]["Descripcion"], productos[producto]["Categoria"], str(productos[producto]["Precio"]), productos[producto]["Imagen"], productos[producto]["SKU"], str(productos[producto]["Cantidad"]), str(productos[producto]["Peso"]), productos[producto]["Dimensiones"], productos[producto]["Fecha Creacion"], productos[producto]["Fecha Modificacion"]))
        print("+" + "-"*171 + "+")

    while True: # Captura del indice del producto
        try:
            opcion = int(input("\n>>> Ingrese el indice del producto a modificar: "))
            if opcion in range(0, len(productos)):
                error = False
                break
            else:
                print("-> Opcion incorrecta...")
        except:
            print("Ingrese un indice valido...")
         
    # Atributos a modificar
    if not error:
        atributos = ["Nombre","Descripcion","Categoria","Precio","Imagen","SKU","Cantidad","Peso","Dimensiones"]
        producto = productos[opcion]
        print("Atributos a modificar de " + productos[opcion]["Nombre"] + ": ")
        # Mostrar los atributos a modificar del producto
        for atributo in range(len(atributos)):
            time.sleep(0.5)
            print(str(atributo) + " - " + atributos[atributo])
        # Capturar la opcion elegida
        while True:
            try:
                op = int(input(">>> Indice del atributo a modificar: "))
                if op in range(0, 9):
                    error1 = False
                    break
                else:
                    print("-> Opcion incorrecta...")                    
            except:
                print("-> Ingrese un indice valido...")
        # Modificar el atributo del producto
        if not error1: 
            while True:
                producto[atributos[op]] = input("Ingrese el valor con el que desea modificar el " + atributos[op]+": ")
                if op == 3 or op == 6 or op ==7: # Validacion para los digitos
                    try:
                        producto[atributos[op]] = int(producto[atributos[op]])
                        break
                    except: 
                        print("-> Informacion incorrecta...")

                elif op == 5: # Validacion para el SKU
                    aux = producto[atributos[op]].split("-")
                    if len(aux) == 3:
                        if len(aux[0]) == 3 and len(aux[1])==3 and len(aux[2])==3:
                            break
                        elif len(aux[0]) == 4 and len(aux[1])==4 and len(aux[2])==4:
                            break
                        else:
                            print("-> Formato incorrecto - (XXX-XXX-XXX o XXXX-XXXX-XXXX)")

                elif op == 8:
                    permitido = ["0","1","2","3","4","5","6","7","8","9", "x", "X"]
                    formato = producto[atributos[op]]
                    if "x" in formato or "X" in formato:
                        if len(formato.split("x")) == 2 or len(formato.split("X")) == 2:
                            error = False
                            for i in list(formato):
                                if i not in permitido:
                                    error = True
                            if not error:
                                break
                            else:
                                print("-> Informacion incorrecta... ")
                        else:
                            print("-> Formato de dimensiones incorrecto (anchoXalto)...")
                elif op == 0 or op == 1 or op == 2 or op == 4: 
                    break

        # Capturar la fecha de modificacion 
        while True:
            fecha = input(">>> Ingrese fecha de modificacion del producto (dia-mes-año): ")
            # Validacion de la fecha
            try:
                fecha_str = datetime.datetime.strptime(fecha, '%d-%m-%Y')
                break
            except:
                print("-> Formato de fecha incorrecto (dd-mm-yyyy)...")
        producto["Fecha Modificacion"] = fecha

        # Guardar el producto modificado en la lista de productos
        productos[opcion] = producto
        print("\n+-----------------+ Producto modificado exitosamente +-----------------+\n")
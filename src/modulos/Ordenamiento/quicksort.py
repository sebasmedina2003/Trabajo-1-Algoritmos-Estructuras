def listar_producto(productos):
    if len(productos) <= 1:
        return productos
    else:
        pivote = productos[0]
        lista_izq = []
        lista_der = []
        for i in range(1, len(productos)):
            if productos[i] < pivote:
                lista_izq.append(productos[i])
            else:
                lista_der.append(productos[i])
        return listar_producto(lista_izq) + [pivote] + listar_producto(lista_der)
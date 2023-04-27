
def listarProductos(lista: list[str]) -> None:
    print("Lista de Productos\n")
    for k in range(0, len(lista)):
        print(f"Producto #{k} {lista[k][0]}")

nombre = input("Ingrese el nombre del producto: ")

while True:
    try:
        precio = float(input("Ingrese el precio del producto: "))
        break
    except ValueError:
        print("Error: el precio debe ser un número. Inténtelo de nuevo.")

while True:
    try:
        cantidad = int(input("Ingrese la cantidad del producto: "))
        break
    except ValueError:
        print("Error: la cantidad debe ser un número entero. Inténtelo de nuevo.")

costo_total = precio * cantidad

print(f"Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad} | Total: {costo_total}")

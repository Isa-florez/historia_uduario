
inventario = []

def agregar_producto():

    print("\n--- AGREGAR PRODUCTO ---")

    nombre = input("Ingrese el nombre del producto: ")
    while True:
        try:
            precio = float(input("Ingrese el precio del producto: "))
            if precio < 0:
                print("El precio no puede ser negativo.")
            else:
                break
        except ValueError:
            print("ERROR: Debe ingresar un número válido.")
          
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad del producto: "))
            if cantidad < 0:
                print("La cantidad no puede ser negativa.")
            else:
                break
        except ValueError:
            print("ERROR: Debe ingresar un número entero válido.")

    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    inventario.append(producto)

    print("Producto agregado correctamente.")

def mostrar_inventario():

    print("\n--- MOSTRAR INVENTARIO ---")

    if len(inventario) == 0:
        print("El inventario está vacío.")
        return

    for producto in inventario:
        print(f"Producto: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")

def calcular_estadisticas():
  
    print("\n--- ESTADÍSTICAS DEL INVENTARIO ---")

    if len(inventario) == 0:
        print("No hay productos para calcular estadísticas.")
        return

    valor_total = 0
    total_productos = 0

    for producto in inventario:
        valor_total += producto["precio"] * producto["cantidad"]
        total_productos += 1

    print(f"Valor total del inventario: {valor_total}")
    print(f"Total de productos registrados: {total_productos}")

def menu():
    while True:
        print("\n========== MENÚ PRINCIPAL ==========")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Calcular estadísticas")
        print("4. Salir")
        print("====================================")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_producto()

        elif opcion == "2":
            mostrar_inventario()

        elif opcion == "3":
            calcular_estadisticas()

        elif opcion == "4":
            print("Saliendo del sistema. Gracias por usar el inventario.")
            break

        else:
            print("Opción inválida. Intente nuevamente.")

menu()

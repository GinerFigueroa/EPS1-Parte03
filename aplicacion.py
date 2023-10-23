# Definir una lista para almacenar los productos
productos = []

# Función para mostrar el menú
def mostrar_menu():
    print("Menú Opciones")
    print("1. Registrar")
    print("2. Eliminar")
    print("3. Editar")
    print("4. Listar")
    print("5. Salir")

# Función para registrar un producto
def registrar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    productos.append({"nombre": nombre, "precio": precio})
    print(f"{nombre} ha sido registrado.")

# Función para listar los productos
def listar_productos():
    if productos:
        print("\nListado de Productos:")
        print("{:<20} {:<10}".format("Nombre", "Precio"))
        for producto in productos:
            nombre = producto['nombre']
            precio = producto['precio']
            print("{:<20} {:<10.2f}".format(nombre, precio))
    else:
        print("No hay productos para mostrar.")
        
# Función para eliminar un producto por nombre
def eliminar_producto():
    if productos:
        nombre_a_eliminar = input("Ingrese el nombre del producto que desea eliminar: ")
        eliminados = [producto for producto in productos if producto['nombre'] == nombre_a_eliminar]
        if eliminados:
            productos[:] = [producto for producto in productos if producto['nombre'] != nombre_a_eliminar]
            print(f"{len(eliminados)} producto(s) con el nombre '{nombre_a_eliminar}' ha(n) sido eliminado(s).")
        else:
            print(f"No se encontraron productos con el nombre '{nombre_a_eliminar}'.")
    else:
        print("No hay productos para eliminar.")

# Función para editar un producto por nombre
def editar_producto():
    if productos:
        nombre_a_editar = input("Ingrese el nombre del producto que desea editar: ")
        for producto in productos:
            if producto['nombre'] == nombre_a_editar:
                nuevo_nombre = input("Ingrese el nuevo nombre del producto: ")
                nuevo_precio = float(input("Ingrese el nuevo precio del producto: "))
                producto['nombre'] = nuevo_nombre
                producto['precio'] = nuevo_precio
                print("Producto editado correctamente.")
                return
        print(f"No se encontró un producto con el nombre '{nombre_a_editar}'.")
    else:
        print("No hay productos para editar.")
        
# Insertar 10 productos reales
productos.extend([
    {"nombre": "Polo", "precio": 10.99},
    {"nombre": "Pantalon", "precio": 20.49},
    {"nombre": "Camisa", "precio": 15.99},
    {"nombre": "Corbata", "precio": 5.99},
    {"nombre": "Blusa", "precio": 30.00},
    {"nombre": "Medias", "precio": 12.99},
    {"nombre": "Gorra", "precio": 8.49},
    {"nombre": "Camiseta", "precio": 25.00},
    {"nombre": "Cordones", "precio": 17.99},
    {"nombre": "Zapatilla", "precio": 22.50}
])

# Bucle principal
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción (1/2/3/4/5): ")

    if opcion == "1":
        registrar_producto()
    elif opcion == "2":
        eliminar_producto()
    elif opcion == "3":
        editar_producto()
    elif opcion == "4":
        listar_productos()
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida (1/2/3/4/5).")
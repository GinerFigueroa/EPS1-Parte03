# Definir una lista para almacenar registros
registros = []

# Función para mostrar el menú
def mostrar_menu():
    print("Menú Opciones")
    print("1. Registrar")
    print("2. Eliminar")
    print("3. Editar")
    print("4. Listar")
    print("5. Salir")

# Función para registrar un elemento
def registrar():
    nombre = input("Ingrese el nombre: ")
    registros.append(nombre)
    print(f"{nombre} ha sido registrado.")

# Función para eliminar un elemento
def eliminar():
    if registros:
        print("Registros disponibles:")
        for i, nombre in enumerate(registros):
            print(f"{i + 1}. {nombre}")
        opcion = int(input("Seleccione el número del registro que desea eliminar: "))
        if 1 <= opcion <= len(registros):
            eliminado = registros.pop(opcion - 1)
            print(f"{eliminado} ha sido eliminado.")
        else:
            print("Opción inválida.")
    else:
        print("No hay registros para eliminar.")

# Función para editar un elemento
def editar():
    if registros:
        print("Registros disponibles:")
        for i, nombre in enumerate(registros):
            print(f"{i + 1}. {nombre}")
        opcion = int(input("Seleccione el número del registro que desea editar: "))
        if 1 <= opcion <= len(registros):
            nuevo_nombre = input("Ingrese el nuevo nombre: ")
            registros[opcion - 1] = nuevo_nombre
            print("Registro editado correctamente.")
        else:
            print("Opción inválida.")
    else:
        print("No hay registros para editar.")

# Función para listar los registros
def listar():
    if registros:
        print("Registros disponibles:")
        for i, nombre in enumerate(registros):
            print(f"{i + 1}. {nombre}")
    else:
        print("No hay registros para mostrar.")

# Bucle principal
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción (1/2/3/4/5): ")

    if opcion == "1":
        registrar()
    elif opcion == "2":
        eliminar()
    elif opcion == "3":
        editar()
    elif opcion == "4":
        listar()
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida (1/2/3/4/5).")

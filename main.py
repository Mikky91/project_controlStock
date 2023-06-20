from funciones_stock import agregar_producto, modificar_producto, crear_tabla_productos, eliminar_producto, mostrar_reportes

# Función para realizar el login de usuario


def login():
    opcion = input("Ingrese la opción de autenticación: [1] Empleados, [2] Visitantes: ")

    if opcion == '1':
        usuario = input("Ingrese su nombre de usuario: ")
        contrasena = input("Ingrese su contraseña: ")

        with open('usuarios.txt', 'r') as file:
            for line in file:
                nombre, password = line.strip().split(',')
                if usuario.lower() == nombre.lower() and contrasena == password:
                    return 'admin'

    elif opcion == '2':
        return 'visitante'

    return False


# Función para el usuario administrador
# Función para el usuario administrador
def menu_administrador():
    while True:
        print("\nSistema de Gestión de Stock (Usuario Administrador)")
        print("---------------------------")
        print("1. Agregar producto")
        print("2. Modificar producto")
        print("3. Eliminar producto")
        print("4. Mostrar reportes")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_producto()
        elif opcion == '2':
            modificar_producto()
        elif opcion == '3':
            eliminar_producto()
        elif opcion == '4':
            nombre = input("Ingrese el nombre del producto a buscar (deje en blanco para mostrar todos): ").upper()
            mostrar_reportes(nombre)
        elif opcion == '5':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# Función para el usuario visitante
def menu_visitante():
    while True:
        print("\nSistema de Gestión de Stock (Usuario Visitante)")
        print("---------------------------")
        print("1. Mostrar reportes")
        print("2. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Ingrese el nombre del producto a buscar (deje en blanco para mostrar todos): ").upper()
            mostrar_reportes(nombre)
        elif opcion == '2':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# Función principal
def main():
    tipo_usuario = login()

    if tipo_usuario == 'admin':
        # Crear la tabla de productos en la base de datos
        crear_tabla_productos()
        menu_administrador()
    elif tipo_usuario == 'visitante':
        menu_visitante()
    else:
        print("Nombre de usuario o contraseña incorrectos.")

if __name__ == '__main__':
    main()

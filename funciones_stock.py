import sqlite3

# Función para verificar el formato del código de producto
def verificar_codigo(codigo):
    if len(codigo) <= 5 and codigo[0].isalpha() and codigo[1:].isdigit():
        return True
    else:
        return False

# Función para crear la tabla de productos en la base de datos
def crear_tabla_productos():
    conn = sqlite3.connect('productos.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS productos
                 (codigo TEXT PRIMARY KEY, nombre TEXT, precio REAL, stock INTEGER, procedencia TEXT, categoria TEXT)''')
    conn.commit()
    conn.close()


# Función para agregar un nuevo producto
def agregar_producto():
    codigo = input("Ingrese el código del producto: ").upper()
    if verificar_codigo(codigo):
        nombre = input("Ingrese el nombre del producto: ").upper()
        precio = float(input("Ingrese el precio del producto: "))
        stock = int(input("Ingrese la cantidad en stock: "))
        procedencia = input("Ingrese la procedencia del producto: ").upper()
        categoria = input("Ingrese la categoría del producto: ").upper()

        conn = sqlite3.connect('productos.db')
        c = conn.cursor()
        c.execute("INSERT INTO productos VALUES (?, ?, ?, ?, ?, ?)", (codigo, nombre, precio, stock, procedencia, categoria))
        conn.commit()
        conn.close()
        print("Producto agregado correctamente.")
    else:
        print("El código de producto ingresado es inválido. ")

# Función para modificar un producto existente
def modificar_producto():
    codigo = input("Ingrese el código del producto a modificar: ").upper()

    conn = sqlite3.connect('productos.db')
    c = conn.cursor()
    c.execute("SELECT * FROM productos WHERE codigo=?", (codigo,))
    producto = c.fetchone()
    conn.close()

    if producto is not None:
        print("Datos del producto:")
        print("Código:", producto[0])
        print("Nombre:", producto[1])
        print("Precio:", producto[2])
        print("Stock:", producto[3])
        print("Procedencia:", producto[4])
        print("Categoría:", producto[5])

        while True:
            print("Opciones de modificación:")
            print("1. Modificar nombre")
            print("2. Modificar precio")
            print("3. Modificar stock")
            print("4. Modificar procedencia")
            print("5. Modificar categoría")
            print("6. Salir")

            opcion = input("Ingrese el número de opción: ")

            if opcion == '1':
                nombre = input("Ingrese el nuevo nombre del producto: ").upper()
                conn = sqlite3.connect('productos.db')
                c = conn.cursor()
                c.execute("UPDATE productos SET nombre=? WHERE codigo=?", (nombre, codigo))
                conn.commit()
                conn.close()
                print("Nombre del producto modificado correctamente.")
            elif opcion == '2':
                precio = float(input("Ingrese el nuevo precio del producto: "))
                conn = sqlite3.connect('productos.db')
                c = conn.cursor()
                c.execute("UPDATE productos SET precio=? WHERE codigo=?", (precio, codigo))
                conn.commit()
                conn.close()
                print("Precio del producto modificado correctamente.")
            elif opcion == '3':
                stock = int(input("Ingrese la nueva cantidad en stock: "))
                conn = sqlite3.connect('productos.db')
                c = conn.cursor()
                c.execute("UPDATE productos SET stock=? WHERE codigo=?", (stock, codigo))
                conn.commit()
                conn.close()
                print("Stock del producto modificado correctamente.")
            elif opcion == '4':
                procedencia = input("Ingrese la nueva procedencia del producto: ").upper()
                conn = sqlite3.connect('productos.db')
                c = conn.cursor()
                c.execute("UPDATE productos SET procedencia=? WHERE codigo=?", (procedencia, codigo))
                conn.commit()
                conn.close()
                print("Procedencia del producto modificada correctamente.")
            elif opcion == '5':
                categoria = input("Ingrese la nueva categoría del producto: ").upper()
                conn = sqlite3.connect('productos.db')
                c = conn.cursor()
                c.execute("UPDATE productos SET categoria=? WHERE codigo=?", (categoria, codigo))
                conn.commit()
                conn.close()
                print("Categoría del producto modificada correctamente.")
            elif opcion == '6':
                print("Saliendo...")
                break
            else:
                print("Opción inválida. Intente nuevamente.")
    else:
        print("No se encontró un producto con el código ingresado.")


# Función para eliminar un producto existente
def eliminar_producto():
    codigo = input("Ingrese el código del producto a eliminar: ").upper()

    conn = sqlite3.connect('productos.db')
    c = conn.cursor()
    c.execute("SELECT * FROM productos WHERE codigo=?", (codigo,))
    producto = c.fetchone()

    if producto is not None:
        print("Datos del producto:")
        print("Código:", producto[0])
        print("Nombre:", producto[1])
        print("Precio:", producto[2])
        print("Stock:", producto[3])

        confirmacion = input("¿Está seguro de que desea eliminar este producto? (S/N): ")
        if confirmacion.lower() == 's':
            c.execute("DELETE FROM productos WHERE codigo=?", (codigo,))
            conn.commit()
            print("Producto eliminado correctamente.")
        else:
            print("No se eliminó el producto.")
    else:
        print("No se encontró un producto con el código ingresado.")

    conn.close()

# Función para mostrar reportes
def mostrar_reportes(nombre_solicitado=None):
    conn = sqlite3.connect('productos.db')
    c = conn.cursor()

    if nombre_solicitado is None:
        c.execute("SELECT * FROM productos")
    else:
        c.execute("SELECT * FROM productos WHERE nombre=?", (nombre_solicitado,))

    productos = c.fetchall()
    conn.close()

    if len(productos) > 0:
        if nombre_solicitado is None:
            print("Reporte de productos:")
        else:
            print("Reporte de productos con el nombre '", nombre_solicitado, "':")

        for producto in productos:
            print("Código:", producto[0])
            print("Nombre:", producto[1])
            print("Precio:", producto[2])
            print("Stock:", producto[3])
            print("--------------------")
    else:
        if nombre_solicitado is None:
            print("No hay productos registrados.")
        else:
            print("No se encontraron productos con el nombre '", nombre_solicitado, "'.")


# Función para realizar el login de usuario
def login():
    usuario = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")

    with open('usuarios.txt', 'r') as file:
        for line in file:
            nombre, password = line.strip().split(',')
            if usuario == nombre and contrasena == password:
                return True

    return False

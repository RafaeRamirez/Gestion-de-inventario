# Este es un diccionario vacío donde se almacenarán los productos, usando el código como clave.
productos = {}

list=[

]
# Función para agregar productos al inventario.
def agregar_productos():
    global productos  # Aseguramos que estamos usando la variable global 'productos'.
    print("Agregar productos al inventario")

    # Pedimos el código del producto.
    codigo = input("Ingresa el código: ")

    # Comprobamos si el código ya existe en el inventario.
    if codigo in productos:
        print("El código ya existe en el inventario")
        return  # Si el código ya existe, no seguimos agregando el producto.
     # Pedimos el nombre, precio y cantidad del producto.

    nombre = input("Ingrese el nombre del producto: ")
    while True:
        try:
            precio = float(input("Ingrese el precio del producto: $"))
            break
        except ValueError:
            print("Valor invalida")

    cantidad = int(input("Ingresa la cantidad de producto: "))

    # Agregamos el producto al diccionario con el código como clave y los detalles como valor.
    productos[codigo] = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    list.append(productos)
    pregunta =input("Desea ver todo el inventario:").lower()
    
    print("Producto registrado ")  # Confirmamos que el producto ha sido agregado.

    while True:
        if pregunta == "si":
            print (list)
            break
        elif pregunta=="no":
            print("continuando al menu...")
            break
        else:
            print("Error: Entrada invalida")
            return
        

# Función para consultar el inventario.
def consultar_Inventario():
    print("\nBienvenido, productos disponibles: ")
    if not productos:  # Si el inventario está vacío, mostramos un mensaje.
        print("No hay productos en el inventario.")
        return  # Salimos de la función si no hay productos.

    # Si hay productos, los mostramos uno por uno.
    for codigo, datos in productos.items():
        print(f"Código: {codigo} | Nombre: {datos['nombre']} | Precio: ${datos['precio']} | Cantidad: {datos['cantidad']}")

# Función para actualizar el precio de un producto.
def actualizar_Precios():
    global productos
    # Pedimos el código del producto a actualizar.
    codigo = input("Ingrese el código del producto que desea actualizar: ")

    # Si el código existe en el inventario, actualizamos el precio.
    if codigo in productos:
      try:
        precio_nuevo = float(input("Ingrese el nuevo precio del producto: $"))
        productos[codigo]["precio"] = precio_nuevo  # Actualizamos el precio del producto.
        print("El precio ha sido actualizado correctamente.")
      except ValueError:
          print("Esta digitando un dato invalido")
    else:
        print("El producto no se encuentra en el inventario.")  # Si no existe, informamos al usuario.

# Función para eliminar un producto del inventario.
def eliminar_productos():
    global productos
    # Pedimos el código del producto a eliminar.
    codigo = input("Ingresa el código del producto: ")

    # Si el código existe, eliminamos el producto del inventario.
    if codigo in productos:
        del productos[codigo]  # Eliminar el producto.
        print(f"Producto '{codigo}' eliminado del inventario.")
    else:
        print(f"El producto '{codigo}' no existe.")  # Si no existe, mostramos un mensaje de error.

# Función para calcular el valor total del inventario.
def calcular_inventario():
    global productos
    print("\nBienvenido, para calcular el valor total del inventario:")
    if not productos:
        print("No hay productos en el inventario.")
        return
    # Calculamos el valor total multiplicando el precio de cada producto por su cantidad y sumando todos los resultados.
    valor_total = lambda: sum(producto["precio"] * producto["cantidad"] for producto in productos.values())
    print(f"El valor total del inventario es: ${valor_total():.2f}")


# Menú principal que se ejecuta mientras el usuario no elija salir.
while True:
    print("\nBienvenido a Gestión de inventario")  # Mensaje inicial.
    print("1. Agregar productos:")
    print("2. Consultar inventario:")
    print("3. Actualizar precios:")
    print("4. Eliminar productos:")
    print("5. Calcular el valor total del inventario:")
    print("6. Salir")  # Opción para salir del programa.

    # Pedimos la opción que el usuario quiere elegir.
    opcion = input("Elige una opción: ")

    # Según la opción que elija, ejecutamos una de las funciones.
    if opcion == "1":
        agregar_productos()  # Agregar un producto.
    elif opcion == "2":
        consultar_Inventario()  # Consultar el inventario.
    elif opcion == "3":
        actualizar_Precios()  # Actualizar el precio de un producto.
    elif opcion == "4":
        eliminar_productos()  # Eliminar un producto.
    elif opcion == "5":
        calcular_inventario()  # Calcular el valor total del inventario.
    elif opcion == "6":
        print("¡Gracias por usar la tienda!")  # Salir.
        break  # Salimos del ciclo while.
    else:
        print("Opción inválida, intenta de nuevo.")  # Si la opción es incorrecta, le pedimos al usuario que lo intente de nuevo.

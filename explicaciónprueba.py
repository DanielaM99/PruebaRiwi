import re  # Importa el módulo 're' para trabajar con expresiones regulares, útil para la validación de cadenas de texto.

inventario = [
    {'nombre': 'pan', 'precio': 23.9, 'cantidad': 8},
    {'nombre': 'sal', 'precio': 15.3, 'cantidad': 15},
    {'nombre': 'soda 250ml', 'precio': 36, 'cantidad': 20},
    {'nombre': 'menta', 'precio': 9.5, 'cantidad': 66},
    {'nombre': 'chicle', 'precio': 1, 'cantidad': 150}
]
# 'inventario' es una lista de diccionarios. Cada diccionario representa un producto
# y contiene las claves 'nombre' (string), 'precio' (float) y 'cantidad' (integer).
# Esta estructura de datos permite organizar y manipular la información de los productos.

def validar_texto_con_espacios(texto):
    """
    Valida si una cadena de texto no está vacía después de eliminar los espacios
    en blanco iniciales y finales.

    Args:
        texto (str): La cadena de texto a validar.

    Returns:
        bool: True si la cadena no está vacía después del stripping, False en caso contrario.
    """
    return bool(texto.strip())
    # La función 'strip()' elimina los espacios en blanco al principio y al final de la cadena.
    # La conversión a booleano determina si la cadena resultante tiene algún contenido.

def validar_letras_y_espacios(texto):
    """
    Valida si una cadena de texto contiene únicamente letras (mayúsculas y minúsculas)
    y espacios en blanco. Utiliza expresiones regulares para realizar la validación.

    Args:
        texto (str): La cadena de texto a validar.

    Returns:
        bool: True si la cadena cumple con el patrón, False en caso contrario.
    """
    return bool(re.fullmatch(r'[a-zA-Z\s]+', texto))
    # 're.fullmatch()' intenta hacer coincidir toda la cadena con el patrón dado.
    # El patrón r'[a-zA-Z\s]+' especifica:
    #   - [a-zA-Z]: cualquier letra mayúscula o minúscula.
    #   - \s: cualquier carácter de espacio en blanco (espacio, tabulador, nueva línea, etc.).
    #   - +: uno o más de los caracteres precedentes.

def validar_numero(mensaje):
    """
    Solicita al usuario ingresar un valor numérico y valida si la entrada es un número
    real (float) positivo. Continúa solicitando la entrada hasta que se proporcione un valor válido.

    Args:
        mensaje (str): El mensaje que se mostrará al usuario para solicitar la entrada.

    Returns:
        float: El número real positivo ingresado por el usuario.
    """
    while True:
        try:
            valor_str = input(mensaje)
            valor = float(valor_str)
            if valor >= 0:
                return valor
            else:
                print("El valor debe ser un número positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")
        # El bloque 'try-except' maneja la excepción 'ValueError' que ocurre si la entrada
        # no se puede convertir a un número real. El bucle 'while True' asegura que la
        # función siga pidiendo la entrada hasta que sea válida.

def validar_cantidad(mensaje):
    """
    Solicita al usuario ingresar una cantidad y valida si la entrada es un número entero
    positivo. Continúa solicitando la entrada hasta que se proporcione un valor válido.

    Args:
        mensaje (str): El mensaje que se mostrará al usuario para solicitar la entrada.

    Returns:
        int: El número entero positivo ingresado por el usuario.
    """
    while True:
        try:
            valor_str = input(mensaje)
            valor = int(valor_str)
            if valor >= 0:
                return valor
            else:
                print("Cantidad inválida, debe ser un entero positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")
        # Similar a 'validar_numero', pero esta función asegura que la entrada sea un entero.

def agregar_producto():
    """
    Permite al usuario agregar un nuevo producto al inventario. Solicita el nombre,
    precio y cantidad del producto, realizando validaciones en el nombre y los valores numéricos.
    Verifica si el producto ya existe en el inventario antes de agregarlo.
    """
    while True:
        nombre = input("Ingrese el nombre del producto: ").strip().lower()
        # Se solicita el nombre del producto, se eliminan los espacios en blanco y se convierte a minúsculas.
        if not validar_letras_y_espacios(nombre):
            print("El nombre del producto no puede contener números o caracteres especiales.")
            continue
            # Si el nombre no cumple con los criterios de validación, se informa al usuario y se reinicia el bucle.

        if nombre in [item['nombre'] for item in inventario]:
            print(f"El producto {nombre} ya existe. Si desea actualizar la información de {nombre}, seleccione la opción 3.")
            return
            # Se verifica si el nombre del producto ya existe en el inventario. Si existe, se informa al usuario
            # y se termina la función para evitar duplicados.

        precio = validar_numero("Ingrese el precio del producto: ")
        # Se solicita y valida el precio del producto utilizando la función 'validar_numero'.

        cantidad = validar_cantidad("Ingrese la cantidad de productos que desea agregar al inventario: ")
        # Se solicita y valida la cantidad del producto utilizando la función 'validar_cantidad'.

        producto = {'nombre': nombre, 'precio': precio, 'cantidad': cantidad}
        # Se crea un nuevo diccionario 'producto' con la información ingresada.

        inventario.append(producto)
        # El nuevo producto se añade a la lista 'inventario'.

        print(f"El producto '{nombre}' ha sido agregado exitosamente al inventario.")
        break
        # Se informa al usuario del éxito de la operación y se sale del bucle.

def consultar_producto():
    """
    Permite al usuario buscar un producto por su nombre en el inventario y muestra sus detalles
    (nombre, precio y cantidad) si se encuentra. Realiza validación en el nombre ingresado.
    """
    while True:
        nombre_producto = input("Ingrese el nombre del producto que desea buscar: ").strip().lower()
        valido = all(caracter.isalpha() or caracter == "" for caracter in nombre_producto)
        # Se solicita el nombre del producto a buscar, se eliminan los espacios y se convierte a minúsculas.
        # Se realiza una validación para asegurar que el nombre solo contenga letras y espacios.

        if valido and nombre_producto:
            break
        else:
            print("El nombre del producto no debe contener números o caracteres especiales.")
            # Si el nombre no es válido, se informa al usuario y se reinicia el bucle.

    encontrado = False
    for producto in inventario:
        if producto['nombre'].lower() == nombre_producto.lower():
            print("\n--- Detalles del Producto ---")
            print(f"Nombre: {producto['nombre']}")
            print(f"Precio: ${producto['precio']:.2f}")
            print(f"Cantidad: {producto['cantidad']}")
            encontrado = True
            break
            # Se itera sobre el inventario para buscar un producto con el nombre ingresado (ignorando mayúsculas).
            # Si se encuentra el producto, se imprimen sus detalles y se marca 'encontrado' como True.

    if not encontrado:
        print(f"No se encontró ningún producto con el nombre '{nombre_producto}'.")
        # Si el bucle termina sin encontrar el producto, se informa al usuario.

def actualizar_precio():
    """
    Permite al usuario modificar el precio de un producto existente en el inventario.
    Solicita el nombre del producto a actualizar y el nuevo precio, realizando validaciones.
    """
    nombre_a_actualizar = input("Ingrese el nombre del producto que desea actualizar: ").strip().lower()
    # Se solicita el nombre del producto a actualizar, se eliminan los espacios y se convierte a minúsculas.

    existe = False
    for producto in inventario:
        if producto['nombre'].lower() == nombre_a_actualizar:
            try:
                nuevo_precio = float(input(f"Ingrese el nuevo precio para '{producto['nombre']}': "))
                if nuevo_precio < 0:
                    print("El precio no puede ser negativo.")
                    return
                producto['precio'] = nuevo_precio
                print(f"El precio de '{producto['nombre']}' ha sido actualizado a ${nuevo_precio:.2f}")
                existe = True
            except ValueError:
                print("Entrada inválida, por favor ingrese un número válido para el precio.")
            break
            # Se busca el producto en el inventario por su nombre (ignorando mayúsculas).
            # Si se encuentra, se solicita el nuevo precio y se intenta convertir a float.
            # Se valida que el nuevo precio no sea negativo. Si la entrada no es un número,
            # se maneja la excepción 'ValueError'.

    if not existe:
        print(f"No se encontró ningún producto con el nombre '{nombre_a_actualizar}'.")
        # Si no se encuentra el producto, se informa al usuario.

def eliminar_producto():
    """
    Permite al usuario eliminar un producto del inventario. Solicita el nombre del producto
    a eliminar y, si se encuentra, lo elimina de la lista 'inventario'.
    """
    nombre_a_eliminar = input("Ingrese el nombre del producto que desea eliminar: ").strip()
    # Se solicita el nombre del producto a eliminar y se eliminan los espacios.

    indice_a_eliminar = -1
    for i, producto in enumerate(inventario):
        if producto['nombre'].lower() == nombre_a_eliminar.lower():
            indice_a_eliminar = i
            break
            # Se itera sobre el inventario para encontrar el índice del producto a eliminar
            # (ignorando mayúsculas en la comparación de nombres).

    if indice_a_eliminar != -1:
        producto_eliminado = inventario.pop(indice_a_eliminar)
        print(f"El producto '{producto_eliminado['nombre']}' ha sido eliminado exitosamente del inventario.")
        # Si se encuentra el producto, se elimina de la lista usando 'pop()' y se informa al usuario.
    else:
        print(f"No se encontró ningún producto con el nombre '{nombre_a_eliminar}'.")
        # Si no se encuentra el producto, se informa al usuario.

def calcular_valor_total():
    """
    Calcula el valor total del inventario multiplicando el precio por la cantidad de cada producto
    y sumando estos valores. Muestra el resultado con dos decimales.
    """
    valor_total = 0
    for producto in inventario:
        valor_total += producto['precio'] * producto['cantidad']
        # Se itera sobre el inventario y se acumula el valor de cada producto.

    print(f"\nEl valor total del inventario es: ${valor_total:.2f}")
    # Se muestra el valor total formateado a dos decimales.

def mostrar_inventario():
    """
    Muestra el inventario actual en detalle, listando el nombre, precio y cantidad de cada producto.
    Si el inventario está vacío, se informa al usuario.
    """
    if not inventario:
        print("El inventario está vacío.")
        return
        # Si la lista 'inventario' está vacía, se muestra un mensaje informativo y se termina la función.

    print("\n--- Inventario ---")
    for producto in inventario:
        print(f"Nombre: {producto['nombre']}")
        print(f"Precio: ${producto['precio']:.2f}")
        print(f"Cantidad: {producto['cantidad']}")
        print("-" * 20)
        # Se itera sobre el inventario y se imprimen los detalles de cada producto con un formato claro.

# Menú principal para interactuar con el inventario
while True:
    print("\n--- Menú ---")
    print("1. Agregar producto")
    print("2. Consultar producto")
    print("3. Actualizar precio del producto")
    print("4. Eliminar producto")
    print("5. Calcular valor total del inventario")
    print("6. Mostrar inventario completo")
    print("7. Salir")

    opcion = input("Seleccione una opción: ")
    # Se muestra el menú de opciones al usuario y se solicita que seleccione una.

    if opcion == '1':
        agregar_producto()
    elif opcion == '2':
        consultar_producto()
    elif opcion == '3':
        actualizar_precio()
    elif opcion == '4':
        eliminar_producto()
    elif opcion == '5':
        calcular_valor_total()
    elif opcion == '6':
        mostrar_inventario()
    elif opcion == '7':
        print("Adiós")
        break
        # Se ejecutan las funciones correspondientes según la opción seleccionada por el usuario.
        # La opción '7' termina el bucle principal y finaliza el programa.

    else:
        print("Opción inválida, por favor intente de nuevo.")
        # Si la opción ingresada no es válida, se informa al usuario.


# PARTE 1 - DEFINICIÓN DE VARIABLES


# String
nombre_tienda = "ElectroTech"

# Lista de productos
productos = ["Laptop", "Tablet", "Celular", "Auriculares", "Monitor"]

# Diccionario (Inventario con precios)
inventario = {
    "Laptop": 1200.50,
    "Tablet": 350.99,
    "Celular": 799.00,
    "Auriculares": 50.99,
    "Monitor": 200.00
}

# Int (cantidad de productos disponibles)
cantidad_productos = len(productos)

# Float (precio promedio calculado automáticamente)
precio_promedio = sum(inventario.values()) / len(inventario)

# Bool
tienda_abierta = True

# Mostrar información
print(f"Tienda: {nombre_tienda}")
print(f"Cantidad de productos: {cantidad_productos}")
print(f"Precio promedio: {precio_promedio:.2f}")
print(f"¿Tienda abierta?: {tienda_abierta}")
print("Productos disponibles:", productos)
print("Inventario:", inventario)

#parte 2
ventas_totales = 0

def tienda_estado():
	global tienda_abierta
	tienda_abierta = not tienda_abierta
	print(f"La tienda esta", {'Abierta' if tienda_abierta else 'Cerrado'})

def registro_venta(productos, cantidad):
	global ventas_totales

	if productos in inventario:
		ventas_totales += inventario[productos] * cantidad
		print(f"Venta regristrada: {cantidad} {productos}(s) por ${inventario[productos] * cantidad}")

	else:
		print("Producto no disponible")

tienda_estado()
registro_venta("Monitor", 2)
print("Ventas Totales:", ventas_totales)

# PARTE 3

# Agregar un nuevo producto
def agregar_producto(nombre, precio):
    productos.append(nombre)
    inventario[nombre] = precio
    print(f"Producto {nombre} agregado con precio ${precio}")

# Eliminar un producto
def eliminar_producto(nombre):
    if nombre in productos:
        productos.remove(nombre)
        del inventario[nombre]
        print(f"Producto {nombre} eliminado correctamente")
    else:
        print("El producto no existe")

# Actualizar el precio de un producto
def actualizar_precio(nombre, nuevo_precio):
    if nombre in inventario:
        inventario[nombre] = nuevo_precio
        print(f"Precio de {nombre} actualizado a ${nuevo_precio}")
    else:
        print("El producto no existe")

# Mostrar inventario
def mostrar_inventario():
    print("Productos disponibles:")
    for nombre, precio in inventario.items():
        print(f"{nombre}: ${precio}")

agregar_producto("Mouse", 25.99)
agregar_producto("Docking", 25.99)
actualizar_precio("Mouse", 25.00)
eliminar_producto("Docking")
mostrar_inventario()
# PARTE 4

# Calcular el precio total del inventario
def calcular_precio_total():
    total = sum(inventario.values())
    print(f"Precio total del inventario: ${total}")

# Filtrar productos por rango de precio
def filtrar_por_precio(precio_min, precio_max):
    print(f"Productos entre ${precio_min} y ${precio_max}:")
    for nombre, precio in inventario.items():
        if precio_min <= precio <= precio_max:
            print(f"{nombre}: ${precio}")

# Reporte de ventas acumuladas
def reporte_ventas():
    print(f"Ventas acumuladas: ${ventas_totales}")

calcular_precio_total()
filtrar_por_precio(50, 1000)
reporte_ventas()

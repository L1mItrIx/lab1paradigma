
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
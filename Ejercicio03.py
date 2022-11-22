# Escribir un programa que guarde en un diccionario los precios de los artículos de la tabla,
# pregunte al usuario por un artículo, un número de unidades y muestre por pantalla el precio de esa cantidad de producto.
# Si el producto no está en el diccionario debe mostrar un mensaje informando de ello.

productos = {'Pan': 1.40, 'Huevos': 2.30, 'Cebolla': 0.85, 'Aceite': 4.35}

articulo = input("Introduce un articulo:")
unidades = float(input("Introduce una cantidad:"))

if articulo.title() in productos:
    print("Por", round(unidades), "unidades debes pagar",productos[articulo.title()]*unidades)
else:
    print("No se encuentra el producto introducido.")

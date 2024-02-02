#Realiza un programa que use un diccionario para gestionar los productos
#Y precios de la tabla, donde se le pregunte al usuario por un producto
#Y la cantidad, al finalizar mostrar en la consola el precio total, si
#El producto no esta debe mostrar un mensaje informando sobre ello

verduleria = {"Inventario": ("Tomates", "Cebollas", "Pepinos"),
               "Precios": (2500, 3500, 3000)}
print("Inventario actual: ")
print(verduleria)

produc = str (input("Ingrese lo que desea comprar de la lista anterior: "))

cantidad = int (input("Ingrese la cantidad que desea de este producto: "))

produc = produc.capitalize()

precioTotal = int

if produc in verduleria["Inventario"] :

    buscarProducto = verduleria["Inventario"].index(produc)
    precioTotal = verduleria["Precios"][buscarProducto]
    precioTotal = precioTotal * cantidad
    print(f"El precio total es de $",precioTotal,)
else:
    print("El producto esta agotado actualmente.")

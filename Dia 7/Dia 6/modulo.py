def si():
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

def largue_num(num):
    res = (num > 10000)

def negate(num):
    return -num


import math

def Colision(bola1, bola2):
    x1, y1, r1 = bola1
    x2, y2, r2 = bola2
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance <= r1 + r2

def Colision2(bola1, bola2):
    x1, y1, z1, r1 = bola1
    x2, y2, z2, r2 = bola2
    distance_euclides = math.sqrt((x2 - x1)**2 + (y2 - y1)) + (z2 - z1)**2
    print(distance_euclides)
    return distance_euclides <= r1 + r2
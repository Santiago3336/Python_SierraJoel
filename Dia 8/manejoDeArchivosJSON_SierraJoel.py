import json
import itemgetter

# #Separe por partes el archivo json para poder manipularlo
# ejercicio1 = open("data.json")
# ejercicio = json.load(ejercicio1)
# clientes = ejercicio["ventas"]["clientes"]
# print(clientes)
# print(type(clientes))
# print("COMERCIALES\n")
# comerciales = ejercicio["ventas"]["comerciales"]
# print(comerciales)
# print(type(ejercicio))
# print("PEDIDOS\n")
# pedidos = ejercicio["ventas"]["pedidos"]
# print(pedidos)
# print(type(ejercicio))

#Ejercicio 1
with open("data.json",'r') as ArchivoJson:
    ejercicio = json.load(ArchivoJson)
def ObtenerFecha(pedido):
    return pedido["fecha"]

pedidos = ejercicio["ventas"]["pedidos"]

PedidosOrdenados = sorted(pedidos, key=ObtenerFecha, reverse=True)

#print(pedidos_ordenados)

with open('Ejercicio1.json', 'w') as outfile:
    json.dump(PedidosOrdenados, outfile, indent=2)

#Ejercicio 2
with open("data.json",'r') as file:
    ejercicio = json.load(file)
    
def ObtenerTotal(pedido):
    return pedido["total"]

pedidos = ejercicio["ventas"]["pedidos"]

PedidosOrdenados = sorted(pedidos, key=ObtenerTotal, reverse=True)[:2]

#print(pedidos_ordenados)

with open('Ejercicio2.json', 'w') as outfile:
    json.dump(PedidosOrdenados, outfile, indent=2)

#Ejercicio 3

with open('data.json', 'r') as file:
    ejercicio = json.load(file)
    
ClientesConPedidos = set() 
for pedido in ejercicio["ventas"]["pedidos"]:
    ClientesConPedidos.add(pedido["id_cliente"]) 
# print(clientes_con_pedidos)

ClientesConPedidos = list(ClientesConPedidos) 

with open('Ejercicio3.json', 'w') as outfile:
    json.dump(ClientesConPedidos, outfile, indent=2)

#Ejercicio 4
with open('data.json', 'r') as file:
    ejercicio = json.load(file)

Pedidos2017Mas500 = []

for pedido in ejercicio["ventas"]["pedidos"]:
    
    año_pedido = int(pedido["fecha"].split("-")[0]) 
    
    if año_pedido == 2017 and pedido["total"] > 500:
        Pedidos2017Mas500.append(pedido)

with open('Ejercicio4.json', 'w') as outfile:
    json.dump(Pedidos2017Mas500, outfile, indent=2)

#Ejercicio 5
with open('data.json', 'r') as file:
    ejercicio = json.load(file)

ComercialesQueCumplen = []

for comercial in ejercicio["ventas"]["comerciales"]:
    
    comision = comercial["comision"]

    if 0.05 <= comision <= 0.11:
        nombre_apellidos = f"{comercial['nombre']} {comercial['apellido1']} {comercial['apellido2']}"
        ComercialesQueCumplen.append(nombre_apellidos)

with open('Ejercicio5.json', 'w') as outfile:
    json.dump(ComercialesQueCumplen, outfile, indent=2)

#Ejercicio 6
with open('data.json', 'r') as file:
    ejercicio = json.load(file)

MayorComision = 0

for comercial in ejercicio["ventas"]["comerciales"]:
    
    comision = comercial["comision"]
    
    if comision > MayorComision:
        MayorComision = comision

with open('Ejercicio6.json', 'w') as outfile:
    json.dump({"MayorComision": MayorComision}, outfile, indent=2)

# 7. Clientes de Sevilla ordenados alfabéticamente
with open('data.json', 'r') as data:
    ejercicio = json.load(file)
clientesSevilla = sorted([{'id': cliente['id'], 'nombre': cliente['nombre'], 'apellido1': cliente['apellido1']} for cliente in
     data['ventas']['clientes'] if cliente['ciudad'] == 'Sevilla'],
    key=itemgetter('apellido1', 'nombre'))
print("\n7. Clientes de sevilla ordenados:")
print(clientesSevilla)

# 8. Nombres de clientes que empiezan por A y terminan por N, y nombres que empiezan por P
nombresANP = sorted(
    [cliente['nombre'] for cliente in data['ventas']['clientes'] if
     (cliente['nombre'].startswith('A') and cliente['nombre'].endswith('n')) or
     cliente['nombre'].startswith('P')])
print("\n8. Nombres de clientes que cumplen la condición:")
print(nombresANP)

# 9. Nombres de los clientes que empiezan por la letra A
nombresA = sorted([cliente['nombre'] for cliente in data['ventas']['clientes'] if cliente['nombre'].startswith('A')])
print("\n9. Nombres de clientes que empiezan por A:")
print(nombresA)

# 10. Comerciales que tengan el apellido "Ruiz"
apellidoRuiz = set([comercial['nombre'] for comercial in data['ventas']['comerciales'] if
                      'Ruiz' in comercial['apellido1']])
print("\n10. Nombres de comerciales con apellido 'Ruiz' (sin duplicados):")
print(apellidoRuiz)


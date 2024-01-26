## ----------------------------------------------------------------
## ---- Ejercicio 1 ----
## ----------------------------------------------------------------

#Impresión en consola
print("Hola, mundo")

# ---- Datos Primitivos ----
# 1. String
texto = "Campus"
print(texto)
print(type(texto))
# 2. INT
numeroEntero = 3
print(numeroEntero)
print(type(numeroEntero))
# 3. Float
numeroDecimal = 3.1
print(numeroDecimal)
print(type(numeroDecimal))
# 4. Double
numeroDecimalLargo = 3.141656465432196874654
print(numeroDecimalLargo)
print(type(numeroDecimalLargo))
# 5. Boolean
booleanoyi = True
print(booleanoyi)
print(type(booleanoyi))

# ---- Entradas parte del usuario ----
entradaUsuario = input("Ingresa tu nombre: ")
print("Tu nombre es: ", entradaUsuario)

# ---- Entradas parte del usuario con definición de tipo de dato primitivo ----
entradaUsuarioNumero = int(input("Ingresa tu edad: "))
print ("Tu edad es: ", entradaUsuarioNumero )


numeroFinal = int(entradaUsuarioNumero)
print(numeroFinal)

# ---- Ciclos ----
# Ciclo FOR

for i in range(5):
    print(i)

# Ciclo FOR 2.0
    
for i in range (5,10,2): #for 'contador' in range (desde,hasta,pasos):
    print(i)

# Ciclo WHILE
booleanito = True
while booleanito == True: #while 'condicion_a_cumplir':
    print("Sigo vivo")
    booleanito = False

# ---- Condicionales ----
texto1 = "Campus"
if texto1 == "Campus":
    print("Soy campus")
else:
    print("No soy campus")

# ---- Funciones ----

# Sin Parametro Sin Retorno

def saludo():
    print("HOLA")

saludo()

# Sin Parametro Con Retorno

def result():
    resultado = 3 * 5
    return resultado

print(result())

# Con Parametro Sin Retorno
def mostrarMisDatos(a,b):
    name = a
    num = b
    print("Bienvenido ", name, " ", num )

mostrarMisDatos('Santiago', 3160514020)

# Con Parametro Con Retorno

def promedio(x,y):
    sumaTotal = x
    cantidad = y
    Total = sumaTotal/cantidad
    return"Su promedio es: ", float(( Total ))

sumaTotal =  input("Ingrese la suma total: ")
cantidad = input("Ingrese la cantidad de digitos: ")

print(promedio(int(sumaTotal),int(cantidad)))

# ---- Arrays ----

listao = list(['Yiyo', 'Sacha', 'Bruno', 'Terry', 'Niña', 'Perla', 'Sparky', 'Laika', 'Princesa', 'Fiorela'])
print(listao[4])

#Diccionario
dict={
    'lote': "2 pisos", 
    'lote1': "4 pisos"
}

print(dict['lote'])



## Desarrollado por Joel Santiago Sierra Leon - 1097492869
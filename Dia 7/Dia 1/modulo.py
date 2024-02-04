# Sin Parametro Sin Retorno

def saludo():
    print("HOLA")

# Sin Parametro Con Retorno

def result():
    resultado = 3 * 5
    return resultado

# Con Parametro Sin Retorno
def mostrarMisDatos(a,b):
    name = a
    num = b
    print("Bienvenido ", name, " ", num )

# Con Parametro Con Retorno

def promedio(x,y):
    sumaTotal = x
    cantidad = y
    Total = sumaTotal/cantidad
    return"Su promedio es: ", float(( Total ))
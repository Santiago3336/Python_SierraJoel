from modulo import funcionFiboDia2

print(funcionFiboDia2())

a = 0
b = 1
c = int

# cond sera la condicion para el Ciclo While, la defino como entero para el requerimiento del 0 y 1

cond = int

cond = int(input("Para continar con la secuencia escribe \n  0 para No | 1 para Si \n "))
if cond == 0 or 1:
    while cond == 1:
        for i in range(0,1,1):
            print(a)
            c = a + b
            a = b
            b = c
        cond = int(input("Para continar con la secuencia escribe \n  0 para No | 1 para Si \n "))
    if cond == 0:
        print ("Has decidido acabar con la secuencia")
else:
    print("Favor solo digite 0 o 1")

## Desarrollado por Joel Santiago Sierra Leon - 1097492869
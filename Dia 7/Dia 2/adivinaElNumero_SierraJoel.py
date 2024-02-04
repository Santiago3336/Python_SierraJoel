from modulo import funcionDia2
import random

funcionDia2()

numPrograma = int
numUsuario = int
intentos = int

numPrograma = random.randint(1,100)

for i in range(1,11,1):
    while numUsuario != numPrograma:
        for j in range(1,11,1):
            print("Intento: ", j)
            numUsuario = int(input("Intenta adivinar el numero "))
            intentos = 0+j
            if i == 10:
                print("No tienes mas intentos 🙁\nVuelve a intentarlo")
            else:
                if numUsuario > numPrograma:
                    print("Pista: \nEl numero que debes adivinar es menor del que ingresaste 🤫")
                elif numUsuario < numPrograma:
                    print("Pista: \nEl numero que debes adivinar es mayor del que ingresaste 🤫")
            if numUsuario == numPrograma:
                print("¡ADIVINASTE EL NUMERO!\nLo lograste en: ", intentos ," intentos", "\nEres el GANADOR🏆")
                break

## Desarrollado por Joel Santiago Sierra Leon - 1097492869
import random

print("Bienvenido a: \n !ADIVINA EL NUMERO¡ \nEl juego consta de:\n1.Habra un numero de 1 a 100\n2.Tu como usuario deberas intentar adivinar el numero\n3.El programa ira arrojando pistas segun te acerques al numero\n4.Tienes un maximo de 10 intenos\n  !Buena Suerte¡")

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
    
        






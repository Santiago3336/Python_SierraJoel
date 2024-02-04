from modulo import pares

T = int(input())
for case in range(T):
    text = input("")
    nums = input("")
    n = 0
    k = 0
    T_n = list()
    textoLista = text.split(" ")
    numsLista = nums.split(" ")
    n = int(textoLista[0])
    k = int(textoLista[1])
    for p in range(n):
        number = int(numsLista[p])
        T_n.append(abs(number))
    result = pares(T_n, n, k)
    print("Case {}: {}".format(case + 1, result))
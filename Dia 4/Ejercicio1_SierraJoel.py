def pares(T_n,n,k):
    pairs=set()
    for i in range(n):
        for j in range(i+1,n):
            if (T_n[i]+T_n[j] % k == 0):
                pairs.add((min(T_n[i],T_n[j]), max(T_n[i],T_n[j])))
            return len(pairs)
        
T = int(input())
for case in range(T):
    texto = input("")
    numeros = input("")
    n = 0
    k = 0
    T_n = list()
    textoLista = texto.split(' ')
    numerosLista = numeros.split(' ')
    #print(textoLista)
    n = int(textoLista[0])
    k = int(textoLista[1])
    #print(numerosLista)
    for p in range(n):
        numerito = int(numerosLista[p])
        T_n.append(abs(numerito))
    result = pares (T_n,n,k)
    print("Case {}:{}".format(case+1,result))
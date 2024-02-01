def pares(T_n,n,k):
    pairs=set()
    for i in range(n):
        for j in range(i+1,n):
            if (T_n[i]+T_n[j] % k == 0):
                pairs.add((min(T_n[i],T_n[j]),max(T_n[i],T_n[j])))
            return len(pairs)
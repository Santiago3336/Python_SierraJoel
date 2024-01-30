coin1 = 10
coin2 = 5
coin3 = 1

quantityCoin = 0
quantityCoin1 = 0
quantityCoin2 = 0
quantityCoin3 = 0

def main(quantityCoin):
    return quantityCoin + 1
    

value = int(input(""))


if value >= 1001:
    print("")
else:
    while value > 9:
        for i in range(0,1,1):
            value = value - coin1
            quantityCoin = main(quantityCoin)
            quantityCoin1 = quantityCoin1 + 1
    while value > 4:
        for i in range(0,1,1):
            value = value - coin2
            quantityCoin = main(quantityCoin)
            quantityCoin2 = quantityCoin2 + 1

    while value >= 1:
        for i in range(0,1,1,):
            value = value - coin3
            quantityCoin = main(quantityCoin)
            quantityCoin3 = quantityCoin3+1

    print(quantityCoin)
    totalQuantityCoin1 = 1 * quantityCoin1
    totalQuantityCoin2 = 1 * quantityCoin2
    totalQuantityCoin3 = 1 * quantityCoin3
    print("10 = ",  totalQuantityCoin1, " 5 = ", totalQuantityCoin2, " 1 = ", totalQuantityCoin3)

## Desarrollado por Joel Santiago Sierra Leon - 1097492869
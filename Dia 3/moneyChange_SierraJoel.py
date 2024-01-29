coin1 = 10
coin2 = 5
coin3 = 1

quantityCoin = 0

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

    while value > 4:
        for i in range(0,1,1):
            value = value - coin2
            quantityCoin = main(quantityCoin)

    while value >= 1:
        for i in range(0,1,1,):
            value = value - coin3
            quantityCoin = main(quantityCoin)

    print(quantityCoin)


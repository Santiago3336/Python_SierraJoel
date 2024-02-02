##Encontrar 3 Bugs del siguiente codigo:

def negate(num):
    return -num

def largue_num(num):
    res = (num > 10000)

negate(b)
neg_b = num
print 'b:', b, 'neg_b:', neg_b

big = largue_num(b)
print 'b is big:', big

##BUGS:

#1 Se usa la función negate y se asigna despues como neg_b
#2 Los prints no contienen los parentesis por ende generara un error
#3 Variable b no definida
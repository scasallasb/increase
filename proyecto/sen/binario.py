def binarizar(decimal):
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario


for i in range(0,16):
    numero = binarizar(i)
    print (numero)
    print ("///")
    for j in numero:
        print (j)

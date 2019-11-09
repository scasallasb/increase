p= "101"
listAngulos=[10,20,30,40]
cont = 0
for i  in range (0, len(p)):
    pos= int(p[i])*listAngulos[len(listAngulos)-len(p) + i]
    cont += pos
print (cont)

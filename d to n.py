nDecimal = eval(input("entrer un décimal positif :"))
print("Le nombre décimal entrer est:", nDecimal)
nbin=[]
while nDecimal > 0:
    value = int(nDecimal / 2)
    # print (value)
    nDecimal = int(nDecimal & 2)
    nbin.append(value)
nbin.reverse()
print("Le nombre binaire est", end=": ")
for x in nbin:
    print(x, end='')

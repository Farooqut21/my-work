#3.32
n = eval(input("Enter n "))
x = 1
while(n/(10*x)!=0):
    x=x*10
while(n>0):

    x = x/n
    print(int(n/x))

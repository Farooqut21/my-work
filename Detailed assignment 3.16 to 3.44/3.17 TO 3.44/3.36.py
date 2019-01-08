#3.36
def reverse_int(n):
    x=0
    while(n!=0):
        x*=10
        x+=n%10
        n=n//10
    return x

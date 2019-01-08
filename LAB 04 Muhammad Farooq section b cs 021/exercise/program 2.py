#2. Calculate the arithmetic sequence of n numbers. The program will generate the nth term of the sequence, whereas the user will enter the first term and the common difference. The program will then ask either to continue or not, if the user will enter yes it will ask the next nth term to calculate.2. Calculate the arithmetic sequence of n numbers. The program will generate the nth term of the sequence, whereas the user will enter the first term and the common difference. The program will then ask either to continue or not, if the user will enter yes it will ask the next nth term to calculate.
a1=int(input("the first number"))
n=int(input("the n number"))
d=int(input("the difference of  number"))
Tn=a1+(n-1)*d
print("the tn term is",Tn)

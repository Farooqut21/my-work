#program 5:Write a program which takes the initial and final values from the user then print the sum ofall the number.
i_value=eval(input("enter the initial value for the range:"))
f_value=eval(input("enter the final value for the range"))
n=range(i_value,f_value)
sum=0
for value in n:
    sum=sum+value
    print("the sum is",sum)
             

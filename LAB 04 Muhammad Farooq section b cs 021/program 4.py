#program 4:Write a program which takes the lower limit and upper limit then find which of the numberare prime number.
a_limit=int(input("enter lower limit range"))
b_limit=int(input("enter upper limit range"))
print("prime number between",a_limit,b_limit,"are")
for number in range(a_limit,b_limit+1):
    if number>1:
        for i in range(2,number):
            if (number%i)==0:
                break
            else:
                print(number)

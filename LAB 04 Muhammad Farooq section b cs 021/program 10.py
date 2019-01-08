#Program 10: Write a Python program to construct the following pattern, using a nested for loop
n=3
for a in range(n):
    for j in range(a):
        print("*",end="")
    print("")
    for a in range(n,0,-1):
        for j in range(a):
            print("*",end="")
        print ("") 

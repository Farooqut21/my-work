#program 11: Write a program which calculates the vowels from the given string.
print("this program will count total number of vowels from user defined sentence")
s=input("enter your string:")
vowels=0
for a in s:
    if (a=="a"or a=="e"or a=="i"or a=="o"or a=="u"or a=='A' or a=='E' or a=='I' or a=='O' or a=='U'):
        vowels=vowels+1
print("number of vowels are:")
print(vowels)
        
        

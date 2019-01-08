#Program 8: Write a program to generate the ASCII Chart from 0 to 256.
print("\t\t\t ASCCII Character")
for i in range(0,256):
    print(i,"=",chr(i),end="\t") #end="\t" is used to place a tab after the displayed string instead of a newline.
    print("\n")

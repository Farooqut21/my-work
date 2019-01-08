#3. Write a program which will check either the giving string is Palindrome or not. Palindrome is a string when we reverse the string it will generate the original string. Example CIVIC, MOM, 010, 1001, etc. So if you enter the word which is Palindrome it will say yes your string is Palindrome otherwise it will generate sorry message.
word=input("enter your word")
print (word[::-1])
if (word==word[::-1]):
    print("yes the word is palidrome")
else:
    print("sorry")

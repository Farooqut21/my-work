#Implement a program that requests from the user a list of words (i.e., strings) and then prints on the screen, one per line, all four-letter strings in the list.
list=[] # create empty list
first_word = input('Enter first word: ')
second_word = input('Enter second word: ')
third_word= input('Enter third word: ')
list.append(first_word)
list.append(second_word)
list.append(third_word)
for i in list:
    print(i)

list=[] # create empty list
first_num = int(input('Enter first int: '))
second_num = int(input('Enter second int: '))
third_num= int(input('Enter third int: '))
list.append(first_num)
list.append(second_num)
list.append(third_num)
def even(list):
    for a in list:
        if a%2==0:
            return True
    return False


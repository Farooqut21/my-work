#3.16
lst=[1,2,3,4]
def swapFL(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    print(lst)

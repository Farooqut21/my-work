#Program 7: Write a program which will check the data type of given data in a loop.
d_list=[300,12.65,5+6j,True,'faisal',(5,-7),[8,52],{"color":"blue","color":"red"}]
for item in d_list:
    print("type of ",item,"is",type(item))

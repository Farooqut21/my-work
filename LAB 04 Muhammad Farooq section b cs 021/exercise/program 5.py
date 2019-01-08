#5. Generate a table from initial value to final, depending upon the user starting and ending range in matrix
row=1
initial=int(input("give the initial value"))
final=int(input("give the final value"))
multiList=[[0 for col in range(final+1)]for row in range(row)]
for a in range(initial,final+1):
    for b in range(initial,final+1):
        multiList[0][b]=a*b
    print(multiList)   


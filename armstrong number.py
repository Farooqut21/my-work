def armstrong(lowervalue,uppervalue):
    for num in range(lowervalue,uppervalue):
        sum=0
        x=num
        o=len(str(num))
        while x>0:
            y=x%10
            sum+=y**o
            x//=10
        if num==sum:
            print(num)

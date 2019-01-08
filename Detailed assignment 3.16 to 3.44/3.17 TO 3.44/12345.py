def digitsplitter(userinput):
    firstdig = userinput / 1000
    seconddig = (userinput / 100) - (firstdig * 10)
    thirddig = userinput / 10 - ((userinput/100) * 10)
    fourthdig = userinput - ((userinput / 10) * 10)
 
    print (firstdig, seconddig, thirddig, fourthdig)

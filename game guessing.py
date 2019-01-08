correct_number=62
numberofguesses=0
guess=0
while guess<100:
    guess=int(input("enter a number from 1 to 100"))
    numberofguesses+=1
    if guess<correct_number:
         print("TOO High.Try again") 
    if guess>correct_number:
             print("Too low.Try againt")
    if guess==correct_number:
        break
if guess==correct_number:
    print("congratulations! you got in",numberofguesses,"guesses")

        
       

        
        

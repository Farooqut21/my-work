#Implement a program that starts by asking the user to enter a login id (i.e., a string). The program then checks whether the id entered by the user is in the list ['joe', 'sue', 'hani', 'sophie'] of valid users. Depending on the outcome, an appropriate message should be printed. Regardless of the outcome, your function should print 'Done.' before terminating. Here is an example of a successful login:
login_id=input('enter login id')
valid_user=['farooq','rafay','adil']
if login_id  in valid_user:
    print("you are in")
    print("done")
else:
    print("unknown user")
    print("done")
    

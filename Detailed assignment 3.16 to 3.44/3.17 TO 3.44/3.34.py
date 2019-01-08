#3.34
def pay(wage,hours):
    payment = 0
    if(hours > 40):
        payment = payment + (hours-40)*wage*1.5
        payment = payment + (40)*wage
    else:
        payment = payment + hours*wage
    return payment

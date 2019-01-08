import math
def collision(x1,y1,r1,x2,y2,r2):
    if(math.sqrt((x1-x2)**2+(y1-y2)**2) > r1+r2):
        return False
    else:
        return True

#programming exercise Q1:
import math
def areaofcylinder(h,r):
    area=2*math.pi*r*h+2*math.pi*(r**2)
    print("the area of the cylinder is",format(area)+"cm\u00b2")
def volumeofcylinder(h,r):
    volume=math.pi*(r**2)*h
    print("the volume of the cylinder is",format(volume)+"cm\u00b3")

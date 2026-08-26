import math
def circle_stats(radius):
     area= math.pi*(radius**2)
     circumference=2*math.pi*radius
     return area,circumference


area,circumference=circle_stats(2)
print("area is : ",round(area,2))
print("circumference : ",round(circumference,2))
import math
def area_triangle(a,b,c):
    s=(a+b+c)/2
    d1=s -a
    d2=s -b
    d3=s -c
    area=math.sqrt(s*d1*d2*d3)
    print(area)
area_triangle(3,4,5)    


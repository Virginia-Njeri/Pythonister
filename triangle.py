import math
def triangle_area():
    a=float(input("Enter your number: "))#area of triangle
    b=float(input("Enter your number: "))
    c=float(input("Enter your number: "))
    s=(a+b+c)/2
    d1=s-a
    d2=s-b
    d3=s-c
    area_triangle=math.sqrt(s*d1*d2*d3)
    print(area_triangle)
triangle_area()    




   

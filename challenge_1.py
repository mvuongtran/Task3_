import math

a = float(input("Enter length of side 1 of a triangle: "))
b = float(input("Enter length of side 2 of a triangle: "))
c = float(input("Enter length of side 3 of a triangle: "))

s = (a + b + c)/2
area = math.sqrt((s*(s-a))*(s-b)*(s-c))
print(f"The area of the triangle is: {round(area,2)}")



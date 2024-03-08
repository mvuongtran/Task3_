import math

side1 = float(input("Enter length of side 1 of a triangle: "))
side2 = float(input("Enter length of side 2 of a triangle: "))
side3 = float(input("Enter length of side 3 of a triangle: "))

s = (side1 + side2 + side3)/2
area = math.sqrt((s*(s-side1))*(s-side2)*(s-side3))
print(f"The area of the triangle is: {round(area,2)}")



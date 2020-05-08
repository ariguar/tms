import math

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
if a + b > c and a + c > b and b + c > a:
    print("This is triangle!")
else:
    print("This is NOT triangle")
CAB = math.acos((b**2 + c**2 - a**2) / (2 * b * c))*180/math.pi
ABC = math.acos((c**2 + a**2 - b**2) / (2 * c * a))*180/math.pi
BCA = 180 - CAB - ABC
print("angle CAB = ", CAB)
print("angle CBA = ", ABC)
print("angle ACB = ", BCA)

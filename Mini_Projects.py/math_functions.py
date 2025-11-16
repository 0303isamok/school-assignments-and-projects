import math
def cone_volume(height, radius):
    grunnflate = radius**2*math.pi
    formel = (grunnflate * height)/3
    return round(formel, 2)
result = cone_volume(2, 2)
print(result)

def poly(a, b, c, x):
    return a*x**2 + b*x + c

a = int(input("value for a"))
b = int(input("value for b"))
c = int(input("value for c"))
x = int(input("value for x"))
result = poly(a, b, c, x)

print(result)


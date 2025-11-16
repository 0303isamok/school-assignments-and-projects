#mengden rektangler
n = 4

def f(x):
    return x**2

areal = 0
bredde = (5-1)/n

for i in range(n):
    hoyde = f(1+i*bredde)
    areal += hoyde*bredde
print(areal)
print (not (3 == 2) or 3 != 4)
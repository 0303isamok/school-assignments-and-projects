def f(x):
    value = 1 + x + ((x**2)/2) + ((x**3)/6) + ((x**4)/24)
    return value

for x in range(1,6):
    result = f(x)
    print(round(result, 2))
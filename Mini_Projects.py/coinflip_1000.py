import random as rd

heads = 0
tails = 0
for coin in range(1, 1001):

    number = rd.randint(1,2)
    if number == 1:
        heads += 1
    else:
        tails += 1
print("heads", heads)
print("tails", tails)
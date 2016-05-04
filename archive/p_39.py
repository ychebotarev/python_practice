__author__ = 'yuriic'
"""
Bloomberg LP Interview Question for SDE-2s

You have a function f1() that generates 0 or 1 with the equal probability.
Write a function f200() that generates a number between 1 and 200 with equal probability.
"""
import random
import numpy as np
import matplotlib.pyplot as plt

def f1():
    return random.randint(0,1)

def f200_obvious():
    res = 0
    for i in range(0,8):
        if f1() == 1:
            res += pow(2,i)

    if res <=200:
        return res
    return f200_obvious()

zeros = 0
ones = 0
for i in range(1,10000):
    if f1() == 1:
        ones+=1
    else:
        zeros+=1

print(zeros,ones)

d=np.zeros(201)
for i in range(1,10000):
    res = f200_obvious()
    d[res] +=1
print(d)

plt.plot(d)
plt.show()
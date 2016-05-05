"""
Write an algorithm to find out how many different summations
you can compute using numbers range from 1 to 1000. 2 constrains
1) Each valid sum must be less than 10000
2) A number can only be used once for a sum
example:
1+2+300 < 10000 is valid
1+2+300+400 < 10000 is valid
1+2+2 is not valid (2 appear twice)
"""

import numpy as np;

def bruteforce():
    limit = 10000
    sums = np.zeros(limit)
    for i in range(1,1000):
        for j in range(limit-1, -1, -1):
            if sums[j] != 0 and j + i < limit:
                sums[j+i] += 1
        sums[i] += 1

    return sum(sums)

print(bruteforce())

def sol2():
    """prove
    If some element can make sum up to N, sum up to N+1 is also possible
        if 1 is not in that list - add 1
        else if there are gaps starting with x - change x to x + 1
        else change first and last element to 1+last+1
    """
    return 10000

print(sol2())
"""
Given an array of integers and a number k, write a function that returns
true if given array can be divided into pairs such that sum of every pair is divisible by k.
"""


def solve(ar, k):
    h = {}
    for i in ar:
        h.setdefault(i % k, 0)
        h[i % k] += 1

    for i in range(k):
        if not i in h:
            continue
        if i == 0 and h[i] % 2 == 1:
            return False
        if h[i] != h[k - 1]:
            return False
    return True

print(solve([3,2,1,2],2))
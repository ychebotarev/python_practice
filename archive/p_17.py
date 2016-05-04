"""
Search an element in an array where difference between adjacent elements is 1
"""


#at every step we may skip abs(current-search)-1 elements
import math
def solve(ar,a):
    c=0
    while True:
        if ar[c]==a:
            return c
        c+=abs(ar[c]-a)
        if c>=len(ar):
            return -1

print(solve([8, 7, 6, 7, 6, 5, 4, 3, 2, 3, 4, 3],3))

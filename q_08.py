"""
Given an array with n distinct elements, convert the given array to a form where all elements are in range from 0 to n-1.
The order of elements is same, i.e., 0 is placed in place of smallest element, 1 is placed for second smallest element, …
n-1 is placed for largest element.
"""


def solve(ar):
    ar1 = sorted(ar)
    h = {}
    for i in range(len(ar1)):
        h[ar1[i]] = i

    result = []
    for i in range(len(ar1)):
        result.append(h[ar[i]])
    return result

print(solve([10, 40, 20]))

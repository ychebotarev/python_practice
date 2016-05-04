"""
Given an array, print the Next Greater Element (NGE) for every element.
The Next greater Element for an element x is the first greater element on the right side of x in array.
Elements for which no greater element exist, consider next greater element as -1.
"""

#return the index of first element from ar that is greater then a
#ar is sorted
def lookup(ar, a):
    if len(ar) == 0:
        return 0
    if len(ar) == 1:
        return 1 if a >=ar[0] else 0

    mid=len(ar)//2
    if a >= ar[mid]:
        return mid+1 if mid == len(ar)-1 else mid+lookup(ar[mid:],a)
    else:
        return lookup(ar[:mid],a)


def solve(ar):
    a1 = sorted(ar)

    for a in ar:
        pos = lookup(a1,a)
        if pos == len(a1):
            print('-1 ')
        else:
            print(a1[pos])

solve([2,7,10,3])

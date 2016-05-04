"""
Given a sorted array and a number, find the count of sum of 2 numbers greater than or iqual to that number
"""


def count_greater_pairs(ar,N):
    si = 0
    ei = len(ar)-1
    pairs = 0
    while si < ei:
        while si < ei and ar[si]+ar[ei]>N:
            ei-=1
        if si>=ei:
            break
        pairs +=(len(ar)-1)-ei
        si+=1

    return pairs


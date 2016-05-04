"""
Given an array of size n and an integer k, return the of count of distinct numbers in all windows of size k.
"""

def solve(ar,k):
    dict = {}
    for i in range(k):
        dict[ar[i]] = dict.get(ar[i], 0) + 1

    c = len(dict)
    s = 1
    while s+k <= len(ar):
        if ar[s-1] !=ar[s+k-1]:
            dict[ar[s-1]] = dict.get(ar[s-1], 0) - 1
            if dict[ar[s-1]] == 0:
                del dict[ar[s-1]]
            dict[ar[s+k-1]] = dict.get(ar[s+k-1], 0) + 1
            c = max(c,len(dict))
        s+=1
    return c

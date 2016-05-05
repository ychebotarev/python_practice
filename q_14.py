__author__ = 'yuriic'

"""
you are given 2 arrays sorted in decreasing order of size m and n respectively.

Input: a number k <= n*n and >= 1

Output: the kth largest sum(a+b) possible. where
a (any element from array 1)
b (any element from array 2)

The Brute force approach will take O(n*n). can anyone find a better logic. thnkx in advance.
"""

def kth_largest_sum(ar1,ar2,k):
    if ar1 is None or ar2 is None or len(ar1) == 0 or len(ar2) == 0:
        return 0

    in1 = len(ar1) - 1
    in2 = len(ar2) - 1

    while k > 1 and in1 > 0 and in2 > 0:
        if ar1[in1-1] + ar2[in2] > ar1[in1] + ar2[in2-1]:
            in1 -= 1
        else:
            in2 -= 1
    return -1 if 1 < k else ar1[in1]+ar2[in2]

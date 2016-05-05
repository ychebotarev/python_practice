"""
Given an array of integers, find the length of the longest sub-sequence
such that elements in the subsequence are consecutive integers,
the consecutive numbers can be in any order.
"""

def fill_subs(i, h):
    if i in h:
        if h[i] != 0:
            return h[i]
        h[i] = fill_subs(i-1, h) + 1
        return h[i]
    return 0


def longest_increasing_subsequence(ar):
    h = {}

    for elem in ar:
        h[elem] = 0

    length = 0
    for elem in ar:
        length = max(length, fill_subs(elem, h))

    return length

print(longest_increasing_subsequence([1, 9, 3, 10, 4, 20, 2]))

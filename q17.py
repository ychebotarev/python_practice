__author__ = 'yuriic'
"""
Given an array of positive and negative numbers,
arrange them in an alternate fashion such that every positive
number is followed by negative and vice-versa maintaining the order of appearance.
Number of positive and negative numbers need not be equal.
If there are more positive numbers they appear at the end of the array.
If there are more negative numbers, they too appear in the end of the array.*
"""

def solve(ar):
    i_n=-1
    i_p=-1

    i=0
    while i<len(ar):
        if ar[i]<0:
            i_n=i
            break
    if i_n == -1:
        return ar
    i=0
    while i<len(ar):
        if ar[i]>=0:
            i_p=i
            break
    if i_p == -1:
        return ar

    swap c_n with i_n



"""
In a string detect the smallest window length with highest number of distinct characters. For eg.
A = “aabcbcdbca”, then ans would be 4 as of “dbca”
"""

from collections import defaultdict


def longest_distinct(input_str):
    dict=defaultdict(0)

    res_i,res_j=-1,-1
    l=[]

    for i,c in enumerate(input_str):
        if dict[c] == 0:
            l.append(c)
        else:
            last = 0
            while last != c:
                last = l.pop()
                dict[last]=dict[last]-1
            if len(l) > res_j - res_i:
                res_j=i
                res_i=res_j-len(l)
        dict[c]=1

    if res_i == -1:
        return input_str
    return input_str[res_i:res_j]



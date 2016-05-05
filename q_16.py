"""
Given 2 set of arrays of size N(sorted +ve integers ) find the median of the resultant array of size 2N.
(dont even think of sorting the two arrays in a third array , though u can sort them. Try something better than order NLogN
"""

def find_median(ar1, ar2):
    median = len(ar1)
    in1 = 0
    in2 = 0
    while median > 0:
        if ar1[in1] < ar2[in2]:
            in1+=1
        else:
            in2+=1
        median -=1
    if in1 == len(ar1):
        return ar2[0]
    if in2 == len(ar2):
        return 0
    return
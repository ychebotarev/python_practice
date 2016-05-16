__author__ = 'yuriic'
"""
There is an array of 3-tuple, in the form of (a, 1, 5).
The first element in the tuple is the id, the second and third elements are both integers,
and the third is always larger than or equal to the second.
Assume that the array is sorted based on the second element of the tuple.
Write a function that breaks each of the 3-tuple into two 2-tuples like (a, 1) and (a, 5), and sort them according to the integer.
E.g. given (a, 1, 5), (b, 2, 4), (c, 7, 8), output (a, 1), (b, 2), (b, 4), (a, 5), (c, 7), (c, 8).
"""

def __merge(a1,a2):
    result=[]

    ind1=0
    ind2=0
    while ind1 < len(a1) and ind2 < len(a2):
        if a1[ind1][1] <a2[ind2][1]:
            result.append(a1[ind1])
            ind1+=1
        else:
            result.append(a2[ind2])
            ind2+=1
    if ind1 < len(a1):
        result.extend(a1[ind1:])
    if ind2 < len(a2):
        result.extend(a2[ind2:])
    return result

def solve(self,tuples):
    first=[]
    second=[]
    for t in tuples:
        first.append( (t[0],t[1]));
        second.append( (t[0],t[2]) )

    second = sorted(second, key=lambda t:t[1])
    return __merge(first,second)

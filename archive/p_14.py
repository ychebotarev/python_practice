"""
Design an algorithm to find all the common elements in two sorted lists of numbers.
For example, for the lists 2, 5, 5, 5 and 2, 2, 3, 5, 5, 7, the output should be 2, 5, 5.
"""
"""
def append_unique(ar,result, start):
    if len(ar) == 0 or start >= len(ar):
        return
    if len(result) == 0:
        result.append(ar[start])

    i=start
    while i < len(ar):
        if result[-1]!=ar[i]:
            result.append(ar[i])
        i+=1
"""

def common_elements(ar1, ar2):
    i1=0
    i2=0

    result=[]

    while i1 < len(ar1) and i2 < len(ar2):
        if ar1[i1] == ar2[i2]:
            result.append(ar1[i1])
            i1+=1
            i2+=1
        else:
            if ar1[i1] < ar2[i2]:
                i1+=1
            else:
                i2+=1

    return result

r = common_elements([2,5,5,5],[2,2,3,5,5,7])
print(r)
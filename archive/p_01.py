"""
You have an unordered array X of n integers. Find the array M containing
n elements where Mi is the product of all integers in X except for Xi. You may
not use division. You can use extra memory. (
"""

def solve(ar):
    res=[1]*len(ar)

    cur=1
    for i in range(0, len(ar)):
        res[i]*=cur
        cur*=ar[i]

    cur=1

    for i in range(len(ar)-1,-1,-1):
        res[i]*=cur
        cur*=ar[i]
    return res

print(solve([1,2,3]))


"""
Given an array where all elements appear even number of times except one.
All repeating occurrences of elements appear in pairs and these pairs are not adjacent
(there cannot be more than two consecutive occurrences of any element). 
Find the element that appears odd number of times.
"""

def solve(ar):
    if len(ar) == 1:
        return ar[0]
    mid = len(ar)//2
    print(ar)
    if ar[mid]!=ar[mid-1] and ar[mid] !=ar[mid+1]:
        return ar[mid]

    if ar[mid]==ar[mid-1]:
        if mid%2==1:
            return solve(ar[mid+1:])
        else:
            return solve(ar[:mid-1])

    else:
        if mid%2==1:
            return solve(ar[:mid])
        else:
            return solve(ar[mid+2:])


#a=[1,2,3,4,5]
#print(a[2:])
print(solve([1, 1, 2, 2, 3, 3, 4, 4, 3, 600, 600, 4, 4]))
print(solve([1, 1, 2]))
print(solve([1, 2, 2]))
print(solve([1, 1, 2, 2 ,3]))
print(solve([1, 1, 2, 3 ,3]))


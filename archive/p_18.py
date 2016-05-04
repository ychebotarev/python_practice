"""
Find the element that appears once in a sorted array
Given a sorted array in which all elements appear twice (one after one) and one element appears only once. Find that element in O(log n) complexity.
"""

def solve(ar):
    if len(ar) == 1:
        return ar[0]
    mid = ar[len(ar)//2]
    print(ar)
    print(len(ar)//2)
    print(mid)
    print(ar[mid])
    print(ar[mid-1])
    if ar[mid-1] != ar[mid] and ar[mid+1]!=ar[mid]:
        return ar[mid]
    return solve(ar[mid+1:]) if ar[mid-1] == ar[mid] else solve(ar[:mid])

#ar = [1, 1, 3, 3, 4, 5, 5, 7, 7, 8, 8]
#mid = ar[len(ar)//2]
#print(mid)
#print(ar[mid+1:])
#print(ar[:mid])

#print(solve([1, 1, 3, 3, 4, 5, 5, 7, 7, 8, 8]))
print(solve([1, 1, 3, 3, 4, 4, 5, 5, 7, 7, 8]))

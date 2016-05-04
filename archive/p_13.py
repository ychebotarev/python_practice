"""
Given a sorted array of integers, using the same array, shuffle the integers to have unique elements and return the index.

Sample input : [3, 3, 4, 5, 5, 6, 7, 7, 7]
Sample output : [3, 4, 5, 6, 7, X, X, X, X]
In this case, it returns an index of 4.
The elements in the array after that index is negligible (don't care what value it is).
"""

def distinct_numbers(ar):

    last_index=0
    for i in range(1,len(ar)):
        if ar[last_index] != ar[i]:
            #print(i,last_index,ar[i],ar[last_index])
            last_index+=1
            ar[last_index]=ar[i]

    return ar[:last_index+1]

print(distinct_numbers([3, 3, 4, 5, 5, 6, 7, 7, 7]))
print(distinct_numbers([3, 4, 5, 7]))
print(distinct_numbers([3, 3]))




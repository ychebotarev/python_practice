"""
Given an array of integers, find length of the largest subarray with sum equals to 0.

Input: arr[] = {15, -2, 2, -8, 1, 7, 10, 23};
Output: 5
The largest subarray with 0 sum is -2, 2, -8, 1, 7
"""

#what does it means sum from i to j iz 0?
#it mean sum from 0 to i is the same as sum from 0 to j

def longest_subarray(ar):
    h={}
    cur_sum=0;
    max_length = 0
    for i in range(len(ar)):
        cur_sum+=ar[i]
        if cur_sum in h:
            max_length = max(max_length, i-h[cur_sum])
        else:
            h[cur_sum]=i
    return max_length

print(longest_subarray([15, -2, 2, -8, 1, 7, 10, 23]))

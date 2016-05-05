"""
given an array of n elements, find if there is a
subset of 3 elements sum up to value T with time complexity O(nlgn).
"""

def check_three_sum_bruteforce(ar, T):
    a=sorted(ar)
    for i in range(len(ar)-2):
        start = i+1
        end=len(ar)-1
        while start < end:
            sum = ar[i]+ar[start]+ar[end]
            if sum == T:
                return True
            if sum > T:
                end -=1
            else:
                start +=1


print(check_three_sum_bruteforce([1,2,3,4],6))
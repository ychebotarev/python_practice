"""Microsoft Interview Question for Software Engineers
Given a number N, write all possible sums of consecutive numbers that add up to N.

That is:
return all pairs (a, k) such that a+(a+1)+...+(a+k)=n

After that:
1. what if N is negative or a is negative;
2. what if N is real and the possible implications of this"""

"""
N = a + a(a+1)+ ... + (a+n) => a = (N - sum(1..n))/(n+1)
Nwo if a is integer - it will form sum
"""

def all_consecutive_sums(N):
    n=2
    sum=1
    res = []
    while sum < N/2:
        if (N - sum)%n == 0:
            res.append( ((N - sum)/n,n) )
        sum+=n
        n+=1
    return res

print(all_consecutive_sums(121))



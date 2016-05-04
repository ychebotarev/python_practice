"""
There's a function that concatenates two strings and returns the length of the resultant string.
When called upon a series of strings how do we minimize the cost of using this function.
Let's say we have 3 strings, A= "abc", B="def", C = "gh".
Now cost of merging AB = 6 and cost of merging the resultant string with C is 8.
Thus the total cost is 6 + 8 = 14.
However, if we merge A and C, then the cost is 5 and then merge B with this, the cost is 8, so the total cost is 13.
Find an algorithm that minimizes the cost of adding such a series of strings.
"""

import heapq
def min_sum(ar):

    if len(ar) < 2:
        return (0,[])

    h=[]
    for s in ar:
        heapq.heappush(h,(len(s),s))

    result=[]

    operation = 0

    while len(h)>= 2:
        s1 = heapq.heappop(h)
        s2 = heapq.heappop(h)

        result.append(s1[1])
        result.append(s2[1])

        operation += s1[0] + s2[0]

        res = s1[1] + s2[1]

        heapq.heappush(h,(len(res),res))

    result.append(result[-1]+result[-2])

    return (result,operation)

r = min_sum(["abc","def","gh"])
print(r[1])
print(r[0])
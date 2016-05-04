"""
For each of the following problems, give an algorithm that finds the desired
numbers within the given amount of time. To keep your answers brief, feel free to
use algorithms from the book as subroutines. For the example, S = {6, 13, 19, 3, 8},
19 − 3 maximizes the difference, while 8 − 6 minimizes the difference.
(a) Let S be an unsorted array of n integers. Give an algorithm that finds the pair
x, y ∈ S that maximizes |x − y|. Your algorithm must run in O(n) worst-case time.
(b) Let S be a sorted array of n integers. Give an algorithm that finds the pair
x, y ∈ S that maximizes |x − y|. Your algorithm must run in O(1) worst-case time.
(c) Let S be an unsorted array of n integers. Give an algorithm that finds the pair
x, y ∈ S that minimizes |x − y|, for x = y. Your algorithm must run in O(n log n)
worst-case time.
(d) Let S be a sorted array of n integers. Give an algorithm that finds the pair
x, y ∈ S that minimizes |x − y|, for x = y. Your algorithm must run in O(n)
worst-case time.
"""

def solve_problem_a(ar):
    if len(ar) < 2:
        return None,None
    i1=0
    i2=1
    diff=abs(ar[0]-ar[1])

    for i in range(2,len(ar)):
        t1 = abs(ar[i1]-ar[i])
        t2 = abs(ar[i2]-ar[i])

        if t1 > diff:
            i2=i
            diff=t1

        if t2 > diff:
            i1=i2
            i2=i
            diff=t2

    return ar[i1], ar[i2]

print(solve_problem_a([]))
print(solve_problem_a([1]))
print(solve_problem_a([1,2]))

print(solve_problem_a([6, 13, 19, 3, 8]))


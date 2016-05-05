__author__ = 'yuriic'
"""
Given two arrays A [n] and B[m], find the smallest
window in A that contains all the elements of B.
"""

#1. hash [values from B] -> position in A
#2. Update hash, find min/max in that hash if all values has positions.

class problem:
    def __init__(self):
        self.h = {}
        self.result = (0,0,0)

    def solve(self, A, B):
        self.h = {}
        self.result = (0,0, len(A)+1)

        for b in B:
            self.h[b] = -1

        for i in range(A):
            if A[i] not in self.h:
                continue

            self.h[A[i]] = i

            self.__updateResult(A)

        return self.result[0], self.result[1]

    def __updateResult(self,A):
        min_value = len(A)
        max_value = 0

        for k,v in self.h.items():
            if v == -1:
                return
            min_value = min(min_value, v)
            max_value = max(max_value, v)

        if max_value - min_value < self.result[2]:

            self.result = min_value, min_value,max_value - min_value


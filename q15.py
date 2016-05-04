__author__ = 'yuriic'
"""
Given a number M (N-digit integer) and K-swap operations(a swap
operation can swap 2 digits), devise an algorithm to get the maximum possible integer?
Examples:
M = 132 K = 1 output = 312
M = 132 K = 2 output = 321
M = 7899 k = 2 output = 9987
M = 8799 and K = 2 output = 9987
"""

from collections import defaultdict

class problem:
    def __init__(self):
        self.digits=[]
        self.sorted = []
        self.h=defaultdict(list)
        self.k=0

    def solve(self, N,k):
        self.h=defaultdict(list)
        self.k = k
        self.digits = self._to_digits(N)
        self.sorted = sorted(self.digits)

        for i in range(self.digits):
            self.h[self.digits[i]].append(i)

        index = 0
        while k > 0 and index > 0:
            if self.digits[index] != self.sorted[index]:
                #find the best open available position
                #swap
                --k
            ++index
        return self.__from_digits()



    def __to_digits(self,N):
        return []
    def __from_digits(self):
        return 0

def k_swap(N,k):
    """
    1. Get all digits of N
    2. Sort digets, reverse the array
    3. Make hash table digit"position
    5. Repeat K times
        a. Replace first non-matching
    """


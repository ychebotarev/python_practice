"""
Design a data structure that supports following operations in Θ(1) time.

insert(x): Inserts an item x to the data structure if not already present.
remove(x): Removes an item x from the data structure if present.
search(x): Searches an item x in the data structure.
getRandom(): Returns a random element from current set of elements
"""

import random;

class Crazy:
    def __init__(self):
        self.h = {}
        self.v = []
        self.length = 0

    def insert(self, value):
        if value in self.h:
            return
        self.v.append(value)
        self.h[value] = len(self.v) - 1

    def remove(self, value):
        if value not in self.h:
            return
        index = self.h[value]
        del self.h[value]
        self.h[self.v[self.length]] = index
        self.v[index] = self.v[self.length]
        self.length -= 1

    def search(self, value):
        return value in self.h

    def getRandom(self):
        return self.v[random.randint(0, self.length)]
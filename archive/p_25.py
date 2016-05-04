"""
Data structure: insert, remove, contains, get random element, all at O(1)
"""
import random

class weird:
    def __init__(self):
        self.dict={}
        self.array=[]

    def add(self,v):
        if v in self.dict:
            return
        self.array.append(v)
        self.dict[v]=len(self.array)-1

    def remove(self,v):
        if v not in self.dict:
            return

        self.array[self.dict[v]] = self.array[-1]
        self.dict[self.array[-1]] = self.dict[v]
        del self.dict[v]

    def random(self):
        return self.array[random.randrange(0,len(self.array))]

    def check(self,v):
        return v in self.dict



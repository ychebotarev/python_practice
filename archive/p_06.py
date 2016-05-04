"""
find the longest common prefix in a list of phrases
"""

def lcp(phrases):
    if phrases is None or len(phrases) == 0:
        return 0
    if len(phrases) == 1:
        return len(phrases[0])

    lcp_index=0
    for i,c in enumerate(phrases[0]):
        for p in phrases[1:]:
            if len(p) <= i:
                return lcp_index
            if p[i]!=c:
                return lcp_index
        lcp_index=i

    return lcp_index
"""
Given a binary tree, implement an iterator that will iterate through its elements.
"""

class node:
    def __init(self,val,l=None,r=None):
        self.l=l
        self.r=r
        self.val=val

class bp_iterator:
    def __init__(self, r, order=traverse_order.pre_order):
        self.root=r
        self.order=order
        self.current=r
        self.path=[]

    def move(self):
        if self.order == traverse_order.pre_order:

            if self.previous is not None and (self.previous.left == self.current or self.previous.right == self.current):
                self.previous=self.current
                if self.current.left is not None:
                    self.current=self.previous.left
                    self.path.append(self.previous)
                    return
                if self.current.right is not None:
                    self.current=self.previous.right
                    self.path.append(self.previous)
                    return
                self.current=self.path.pop()
                self.move()
                return
            if self.previous==self.current.left:
                if self.previous.right is not None:
                    self.current = self.previous.right
                    return

            #we come from the last node
            self.previous=self.current
            self.current=self.path.pop()
            self.move()



    def current(self):
        self.current

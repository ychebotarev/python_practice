"""
LRUCache
"""

class LRUCache:
    class DQNode:
        def __init__(self,v):
            self.val=v
            self.next=None
            self.prev=None
    class DQ:
        def __init_(self,k):
            self.max_items=k
            self.size=0
            self.head=None
            self.tail=None

        def remove(self,node):
            self.size-=1
            if self.head == node :
                self.head = node.next
            elif self.tail == node:
                self.tail = self.tail.prev
            else:
                if node.prev != None:
                    node.prev.next=node.next

            if self.head is None or self.tail is None:
                self.head = None
                self.tail = None

        def add(self,node):
            if self.size == self.max_items:
                self.remove(self.tail)
            self.size +=1
            if self.head is None:
                self.head=node
                self.tail=node
            else:
                self.head.prev=node
            node.next = self.head
            self.head=node

        def update(self,node):
            self.remove(node)
            self.add(node)

        def is_full(self):
            return self.max_items == self.size


    def __init__(self,k):
        self.dict={}
        self.dq=LRUCache.DQ()

    def add(self,v):
        if v in self.dict:
            self.dq.update(self.dict[v])
        else:
            if self.dq.is_full():
                node = dict[self.dq.tail.val]
                del self.dict[node.val]
                self.dq.remove(node)
            node = LRUCache.DQNode(v)
            self.dict[v]=node
            self.dq.add(node)







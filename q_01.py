__author__ = 'yuriic'

"""
Implement LRU.
"""

class node:
    def __init__(self, value, prev = None, next = None ):
        self.value = value
        self.next= next
        self.prev= prev


class LRU:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = 0
        self.hash={}
        self.root = None
        self.tail = None

    def add(self, value):
        if value in self.hash:
            self.__bubble(self.hash[value])
        else:
            if self.LRU_full:
                self.__pop()
            self.__push(value)

    def top(self):
        if self.root is not None:
            return self.root.value
        return None

    @property
    def LRU_full(self):
        return self.items >= self.capacity

    def __bubble(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev

        node.prev = None
        node.next = self.root
        if self.root is not None:
            self.root.prev = node
        self.root = node


    def __pop(self):
        if not self.tail:
            return
        del self.hash[self.tail.value]
        self.tail = self.tail.prev
        self.items -= 1


    def __push(self, value):
        if self.LRU_full:
            return
        new_root = node(value, None, self.root)
        if self.root is not None:
            self.root.prev=new_root
        self.root = new_root
        self.items += 1
        if self.tail is None:
            self.tail = new_root
        self.hash[value]=self.root


lru = LRU(3)
lru.add(1)
print(lru.top(), lru.items)
lru.add(2)
print(lru.top(), lru.items)
lru.add(1)
print(lru.top(), lru.items)
lru.add(3)
lru.add(4)
print(lru.top(), lru.items)
lru.add(5)
print(lru.top(), lru.items)
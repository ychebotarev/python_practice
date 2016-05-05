"""
In Linked list, Node has two pointers, one points to next node, other points to arbitrary node in the linked list.
Write a function to return a new list which is clone of the given linked list.
"""

class ll_item:
    def __init__(self,v,n,r = None):
        self.v=v
        self.next=n
        self.random=r

class problem:
    def __init__(self):
        self.clone=None
        self.root=None

    def clone(self, root):
        self.root=root
        self.clone = self.__simple_clone(self.root)

        c = self.clone
        r = root

        while c is not None:
            r.random = c.random
            c.random = c.random.random
        return self.clone

    def __simple_clone(self, root):
        if root is None:
            return None
        clone = ll_item(root.v)
        clone.random = root.random
        root.random=clone
        clone.next = self.__simple_clone(root.next)
        return clone

"""
Find a linked list has circle in it, If it has loop, find origin of the loop.
"""

class list_node:
    def __init__(self,v,next):
        self.value = v
        self.next = next

def has_loops(list_item):
    if list_item is None:
        return False
    fast=list_item
    slow=list_item.next

    while fast and slow and fast.next:
        if fast == slow:
            return True
        fast = fast.next.next
        slow = slow.next
    return False

"""
An array is sorted and rotated by k times.
Find an element in an array. (efficient and logarithmic time solution is expected)
"""

def bsearch(ar, elem):
    return False

def find(ar, elem):
    m = len(ar) //2

    if ar[m] == elem:
        return True

    if ar[0] < ar[m] and elem < ar[m]:
        return bsearch(ar[0:m], elem)
    if ar[m] < ar[-1] and elem > ar[m]:
        return bsearch(ar[m:], elem)

    return find(ar[m:],elem) if elem > ar[m] else find(ar[:m],elem)
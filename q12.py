__author__ = 'yuriic'
"""
Given two sorted linked lists of integers write an algorithm to merge the two linked lists such that the resulting linked
list is in sorted order. You are expected to define the data structure for linked list as well.
Analyze the time and space complexity of the merge algorithm.
"""

class node:
    def __init__(self,value,next):
        self.v=value
        self.next=next


def merge_destroy(l1, l2):
    if l1 is None:
        return l2
    if l2 is None:
        return l1

    if l1.value < l2.value:
        root = l1
        l1 = root.next
    else:
        root = l2
        l2 = root.next

    current = root

    while True:

        if l1 is None:
            current.next = l2
            return root

        if l2 is None:
            current.next = l1
            return root

        if l1.value < l2.value:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next

    return None
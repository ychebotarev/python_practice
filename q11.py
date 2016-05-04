__author__ = 'yuriic'
"""
Given a sorted integer array, write a method that builds a balanced binary search tree. What is the runtime complexity?
Hint: Recursion.
Follow-up: Non-recursive solution
"""

class node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def build_bst(ar):
    if ar.length == 0:
        return None
    if ar.length == 1:
        return node(ar[0])
    midpoint = len(ar) // 2;
    return node(ar[midpoint], build_bst(ar[0:midpoint]), build_bst(ar[midpoint+1:]))

#Follow-up: Non-recursive solution


def build_bst_no_recursion(ar):

    if ar.length == 0:
        return None
    if ar.length == 1:
        return node(ar[0])

    midpoint = len(ar) // 2;
    root = node(ar[midpoint])
    nodes = []
    ranges= []

    node.append(root);
    ranges.append((0, midpoint))
    ranges.append((midpoint+1, len(ar)))

    while True:
        new_nodes = []
        new_ranges=[]
        for i in range(len(nodes)):
            current_root = nodes[i]
    return root

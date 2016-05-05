"""
The diameter of a tree is the number of nodes on the longest path between two leaves in the tree.
The diagram below shows a tree with diameter nine,
the leaves that form the ends of a longest path are shaded
(note that there is more than one path in each tree of length nine, but no path longer than nine nodes).

In particular, note that the diameter of a tree T is the largest of the following quantities:

the diameter of T's left subtree
the diameter of T's right subtree
the longest path between leaves that goes through the root of T
Given the root node of the tree, return the diameter of the tree
"""

class node:
    def __init__(self, value, left=None, right=None):
        self.v =  value
        self.l = left
        self.r = right

def __get_tree_diameter_impl(root):
    if root is None:
        return 0,0
    r1 = get_tree_diameter(root.l)
    r2 = get_tree_diameter(root.l)
    diameter = max(1+r1[1]+r2[1], r1[0], r2[0])
    longest_branch = 1 + max(r1[1], r2[1])

    return diameter, longest_branch


def get_tree_diameter(root):
    if root is None:
        return 0
    r = __get_tree_diameter_impl(root)
    return r[0]
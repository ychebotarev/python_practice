"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
"""
import math
class Leaf:
    def __init__(self, x, l = None, r = None):
        self.val = x
        self.left = l
        self.right = r

    def __str__(self, level=0):
        ret = "\t"*level+repr(self.val)+"\n"
        if self.left != None:
            ret += self.left.__str__(level+1)
        if self.right != None:
            ret += self.right.__str__(level+1)
        return ret

    def __repr__(self):
        return '<tree node representation>'


def sortedArrayToBST(nums):
    if len(nums) == 0:
        return None

    if len(nums) == 1:
        return Leaf(nums[0])
    midpoint = math.ceil(len(nums)/2)-1
    root=Leaf(nums[midpoint])
    a_l=nums[0:midpoint]
    a_r=nums[midpoint+1:]
    root.left=sortedArrayToBST(a_l)
    root.right=sortedArrayToBST(a_r)
    return root

def solve(nums):
    root = sortedArrayToBST(nums)
    return root

l = solve([1,2,3,4,5,6,7])
print(l)
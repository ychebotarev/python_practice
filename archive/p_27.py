"""
Given a binary tree, find the maximum path sum.
"""


class Leaf:
    def __init__(self, x, l = None, r = None):
        self.val = x
        self.left = l
        self.right = r

class Solution:
    def maxPathSum(self, root):
        if root is None:
            return 0
        mx_l, lb_l = self.muxBranch(root.left)
        mx_r, lb_r = self.muxBranch(root.right)
        return max(root.val+lb_l+lb_r,mx_l,mx_r)

    def muxBranch(self,root):
        if root is None:
            return (0,0)
        mx_l, lb_l = self.muxBranch(root.left)
        mx_r, lb_r = self.muxBranch(root.right)

        return (max(root.val+lb_l+lb_r,mx_l,mx_r), root.val+max(lb_l,lb_r))
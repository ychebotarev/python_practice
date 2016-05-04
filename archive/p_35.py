# Definition for a binary tree node.
"""
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

For example:
Given the following binary tree,
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
You should return [1, 3, 4].
"""

class TreeNode:
    def __init__(self, x, l = None, r = None):
        self.val = x
        self.left = l
        self.right = r

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def rightSideView(self, root):
        if root == None:
            return []
        l = self.rightSideView(root.left)
        r = self.rightSideView(root.right)

        result=[root.val]
        result.extend(r)
        if (len(l)>len(r)):
            result.extend(l[-(len(l)>len(r))])
        return result

d = Solution()
t = TreeNode(1, l = TreeNode(2,None, TreeNode(5)), r = TreeNode(3, None, TreeNode(4)))

print(d.rightSideView(t))

"""
Populating Next Right Pointers in Each Node
"""

class Leaf:
     def __init__(self, x, l = None, r = None):
        self.val = x
        self.left = l
        self.right = r
        self.next = None

def first_subling_with_childs(leaf):
    while True:
        if leaf==None:
            return None
        if leaf.left != None or leaf.right != None:
            return leaf
        leaf = leaf.next


def first_child(leaf):
    if leaf == None:
        return None
    return leaf.left if leaf.left != None else leaf.right

def connect_sublings(root):
    if root == None:
        return
    root.next = None
    connect_level(root)

def connect_level(root):
    if root == None:
        return
    current = root
    while current!= None:
        next = first_subling_with_childs(current.next)
        subling = first_child(next)
        if current.left != None:
            if current.right != None:
                current.left.next=current.right
            else:
                current.left.next = subling
        if current.right != None:
            current.right.next = subling
        current = next
    connect_level(first_child(first_subling_with_childs(root)))

root = Leaf(1, Leaf(2),Leaf(3))
connect_sublings(root)

print(root.left.next.val)
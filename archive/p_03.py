"""
BFS without recursion
"""

class node:
    def __init__(self,v,l=None,r=None):
        self.value = v
        self.left=l
        self.right=r

class DFS_norecursion:
    def __init__(self):
        self.current=None
        self.bfs_stack=[]

    def process(self,process_func):
        process_func(self.current.value)
        self.last_processed=self.current
        self.bfs_stack.pop()
        self.current = None if len(self.bfs_stack) == 0 else self.bfs_stack[-1]

    def next(self, next_item):
        self.bfs_stack.append(next_item)
        self.current = next_item

    def do_dsr(self, root, process_func):
        self.last_processed=None
        self.current=root
        self.bfs_stack=[]
        self.bfs_stack.append(root)

        while self.current!=None:
            if self.current.left is not None and self.last_processed==self.current.left:
                if self.current.right!=None:
                    self.next(self.current.right)
                else:
                    self.process(process_func)
            elif self.current.right is not None and self.last_processed==self.current.right:
                self.process(process_func)
            else:
                if self.current.left!=None:
                    self.next(self.current.left)
                elif self.current.right !=None:
                    self.next(self.current.left)
                else:
                    self.process(process_func)


class BFS_norecursion:
    class list_node:
        def __init__(self, v):
            self.v=v

    def __init__(self):
        self.list_head=None
        self.list_tail=None

    def add(self, next_item):
        if next_item is None:
            return
        new_tail = BFS_norecursion.list_node(next_item)
        if self.list_tail is not None:
            self.list_tail.next = new_tail
        self.list_tail = new_tail

    def process(self,process_func):
        if self.list_head is not None:
            process_func(self.list_head.v.value)
            self.list_head=self.list_head.next


    def do_bfs(self, root, process_func):
        if root is None:
            return
        self.add(root)
        while self.list_tail is not None:
            self.add(self.list_tail.v.left)
            self.add(self.list_tail.v.right)
            self.process(process_func)


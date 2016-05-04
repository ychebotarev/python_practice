__author__ = 'yuriic'

class SQNode:
    def __init__(self, data, prev = None, next = None):
        self.data=data
        self.prev=prev
        self.next=next

class SQ:
    def __init__(self):
        self.deque_top=None
        self.deque_bottom=None

    def push(self,data):
        if self.deque_top == None:
            self.deque_top = SQNode(data,None,None)
            self.deque_bottom = self.deque_top
        else:
            prev_top = self.deque_top
            self.deque_top = SQNode(data,None,prev_top)
            prev_top.prev = self.deque_top

    def enqueue(self, data):
        self.push(data)

    def pop(self):
        if self.deque_top == None:
            return None

        result = self.deque_top
        self.deque_top = result.next

        if self.deque_top == None:
            self.deque_bottom = None
        else:
            self.deque_top.prev = None

        return result

    def dequeue(self):
        if self.deque_bottom == None:
            return None
        result = self.deque_bottom
        self.deque_bottom = result.prev

        if self.deque_bottom == None:
            self.deque_top = None
        else:
            self.deque_bottom.next = None
        return result

    def __str__(self):
        return "hello from SQ"

    def __repr__(self):
        return '<tree node representation>'


class fun:
    def __str__(self):
        return "hello from fun"

f = fun()
print(f)

print('hello')
sq = SQ()
sq.push(3)
sq.push(2)
sq.enqueue(1)
print(sq)
print(sq.pop())
print(sq)
print(sq.dequeue())
print(sq)

"""
connect all sublings
"""

class node:
    def __init__(self,v,l=None,r=None):
        self.v=v
        self.l=l
        self.r=r
        self.s=None


def get_first_child_subling(item):
    if item is None:
        return None

    if item.l is not None:
        return item.l
    if item.r is not None:
        return item.l
    return get_first_child_subling(item.s)

def connect_sublings(item):
    if item is None:
        return

    if item.l is not None:
        item.l.s= item.r if item.r is not None else get_first_child_subling(item.s)

    if item.r is not None:
        item.r.s=get_first_child_subling(item.s)

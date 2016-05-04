"""
4. Your job is to arrange n ill-behaved children in a straight line, facing front. You
are given a list of m statements of the form “i hates j”. If i hates j, then you do not
want put i somewhere behind j, because then i is capable of throwing something
at j.
(a) Give an algorithm that orders the line, (or says that it is not possible) in
O(m + n) time.

(b) Suppose instead you want to arrange the children in rows such that if i hates
j, then i must be in a lower numbered row than j. Give an efficient algorithm
to find the minimum number of rows needed, if it is possible.
"""

class relation:
    def __init__(self, name):
        self.name = name
        self.hates = []
        self.hated = 0

    def add_hate(self, person):
        self.hates.append(person.name)
        person.hated +=1

    def __str__(self):
        h = ",".join(self.hates)
        return self.name + " ,hates: [" + h + "]"+" ,hated by:"+str(self.hated)


def arrange_childrens(relations):
    all_childrens= {}
    for r in relations:
        child_name = r[0]
        child_hates = r[1]

        if not child_name in all_childrens:
            all_childrens[child_name] = relation(child_name)
        if not child_hates in all_childrens:
            all_childrens[child_hates] = relation(child_hates)

        all_childrens[child_name].add_hate(all_childrens[child_hates])

    order = []

    for k,v in all_childrens.items():
        print(v)
        if v.hated == 0:
            order.append(k)

    i=0

    while(i<len(order)):
        for n in all_childrens[order[i]].hates:
            h = all_childrens[n]
            h.hated -=1
            if h.hated == 0:
                order.append(h.name)
        i+=1

    return order


relations = [ ("a","b"),("a","c"),("c","b")]
print(arrange_childrens(relations))

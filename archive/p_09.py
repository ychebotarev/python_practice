"""
Check is it is possible to create palindrome from a string
"""
from collections import defaultdict

def is_palindromable(input_str):
    d=defaultdict(lambda:0)
    for c in input_str:
        d[c]=d[c]+1

    if len(input_str) % 2 == 0:
        #even = check if all occurance are even
        if not all(o % 2 == 0 for o in d.values()):
            return False
    else:
        if sum(o % 2 == 1 for o in d.values())>1:
            return False
    l = list(input_str)

    current_index=0
    for k,v in d.items():
        for i in range(0,v//2):
            l[current_index]=k
            l[len(input_str)-current_index-1]=k
            current_index+=1
        if v % 2 == 1:
            l[len(input_str)//2]=k

    return ''.join(l)



print(is_palindromable("a"))
print(is_palindromable("ab"))
print(is_palindromable("aab"))
print(is_palindromable("aabb"))
print(is_palindromable("aaabbb"))
print(is_palindromable("aaabb"))
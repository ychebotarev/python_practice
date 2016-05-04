"""
Find the length of the longest correct subsequince of brackets of the same type

Exapmple - [[][]] - 6
"""
def solve(str):
    result = 0
    list=[]
    for i, c in enumerate(str):
        if c == '[':
            list.append(i)
        else:
            if len(list) > 0:
                s = list.pop()
                result = max(result,i-s+1)
    return result


print(solve("[[][]]"))
print(solve("[[][][]"))
print(solve("[[[][][]]"))
print(solve("[["))
print(solve("]]"))
print(solve("]["))


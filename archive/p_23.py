"""
Create a powerset
"""

def power_set(input):
    if len(input) == 0:
        return []
    if len(input) == 1:
        return [input,[]]

    res = power_set(input[1:])
    k=[input[0]]
    result=[]

    for r in res:
        result.append(r)
        result.append(k+r)
    return result


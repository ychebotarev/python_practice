"""

You have three arrays
Merge the first two based no positions from corresponding items fro 3rd array
Negative items in 3rd array mean we don't wabt the corresponding item from 2nd array ni merged array.

Story - You gemerate set of Ads, and Set of Web results. Web results are already ordered.
You want optimally insert ads on the apge. You run a model and for each item in Ads array model predict where it should go in resulting array


Example:

a1:  10 11 12 13
a2:  01 02 03 04
a3:  01 -1 -1 03

res: 10 01 11 12 04 13

"""

def solve(a1, a2,a3):
    #few assumptions. Since this is Ads and Ads generate revenue - we must try hard to build resulting page
    dict={}

    if (a2 == None or a3 == None):
        return a1
    #this will set default values for dict
    for i in range(min(len(a2),len(a3))):
        if a3[i]>=0:
            dict[a3[i]]=a2[i]

    d = sorted(dict.items())

    i = 0
    j = 0
    k=0
    result = []

    while i < len(a1) and j< len(d):
        if d[j][0] == k:
            result.append(d[j][1])
            j+=1
        else:
            result.append(a1[i])
            i+=1
        k+=1

    while j < len(d):
            result.append(d[j][1])
            j+=1

    while i < len(a1):
            result.append(a1[i])
            i+=1

    print(result)
    return result

def solve_acceptable(a1, a2,a3):
    if (a2 == None or a3 == None):
        return a1

    dict={}
    for i in range(min(len(a2),len(a3))):
        if a3[i]>=0:
            dict[a3[i]]=a2[i]
    result = a1.copy() if a1 != None else []
    for d in sorted(dict.items()):
        result.insert(d[0],d[1])
    return result

solve_acceptable([10, 11, 12, 13],[1, 2, 3, 4],[1, -1, -1, 100])
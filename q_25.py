"""
Two pairs (a, b) and (c, d) are said to be symmetric if c is equal to b and a is equal to d.
For example (10, 20) and (20, 10) are symmetric. Given an array of pairs find all symmetric pairs in it.

Input: arr[] = {{11, 20}, {30, 40}, {5, 10}, {40, 30}, {10, 5}}
Output: Following pairs have symmetric pairs
        (30, 40)
        (5, 10)
"""

from collections import defaultdict


def get_symmetric_pairs(pairs):
    h = defaultdict(list)
    for pair in pairs:
        h[pair[0]].append(pair[1])
    print(h)
    symmetric_pairs = {}
    for pair in pairs:
        if pair[1] in h and pair[0] in h[pair[1]] and min(pair[0], pair[1]) not in symmetric_pairs:
            symmetric_pairs[min(pair[0], pair[1])] = max(pair[0], pair[1])
    return [(key, value) for key, value in symmetric_pairs.items()]


print(get_symmetric_pairs([(11, 20), (30, 40), (5, 10), (40, 30), (10, 5)]))

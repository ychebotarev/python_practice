"""
Count all possible walks from a source to a destination with exactly k edges
"""

def count_walks(graph, Size, k, u, v):
    if k == 0:
        return 1 if u == v else 0
    if k == 1:
        return 1 if graph[u][v] else 0

    walks = 0
    for i in range(Size):
        if graph[u][i]:
            walks +=count_walks(graph,Size,k-1,i,v)
    return walks


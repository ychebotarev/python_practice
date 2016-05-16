__author__ = 'yuriic'
"""
Given a start position and an target position on the grid. You can move up,down,left,right from one node to another adjacent one on the grid. However there are some walls on the grid that you cannot pass. Now find the shortest path from the start to the target.
(This is easy done by BFS)
Extend. If you can remove three walls, then what is the shortest path from start to the target. (I have no ideal except for enumerate all the possibility of three walls. It must be the silly solution.) Does anyone have any idea?
"""
"""
I'm not going to code it.


1. Build simple fastest path.
2. For each step keep the number of steps required to reach that path
3. Repeat
    Build new path by eliminating one wall
        go throught pass
        if any cell has wall - check if it is possible to reach another cell in path if we eliminate this wall
        pick the one we highes gain
        repeat twice

    Do the same for other combinations of walls
        remove one wall then remove 2 walls
        remove 2 walls then remove 1 wall
        remove 3 walls
"""
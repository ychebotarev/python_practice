"""
spiral matrix c++
using System;

//print psiral matrix

class Solution
{
    static void print_spiral_matrix(int[,] m, int rows, int cols)
    {
        int l = 0;
        int r=cols-1;
        int t=0;
        int b=rows-1;

        while(l<=r && t<=b)
        {
            for(int i=l; i<=r;++i)
            {
                Console.Write(m[t,i]);
                Console.Write(",");
            }
            ++t;
            for(int j=t; j<=b;++j)
            {
                Console.Write(m[j,r]);
                Console.Write(",");

            }
            --r;
            for(int i=r; i>=l;--i)
            {
                Console.Write(m[b,i]);
                Console.Write(",");
            }
            --b;
            for(int j=b; j>=t;--j)
            {
                Console.Write(m[j,l]);
                Console.Write(",");
            }
            ++l;
        }
        Console.WriteLine("\nDone");
    }

    static void Main(string[] args)
    {

        int[,] m = new int[3, 5]
        {
            {1, 2, 3, 4, 5},
            {6, 7, 8, 9, 10},
            {11, 12, 13, 14, 15}

        };
        print_spiral_matrix(m,3,5);
    }
}
"""

"""
Imprelent a function to check if tree is BST
"""

class node:
    def __init__(self,v,l=None,r=None):
        self.v=v
        self.l=l
        self.r=r

def is_bst(root):
    if root is None:
        return True

    if root.l is not None and root.l.v>root.v:
        return False
    if root.l is not None and root.l.v>root.v:
        return False
    if root.r is not None and root.r.v<root.v:
        return False

    return is_bst(root.l) and is_bst(root.r)

print(is_bst(node(10, node(1), node(20))))
print(is_bst(node(10, node(100), node(20))))
print(is_bst(node(10, node(9,node(10),node(11)), node(20))))


import heapq
import itertools

def give_average_score(test_results):
    dict={}

    for k, g in itertools.groupby(test_results, lambda x: x[0]):
        dict[k]=[x[1] for x in list(g)]

    result={}

    for k,v in dict.items():
        heapq.heapify(v)
        t=heapq.nlargest(5,v)
        result[k]=sum(t)/len(t)
    return result


r = give_average_score([("1",1),("1",2),("1",1),("1",3),("1",1),("1",5),("2",10)])
print(r)
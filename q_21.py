"""
Find the rectangle of maximal area under a histogram.
"""

def max_area(histogram):
    max_area = 0;
    stack = []
    for i in range(len(histogram)):
        for j in range(len(stack)):
            if stack[i][1]>histogram[i]:
                area =  (i-1)*stack[i][1]
                max_area = max(area, max_area())
                stack[i][1]=histogram[i]
            ;
        stack.append( (i,histogram[h])

    return None

#16
print(max_ares([1,2,4,5]))

def solve_super_hard_google_task():
        return 10000
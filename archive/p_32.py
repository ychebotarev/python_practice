'''
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

For example,
Given height = [2,1,5,6,2,3],
return 10.
'''

class problem_2:
    def __init__(self):
        self.result=[]

    def solve(self, height):
        result = 0
        list = []
        i=0

        while True:
            if i >= len(height):
                break
            if len(list) == 0:
                result = max(result,height[i] * 1)#just to be clear we calculating area
                list.append((i, height[i]))
                i+=1
                continue
            last = list[-1]

            if height[i] >= last[1]:
                list.append((i,height[i]))
                i+=1
            else:
                result = max(result, last[1]*(i-last[0]))
                list.pop()


        return result


d = problem_2()
print(d.solve([2,1,5,6,2,3]))
print(d.solve([1,1,1,1,1,1]))


"""
Google Interview Question
find the no of possible patterns in android lock screen. write a program to count them.
"""

total_path - 0

def get_nabours(point):
    d={1:[2,4,5], ...}
    return d[point]

def get_path_starting_with(start_point, min_path_length, exclude_points):
    total_path=0
    for neibour_point in get_nabours(start_point):
        if  neibour_point not in exclude_points:
            if min_path_length>1:
                total_path+=1
                min_path_length-=1
            total_path+=get_path_starting_with(neibour_point,min_path_length-1, exclude_points+start_point)
    return total_path

total_path=0
for point in [1,2,3,4,5,6,7,8,9]:
    for naibour_point in get_nabours(point):
        total_path+=get_path_starting_with(naibour_point,3, [point])


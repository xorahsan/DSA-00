# jump search

"""
The idea is to do less comparisions
First take suitable step size which is sqrt(n) 
then for sorted array, get interval by step 
then do linear for that short interval
"""

from math import sqrt
import pandas as pd
from time import perf_counter

data_frame = pd.read_csv("cities.csv")
array = data_frame.values.tolist()

array = sorted(array, key = lambda x: x[0])

item = (input("Enter a City name to get data: ")).lower()

def jumpSearch(item, array):

    # get root of given array length
    m = int(sqrt(len(array)))

    point_of_interest = [0, m-1]
    pointer = m

    total_iterations = 0 
    while pointer<= len(array)-1:
        total_iterations = total_iterations + 1
        if item == array[point_of_interest[0]][0].lower():
            print(f"The given item {item} found at index {point_of_interest[0]} in {total_iterations} iterations!")
            return array[point_of_interest[0]]

        if item == array[point_of_interest[1]][0].lower():
            print(f"The given item {item} found at index {point_of_interest[1]} in {total_iterations} iterations!")
            return array[point_of_interest[1]]

        if item> array[point_of_interest[0]][0].lower() and item< array[point_of_interest[1]][0].lower():
            break
        point_of_interest = [pointer,pointer+m-1]
        pointer = pointer + m

    isExist = False
    found_index = -1
    for check_item in range(point_of_interest[0],point_of_interest[1]+1):
        total_iterations = total_iterations + 1
        if check_item >= len(array):
            break
        if item == array[check_item][0].lower():
            isExist,found_index = True,check_item
            break


    if isExist:
        print(f"The given item {item} found at index {found_index} in {total_iterations} iterations!")
        return array[found_index]
    return f"The given item {item} is not in Array in {total_iterations} iterations!"
    
start = perf_counter()
print(jumpSearch(item, array))
end = perf_counter()
print(f"Total time taken was {end-start} seconds")





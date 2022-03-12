# interpolation search

"""
The idea is to do less comparisions with a formula that gives close index
"""

from math import sqrt
import pandas as pd
from time import perf_counter


array = [15,17,31,49,78,79,90,91,99,108,154]


item = int(input("Enter a number: "))

def interpolationSearch(item, array):
    count = 0
    low, high = 0 , len(array)-1
    pos = int(low + (((high-low)/(array[high]-array[low]))*(item-array[low])))
    if array[pos] == item:
        return pos
    else:
        while low<=high:
            count = count+1
            pos = int(low + (((high-low)/(array[high]-array[low]))*(item-array[low])))
            if array[pos] < item:
                low = pos+1
            else:
                high = pos-1

    return (pos,count)
    

print(interpolationSearch(item, array))





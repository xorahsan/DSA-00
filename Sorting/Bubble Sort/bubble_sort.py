unsorted_array = [9,3,4,6,2,8,10,1,7,5]

def bubbleSort(arr):
    
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0,len(arr)-1):
            if arr[i] > arr[i+1]:
                sorted = False
                arr[i],arr[i+1]= arr[i+1],arr[i]

bubbleSort(unsorted_array)

# Best case: O(n)
# Average case: O(n2)
# Worst case: O(n2)
# Space complexity: O(1)
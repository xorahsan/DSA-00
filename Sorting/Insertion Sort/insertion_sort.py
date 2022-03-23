unsorted_array = [9,3,4,6,2,8,10,1,7,5]

def insertionSort(arr):
    
    for i in range(1,len(arr)):

        while arr[i] < arr[i-1] and i>0:
            arr[i],arr[i-1]=arr[i-1],arr[i]
            i = i-1
        

insertionSort(unsorted_array)

# Best case: O(n)
# Average case: O(n2)
# Worst case: O(n2)
# Space complexity: O(1)
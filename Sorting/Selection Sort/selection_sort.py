unsorted_array = [9,3,4,6,2,8,10,786,3434,1,7,5]

def selectionSort(arr):
    
    for i in range(0,len(arr)-1):
        min = i
        for j in range(i+1,len(arr)):
            
            if arr[j]<arr[min]:
                min = j
            
        arr[i],arr[min]=arr[min],arr[i]

    print(arr)
                
selectionSort(unsorted_array)

# Best case: O(n2)
# Average case: O(n2)
# Worst case: O(n2)
# Space complexity: O(1)
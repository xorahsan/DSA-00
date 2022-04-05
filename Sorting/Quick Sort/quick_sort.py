unsorted_array = ["D","A","Z","D","E"]

def quickSort(arr):
    
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()

        smaller_than_pivot, greater_than_pivot = [],[]
        
        for element in arr:
            smaller_than_pivot.append(element) if element < pivot else greater_than_pivot.append(element)
                
        return quickSort(smaller_than_pivot) + [pivot] + quickSort(greater_than_pivot)


print(quickSort(unsorted_array))

# Best case: O(nlogn)
# Average case: O(nlogn)
# Worst case: O(n2)
# Space complexity: O(logn)
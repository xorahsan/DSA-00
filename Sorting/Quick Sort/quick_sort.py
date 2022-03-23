unsorted_array = ["D","A","Z","D","E"]

def quickSort(arr):
    
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()

        smaller_than_pivot, greater_than_pivot = [],[]
        
        for element in arr:
            if element < pivot:
                smaller_than_pivot.append(element)
            else:
                greater_than_pivot.append(element)
        
        return quickSort(smaller_than_pivot) + [pivot] + quickSort(greater_than_pivot)


print(quickSort(unsorted_array))
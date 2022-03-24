unsorted_arr = [5,1,3,8,9,2,6,8,7,1]

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left_partition, right_partition = arr[:mid], arr[mid:]

        mergeSort(left_partition)
        mergeSort(right_partition)

        i,j,k = 0,0,0

        while i < len(left_partition) and j < len(right_partition):
            if left_partition[i] < right_partition[j]:
                arr[k] = left_partition[i]
                i = i+1
            else:
                arr[k] = right_partition[j]
                j = j+1
            k = k+1

        while i< len(left_partition):
            arr[k] = left_partition[i]
            i,k = i+1,k+1

        while j< len(right_partition):
            arr[k] = right_partition[j]
            j,k = j+1,k+1

mergeSort(unsorted_arr)
print(unsorted_arr)

# Best case: O(nlogn)
# Average case: O(nlogn)
# Worst case: O(nlogn)
# Space complexity: O(n)
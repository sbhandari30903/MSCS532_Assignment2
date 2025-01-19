unsorted_array = [34, 7, 23, 32, 5, 32, 62, 18, 41, 12, 3, 29]

def quicksort(arr, left, right):
    if left < right:
        parti = partition(arr, left, right)
        quicksort(arr, left, parti -1)
        quicksort(arr, parti+1, right)


def partition(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]

    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    if arr[i] > pivot:        
        arr[i], arr[right] = arr[right], arr[i]
    return i

quicksort(unsorted_array, 0, len(unsorted_array)-1)
print(unsorted_array)
    


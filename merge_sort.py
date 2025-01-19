unsorted_array = [34, 7, 23, 32, 5, 32, 62, 18, 41, 12, 3, 29]
def mergesort(arr):
    if len(arr) > 1:
        left = arr[:len(arr)//2]
        right = arr[len(arr)//2:]
        mergesort(left)
        mergesort(right)

        #merge
        i = 0 #left
        j = 0 #right
        k = 0 #main
        while (i < len(left) and j < len(right)):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            k += 1
            i += 1

        while j < len(right): 
            arr[k] = right[j]
            k += 1
            j += 1

mergesort(unsorted_array)
print(unsorted_array)            

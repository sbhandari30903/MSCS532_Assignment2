import matplotlib.pyplot as plt
import numpy as np
import time

def mergesort(arr, depth=0):
    if len(arr) > 1:
        left = arr[:len(arr)//2]
        right = arr[len(arr)//2:]
        ldepth = mergesort(left, depth+1)
        rdepth = mergesort(right, depth+1)

        #merge
        i = 0 #left
        j = 0 #right
        k = 0 #main
        #merge part compares 2 sorted array and merge them
        while (i < len(left) and j < len(right)):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        #add the elements from left array to main array
        while i < len(left):
            arr[k] = left[i]
            k += 1
            i += 1
        #add the elements form right array to main array
        while j < len(right): 
            arr[k] = right[j]
            k += 1
            j += 1
        return max(ldepth, rdepth)
    return depth

def gettime(arr):
    t1 = time.time()
    depth = mergesort(arr)
    t2 = time.time()
    return t2-t1, depth

unsorted_array = np.random.randint(1, 10001, 990)
# Convert to a list if needed
unsorted_array_list = unsorted_array.tolist()

sorted_array = np.arange(1, 991)
# Convert to a list if needed
sorted_array_list = sorted_array.tolist()

reverse_sorted_array = np.arange(990, 0, -1)
# Convert to a list if needed
reverse_sorted_array_list = reverse_sorted_array.tolist()

#get time and recurssion depth
t1,d1 = gettime(unsorted_array_list)
t2,d2 = gettime(sorted_array_list)
t3,d3 = gettime(reverse_sorted_array_list)
t =[t1,t2,t3]
print(t)

d = [d1,d2,d3]
arrtype = ['unsorted', 'sorted', 'reverse']

plt.figure(figsize=(8,6))
plt.plot(arrtype, t, label='Time taken to sort different types of array')
plt.xlabel('Array type')
plt.ylabel('time taken (s)')
plt.title('Merge Sort')
plt.legend()
plt.savefig('mergesort.png')    

plt.figure(figsize=(8,6))
plt.plot(arrtype, d, label='Recurssion Depth')
plt.xlabel('Array type')
plt.ylabel('Depth')
plt.title('Merge Sort')
plt.legend()
plt.savefig('mergesortdepth.png')

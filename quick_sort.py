import matplotlib.pyplot as plt
import numpy as np
import time

def quicksort(arr, left, right, depth=0):
    if left < right:
        parti = partition(arr, left, right)
        ldepth = quicksort(arr, left, parti-1, depth+1)
        rdepth = quicksort(arr, parti+1, right, depth+1)
        return max(ldepth, rdepth)
    return depth


def partition(arr, left, right):
    i = left # i goes from left to right
    j = right - 1 #j goes from right to left
    pivot = arr[right] #pivot is right most element

    #loops until i and j cross eachother
    while i < j:
        # i checks elements less than pivot element
        while i < right and arr[i] < pivot:
            i += 1
        # j checks for elements greater than pivot element
        while j > left and arr[j] >= pivot:
            j -= 1
        #swap elements at i and j if i and j has not crossed eacheother    
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    #swap the element at i with pivot element to get values smaller than pivot in the left side        
    if arr[i] > pivot:        
        arr[i], arr[right] = arr[right], arr[i]
    return i


def quicksortmiddle(arr, left, right, mdepth=0):
    if left < right:
        parti = partitionmiddle(arr, left, right)
        ldepth = quicksortmiddle(arr, left, parti-1, mdepth+1)
        rdepth = quicksortmiddle(arr, parti+1, right, mdepth+1)
        return max(ldepth, rdepth)
    return mdepth

def partitionmiddle(arr, left, right):
    i = left # i goes from left to right
    j = right - 1 #j goes from right to left
    pivot = arr[(left+right)//2] #pivot is middle element

    #loops until i and j cross eachother
    while i < j:
        # i checks elements less than pivot element
        while i < right and arr[i] < pivot:
            i += 1
        # j checks for elements greater than pivot element
        while j > left and arr[j] >= pivot:
            j -= 1
        #swap elements at i and j if i and j has not crossed eacheother    
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    #swap the element at i with pivot element to get values smaller than pivot in the left side        
    if arr[i] > pivot:        
        arr[i], arr[right] = arr[right], arr[i]
    return i


def gettime(arr):
    t1 = time.time()
    depth = quicksort(arr, 0, len(arr)-1)
    t2 = time.time()
    return t2-t1, depth

def mgettime(arr):
    t1 = time.time()
    mdepth = quicksortmiddle(arr, 0, len(arr)-1)
    t2 = time.time()
    return t2-t1, mdepth

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
t1,d1 = mgettime(unsorted_array_list)
t2,d2 = mgettime(sorted_array_list)
t3,d3 = mgettime(reverse_sorted_array_list)
t =[t1,t2,t3]
print(t)

d = [d1,d2,d3]
arrtype = ['unsorted', 'sorted', 'reverse']

plt.figure(figsize=(8,6))
plt.plot(arrtype, t, label='Time taken to sort')
plt.xlabel('Array type')
plt.ylabel('time taken(s)')
plt.title('Quick Sort with middle element as pivot')
plt.legend()
plt.savefig('quicksort.png')

plt.figure(figsize=(8,6))
plt.plot(arrtype, d, label='Recurssion Depth')
plt.xlabel('Array type')
plt.ylabel('Depth')
plt.title('Quick Sort with middle element as pivot')
plt.legend()
plt.savefig('quicksortdepth.png')

    


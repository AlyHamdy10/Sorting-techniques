from random import randint
import time


def quick_sort(arr, p, r):
    if p < r:
        q = random_pivot(arr, p, r)
        quick_sort(arr, p, q-1)
        quick_sort(arr, q+1, r)


def random_pivot(arr, p, r):
    i = randint(p, r)
    arr[i], arr[r] = arr[r], arr[i]
    return partition(arr, p, r)


def partition(arr, p, r):
    x = arr[r]
    i = p - 1
    # python does not include the second operand ex: [p,r[
    for j in range(p, r):
        if arr[j] <= x:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1


def merge(arr, left, mid, right):
    nL = mid - left + 1
    nR = right - mid

    L_array = [0] * nL
    R_array = [0] * nR

    for i in range(0, nL):
        L_array[i] = arr[i + left]
    for i in range(0, nR):
        R_array[i] = arr[i + mid + 1]

    i = 0
    j = 0
    k = left

    while i < nL and j < nR:
        if L_array[i] <= R_array[j]:
            arr[k] = L_array[i]
            i += 1
        else:
            arr[k] = R_array[j]
            j += 1
        k += 1
    while i < nL:
        arr[k] = L_array[i]
        i += 1
        k += 1
    while j < nR:
        arr[k] = R_array[j]
        j += 1
        k += 1


def merge_sort(arr, first, last):
    if first < last:
        mid = (first + last) // 2
        merge_sort(arr, first, mid)
        merge_sort(arr, mid + 1, last)
        merge(arr, first, mid, last)


def insertion_sort(arr):
    for i in range(1, len(arr)):  # loop to compare each i'th element with all the elements before it
        key = arr[i]  # i'th element being the key in the comparison
        hole = i  # current position of the key in the array after changes
        # while the hole is not the first element in the array and the previous is larger
        while(hole > 0 and arr[hole-1] > key):
            arr[hole] = arr[hole - 1]  # shift the previous element right
            hole = hole - 1
        # place the key in the right position after shifting all larger elements on the right of the new key's position
        arr[hole] = key


def selection_sort(arr):
    for i in range(len(arr) - 1):  # loop around all elements except last one
        i_min = i
        # compares the current key with every element in the array to check if it's the smallest or not
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i_min]:     # if not replace the i_min with the smaller element index
                i_min = j
        if i != i_min:  # if a change occured in the i_min, swap
            arr[i], arr[i_min] = arr[i_min], arr[i]


def generate_unsorted(size):
    arr = [0] * size
    for i in range(size):
        arr[i] = randint(0, size)
    return arr


size = int(input("Enter the array's size:"))
arr = generate_unsorted(size)
# Quick Sort
t_array = arr.copy
begin = time.time()
quick_sort(arr, 0, size-1)
time.sleep(1)
end = time.time()
exec_time = end - begin
print("Running time for Quick Sort is \t\t" + str(exec_time*1000) + " ms")
# Merge Sort
t_array = arr.copy
begin = time.time()
merge_sort(arr, 0, size-1)
time.sleep(1)
end = time.time()
exec_time = end - begin
print("Running time for Merge Sort is \t\t" + str(exec_time*1000) + " ms")
# Selection Sort
t_array = arr.copy
begin = time.time()
selection_sort(arr)
time.sleep(1)
end = time.time()
exec_time = end - begin
print("Running time for Selection Sort is \t" + str(exec_time*1000) + " ms")
# Insertion Sort
t_array = arr.copy
begin = time.time()
insertion_sort(arr)
time.sleep(1)
end = time.time()
exec_time = end - begin
print("Running time for Insertion Sort is \t" + str(exec_time*1000) + " ms")

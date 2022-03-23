from random import randint
import time


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


def merge_sort(arr, first, last, threshold):
    if first < last:
        if (last - first) < threshold:  # last - first + 1
            selection_sort(arr, first, last)
            return
        else:
            mid = (first + last) // 2
            merge_sort(arr, first, mid, threshold)
            merge_sort(arr, mid + 1, last, threshold)
            merge(arr, first, mid, last)
    else:
        return


def selection_sort(arr, first, last):
    for i in range(first, last):  # loop around all elements except last one
        i_min = i
        # compares the current key with every element in the array to check if it's the smallest or not
        for j in range(i+1, last+1):
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

# hybrid merge selection sort
t_arr = arr.copy
begin = time.time()
merge_sort(arr, 0, size-1, 6)
time.sleep(1)
end = time.time()
exec_time = end - begin
print("Running time for Hybrid Merge Selection Sort is \t" +
      str(exec_time*1000) + " ms")

# merge sort
t_arr = arr.copy
begin = time.time()
merge_sort(arr, 0, size-1, 0)
time.sleep(1)
end = time.time()
exec_time = end - begin
print("Running time for Merge Sort is \t\t\t\t" +
      str(exec_time*1000) + " ms")

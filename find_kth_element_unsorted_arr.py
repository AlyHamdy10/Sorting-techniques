from random import randint


def partition(arr, p, r, k):  # add while 0 <= k < size
    x = arr[r]
    i = p - 1
    # python does not include the second operand ex: [p,r[
    for j in range(p, r):
        if arr[j] <= x:  # p<k<r
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    if i + 1 == k:
        return arr[i]
    elif i + 1 < k:
        return partition(arr, i+1, r, k)
    else:
        return partition(arr, p, i, k)


def generate_unsorted(size):
    arr = [0] * size
    for i in range(size):
        arr[i] = randint(0, size)
    return arr


#size = int(input("Enter the array's size:"))
k = int(input("Enter k:"))
#arr = generate_unsorted(size)
arr = [6, 0, 7, 3, 1, 5, 9, 8, 4, 2]
size = 10
print(arr)
print(partition(arr, 0, size-1, k))
arr.sort()
print(arr)

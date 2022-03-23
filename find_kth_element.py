def partition(arr, p, r, k):  # fn using last element as pivot
    x = arr[r]  # r is the index of the last element
    i = p - 1
    for j in range(p, r):
        if arr[j] < x:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
            print(arr)
    arr[i+1], arr[r] = arr[r], arr[i+1]
    if (i+1) == k:
        return arr[i]
    elif (i+1) > k:
        return partition(arr, p, i, k)
    else:
        return partition(arr, i+2, r, k)


k = int(input("Enter K"))
arr = [6, 0, 7, 3, 1, 5, 9, 8, 4, 2]
size = 10
print(arr)
print(partition(arr, 0, size-1, k))
arr.sort()
print(arr)

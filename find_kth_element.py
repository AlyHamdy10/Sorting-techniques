from random import randint


def kth_element(arr, first, last, k):
    while True:
        pivot = random_pivot(arr, first, last)
        if (pivot+1) == k:
            return arr[pivot]
        elif (pivot + 1) > k:
            last = pivot - 1
        else:
            first = pivot + 1


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


while True:
    k = 0
    size = 10
    while k < 1 or k > size:
        k = int(input("Enter K:  "))
        if k < 1 or k > size:
            print(">>>Out of bound<<<")
    arr = [6, 0, 7, 3, 1, 5, 9, 8, 4, 2]
    print(arr)
    print(str(k) + "th smallest element is:\t" +
          str(kth_element(arr, 0, size-1, k)))
    arr.sort()
    print(arr)
    print()

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

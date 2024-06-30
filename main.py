import random
import time
import heapq

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index], arr[i]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def heap_sort(arr):
    n = len(arr)
    heapq.heapify(arr)
    sorted_arr = []
    
    for _ in range(n):
        sorted_arr.append(heapq.heappop(arr))

    arr[:] = sorted_arr 

def merge_sort(arr):
    if len(arr) > 1:
        mid_point = len(arr) // 2
        l = arr[:mid_point]
        r = arr[mid_point:] 

        merge_sort(l) 
        merge_sort(r) 

        i = 0
        j = 0
        k = 0

        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                j += 1
            k += 1

        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1
        
        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1

arr = [5, 3, 2, 1, 4, 6]
merge_sort(arr)
print(arr)

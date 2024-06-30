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


arr = [5, 3, 2, 1, 4, 6]
insertion_sort(arr)
print(arr)

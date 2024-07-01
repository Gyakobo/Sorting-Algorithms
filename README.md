# Sorting Algorithms

![image](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![image](https://img.shields.io/badge/windows%20terminal-4D4D4D?style=for-the-badge&logo=windows%20terminal&logoColor=white)

Author: [Andrew Gyakobo](https://github.com/Gyakobo)

## Intro

This intro serves to test out 5 various sorting algorithms and possibly determing their big-Oh notation through this example.

## Methodology

For starters, we start by importing all the necessary libraries and their respective methods. On a side note, I also add a bunch of ANSI sequence that will color code the console outputted text. By the way, if you're interested in color coding in python then please go through this [repo](https://github.com/Gyakobo/python-colored-console-output) I wrote.

```python
from random import randint
import time
import heapq

# Colors
# ANSI escape sequences for text colors
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
RESET = "\033[0m"
```

Afterwards, we then write out the sorting algorithms:

1) Both **Selection Sort** and **Insertion Sort** are $O(n^{2})$ algorithms, making them inefficient for large datasets. They work reasonably fast for small array but become impractically slow as the array size increases.

```python
# Selection Sort
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
```

2) **Heap Sort** has $O(n log n)$ time complexity, making it much more efficienct for larger datasets compared to selection and insertion sort. It performs consistently well but usually not as fast as quicksort.

```python
# Heap Sort
def heap_sort(arr):
    n = len(arr)
    heapq.heapify(arr)
    sorted_arr = []
    
    for _ in range(n):
        sorted_arr.append(heapq.heappop(arr))

    arr[:] = sorted_arr 
```

3) **Merge Sort** also has $O(n log n)$ time complexity and provides stable sorting, but it requires additional space for merging, which could be a disadvantage in memory-constrained environments.

```python
# Merge Sort
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
```

4) **Quick Sort** is typically the fastest of the algorithms tested due to its $O(n log n)$ average-case time complexity, though it has a worst-case time complexity of $O(n^{2})$. It is efficient for large datasets, but care must be taken to avoid the worst-case scenario (e.g., using a good pivot strategy).

```python
# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot_point = arr[len(arr) // 2]
    left    = [] 
    middle  = [] 
    right   = [] 

    for x in arr:
        if x < pivot_point:
            left.append(x)
    for x in arr:
        if x == pivot_point:
            middle.append(x)
    for x in arr:
        if x > pivot_point:
            right.append(x)

    return quick_sort(left) + middle + quick_sort(right)
```

## License
MIT
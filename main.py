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

# Heap Sort
def heap_sort(arr):
    n = len(arr)
    heapq.heapify(arr)
    sorted_arr = []
    
    for _ in range(n):
        sorted_arr.append(heapq.heappop(arr))

    arr[:] = sorted_arr 

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

def sorting_algorithm(sizes):
    algorithms = {
        'Selection Sort': selection_sort,
        'Insertion Sort': insertion_sort,
        'Heap Sort': heap_sort,
        'Merge Sort': merge_sort,
        'Quick Sort': quick_sort
    }

    results = {name: [] for name in algorithms}

    for size in sizes:
        arr = [randint(0, 1000000) for _ in range(size)]
        for name, func in algorithms.items():
            temp_arr = arr.copy()
            start_time = time.time()
            if name == "Quick Sort":
                temp_arr = func(temp_arr)
            else:
                func(temp_arr)
            end_time = time.time()
            results[name].append(end_time - start_time)
            
            if name == "Selection Sort":
                print(RED + f"{name} completed for size {size} in {end_time - start_time:.4f} seconds." + RESET)
            if name == "Insertion Sort":  
                print(GREEN + f"{name} completed for size {size} in {end_time - start_time:.4f} seconds." + RESET)
            if name == "Heap Sort":  
                print(YELLOW + f"{name} completed for size {size} in {end_time - start_time:.4f} seconds." + RESET)
            if name == "Merge Sort":  
                print(MAGENTA + f"{name} completed for size {size} in {end_time - start_time:.4f} seconds." + RESET)
            else:
                print(CYAN + f"{name} completed for size {size} in {end_time - start_time:.4f} seconds." + RESET)

        print(end="\n\n")

    return results

def main():
    sizes = [10, 100, 1000, 10000, 100000, 1000000, 10000000]
    results = sorting_algorithm(sizes)

    for name, times in results.items():
        print(f"\n{name}:")
        for size, time_taken in zip(sizes, times):
            print(f"Size {size}: {time_taken:.4f} seconds")

if __name__ == "__main__":
    main()



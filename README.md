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

1) Selection Sort

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
    ```


## License
MIT
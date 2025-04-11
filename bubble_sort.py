#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    swap_count = 0
    n = len(a)
    
    for i in range(n):
        # Track if no swaps occur in this pass
        swapped = False
        
        for j in range(0, n - 1 - i):
            # For ascending order, swap if current > next
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swap_count += 1
                swapped = True
        
        # If no swaps occurred in this pass, array is sorted
        if not swapped:
            break
    
    # Print the required output
    print(f"Array is sorted in {swap_count} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
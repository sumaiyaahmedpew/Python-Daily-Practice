# problem_25 Array Copy and Independence Check
import numpy as np

def check_copy_behavior(arr):
    shallow = arr.view()
    deep = arr.copy()

    print("Original:", arr)
    arr[0] = 999
    print("\nAfter modifying original...")
    print("Original:", arr)
    print("Shallow copy:", shallow)
    print("Deep copy:", deep)

arr = np.array([1, 2, 3, 4])
check_copy_behavior(arr)

import random
import time

def sequential_search(arr, target):
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            return i, comparisons
    return -1, comparisons

def binary_search(arr, target):
    comparisons = 0
    left, right = 0, len(arr) - 1
    
    while left <= right:
        comparisons += 1
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1, comparisons

def main():
    print("Search Algorithms Comparison")
    print("=" * 30)
    
    test_data = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target = 7
    
    seq_pos, seq_comps = sequential_search(test_data, target)
    bin_pos, bin_comps = binary_search(test_data, target)
    
    print(f"Sequential Search: Found at position {seq_pos} with {seq_comps} comparisons")
    print(f"Binary Search: Found at position {bin_pos} with {bin_comps} comparisons")

if __name__ == "__main__":
    main()
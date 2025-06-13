import random
import time

def sequential_search(arr, target):
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            return i, comparisons
    return -1, comparisons

def main():
    print("Search Algorithms Comparison")
    print("=" * 30)
    
    test_data = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target = 7
    
    position, comps = sequential_search(test_data, target)
    print(f"Sequential Search: Found at position {position} with {comps} comparisons")

if __name__ == "__main__":
    main()
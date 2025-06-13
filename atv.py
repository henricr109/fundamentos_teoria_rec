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

def measure_performance(search_func, arr, target):
    start_time = time.time()
    position, comparisons = search_func(arr, target)
    end_time = time.time()
    execution_time = (end_time - start_time) * 1000
    return position, comparisons, execution_time

def generate_sorted_data(size):
    return list(range(1, size + 1, 2))

def main():
    print("Search Algorithms Comparison")
    print("=" * 30)
    
    data_sizes = [1000, 10000, 100000]
    
    for size in data_sizes:
        print(f"\nTesting with {size} elements:")
        data = generate_sorted_data(size)
        
        random_target = data[random.randint(0, len(data) - 1)]
        missing_target = data[-1] + 100
        
        print(f"Average case (target: {random_target}):")
        seq_pos, seq_comps, seq_time = measure_performance(sequential_search, data, random_target)
        bin_pos, bin_comps, bin_time = measure_performance(binary_search, data, random_target)
        
        print(f"  Sequential: Position {seq_pos}, {seq_comps} comparisons, {seq_time:.4f}ms")
        print(f"  Binary: Position {bin_pos}, {bin_comps} comparisons, {bin_time:.4f}ms")

if __name__ == "__main__":
    main()
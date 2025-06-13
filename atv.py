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

def run_test_case(data, target, case_name):
    print(f"\n{case_name} (target: {target}):")
    
    seq_pos, seq_comps, seq_time = measure_performance(sequential_search, data, target)
    bin_pos, bin_comps, bin_time = measure_performance(binary_search, data, target)
    
    print(f"  Sequential: Position {seq_pos}, {seq_comps} comparisons, {seq_time:.4f}ms")
    print(f"  Binary: Position {bin_pos}, {bin_comps} comparisons, {bin_time:.4f}ms")
    
    if seq_time > 0 and bin_time > 0:
        speedup = seq_time / bin_time
        print(f"  Binary search is {speedup:.2f}x faster")
    
    return (seq_comps, seq_time), (bin_comps, bin_time)

def main():
    print("Search Algorithms Performance Comparison")
    print("=" * 50)
    
    data_sizes = [1000, 10000, 100000]
    results = []
    
    random.seed(42)
    
    for size in data_sizes:
        print(f"\nTesting with {size:,} elements:")
        print("-" * 30)
        
        data = generate_sorted_data(size)
        
        random_target = data[random.randint(0, len(data) - 1)]
        missing_target = data[-1] + 100
        
        avg_seq, avg_bin = run_test_case(data, random_target, "Average case")
        worst_seq, worst_bin = run_test_case(data, missing_target, "Worst case")
        
        results.append({
            'size': size,
            'avg_case': {'seq': avg_seq, 'bin': avg_bin},
            'worst_case': {'seq': worst_seq, 'bin': worst_bin}
        })
    
    print("\n" + "=" * 50)
    print("SUMMARY")
    print("=" * 50)
    
    for result in results:
        size = result['size']
        print(f"\nData size: {size:,} elements")
        print(f"Average case - Sequential: {result['avg_case']['seq'][0]} comparisons")
        print(f"Average case - Binary: {result['avg_case']['bin'][0]} comparisons")
        print(f"Worst case - Sequential: {result['worst_case']['seq'][0]} comparisons")
        print(f"Worst case - Binary: {result['worst_case']['bin'][0]} comparisons")

if __name__ == "__main__":
    main()
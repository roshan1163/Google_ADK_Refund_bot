# Sorting Algorithms in Data Structures and Algorithms (DSA)

This guide covers common sorting algorithms in Data Structures & Algorithms (DSA), including their explanations, Python implementations, and complexity analysis.

---

## 📊 Summary of Sorting Algorithms

| Algorithm | Best Time | Average Time | Worst Time | Space Complexity | Stable? | In-Place? |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Bubble Sort** | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | Yes | Yes |
| **Selection Sort** | $O(n^2)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | No | Yes |
| **Insertion Sort** | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | Yes | Yes |
| **Merge Sort** | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(n)$ | Yes | No |
| **Quick Sort** | $O(n \log n)$ | $O(n \log n)$ | $O(n^2)$ | $O(\log n)$ | No | Yes |
| **Heap Sort** | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(1)$ | No | Yes |
| **Counting Sort** | $O(n + k)$ | $O(n + k)$ | $O(n + k)$ | $O(k)$ | Yes | No |
| **Radix Sort** | $O(n \cdot d)$ | $O(n \cdot d)$ | $O(n \cdot d)$ | $O(n + k)$ | Yes | No |
| **Bucket Sort** | $O(n + k)$ | $O(n + k)$ | $O(n^2)$ | $O(n)$ | Yes | No |

*Note: $n$ is the number of elements, $k$ is the key range, and $d$ is the number of digits.*

---

## 1. Bubble Sort

### Concept
Bubble Sort works by repeatedly swapping adjacent elements if they are in the wrong order. With each pass, the largest unsorted element "bubbles up" to its correct position at the end.

### Python Implementation
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
```

---

## 2. Selection Sort

### Concept
Selection Sort repeatedly selects the minimum element from the unsorted segment and moves it to the beginning of the array.

### Python Implementation
```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
```

---

## 3. Insertion Sort

### Concept
Insertion Sort builds the sorted array one item at a time. It works similarly to sorting playing cards in your hands: taking one element and placing it into its correct position among the already sorted elements.

### Python Implementation
```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
```

---

## 4. Merge Sort

### Concept
Merge Sort is a **Divide and Conquer** algorithm. It continuously splits the array into two halves, recursively sorts them, and then merges the two sorted halves.

### Python Implementation
```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

---

## 5. Quick Sort

### Concept
Quick Sort is a **Divide and Conquer** algorithm. It selects a 'pivot' element, partitions the array such that elements smaller than the pivot go to the left and larger elements go to the right, and then recursively sorts the sub-arrays.

### Python Implementation
```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)
```

---

## 6. Heap Sort

### Concept
Heap Sort converts the array into a **Max-Heap**, repeatedly extracts the maximum element (root), places it at the end of the array, and reduces the heap size, re-heapifying each time.

### Python Implementation
```python
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[left] > arr[largest]:
        largest = left
        
    if right < n and arr[right] > arr[largest]:
        largest = right
        
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
        
    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
        
    return arr
```

---

## 7. Counting Sort

### Concept
Counting Sort is a non-comparison sorting technique based on keys between a specific range. It counts the occurrences of each unique element and uses arithmetic to determine their positions in the sorted output.

### Python Implementation
```python
def counting_sort(arr):
    if not arr:
        return arr
    
    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1
    
    count = [0] * range_of_elements
    output = [0] * len(arr)
    
    for num in arr:
        count[num - min_val] += 1
        
    for i in range(1, len(count)):
        count[i] += count[i - 1]
        
    for num in reversed(arr):
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1
        
    return output
```

---

## 8. Radix Sort

### Concept
Radix Sort sorts elements digit by digit, starting from the least significant digit (LSD) to the most significant digit (MSD). It uses Counting Sort as a subroutine to sort the digits.

### Python Implementation
```python
def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1
        
    for i in range(1, 10):
        count[i] += count[i - 1]
        
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    if not arr:
        return arr
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10
    return arr
```

---

## 9. Bucket Sort

### Concept
Bucket Sort distributes input elements into several buckets. Each bucket is then sorted individually (either using another algorithm or recursively), and the sorted buckets are concatenated.

### Python Implementation
```python
def bucket_sort(arr):
    if len(arr) == 0:
        return arr
    
    bucket_count = len(arr)
    max_val, min_val = max(arr), min(arr)
    val_range = (max_val - min_val) / bucket_count
    
    if val_range == 0:
        return arr
    
    buckets = [[] for _ in range(bucket_count)]
    
    for num in arr:
        index = int((num - min_val) / val_range)
        if index == bucket_count:
            index -= 1
        buckets[index].append(num)
        
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))
        
    return sorted_arr
```

---

## 💡 When to Use Which Algorithm?

1. **Small Arrays / Nearly Sorted Data**: **Insertion Sort** is efficient and simple for small datasets or data that is already largely sorted.
2. **General Purpose Large Datasets**: **Merge Sort** or **Quick Sort**.
   - Use **Merge Sort** if guaranteed $O(n \log n)$ time complexity and stability are required.
   - Use **Quick Sort** for better cache utilization and practical speed when memory is limited (in-place).
3. **Memory-Constrained Systems**: **Heap Sort** (offers $O(n \log n)$ time with $O(1)$ extra space).
4. **Small Integer Range**: **Counting Sort** or **Radix Sort** (achieves linear time complexity $O(n)$).

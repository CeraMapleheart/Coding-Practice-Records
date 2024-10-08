
# Time Complexities in Algorithms

Time complexity is a measure of the amount of time an algorithm takes to complete as a function of the input size. It helps in analyzing and predicting the performance of algorithms.

This guide will walk you through common time complexities, how to calculate them, and examples of problems where these complexities arise.

## 1. Constant Time: O(1)
An algorithm with constant time complexity will always execute in the same amount of time regardless of the input size.

### Example:
- Accessing an element from an array using its index: `arr[5]`
- Pushing or popping elements from a stack or queue.

### Explanation:
```python
# Example of O(1)
def constant_example(arr):
    return arr[0]  # Accessing an element from the array (indexing is O(1))
```

## 2. Logarithmic Time: O(log n)
Algorithms with logarithmic time complexity reduce the problem size with each step. This often happens with divide-and-conquer algorithms.

### Example:
- Binary Search
- Finding an element in a balanced binary search tree (BST)

### Explanation:
```python
# Example of O(log n)
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```

## 3. Linear Time: O(n)
Linear time complexity means that the running time increases linearly with the size of the input. This is common in algorithms that involve iterating over the input once.

### Example:
- Finding the maximum element in an array.
- Linear Search

### Explanation:
```python
# Example of O(n)
def find_max(arr):
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val
```

## 4. Linearithmic Time: O(n log n)
This complexity arises in algorithms that involve both dividing the input and iterating over it. Many efficient sorting algorithms exhibit this complexity.

### Example:
- Merge Sort
- Quick Sort (average case)

### Explanation:
```python
# Example of O(n log n)
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
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

## 5. Quadratic Time: O(n^2)
Quadratic time complexity often arises from algorithms that involve nested loops, where each element in the input is compared to every other element.

### Example:
- Bubble Sort
- Insertion Sort
- Checking for duplicates in an unsorted array using brute force.

### Explanation:
```python
# Example of O(n^2)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
```

## 6. Cubic Time: O(n^3)
Cubic time complexity typically arises in algorithms that involve three nested loops.

### Example:
- Multiplying two matrices.
- Solving the all-pairs shortest path using Floyd-Warshall algorithm.

### Explanation:
```python
# Example of O(n^3)
def matrix_multiply(A, B):
    n = len(A)
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]
    return result
```

## 7. Exponential Time: O(2^n)
Exponential time complexity typically arises in recursive algorithms where the problem size doubles with each step. These algorithms are inefficient for large inputs.

### Example:
- Recursive calculation of Fibonacci numbers.
- Solving the Traveling Salesman Problem using brute force.

### Explanation:
```python
# Example of O(2^n)
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
```

## 8. Factorial Time: O(n!)
Factorial time complexity usually arises in problems that involve generating all permutations or combinations of a set.

### Example:
- Solving the Traveling Salesman Problem by generating all possible routes.
- Generating all permutations of a string.

### Explanation:
```python
# Example of O(n!)
from itertools import permutations

def all_permutations(s):
    return list(permutations(s))
```

## How to Calculate Time Complexity

### Steps:
1. **Identify the basic operations**: Focus on the fundamental operation (e.g., comparison, addition) that contributes the most to the running time.
2. **Analyze loops**: 
   - A single loop contributes `O(n)`.
   - Nested loops contribute `O(n^2)`, `O(n^3)`, etc.
3. **Recursive algorithms**: Use recurrence relations (e.g., Master Theorem) to calculate the complexity of divide-and-conquer algorithms.
4. **Drop constants and non-dominant terms**: When expressing time complexity, focus on the term that grows the fastest as input size increases.

### Common Pitfalls:
- Confusing worst-case, best-case, and average-case complexities.
- Overlooking hidden constant factors (they matter for practical performance but are ignored in asymptotic analysis).

## Conclusion
Time complexity is a crucial aspect of algorithm design and analysis. It helps developers evaluate the efficiency of their algorithms and choose the best one for a given problem. While constant time algorithms are the most efficient, many real-world problems require trade-offs between time complexity and space complexity.

Understanding time complexity allows you to make informed decisions and optimize your code for better performance.

---

### Resources:
- [Big-O Cheat Sheet](https://www.bigocheatsheet.com/)
- [Master Theorem](https://en.wikipedia.org/wiki/Master_theorem)

<!---LeetCode Topics Start-->
# LeetCode Topics
## Array
|  |
| ------- |
| [0001-two-sum](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0001-two-sum) |
| [0004-median-of-two-sorted-arrays](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0004-median-of-two-sorted-arrays) |
| [0027-remove-element](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0027-remove-element) |
| [0048-rotate-image](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0048-rotate-image) |
| [0054-spiral-matrix](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0054-spiral-matrix) |
| [0056-merge-intervals](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0056-merge-intervals) |
| [0075-sort-colors](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0075-sort-colors) |
| [0080-remove-duplicates-from-sorted-array-ii](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0080-remove-duplicates-from-sorted-array-ii) |
| [0088-merge-sorted-array](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0088-merge-sorted-array) |
| [0121-best-time-to-buy-and-sell-stock](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0121-best-time-to-buy-and-sell-stock) |
| [0136-single-number](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0136-single-number) |
| [0137-single-number-ii](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0137-single-number-ii) |
| [0167-two-sum-ii-input-array-is-sorted](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0167-two-sum-ii-input-array-is-sorted) |
| [0169-majority-element](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0169-majority-element) |
| [0209-minimum-size-subarray-sum](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0209-minimum-size-subarray-sum) |
| [0217-contains-duplicate](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0217-contains-duplicate) |
| [0228-summary-ranges](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0228-summary-ranges) |
| [0238-product-of-array-except-self](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0238-product-of-array-except-self) |
| [0260-single-number-iii](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0260-single-number-iii) |
| [0643-maximum-average-subarray-i](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0643-maximum-average-subarray-i) |
| [0870-magic-squares-in-grid](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0870-magic-squares-in-grid) |
| [0921-spiral-matrix-iii](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0921-spiral-matrix-iii) |
| [1556-make-two-arrays-equal-by-reversing-subarrays](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/1556-make-two-arrays-equal-by-reversing-subarrays) |
| [1615-range-sum-of-sorted-subarray-sums](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/1615-range-sum-of-sorted-subarray-sums) |
| [2163-kth-distinct-string-in-an-array](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/2163-kth-distinct-string-in-an-array) |
| [2255-minimum-swaps-to-group-all-1s-together-ii](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/2255-minimum-swaps-to-group-all-1s-together-ii) |
| [2350-find-closest-number-to-zero](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/2350-find-closest-number-to-zero) |
| [2727-number-of-senior-citizens](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/2727-number-of-senior-citizens) |
## Hash Table
|  |
| ------- |
| [0001-two-sum](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0001-two-sum) |
| [0003-longest-substring-without-repeating-characters](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0003-longest-substring-without-repeating-characters) |
| [0013-roman-to-integer](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0013-roman-to-integer) |
| [0169-majority-element](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0169-majority-element) |
| [0217-contains-duplicate](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0217-contains-duplicate) |
| [0424-longest-repeating-character-replacement](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0424-longest-repeating-character-replacement) |
| [0567-permutation-in-string](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0567-permutation-in-string) |
| [0782-jewels-and-stones](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0782-jewels-and-stones) |
| [0870-magic-squares-in-grid](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0870-magic-squares-in-grid) |
| [1556-make-two-arrays-equal-by-reversing-subarrays](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/1556-make-two-arrays-equal-by-reversing-subarrays) |
| [1557-check-if-a-string-contains-all-binary-codes-of-size-k](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/1557-check-if-a-string-contains-all-binary-codes-of-size-k) |
| [2163-kth-distinct-string-in-an-array](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/2163-kth-distinct-string-in-an-array) |
| [3276-minimum-number-of-pushes-to-type-word-ii](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/3276-minimum-number-of-pushes-to-type-word-ii) |
## Divide and Conquer
|  |
| ------- |
| [0004-median-of-two-sorted-arrays](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0004-median-of-two-sorted-arrays) |
| [0169-majority-element](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0169-majority-element) |
## Sorting
|  |
| ------- |
| [0056-merge-intervals](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0056-merge-intervals) |
| [0075-sort-colors](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0075-sort-colors) |
| [0088-merge-sorted-array](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0088-merge-sorted-array) |
| [0169-majority-element](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0169-majority-element) |
| [0217-contains-duplicate](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0217-contains-duplicate) |
| [1556-make-two-arrays-equal-by-reversing-subarrays](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/1556-make-two-arrays-equal-by-reversing-subarrays) |
| [1615-range-sum-of-sorted-subarray-sums](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/1615-range-sum-of-sorted-subarray-sums) |
| [3276-minimum-number-of-pushes-to-type-word-ii](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/3276-minimum-number-of-pushes-to-type-word-ii) |
## Counting
|  |
| ------- |
| [0169-majority-element](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0169-majority-element) |
| [2163-kth-distinct-string-in-an-array](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/2163-kth-distinct-string-in-an-array) |
| [3276-minimum-number-of-pushes-to-type-word-ii](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/3276-minimum-number-of-pushes-to-type-word-ii) |
## Two Pointers
|  |
| ------- |
| [0027-remove-element](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0027-remove-element) |
| [0075-sort-colors](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0075-sort-colors) |
| [0080-remove-duplicates-from-sorted-array-ii](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0080-remove-duplicates-from-sorted-array-ii) |
| [0088-merge-sorted-array](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0088-merge-sorted-array) |
| [0125-valid-palindrome](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0125-valid-palindrome) |
| [0167-two-sum-ii-input-array-is-sorted](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0167-two-sum-ii-input-array-is-sorted) |
| [0392-is-subsequence](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0392-is-subsequence) |
| [0567-permutation-in-string](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0567-permutation-in-string) |
| [1615-range-sum-of-sorted-subarray-sums](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/1615-range-sum-of-sorted-subarray-sums) |
| [1894-merge-strings-alternately](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/1894-merge-strings-alternately) |
## Math
|  |
| ------- |
| [0009-palindrome-number](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0009-palindrome-number) |
| [0013-roman-to-integer](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0013-roman-to-integer) |
| [0048-rotate-image](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0048-rotate-image) |
| [0273-integer-to-english-words](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0273-integer-to-english-words) |
| [0870-magic-squares-in-grid](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0870-magic-squares-in-grid) |
| [1013-fibonacci-number](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/1013-fibonacci-number) |
| [1806-count-of-matches-in-tournament](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/1806-count-of-matches-in-tournament) |
| [3567-convert-date-to-binary](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/3567-convert-date-to-binary) |
## Simulation
|  |
| ------- |
| [0054-spiral-matrix](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0054-spiral-matrix) |
| [0921-spiral-matrix-iii](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0921-spiral-matrix-iii) |
| [1806-count-of-matches-in-tournament](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/1806-count-of-matches-in-tournament) |
## Graph
|  |
| ------- |
| [1916-find-center-of-star-graph](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/1916-find-center-of-star-graph) |
## Bit Manipulation
|  |
| ------- |
| [0136-single-number](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0136-single-number) |
| [0137-single-number-ii](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0137-single-number-ii) |
| [0260-single-number-iii](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0260-single-number-iii) |
| [1557-check-if-a-string-contains-all-binary-codes-of-size-k](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/1557-check-if-a-string-contains-all-binary-codes-of-size-k) |
## Sliding Window
|  |
| ------- |
| [0003-longest-substring-without-repeating-characters](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0003-longest-substring-without-repeating-characters) |
| [0209-minimum-size-subarray-sum](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0209-minimum-size-subarray-sum) |
| [0424-longest-repeating-character-replacement](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0424-longest-repeating-character-replacement) |
| [0567-permutation-in-string](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0567-permutation-in-string) |
| [0643-maximum-average-subarray-i](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0643-maximum-average-subarray-i) |
| [2255-minimum-swaps-to-group-all-1s-together-ii](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/2255-minimum-swaps-to-group-all-1s-together-ii) |
## String
|  |
| ------- |
| [0003-longest-substring-without-repeating-characters](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0003-longest-substring-without-repeating-characters) |
| [0013-roman-to-integer](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0013-roman-to-integer) |
| [0014-longest-common-prefix](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0014-longest-common-prefix) |
| [0125-valid-palindrome](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0125-valid-palindrome) |
| [0273-integer-to-english-words](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0273-integer-to-english-words) |
| [0392-is-subsequence](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0392-is-subsequence) |
| [0424-longest-repeating-character-replacement](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0424-longest-repeating-character-replacement) |
| [0567-permutation-in-string](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0567-permutation-in-string) |
| [0678-valid-parenthesis-string](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0678-valid-parenthesis-string) |
| [0782-jewels-and-stones](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0782-jewels-and-stones) |
| [0812-rotate-string](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0812-rotate-string) |
| [1557-check-if-a-string-contains-all-binary-codes-of-size-k](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/1557-check-if-a-string-contains-all-binary-codes-of-size-k) |
| [1737-maximum-nesting-depth-of-the-parentheses](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/1737-maximum-nesting-depth-of-the-parentheses) |
| [1894-merge-strings-alternately](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/1894-merge-strings-alternately) |
| [2163-kth-distinct-string-in-an-array](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/2163-kth-distinct-string-in-an-array) |
| [2727-number-of-senior-citizens](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/2727-number-of-senior-citizens) |
| [3276-minimum-number-of-pushes-to-type-word-ii](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/3276-minimum-number-of-pushes-to-type-word-ii) |
| [3567-convert-date-to-binary](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/3567-convert-date-to-binary) |
## Rolling Hash
|  |
| ------- |
| [1557-check-if-a-string-contains-all-binary-codes-of-size-k](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/1557-check-if-a-string-contains-all-binary-codes-of-size-k) |
## Hash Function
|  |
| ------- |
| [1557-check-if-a-string-contains-all-binary-codes-of-size-k](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/1557-check-if-a-string-contains-all-binary-codes-of-size-k) |
## Dynamic Programming
|  |
| ------- |
| [0121-best-time-to-buy-and-sell-stock](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0121-best-time-to-buy-and-sell-stock) |
| [0392-is-subsequence](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0392-is-subsequence) |
| [0678-valid-parenthesis-string](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0678-valid-parenthesis-string) |
| [1013-fibonacci-number](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/1013-fibonacci-number) |
## Recursion
|  |
| ------- |
| [0273-integer-to-english-words](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0273-integer-to-english-words) |
| [1013-fibonacci-number](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/1013-fibonacci-number) |
## Memoization
|  |
| ------- |
| [1013-fibonacci-number](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/1013-fibonacci-number) |
## Binary Search
|  |
| ------- |
| [0004-median-of-two-sorted-arrays](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0004-median-of-two-sorted-arrays) |
| [0167-two-sum-ii-input-array-is-sorted](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0167-two-sum-ii-input-array-is-sorted) |
| [0209-minimum-size-subarray-sum](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0209-minimum-size-subarray-sum) |
| [1615-range-sum-of-sorted-subarray-sums](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/1615-range-sum-of-sorted-subarray-sums) |
## Stack
|  |
| ------- |
| [0678-valid-parenthesis-string](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0678-valid-parenthesis-string) |
| [1737-maximum-nesting-depth-of-the-parentheses](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/1737-maximum-nesting-depth-of-the-parentheses) |
## Greedy
|  |
| ------- |
| [0678-valid-parenthesis-string](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0678-valid-parenthesis-string) |
| [3276-minimum-number-of-pushes-to-type-word-ii](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/3276-minimum-number-of-pushes-to-type-word-ii) |
## String Matching
|  |
| ------- |
| [0812-rotate-string](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0812-rotate-string) |
## Trie
|  |
| ------- |
| [0014-longest-common-prefix](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0014-longest-common-prefix) |
## Prefix Sum
|  |
| ------- |
| [0209-minimum-size-subarray-sum](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0209-minimum-size-subarray-sum) |
| [0238-product-of-array-except-self](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0238-product-of-array-except-self) |
## Matrix
|  |
| ------- |
| [0048-rotate-image](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0048-rotate-image) |
| [0054-spiral-matrix](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0054-spiral-matrix) |
| [0870-magic-squares-in-grid](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0870-magic-squares-in-grid) |
| [0921-spiral-matrix-iii](https://github.com/CeraMapleheart/Coding-Practice-Records/tree/master/0921-spiral-matrix-iii) |
<!---LeetCode Topics End-->
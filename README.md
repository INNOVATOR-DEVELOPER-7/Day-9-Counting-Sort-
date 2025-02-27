# Day-9-Counting-Sort-
Here Python Program for Counting Sort. Day 9 of Day 365.
- Initial Setup: Determine the range of the input data (the maximum and minimum values).
- Count Array: Create a count array to store the count of each unique element.
- Counting Elements: Count each element in the input array and store the count in the count array.
- Cumulative Count: Modify the count array such that each element at each index stores the sum of previous counts. This gives the position of each element in the output array.
- Build the Output Array: Traverse the input array and place each element in its correct position in the output array, decreasing the count for each element.
- Copy the Output Array: Copy the sorted elements from the output array back to the original array.

Here's a visual representation using the example array [4, 2, 2, 8, 3, 3, 1]:

1. Initial Array: [4, 2, 2, 8, 3, 3, 1]
2. Count Array:
   - Count each element: [1, 2, 2, 4, 1, 3, 8] -> [1, 2, 2, 1, 1, 0, 0, 1]
   - Result: [0, 1, 2, 2, 1, 0, 0, 1]
3. Cumulative Count:
   - Modify count array: [1, 3, 5, 6, 6, 6, 6, 7]
   - Result: [1, 1, 3, 5, 1, 6, 6, 7]
4. Build Output Array:
   - Place elements in sorted order
   - Result: [1, 2, 2, 3, 3, 4, 8]
5. Final Sorted Array: [1, 2, 2, 3, 3, 4, 8]

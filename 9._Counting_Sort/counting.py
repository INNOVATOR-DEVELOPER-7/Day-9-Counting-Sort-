def counting_sort(array):
    max_val = max(array)
    n = len(array)
    count = [0] * (max_val + 1)  # Initialize count array with all zeros
    output = [0] * n  # Output array to store sorted values

    # Store the count of each element
    for num in array:
        count[num] += 1

    # Update count array to store the cumulative count of elements
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Build the output array using the count array
    for i in range(n - 1, -1, -1):
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1

    # Copy the sorted values to the original array
    for i in range(n):
        array[i] = output[i]

# Get list of numbers from the user
user_input = input("Enter numbers separated by space: ")
array = list(map(int, user_input.split()))

# Perform counting sort
counting_sort(array)

# Print the sorted array
print("Sorted array:", array)

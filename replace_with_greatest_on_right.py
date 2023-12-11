def replace_with_greatest_on_right(arr):
    n = len(arr)
    max_right = arr[n - 1]
    arr[n - 1] = -1  # The rightmost element will always be replaced with -1

    for i in range(n - 2, -1, -1):
        temp = arr[i]
        arr[i] = max_right
        max_right = max(max_right, temp)

    return arr

# Example usage
input_array = [17, 18, 5, 4, 6, 1]
result_array = replace_with_greatest_on_right(input_array)
print(result_array)
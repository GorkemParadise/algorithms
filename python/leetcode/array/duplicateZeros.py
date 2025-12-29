def duplicateZeros(self, arr):
    zeros = arr.count(0)
    n = len(arr)
    i = n - 1
    j = n + zeros - 1

    while i >= 0:
        if j < n:
            arr[j] = arr[i]
        if arr[i] == 0:
            j -= 1
            if j < n:
                arr[j] = 0
        i -= 1
        j -= 1
    return arr

# Example usage:
arr = [1,0,2,3,0,4,5,0]
print(duplicateZeros(None, arr))  # Output: [1,0,0,2,3,0,0,4]
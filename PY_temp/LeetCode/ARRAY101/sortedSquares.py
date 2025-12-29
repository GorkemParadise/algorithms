def sortedSquares(self, nums):
    return sorted(x * x for x in nums)

# Example usage:
nums = [-4, -1, 0, 3, 10]
print(sortedSquares(None, nums))  # Output: [0, 1, 9, 16, 100]
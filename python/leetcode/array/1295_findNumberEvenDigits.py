def findNumbers(self, nums):
    count = 0
    for k in nums:
        if len(str(k)) % 2 == 0:
            count += 1
    return count

# Example usage:
nums = [12, 345, 2, 6, 7896]
result = findNumbers(None, nums)
print(result)  # Output: 2
"""
Problem: 1295. Find Numbers with Even Number of Digits
Link: https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
Difficulty: Easy
"""



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
"""
Problem: 977. Squares of a Sorted Array
Link: https://leetcode.com/problems/squares-of-a-sorted-array/
Difficulty: Easy
"""



def sortedSquares(self, nums):
    return sorted(x * x for x in nums)

# Example usage:
nums = [-4, -1, 0, 3, 10]
print(sortedSquares(None, nums))  # Output: [0, 1, 9, 16, 100]
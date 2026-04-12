"""
Problem: 26. Remove Duplicates from Sorted Array
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
Difficulty: Easy
"""


class Solution:
    def removeDuplicates(self, nums):
        seen = []
        total = 0
        for k in nums:
            if k not in seen:
                seen.append(k)
                nums[total] = k
                total += 1
        return total
    
# Example usage:
solution = Solution()
nums = [1, 1, 2]
length = solution.removeDuplicates(nums)
print(length)  # Output: 2
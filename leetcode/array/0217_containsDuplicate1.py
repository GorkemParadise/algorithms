class Solution:
    def containsDuplicate(self, nums):
        h = set()
        for num in nums:
            if num in h:
                return True
            else:
                h.add(num)
            
        return False
    

# Example usage:
solution = Solution()
print(solution.containsDuplicate([1, 2, 3, 1]))  # Output: True
print(solution.containsDuplicate([1, 2, 3, 4]))  # Output: False
print(solution.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # Output: True
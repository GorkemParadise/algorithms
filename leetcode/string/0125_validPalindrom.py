class Solution:
    def isPalindrome(self, s):
        filtered = [char.lower() for char in s if char.isalnum()]
        return filtered == filtered[::-1]

solution = Solution()
kk = solution.isPalindrome("A man, a plan, a canal: Panama")
print(kk)  # Output: True
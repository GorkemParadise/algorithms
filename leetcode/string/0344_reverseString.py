class Solution:
    def reverseString(self, s):
        right = len(s)-1
        left = 0
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s
    


sss = ["h","e","l","l","o"]
sol = Solution()
mm = sol.reverseString(sss)
print(mm)



'''
Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]


'''
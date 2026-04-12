class Solution:
    def reverse(self, x: int) -> int:
        MIN_INT = -2**31
        MAX_INT = 2**31 - 1
        
        res = 0
        num = abs(x)
        
        while num != 0:
            pop = num % 10
            num //= 10
            res = (res * 10) + pop
        if x < 0:
            res = -res
        if res < MIN_INT or res > MAX_INT:
            return 0
            
        return res



""" Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21 """
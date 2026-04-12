class Solution:
    def myAtoi(self, s):
        s = s.lstrip()
        if not s:
            return 0
        sign = 1
        if s[0] in ('-', '+'):
            if s[0] == '-':
                sign = -1
            s = s[1:]
        num = 0
        for char in s:
            if not char.isdigit():
                break
            num = num * 10 + int(char)
        num *= sign
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX
        return num
    

solution = Solution()
kk = solution.myAtoi("   -42cc552")
print(kk)  # Output: -42
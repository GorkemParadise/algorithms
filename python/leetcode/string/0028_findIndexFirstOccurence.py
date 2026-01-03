class Solution:
    def strStr(self, haystack, needle):
        if not needle:
            return 0
        
        h_len = len(haystack)
        n_len = len(needle)
        
        for i in range(h_len - n_len + 1):
            if haystack[i:i + n_len] == needle:
                return i
        return -1

sol = Solution()
o1 = sol.strStr("hello", "ll")  # Output: 2
o2 = sol.strStr("aaaaa", "bba")  # Output: -1
print(o1)
print(o2)
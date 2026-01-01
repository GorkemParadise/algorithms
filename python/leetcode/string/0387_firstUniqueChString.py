class Solution:
    def firstUniqChar(self, s):
        unique = []
        repeated = set()

        for ch in s:
            if ch in repeated:
                continue
            if ch in unique:
                unique.remove(ch)
                repeated.add(ch)
            else:
                unique.append(ch)

        if not unique:
            return -1

        return s.index(unique[0])



sol = Solution()
mm = sol.firstUniqChar("leetcodecode")
print(mm)

'''
Example 1:
Input: s = "leetcode"
Output: 0

Explanation:
The character 'l' at index 0 is the first character that does not occur at any other index.


Example 2:
Input: s = "loveleetcode"
Output: 2


Example 3:
Input: s = "aabb"
Output: -1
'''
        
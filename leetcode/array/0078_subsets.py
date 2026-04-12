class Solution:
    def subsets(self, nums):
        seen = [[]] 

        for num in nums:
            new_subsets = []
            for s in seen:
                new_subsets.append(s + [num])
            seen.extend(new_subsets)

        return seen


sol = Solution()
ss = sol.subsets([1,2,3])
print(ss)
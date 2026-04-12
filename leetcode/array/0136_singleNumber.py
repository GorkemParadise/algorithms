class Solution():
    def singleNumber(self, nums):
        return 2*sum(set(nums)) - sum(nums)
    

nums = [1, 1, 2, 2, 3]
print(Solution().singleNumber(nums))
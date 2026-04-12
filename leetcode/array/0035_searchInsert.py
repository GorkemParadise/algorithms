def find(nums, target):
    for k in range(len(nums)):
        if nums[k] >= target:
            return k
    return(len(nums))

class Solution:
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return(find(nums, target))

sol = Solution()
dd = sol.searchInsert([1,3,5,6], 7)
print(dd)


"""
Input: nums = [1,3,5,6], target = 5
Output: 2


Input: nums = [1,3,5,6], target = 2
Output: 1


Input: nums = [1,3,5,6], target = 7
Output: 4

"""
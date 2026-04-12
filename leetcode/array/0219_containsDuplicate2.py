class Solution:
    def containsNearbyDuplicate(self, nums, k):
        num_set = set()
        for i in range(len(nums)):
            if nums[i] in num_set:
                return True
            num_set.add(nums[i])
            if len(num_set) > k:
                num_set.remove(nums[i - k])
        return False

sol = Solution()
sol.containsNearbyDuplicate([1,2,3,1], 3)

'''
Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
'''
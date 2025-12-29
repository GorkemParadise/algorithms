class Solution:
    def moveZeroes(self, nums):
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        return nums
    
sol = Solution()
print(sol.moveZeroes([0,1,0,3,12]))





'''
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
'''

'''
Input:
[0,0,1]
Expected:
[1,0,0]
'''

'''
Input:
[0,0]
Expected:
[0,0]

'''
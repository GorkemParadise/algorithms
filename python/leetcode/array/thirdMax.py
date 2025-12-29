class Solution:
    def thirdMax(self, nums):
        newNums = set(sorted(nums))
        if len(newNums) < 3:
            return max(newNums)
        else:
            return sorted(newNums)[-3]
    

sol = Solution()
k=sol.thirdMax([3,2,1])
print(k)






'''
Example 1:

Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.
Example 2:

Input: nums = [1,2]
Output: 2
Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.

'''
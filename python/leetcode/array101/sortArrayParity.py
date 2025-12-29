class Solution:
    def sortArrayByParity(self, nums):
        even = []
        odd = []
        for num in nums:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)
        ans = even + odd
        return ans

sol = Solution()
res = sol.sortArrayByParity([3,1,2,4])
print(res)

'''
Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

'''
        
class Solution:
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        bos = []
        myList=set(nums)
        for i in range(1,n+1):
            if i not in myList:
                bos.append(i)
        return bos








'''
Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]

'''
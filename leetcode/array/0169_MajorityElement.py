class Solution:
    def majorityElement(self, nums):
        n = len(nums)/2
        myHash = {}
        for num in nums:
            if num in myHash:
                myHash[num] += 1
            else:
                myHash[num] = 1
        maxElement = 0
        for num, count in myHash.items():
            if count > n:
                maxElement = num
        return maxElement

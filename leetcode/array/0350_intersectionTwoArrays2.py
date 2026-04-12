class Solution:
    def intersect(self, nums1, nums2):
        ans = []
        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                ans.append(nums1[i])
                i += 1
                j += 1
        return ans


    
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

sol = Solution()
ll = sol.intersect([1,2,2,1], [2])
print(ll)

''' 
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]

Input:
[1,2,2,1]
[2,2]
OutPut:
[2,2]
'''
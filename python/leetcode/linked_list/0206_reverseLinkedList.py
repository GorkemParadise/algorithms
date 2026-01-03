# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head):
        prev = None # None
        curr = head # [1,2,3,4,5]
        
        while curr: # while curr is not None
            next = curr.next # [2,3,4,5], [3,4,5], [4,5], [5], None
            curr.next = prev # None
            prev = curr # [1], [2,1], [3,2,1], [4,3,2,1], [5,4,3,2,1]
            curr = next # [2,3,4,5] , [3,4,5], [4,5], [5], None

        return prev # [5,4,3,2,1]


'''
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Input: head = []
Output: []

Input: head = [1,2]
Output: [2,1]
'''
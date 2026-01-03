from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0) # 1
        dummy.next = head # 2
        first = dummy # 1
        second = dummy # 1
        
        for l in range(n + 1): # index 0 to 3
            first = first.next # 2 , 3 , 4 , 5
            
        while first: # first is not None
            first = first.next # 3 , 4 , 5 , None
            second = second.next # 2 , 3 , 4
            
        second.next = second.next.next # drop 4 get 5
        
        return dummy.next # 1, 2, 3, 5



'''
Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        length = 0
        start = head

        while start != None:
            length += 1
            start = start.next
        
        #handle edge cases, when removing from first when l == 0
        l = length - n
     
        start = head

        if l == 0:
            return head.next

            
        for i in range(l-1):
            start = start.next
        

        start.next = start.next.next

        return head


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        length = 0

        start = head

        while start:
            length += 1
            start = start.next

        start = head

        if n == length:
            return start.next
        for i in range(length - n-1):
            start = start.next
        
        if not start or not start.next:
            temp = None
        else:
            temp = start.next.next
           
        start.next = temp

        return head
        

        


        
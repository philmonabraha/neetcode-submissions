# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        origin = head
        length = 0

        while head != None:
            length += 1
            head = head.next
        
        head = origin

        nodeindex = length - n -1

        for i in range(nodeindex):
            head = head.next
    
        
        if head.next:
            temp = head.next.next
        else:
            temp = None
        
        head.next = temp



        return origin
    

        
        
        
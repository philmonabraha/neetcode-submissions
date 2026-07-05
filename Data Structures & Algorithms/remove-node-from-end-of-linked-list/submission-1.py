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

        nodeindex = length - n

        while nodeindex != 0:
            head = head.next
            nodeindex -= 1
        
        if head.next:
            temp = head.next.next
        else:
            temp = None
        
        returnitem = head.next
        head.next = temp

        head = origin

        return head
    

        
        
        
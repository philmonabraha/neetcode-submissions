# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        
        length = 0
        start = head

        while start != None:
            length += 1
            start = start.next
        
        start = head
        for i in range(length//2):
            start = start.next
        
        half = []
        while start != None:
            half.insert(0, start)
            start = start.next
        
        for item in half:
            temp = head.next
            head.next = item
            item.next = temp
            head = head.next.next


        
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        start = head
        stack = []

        length = 0
        
        while start is not None:
            stack.append(start)
            start = start.next
            length += 1

        start = head

        while len(stack) > (length + 1) // 2:

            temp = start.next
            start.next = stack.pop()
            start.next.next = temp
            start = start.next.next

            length -= 1
        
        start.next = None

        







        

        

        
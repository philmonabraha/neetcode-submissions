# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:


        stack = []

        start = head

        while start:
            stack.append(start)
            start = start.next

        start = head

        for i in range(len(stack)//2):

            end = stack.pop()

            temp = start.next
            start.next = end
            end.next = temp
            start = temp

        start.next = None


        
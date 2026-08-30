# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        length = 0

        counter = head

        while counter is not None:

            length += 1
            counter = counter.next

        counter = head

        if length - n > 0:
            x = length - n
        else:
            x = n - length

        while x > 0:

            counter = counter.next
            x -= 1

        counter.next = counter.next.next




        

        
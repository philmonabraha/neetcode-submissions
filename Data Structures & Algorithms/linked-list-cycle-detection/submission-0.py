# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        p1, p2 = head, head.next

        while p1 != None or p2 != None:

            if p1 == p2:
                return True

            p1 = p1.next
            p2 = p2.next.next

        return False


        
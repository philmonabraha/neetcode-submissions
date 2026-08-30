# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head.next.next == null:
            head.next.next = head.next
            head.next = null;
            return
        
        return self.reverseList(head.next)


        
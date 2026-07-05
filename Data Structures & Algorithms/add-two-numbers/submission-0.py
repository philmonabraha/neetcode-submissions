# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:


        head1, head2 = l1, l2

        added = List()
        pointer = added

        while head1 != None and head2 != None:

            s1 = head1.val
            s2 = head2.val

            added.next = List(val=s1+s2)
            added = added.next

        return pointer.next


        
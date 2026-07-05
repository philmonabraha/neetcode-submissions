# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:


        head1, head2 = l1, l2

        added = ListNode()
        pointer = added

        while head1 != None and head2 != None:

            s1 = head1.val
            s2 = head2.val

            res = str(s1+s2)

            for i in range(len(res)-1, -1, -1):
                added.next = ListNode(val=int(i))
                added = added.next

            head1 = head1.next
            head2 = head2.next

        return pointer.next


        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        head = dummy
        carry = 0

        while l1 or l2:

            if l1 and not l2:
                val = l1.val + carry

            elif not l1 and l2:
                val = l2.val + carry
            
            else:
                val = l1.val + l2.val + carry

            dummy.next = ListNode(val%10)
            carry = val // 10
            dummy = dummy.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry != 0:
            dummy.next = ListNode(val=carry)

        return head.next



        
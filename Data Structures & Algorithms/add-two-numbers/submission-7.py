# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:


        head1, head2 = l1, l2

        s1 = ""
        s2 = ""

        while head1 != None:
            s1 = str(head1.val) + s1
            head1 = head1.next

        while head2 != None:
            s2 = str(head2.val) + s2            
            head2 = head2.next

        result = str(int(s1)+int(s2))

        resultnode = ListNode()
        pointer = resultnode

        for i in range(len(result)-1, -1, -1):
            resultnode.next = ListNode(val=int(result[i]))
            resultnode = resultnode.next

        return pointer.next


        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:


        dummy = ListNode() 
        
        while head != None:

            temp = dummy.next
            node = ListNode(val=head.val,next=temp)
            dummy.next = node

            head = head.next

        return dummy.next


        
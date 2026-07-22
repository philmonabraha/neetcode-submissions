# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:


        
        
        prev = None

        start = head

        while head != None:

            tail = head
            curr = tail         

            index = k

            while curr and index > 0:

                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
                index -= 1

            prev = tail
            head = tail.next

        return head
                




        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:


        start = head

        prev = None

        while head:

            pt1 = head

            for i in range(k):
                nextnode = head.next
                head.next = prev
                prev = head
                head = nextnode

                if k == 0:
                    start = prev

            pt1.next = nextnode



        return prev





        


        
        




        
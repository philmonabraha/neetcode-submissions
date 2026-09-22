# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:


        start = head
        end = head

        #need to account for when end fewer than k nodes left

        #global head
        global_head = start

        for i in range(k):
            global_head = global_head.next
     
        while end:

            few_nodes = False

            for i in range(k):
                if not end:
                    few_nodes = True
                    break           
                end = end.next
            
            if few_nodes:
                break
            
            initial = start

            while start != end:
                temp = start.next
                temp.next = start
                start = temp
            
            initial.next = end.next
            start = initial.next
            end = start

        return global_head


        
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

        previous_tail = None
     
        while start:

            end = start

            few_nodes = False

            for i in range(k):
                if not end:
                    few_nodes = True
                    break           
                end = end.next
            
            if few_nodes:
                break
            
            initial = start

            
            prev = end

            while start != end:
                temp = start.next
                start.next = prev
                prev = start
                start = temp

            # prev is now the head of the reversed group

            # First reversed group
            if previous_tail is None:
                global_head = prev
            else:
                previous_tail.next = prev

            # initial used to be the first node,
            # now it is the tail
            previous_tail = initial

            # start is already end,
            # which is the beginning of next group
            end = start

        return global_head


        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:


        returnnode = ListNode()

        for i in lists:

            currentmin = lists[0]

            for l in lists:

                if currentmin == None:
                    currentmin = l
                 
                elif l.val and l.val < currentmin.val:
                    currentmin = l
            
            returnnode.next = currentmin
            returnnode = returnnode.next
            currentmin = currentmin.next

        
        return returnnode
            






        
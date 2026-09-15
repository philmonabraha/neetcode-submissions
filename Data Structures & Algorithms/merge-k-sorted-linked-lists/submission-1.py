# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        dummy = ListNode() 
        head = dummy


        controller = True
        

        while controller:

            i = 0 
            while i < len(lists) and lists[i] == []:
                i += 1
            if i == len(lists):
                controller = False
            
            minimum_node = lists[i]

            for j in range(0, len(lists)):
                if lists[j] and lists[j].val < minimum_node.val:
                    minimum_node = lists[j]

            dummy.next = minimum_node
            dummy = dummy.next
            dummy.next = None

        return head.next









        
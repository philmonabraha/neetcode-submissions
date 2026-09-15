# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        dummy = ListNode() 
        head = dummy

        while True:
            
            minimum_node = -1

            for j in range(len(lists)):
                if not lists[j]:
                    continue          
                if minimum_node == -1 or lists[j].val < lists[minimum_node].val:
                        minimum_node = i

            if minimum_node == -1:
                break

            dummy.next = lists[minimum_node]
            lists[minimum_node] = lists[minimum_node].next
            dummy = dummy.next
            
        return head.next









        
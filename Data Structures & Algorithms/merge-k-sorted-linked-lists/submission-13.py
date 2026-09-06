# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        dummy = ListNode() 
        head = dummy

        heap = []

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, [node.val, i, node])

        while heap:

            val, i, node = heapq.heappop(heap)

            dummy.next = node
            node = node.next
            dummy = dummy.next         
            if node:
                heapq.heappush(heap, [node.val, i, node])
        
        return head.next









        
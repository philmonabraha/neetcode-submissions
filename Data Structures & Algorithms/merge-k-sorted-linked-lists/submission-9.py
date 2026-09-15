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

        for node in lists:
            heapq.heappush(heap, [node.val, node])

        while heap:

            val, node = heapq.heappop(heap)

            dummy.next = lists[node]
            lists[node] = lists[node].next
            dummy = dummy.next         
            if lists[node]:
                heapq.heappush(heap, [node.val, node])
        
        return head.next









        
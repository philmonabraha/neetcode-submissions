# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        
        returnnode = ListNode()
        head = returnnode

        while True:

            minindex = -1

            for i in range(len(lists)):

                l = lists[i]

                if minindex == -1 or l.val and l.val < lists[minindex].val:
                    minindex = i


            if minindex == -1:
                break

            returnnode.next = lists[minindex]
            returnnode = returnnode.next
            lists[minindex] = lists[minindex].next


        
        return head.next
            






        
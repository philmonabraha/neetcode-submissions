# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        reversed_list = ListNode()

        while head != None:
       
            reversed_list.next = reversed_list
            reversed_list = head
            head = head.next

        return reversed_list


        
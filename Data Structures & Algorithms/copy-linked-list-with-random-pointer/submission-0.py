"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':


        start = head
        
        copied = Node(0)
        c = copied
        #return c.next

        dictionary = {}

        while start != None:

            if start not in dictionary:           
                dictionary[start] = Node(start.val)

            copied.next = dictionary[start]
            copied = copied.next
            start = start.next

        copied = c.next
        start = head

        while start != None:

            copied.random = dictionary[start]
            start = start.next
            copied = copied.next

        return c.next



        
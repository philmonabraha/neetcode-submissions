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

        dummy = Node(x=0)
        res = dummy

        hashmap = {}
        start = head

        while start:
   
            if start not in hashmap:
                node = Node(x=start.val)
                hashmap[start] = node
                res.next = node       
            else:
                res.next = hashmap[start]
            
            if start.random not in hashmap:

                if start.random:
                    hashmap[start.random] = Node(start.random.val)
                else:
                    hashmap[start.random] = None         
            
            res.next.random = hashmap[start.random]          
            res = res.next
            start = start.next

        return dummy.next
        
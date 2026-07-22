class ListNode:

    def __init__(self, val, nextitem, previtem):
        self.val = val
        self.nextitem = nextitem
        self.previtem = previtem


class LRUCache:

    def __init__(self, capacity: int):

        self.dictionary = {}
        self.capacity = capacity
        self.size = 0
        self.node = ListNode(0,None)
        self.head = self.node     

    def remove(current):
            current.prev.next = current.next
            current.next.prev = current.prev

            self.node.next = current
            current.prev = self.node
            self.node = self.next

    
    def get(self, key: int) -> int:

        if key in self.dictionary:

            node = self.dictionary[key]
            self.remove(node)
            return self.dictionary[key].val

        else:

            return -1

    def put(self, key: int, value: int) -> None:

        if self.size < self.capacity:

            if key in self.dictionary:
                self.dictionary[key].val = value
                node = self.dictionary[key]
                remove(node)
            else:
                self.dictionary[key] = ListNode(value, None, self.node)
                self.node.next = self.dictionary[key]
                self.size += 1

        else:

            temp = self.head
            self.head = self.head.next
            self.dictionary.remove(temp)
            self.size -= 1


            if key in self.dictionary:
                self.dictionary[key].val = value
                node = self.dictionary[key]
                remove(node)
            else:
                self.dictionary[key] = ListNode(value, None, self.node)
                self.node.next = self.dictionary[key]
                self.size += 1


            

        

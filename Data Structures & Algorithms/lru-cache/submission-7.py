class List:

    def __init__(self, val, nextt = None, prev = None):
        self.val = val
        self.nextt = nextt
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):

        self.hashmap = {}
        self.head = List(val = 0)
        self.tail = List(val = 0)
        self.head.nextt = self.tail
        self.tail.prev = self.head
        self.size = 0
        self.capacity = capacity
        

    def get(self, key: int) -> int:

        if key in self.hashmap:
            self.remove(self.hashmap[key])
            self.stitch(self.hashmap[key])
            return self.hashmap[key]
        else:
            return -1


    def put(self, key: int, value: int) -> None:

        if self.size + 1 > self.capacity:
            del self.hashmap[key]
            removefirst()
        
        if key in self.hashmap:
            self.hashmap[key].val = value       
            self.remove(self.hashmap[key])
            self.stitch(self.hashmap[key])
            

        else:
            node = List(val=value)
            #stich at the back
            self.hashmap[key] = node
            self.stitch(self.hashmap[key])
        
        self.size += 1

    def removefirst(self):
        temp = self.head.nexxt.nexxt 
        self.head.nexxt = temp

    def remove(self, node):
        prev = node.prev
        nextt = node.nextt
        prev.nextt = nextt
        nextt.prev = prev

    def stitch(self, node):
        temp = self.tail.prev
        temp.next = node
        node.prev = temp
        node.next = self.tail
        self.tail.prev = node




        

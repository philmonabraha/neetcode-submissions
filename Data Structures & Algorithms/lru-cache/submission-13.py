class List:

    def __init__(self, val, key, nextt = None, prev = None):
        self.val = val
        self.key = key
        self.nextt = nextt
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):

        self.hashmap = {}
        self.head = List(val = 0, key = 0)
        self.tail = List(val = 0, key = 0)
        self.head.nextt = self.tail
        self.tail.prev = self.head
        self.size = 0
        self.capacity = capacity
        

    def get(self, key: int) -> int:

        if key in self.hashmap:
            self.remove(self.hashmap[key])
            self.stitch(self.hashmap[key])
            return self.hashmap[key].val
        else:
            return -1


    def put(self, key: int, value: int) -> None:
     
        if key in self.hashmap:
            self.hashmap[key].val = value       
            self.remove(self.hashmap[key])
            self.stitch(self.hashmap[key])
            
        else:
            node = List(val=value, key=key)
            #stich at the back
            self.hashmap[key] = node
            self.stitch(self.hashmap[key])
            self.size += 1

            if self.size > self.capacity:
                self.removefirst()
        
            

    def removefirst(self):
        temp = self.head.nextt
        self.remove(temp)
        del self.hashmap[temp.key]      
        self.size -= 1


    def remove(self, node):
        prev = node.prev
        nextt = node.nextt
        prev.nextt = nextt
        nextt.prev = prev

    def stitch(self, node):
        temp = self.tail.prev
        temp.nextt = node
        node.prev = temp
        node.nextt = self.tail
        self.tail.prev = node




        

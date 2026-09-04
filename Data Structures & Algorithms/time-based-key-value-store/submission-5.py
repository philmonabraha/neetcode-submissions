class TimeMap:

    def __init__(self):

        self.hashmap = {}
     
    def set(self, key: str, value: str, timestamp: int) -> None:

        if key not in self.hashmap:
            self.hashmap[key] = [[timestamp, value]]
        else:
            self.hashmap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.hashmap:
            return ""
        
        else:
            values = self.hashmap[key]
            left = 0
            right = len(values) - 1

            res = ""

            while left <= right:

                mid = left + (right - left) //2

                if values[mid][0] <= timestamp:
                    res = values[mid][0]
                    left = mid + 1
                else:
                    right = mid - 1
            
            return res

        

        

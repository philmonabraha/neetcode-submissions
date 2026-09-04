class TimeMap:

    def __init__(self):

        self.hashmap = {}
     
    def set(self, key: str, value: str, timestamp: int) -> None:

        if key not in self.hashmap:
            self.hashmap[key] = [[timestamp, value]]
        else:
            self.hashmap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:

        if key not in selfhashmap:
            return ""
        
        else:
            values = self.hashmap[key]
            left = 0
            right = len(values) - 1

            while left < right:

                mid = left + (right - left) //2

                if values[mid][0] == timestamp:
                    largest = mid   
                    while largest < right and values[mid][0] == values[largest][0]:
                        largest += 1
                    return values[largest][1]
                
                elif values[mid][0] > timestamp:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return ""

        

        

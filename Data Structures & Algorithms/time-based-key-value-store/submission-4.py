class TimeMap:

    def __init__(self):

        self.dictionary = {}    

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key not in self.dictionary:
            self.dictionary[key] = [[timestamp, value]]
        else:
            self.dictionary[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.dictionary:
            return ""
        else:
            value = self.dictionary[key]

            left, right = 0, len(value) - 1

            while left <= right:

                mid = (left + right )//2  

                if value[mid][0] == timestamp:
                    val = mid 
                    
                    while value[val][0] == value[mid][0]:
                        val += 1

                    return value[val][1]

                if value[mid][0] < timestamp:

                    left = mid + 1
                else:
                    right = mid - 1
            
            return ""
            

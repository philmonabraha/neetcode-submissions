class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        

        res = []

        index = 0
        condition = True
        
        while condition:

            interval = intervals[index]
                   
            if interval[0] > newInterval[0] or (interval[0] == newInterval[0] and interval[1] > newInterval[1]):
                
                condition = False
            index += 1

        
        res = interval[:index-1].append(newInterval) 
        res = res +  interval[index:]


        return res
                
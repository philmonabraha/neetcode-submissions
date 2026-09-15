class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        trust_map = {}

        for x, y in trust:
            if x not in trust_map:
                trust[x] = set()
            trust_map[x].add(y)

        for i in range(1,n+1):
            if i not in trust_map:
                for val in trust_map.values():
                    if i not in val:
                        break
                return i
        
        return -1
                
                


        
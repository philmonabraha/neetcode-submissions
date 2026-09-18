class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:


        hashmap = {i:[] for i in range(numCourses)}

        for x,y in prerequisites:        
            hashmap[x].append(y)

        visited = set()
        
        def dfs(crs):

            if crs in visited:
                return False
            
            if hashmap[crs] == []:
                return True
  
            visited.add(crs)
            
            for item in hashmap[crs]:
                if not dfs(item):
                    return False
                
            visited.remove(crs)
            hashmap[crs] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True

        
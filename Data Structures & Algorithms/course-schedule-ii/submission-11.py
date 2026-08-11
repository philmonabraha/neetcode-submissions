class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        premap = {}
        for i in range(numCourses):
            premap[i] = []

        for pre, crs in prerequisites:
            premap[crs].append(pre)

        visit = set()
        visited = set()
        path = []

        def dfs(crs):

            if crs in visit:
                return False
            if premap[crs] == []:
                if crs not in visited:
                    path.append(crs)
                return True

            visit.add(crs)
            for pre in premap[crs]:
                if not dfs(pre):
                    return False
            visit.remove(crs)
            visited.add(crs)
            premap[crs] = []

            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return path

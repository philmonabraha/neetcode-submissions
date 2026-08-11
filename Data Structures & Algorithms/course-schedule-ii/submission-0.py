class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        premap = {}
        for i in range(numCourses):
            premap[i] = []

        for pre, crs in prerequisities:
            premap[crs].append(crs)

        visit = set()
        path = []

        def dfs(crs):

            if crs in visit:
                return False
            if premap[crs] == []:
                path.append(crs)
                return True

            visit.add(crs)
            for pre in premap[crs]:
                if pre in visit:
                    return False
                dfs(pre)
            visit.remove(crs)

            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return path

        
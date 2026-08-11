class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        premap = {}
        for i in range(numCourses):
            premap[i] = []

        for pre, crs in prerequisites:
            premap[crs].append(pre)

        visit = set()
        path = []

        def dfs(crs):

            nonlocal path

            if crs in visit:
                return False
            if premap[crs] == []:
                path.append(crs)
                return True

            visit.add(crs)
            for pre in premap[crs]:
                if not dfs(pre):
                    return False
            visit.remove(crs)
            premap[crs] = []

            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return path

        
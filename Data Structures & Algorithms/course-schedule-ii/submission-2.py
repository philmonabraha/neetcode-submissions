class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        preq = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preq[crs].append(pre)
        
        completed = set()
        order = []
        visiting = set()
        
        def dfs(i):

            nonlocal order 

            if i in visiting:
                return False
            if preq[i] == []:
                if i not in completed:
                    completed.add(i)
                    order.append(i)
                return True
            visiting.add(i)
            for item in preq[i]:
                if not dfs(item):
                    return False      
            visiting.remove(i)
            preq[i] = []
            if i not in completed:
                completed.add(i)
                order.append(i)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return order



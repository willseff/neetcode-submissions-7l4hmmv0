class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create adjencency graph
        adjGraph = {}
        for course, prereq in prerequisites:
            if course in adjGraph:
                adjGraph[course].append(prereq)
            else:
                adjGraph[course] = [prereq]
            
            if prereq not in adjGraph:
                adjGraph[prereq] = []
        
        def dfs(course, adjGraph, visit):
            if course in visit: 
                return False
            if not adjGraph[course]:
                return True
            
            visit.add(course)
            res = True
            for prereq in adjGraph[course]:
                res = dfs(prereq, adjGraph, visit) and res
            visit.remove(course)
            
            return res
        
        for key in adjGraph:
            if not dfs(key, adjGraph, set()):
                return False
        return True
        
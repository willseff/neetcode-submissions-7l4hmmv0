class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        # create adjencency graph
        adjGraph = {}
        for course, prereq in prerequisites:
            if course in adjGraph:
                adjGraph[course].append(prereq)
            else:
                adjGraph[course] = [prereq]

            if prereq not in adjGraph:
                adjGraph[prereq] = []

        def dfs(course, adjGraph, visit, cache):
            if course in visit:
                return False
            if not adjGraph[course]:
                return True
            
            if course in cache:
                return cache[course]

            visit.add(course)
            res = True
            for prereq in adjGraph[course]:
                res = dfs(prereq, adjGraph, visit, cache) and res
            
            cache[course] = res
            visit.remove(course)

            return cache[course]

        for key in adjGraph:
            if not dfs(key, adjGraph, set(), {}):
                return False
        return True


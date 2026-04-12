class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjGraph = {}
        for i in range(n):
            adjGraph[i] = []
        for node1, node2 in edges:
            adjGraph[node1].append(node2)
            adjGraph[node2].append(node1)

        print(adjGraph)

        def bfs(node, adjList):
            visit = set()
            visit.add(node)

            queue = []
            queue.append(node)
            
            while queue:
                for i in range(len(queue)):
                    curr = queue.pop(0)
                    for neighbor in adjList[curr]:
                        if neighbor not in visit:
                            visit.add(neighbor)
                            queue.append(neighbor)
            return visit

        nodeSet = set(range(n))
        res = 0
        while nodeSet:
            connectedComponents = bfs(nodeSet.pop(), adjGraph)
            print(connectedComponents)
            nodeSet = nodeSet - connectedComponents
            res += 1
        return res

            

        
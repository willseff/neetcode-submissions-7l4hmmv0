class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 1 and not edges:
            return True
        elif n==1:
            return False
        adjGraph = {}
        for node1, node2 in edges:
            if node1 in adjGraph:
                adjGraph[node1].append(node2)
            else:
                adjGraph[node1] = [node2]
            
            if node2 in adjGraph:
                adjGraph[node2].append(node1)
            else: 
                adjGraph[node2] = [node1]
        print(adjGraph)
        
        def bfs(node, adjList):
            visit = set()
            visit.add(node)
            queue = []
            queue.append(node)

            while queue:
                for i in range(len(queue)):
                    curr = queue.pop(0)
                    print('current node: ' + str(node))
                    for neighbor in adjList[curr]:
                        if neighbor not in visit:
                            print("add neighbour: " + str(neighbor))
                            visit.add(neighbor)
                            queue.append(neighbor)
            print(visit)
            return len(visit)

        return (bfs(edges[0][0], adjGraph) == (n)) and (len(edges) == n-1)

        
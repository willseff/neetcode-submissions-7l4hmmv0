# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        def bfs(root):
            queue = deque()
            levels = []

            if root:
                queue.append(root)

            while queue:
                level = []
                print(len(queue))
                for i in range(len(queue)):
                    curr = queue.popleft()
                    level.append(curr)
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
                
                levels.append(level)
                print(level)

            return levels
        levels = bfs(root)
        #check length of each level is 2x the previous one, except for last level
        top_level = levels[0]
        for level in levels[1:-1]:
            if (len(top_level) * 2) != len(level):
                print(len(top_level))
                print(len(level))
                print('level sizes not match')
                return False
            top_level = level

        if len(levels) == 1:
            return True
        # check second last level if each node follows pattern

        def isFull(node):
            return node.left and node.right
        
        def hasChild(node):
            return node.left or node.right

        prev_node = levels[-2][0] if levels[-2][0] else None

        for node in levels[-2][-1:]:
            if not isFull(prev_node) and hasChild(node):
                return False
        
        for node in levels[-2]:
            if node.right and not node.left:
                return False

        return True


            



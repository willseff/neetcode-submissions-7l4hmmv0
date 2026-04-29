"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        queue = deque()

        if root: 
            queue.append(root)
        
        while len(queue) > 0:
            levelSize = len(queue)
            for i in range(levelSize):
                curr = queue.popleft()
                if queue and i != (levelSize -1):
                    curr.next = queue[0]
        
                if curr.left:
                    queue.append(curr.left)
                
                if curr.right:
                    queue.append(curr.right)
            
        return root


        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def getLeafNodes(root): 
            leafNodes = []
            queue = deque()
            
            if root:
                queue.append(root)
            
            while queue:
                for i in range(len(queue)):
                    curr = queue.popleft()
                    if not curr.right and not curr.left:
                        leafNodes.append(curr.val)

                    if curr.right:
                        queue.append(curr.right)
                    
                    if curr.left:
                        queue.append(curr.left)

            return leafNodes

        def inOrder(root, target):
            if not root:
                return
            
            print(root.val)

            if root.left:
                if not root.left.right and not root.left.left and root.left.val == target:
                    root.left = None

            if root.right:
                if not root.right.right and not root.right.left and root.right.val == target:
                    root.right = None
            

            inOrder(root.left, target)
            inOrder(root.right, target)

        inOrder(root, target)
        leafNodes = getLeafNodes(root)
        print(leafNodes)
        while target in leafNodes:
            print('iter 1')
            inOrder(root, target)
            leafNodes = getLeafNodes(root)
            if not root.left and not root.right and root.val == target:

                return None

        return root

        
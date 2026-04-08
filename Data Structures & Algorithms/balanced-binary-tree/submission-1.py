# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        else: 
            return 0

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root:
            maxDepthDiff = self.maxDepth(root.left) - self.maxDepth(root.right)
            print(maxDepthDiff)
            if (maxDepthDiff not in [-1, 0, 1]):
                return False

            else:
                return(self.isBalanced(root.right) and self.isBalanced(root.left))
        
        return True
            